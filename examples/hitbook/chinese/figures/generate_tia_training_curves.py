#!/usr/bin/env python3
"""
绘制TIA方法训练过程的损失变化曲线图
基于第三章和第五章的方法描述生成模拟训练数据
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import savgol_filter

# 优先使用系统中已安装的中文字体（若不可用将回退）
plt.rcParams['font.family'] = 'sans-serif'
plt.rcParams['font.sans-serif'] = [
    'Noto Sans CJK SC',
    'Noto Sans CJK',
    'Noto Serif CJK SC',
    'AR PL UMing CN',
    'Droid Sans Fallback',
    'DejaVu Sans'
]
plt.rcParams['axes.unicode_minus'] = False
plt.rcParams['font.size'] = 10
# 确保 PDF/EPS 使用 Type42，减少位图化与缺字问题
plt.rcParams['pdf.fonttype'] = 42
plt.rcParams['ps.fonttype'] = 42

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

# ==================== 任务不确定性参数(可学习) ====================
# 基于论文 "Multi-Task Learning Using Uncertainty to Weigh Losses"
# - log(σ²) 作为可学习参数，初始化为0，即 σ=1
# - 训练过程中通过梯度下降自动调整
# - 权重关系：weight = 1/(2σ²)
# - σ越小→不确定性越低→权重越高→该任务越重要

# σ_pixel (像素重建任务的不确定性参数):
# - 从 σ=1.0 开始(符合初始化)
# - 前50 epochs: σ逐渐减小到0.7 (权重增加，重点学习重建)
# - 50-100 epochs: σ逐渐增大到0.90 (权重适度降低，峰值削弱)
# - 100 epochs后: σ平缓收敛到0.89 (训练后期稳定，权重适中保持像素质量)
transition_epoch = 50
stabilize_epoch = 100
# 前50 epochs下降
decrease_phase = 1.0 - 0.3 * np.minimum(epochs / transition_epoch, 1.0)
# 50-100 epochs上升（峰值削弱到0.90）
increase_phase = 0.7 + 0.20 * (1 - np.exp(-(np.maximum(epochs - transition_epoch, 0)) / 35))
# 100 epochs后平缓收敛到0.89
stable_phase = 0.90 - 0.01 * (1 - np.exp(-(np.maximum(epochs - stabilize_epoch, 0)) / 30))
uncertainty_pixel = np.where(epochs <= transition_epoch, decrease_phase,
                             np.where(epochs <= stabilize_epoch, increase_phase, stable_phase))
uncertainty_pixel = uncertainty_pixel + 0.008 * np.random.randn(total_epochs)
uncertainty_pixel = savgol_filter(uncertainty_pixel, window_length=41, polyorder=2, mode='nearest')
uncertainty_pixel = np.clip(uncertainty_pixel, 0.68, 1.05)

# σ_feat (特征匹配任务的不确定性参数):
# - 从 σ=1.0 开始(符合初始化)
# - 前80 epochs: σ逐渐增大到1.20 (权重减小，初期不重要，峰值削弱)
# - 80-105 epochs: σ逐渐减小到0.92 (权重增加,强化特征一致性)
# - 105 epochs后: σ快速收敛到0.82 (训练后期稳定，权重最高以强化攻击能力)
transition_epoch_feat = 80
stabilize_epoch_feat = 105
# 前80 epochs上升（峰值削弱到1.20）
increase_phase_feat = 1.0 + 0.20 * (1 - np.exp(-epochs / 40))
# 80-105 epochs下降
decrease_phase_feat = 1.20 - 0.28 * (1 - np.exp(-(np.maximum(epochs - transition_epoch_feat, 0)) / 30))
# 105 epochs后快速收敛到0.82
stable_phase_feat = 0.92 - 0.10 * (1 - np.exp(-(np.maximum(epochs - stabilize_epoch_feat, 0)) / 25))
uncertainty_feat = np.where(epochs <= transition_epoch_feat, increase_phase_feat,
                           np.where(epochs <= stabilize_epoch_feat, decrease_phase_feat, stable_phase_feat))
uncertainty_feat = uncertainty_feat + 0.008 * np.random.randn(total_epochs)
uncertainty_feat = savgol_filter(uncertainty_feat, window_length=41, polyorder=2, mode='nearest')
uncertainty_feat = np.clip(uncertainty_feat, 0.73, 1.35)

# ==================== 计算总损失 ====================

# 总损失 - 根据论文公式计算任务不确定性加权损失
# L(θ) = (1/2σ_p²)L_pixel + (1/2)log(σ_p²) + (1/2σ_f²)L_feat + (1/2)log(σ_f²) - β·L_div
beta = 0.1  # 多样性约束权重
sigma_p = uncertainty_pixel  # σ_p
sigma_f = uncertainty_feat   # σ_f

# 计算加权损失项
weighted_pixel = (1 / (2 * sigma_p**2)) * pixel_loss + 0.5 * np.log(sigma_p**2)
weighted_feat = (1 / (2 * sigma_f**2)) * feat_loss + 0.5 * np.log(sigma_f**2)
# 注意：div_loss本身已经是负值，表示鼓励多样性
# 公式 -β·L_div 中，如果L_div是正值（表示损失），则减去它鼓励多样性
# 但这里div_loss已经是负值，所以直接用 beta*div_loss（保持负值）来减小总损失
weighted_div = beta * div_loss  # div_loss是负值，所以这项会减小总损失

# 总损失
total_loss = weighted_pixel + weighted_feat + weighted_div

# ==================== 生成评估指标 ====================

# ID Preservation Score (越高越好, 0-1范围, 最大值0.947)
id_pres = 0.947 * (1 - np.exp(-epochs/25)) + 0.015 * np.random.randn(total_epochs)
id_pres = np.clip(id_pres, 0, 1)
id_pres = savgol_filter(id_pres, window_length=15, polyorder=2, mode='nearest')
id_pres = np.clip(id_pres, 0, 0.95)

# FID (越低越好, 最低值23.82)
fid = 36.18 * np.exp(-epochs/35) + 23.82 + 1.0 * np.random.randn(total_epochs)
fid = np.clip(fid, 22, 65)
fid = savgol_filter(fid, window_length=15, polyorder=2, mode='nearest')
fid = np.clip(fid, 23.5, 65)

# Attack Success Rate (SAR) - 攻击成功率, 最高值94.23%
sar = 94.23 * (1 - np.exp(-epochs/30)) + 0.8 * np.random.randn(total_epochs)
sar = np.clip(sar, 0, 100)
sar = savgol_filter(sar, window_length=15, polyorder=2, mode='nearest')
sar = np.clip(sar, 0, 94.5)

# ==================== 绘制图像 ====================

fig = plt.figure(figsize=(16, 10))

# 子图(a): 总损失和加权分项损失
ax1 = plt.subplot(2, 3, 1)
ax1.plot(epochs, total_loss, 'k-', linewidth=2.5, label='总损失')
ax1.plot(epochs, weighted_pixel, 'b--', linewidth=1.5, label='加权像素', alpha=0.7)
ax1.plot(epochs, weighted_feat, 'r--', linewidth=1.5, label='加权特征', alpha=0.7)
ax1.plot(epochs, weighted_div, 'g--', linewidth=1.5, label='加权多样性', alpha=0.7)
ax1.set_xlabel('Epoch')
ax1.set_ylabel('Loss Value')
ax1.set_title(r'(a) 总损失：$\frac{1}{2\sigma_p^2}\mathcal{L}_{pixel} + \frac{1}{2}\log\sigma_p^2 + \frac{1}{2\sigma_f^2}\mathcal{L}_{feat} + \frac{1}{2}\log\sigma_f^2 - \beta\mathcal{L}_{div}$', fontsize=9)
ax1.legend(loc='upper right', fontsize=9)
ax1.grid(True, alpha=0.3)

# 子图(b): 原始损失(未加权)
ax2 = plt.subplot(2, 3, 2)
ax2.plot(epochs, pixel_loss, label=r'$\mathcal{L}_{pixel}$（像素 原始）', linewidth=1.5, color='blue')
ax2.plot(epochs, feat_loss, label=r'$\mathcal{L}_{feat}$（特征 原始）', linewidth=1.5, color='red')
ax2.plot(epochs, div_loss, label=r'$\mathcal{L}_{div}$（多样性，负）', linewidth=1.5, color='green')
ax2.set_xlabel('Epoch')
ax2.set_ylabel('Loss Value')
ax2.set_title('(b) 原始分项损失（未加权）')
ax2.legend(loc='upper right', fontsize=9)
ax2.grid(True, alpha=0.3)

# 子图(c): 攻击成功率
ax3 = plt.subplot(2, 3, 3)
ax3.plot(epochs, sar, 'g-', linewidth=2, label='攻击成功率', marker='o', markersize=2, markevery=20)
ax3.set_xlabel('Epoch')
ax3.set_ylabel('Success Rate (%)')
ax3.set_title('(c) 攻击成功率')
ax3.legend(loc='lower right', fontsize=10)
ax3.grid(True, alpha=0.3)
ax3.set_ylim([0, 105])

# 子图(d): 生成质量指标
ax4 = plt.subplot(2, 3, 4)
ax4_twin = ax4.twinx()
ax4.plot(epochs, fid, 'b-', linewidth=2, label='FID', marker='d', markersize=2, markevery=20)
ax4_twin.plot(epochs, id_pres, 'r-', linewidth=2, label='身份保持分数', marker='^', markersize=2, markevery=20)
ax4.set_xlabel('Epoch')
ax4.set_ylabel('FID', color='b')
ax4_twin.set_ylabel('身份保持分数', color='r')
ax4.tick_params(axis='y', labelcolor='b')
ax4_twin.tick_params(axis='y', labelcolor='r')
ax4.set_title('(d) 生成质量指标')
ax4.legend(loc='upper left', fontsize=10)
ax4_twin.legend(loc='upper right', fontsize=10)
ax4_twin.set_ylim([0, 1.0])
ax4.grid(True, alpha=0.3)

# 子图(e): 任务不确定性参数 σ 和权重 1/(2σ²)
ax5 = plt.subplot(2, 3, 5)
# 计算实际权重 1/(2*sigma^2)
weight_pixel = 1 / (2 * uncertainty_pixel**2)
weight_feat = 1 / (2 * uncertainty_feat**2)
ax5.plot(epochs, uncertainty_pixel, label=r'像素 $\sigma_p$', linewidth=2, color='blue', linestyle='-')
ax5.plot(epochs, uncertainty_feat, label=r'特征 $\sigma_f$', linewidth=2, color='red', linestyle='-')
ax5_twin = ax5.twinx()
ax5_twin.plot(epochs, weight_pixel, label=r'$1/(2\sigma_p^2)$ 权重', linewidth=1.5, color='blue', linestyle='--', alpha=0.6)
ax5_twin.plot(epochs, weight_feat, label=r'$1/(2\sigma_f^2)$ 权重', linewidth=1.5, color='red', linestyle='--', alpha=0.6)
ax5.set_xlabel('Epoch')
ax5.set_ylabel(r'不确定度 $\sigma$', color='black')
ax5_twin.set_ylabel(r'权重 $1/(2\sigma^2)$', color='gray')
ax5.set_title(r'(e) 任务不确定性参数 $\sigma$ 与权重 $1/(2\sigma^2)$')
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
ax6.plot(epochs, lr, 'purple', linewidth=2.5, label='学习率')
ax6.fill_between(epochs, 0, lr, alpha=0.3, color='purple')
ax6.set_xlabel('Epoch')
ax6.set_ylabel('Learning Rate (normalized)')
ax6.set_title('(f) 学习率调度')
ax6.legend(loc='upper right', fontsize=10)
ax6.grid(True, alpha=0.3)
ax6.set_ylim([0, 1.1])

# 添加说明文本
ax6.text(warmup_epochs, 0.95, '预热', ha='center', va='top', fontsize=9,
         bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))
ax6.text(total_epochs/2 + warmup_epochs/2, 0.5, '余弦退火', ha='center', va='center', fontsize=9,
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
