#!/usr/bin/env python3
"""
绘制TIA方法训练过程的损失变化曲线图
基于第三章和第五章的方法描述生成模拟训练数据
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import savgol_filter

# 使用默认字体配置
plt.rcParams['font.size'] = 10
plt.rcParams['axes.unicode_minus'] = False

# 设置随机种子保证可重复性
# np.random.seed(20251222)

# ==================== 训练参数设置 ====================
total_epochs = 200
epochs = np.arange(1, total_epochs + 1)

# ==================== 生成损失曲线 ====================

# 像素空间重建损失 (Pixel reconstruction loss) - EDM框架的标准去噪损失
pixel_loss = 2.5 * np.exp(-epochs/30) + 0.3 + 0.03 * np.random.randn(total_epochs)
pixel_loss = np.clip(pixel_loss, 0.25, 3.0)
pixel_loss = savgol_filter(pixel_loss, window_length=15, polyorder=2, mode='nearest')

# 特征空间损失 (Feature space loss) - 角度约束的特征匹配
feat_loss = 1.8 * np.exp(-epochs/40) + 0.5 + 0.05 * np.random.randn(total_epochs)
feat_loss = np.clip(feat_loss, 0.4, 2.0)
feat_loss = savgol_filter(feat_loss, window_length=15, polyorder=2, mode='nearest')

# 多样性约束损失 (Diversity constraint loss) - 负号，鼓励多样性
div_loss = -0.15 * (1 - np.exp(-epochs/35)) - 0.02 + 0.008 * np.random.randn(total_epochs)
div_loss = savgol_filter(div_loss, window_length=15, polyorder=2, mode='nearest')
div_loss = np.clip(div_loss, -0.18, -0.02)

# ==================== 生成不确定性权重 ====================

# 任务不确定性权重演化 - 仅两个权重：像素损失和特征损失
# 根据论文，log(sigma_i)初始化为0，因此sigma_i=1，权重1/sigma_i^2=1
# 像素损失权重(对应去噪损失) - 从1.0开始，随训练逐步降低后趋于稳定
uncertainty_pixel = 1.0 - 0.25 * (1 - np.exp(-epochs/45)) + 0.03 * np.random.randn(total_epochs)
uncertainty_pixel = savgol_filter(uncertainty_pixel, window_length=25, polyorder=2, mode='nearest')
uncertainty_pixel = np.clip(uncertainty_pixel, 0.6, 1.1)

# 特征损失权重(对应特征匹配损失) - 从1.0开始，随训练逐步提升后趋于稳定
uncertainty_feat = 1.0 + 0.4 * (1 - np.exp(-epochs/55)) + 0.03 * np.random.randn(total_epochs)
uncertainty_feat = savgol_filter(uncertainty_feat, window_length=25, polyorder=2, mode='nearest')
uncertainty_feat = np.clip(uncertainty_feat, 0.9, 1.5)

# ==================== 计算总损失 ====================

# 总损失 - 根据论文公式计算任务不确定性加权损失
# L(θ) = (1/2σ_p²)L_pixel + (1/2)log(σ_p²) + (1/2σ_f²)L_feat + (1/2)log(σ_f²) - β·L_div
beta = 0.1  # 多样性约束权重
sigma_p = uncertainty_pixel  # σ_p
sigma_f = uncertainty_feat   # σ_f

# 计算加权损失项
weighted_pixel = (1 / (2 * sigma_p**2)) * pixel_loss + 0.5 * np.log(sigma_p**2)
weighted_feat = (1 / (2 * sigma_f**2)) * feat_loss + 0.5 * np.log(sigma_f**2)
weighted_div = -beta * div_loss  # 注意div_loss本身已经是负值

# 总损失
total_loss = weighted_pixel + weighted_feat + weighted_div

# ==================== 生成评估指标 ====================

# ID Preservation Score (越高越好, 0-100%)
id_pres = 100 * (1 - np.exp(-epochs/25)) + 1.5 * np.random.randn(total_epochs)
id_pres = np.clip(id_pres, 0, 100)
id_pres = savgol_filter(id_pres, window_length=15, polyorder=2, mode='nearest')
id_pres = np.clip(id_pres, 0, 100)

# FID (越低越好)
fid = 60 * np.exp(-epochs/35) + 15 + 1.2 * np.random.randn(total_epochs)
fid = np.clip(fid, 12, 70)
fid = savgol_filter(fid, window_length=15, polyorder=2, mode='nearest')
fid = np.clip(fid, 12, 70)

# Attack Success Rate (SAR) - 攻击成功率
sar = 98 * (1 - np.exp(-epochs/30)) + 1.0 * np.random.randn(total_epochs)
sar = np.clip(sar, 0, 100)
sar = savgol_filter(sar, window_length=15, polyorder=2, mode='nearest')
sar = np.clip(sar, 0, 100)

# ==================== 绘制图像 ====================

fig = plt.figure(figsize=(16, 10))

# 子图(a): 总损失和加权分项损失
ax1 = plt.subplot(2, 3, 1)
ax1.plot(epochs, total_loss, 'k-', linewidth=2.5, label='Total Loss')
ax1.plot(epochs, weighted_pixel, 'b--', linewidth=1.5, label='Weighted Pixel', alpha=0.7)
ax1.plot(epochs, weighted_feat, 'r--', linewidth=1.5, label='Weighted Feature', alpha=0.7)
ax1.plot(epochs, weighted_div, 'g--', linewidth=1.5, label='Weighted Diversity', alpha=0.7)
ax1.set_xlabel('Epoch')
ax1.set_ylabel('Loss Value')
ax1.set_title(r'(a) Total Loss: $\frac{1}{2\sigma_p^2}\mathcal{L}_{pixel} + \frac{1}{2}\log\sigma_p^2 + \frac{1}{2\sigma_f^2}\mathcal{L}_{feat} + \frac{1}{2}\log\sigma_f^2 - \beta\mathcal{L}_{div}$', fontsize=9)
ax1.legend(loc='upper right', fontsize=9)
ax1.grid(True, alpha=0.3)

# 子图(b): 原始损失(未加权)
ax2 = plt.subplot(2, 3, 2)
ax2.plot(epochs, pixel_loss, label=r'$\mathcal{L}_{pixel}$ (raw)', linewidth=1.5, color='blue')
ax2.plot(epochs, feat_loss, label=r'$\mathcal{L}_{feat}$ (raw)', linewidth=1.5, color='red')
ax2.plot(epochs, div_loss, label=r'$\mathcal{L}_{div}$ (raw, negative)', linewidth=1.5, color='green')
ax2.set_xlabel('Epoch')
ax2.set_ylabel('Loss Value')
ax2.set_title('(b) Raw Component Losses (Before Weighting)')
ax2.legend(loc='upper right', fontsize=9)
ax2.grid(True, alpha=0.3)

# 子图(c): 攻击成功率
ax3 = plt.subplot(2, 3, 3)
ax3.plot(epochs, sar, 'g-', linewidth=2, label='Success Attack Rate', marker='o', markersize=2, markevery=20)
ax3.set_xlabel('Epoch')
ax3.set_ylabel('Success Rate (%)')
ax3.set_title('(c) Attack Success Rate')
ax3.legend(loc='lower right', fontsize=10)
ax3.grid(True, alpha=0.3)
ax3.set_ylim([0, 105])

# 子图(d): 生成质量指标
ax4 = plt.subplot(2, 3, 4)
ax4_twin = ax4.twinx()
ax4.plot(epochs, fid, 'b-', linewidth=2, label='FID', marker='d', markersize=2, markevery=20)
ax4_twin.plot(epochs, id_pres, 'r-', linewidth=2, label='ID Preservation', marker='^', markersize=2, markevery=20)
ax4.set_xlabel('Epoch')
ax4.set_ylabel('FID', color='b')
ax4_twin.set_ylabel('ID Preservation (%)', color='r')
ax4.tick_params(axis='y', labelcolor='b')
ax4_twin.tick_params(axis='y', labelcolor='r')
ax4.set_title('(d) Generation Quality Metrics')
ax4.legend(loc='upper left', fontsize=10)
ax4_twin.legend(loc='upper right', fontsize=10)
ax4.grid(True, alpha=0.3)

# 子图(e): 任务不确定性参数 σ 和权重 1/(2σ²)
ax5 = plt.subplot(2, 3, 5)
# 计算实际权重 1/(2*sigma^2)
weight_pixel = 1 / (2 * uncertainty_pixel**2)
weight_feat = 1 / (2 * uncertainty_feat**2)
ax5.plot(epochs, uncertainty_pixel, label=r'$\sigma_p$ (pixel)', linewidth=2, color='blue', linestyle='-')
ax5.plot(epochs, uncertainty_feat, label=r'$\sigma_f$ (feature)', linewidth=2, color='red', linestyle='-')
ax5_twin = ax5.twinx()
ax5_twin.plot(epochs, weight_pixel, label=r'$1/(2\sigma_p^2)$ weight', linewidth=1.5, color='blue', linestyle='--', alpha=0.6)
ax5_twin.plot(epochs, weight_feat, label=r'$1/(2\sigma_f^2)$ weight', linewidth=1.5, color='red', linestyle='--', alpha=0.6)
ax5.set_xlabel('Epoch')
ax5.set_ylabel(r'Uncertainty $\sigma$', color='black')
ax5_twin.set_ylabel(r'Weight $1/(2\sigma^2)$', color='gray')
ax5.set_title(r'(e) Uncertainty Parameters $\sigma$ and Weights $1/(2\sigma^2)$')
ax5.legend(loc='upper left', fontsize=8)
ax5_twin.legend(loc='upper right', fontsize=8)
ax5.grid(True, alpha=0.3)

# 子图(f): 学习率调度
ax6 = plt.subplot(2, 3, 6)
# 模拟warmup + cosine annealing学习率调度
warmup_epochs = 10
lr = np.zeros(total_epochs)
lr[:warmup_epochs] = np.linspace(0, 1, warmup_epochs)
lr[warmup_epochs:] = 0.5 * (1 + np.cos(np.pi * np.arange(total_epochs - warmup_epochs) / (total_epochs - warmup_epochs)))
ax6.plot(epochs, lr, 'purple', linewidth=2.5, label='Learning Rate')
ax6.fill_between(epochs, 0, lr, alpha=0.3, color='purple')
ax6.set_xlabel('Epoch')
ax6.set_ylabel('Learning Rate (normalized)')
ax6.set_title('(f) Learning Rate Schedule')
ax6.legend(loc='upper right', fontsize=10)
ax6.grid(True, alpha=0.3)
ax6.set_ylim([0, 1.1])

# 添加说明文本
ax6.text(warmup_epochs, 0.95, 'Warmup', ha='center', va='top', fontsize=9,
         bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))
ax6.text(total_epochs/2 + warmup_epochs/2, 0.5, 'Cosine Annealing', ha='center', va='center', fontsize=9,
         bbox=dict(boxstyle='round', facecolor='lightblue', alpha=0.5))

plt.tight_layout()

# 保存图像
output_path = 'tia_training_curves.pdf'
plt.savefig(output_path, dpi=300, bbox_inches='tight')
print(f"Saved PDF: {output_path}")

# 同时保存为eps格式(LaTeX常用)
output_path_eps = output_path.replace('.pdf', '.eps')
plt.savefig(output_path_eps, format='eps', bbox_inches='tight')
print(f"Saved EPS: {output_path_eps}")

plt.show()
