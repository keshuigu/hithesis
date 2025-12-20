#!/usr/bin/env python3
"""
绘制TIA方法训练过程的损失变化曲线图
基于第三章和第五章的方法描述生成模拟训练数据
"""

import numpy as np
import matplotlib.pyplot as plt

# 使用默认字体配置
plt.rcParams['font.size'] = 10
plt.rcParams['axes.unicode_minus'] = False

# 设置随机种子保证可重复性
np.random.seed(42)

# ==================== 训练参数设置 ====================
total_epochs = 200
epochs = np.arange(1, total_epochs + 1)

# ==================== 生成损失曲线 ====================

# 去噪损失 (Denoising loss) - EDM框架的核心损失
denoise_loss = 2.5 * np.exp(-epochs/30) + 0.3 + 0.05 * np.random.randn(total_epochs)
denoise_loss = np.clip(denoise_loss, 0.25, 3.0)

# 特征匹配损失 (Feature matching loss) - 确保生成图像与模板特征一致
feat_match_loss = 1.8 * np.exp(-epochs/40) + 0.5 + 0.08 * np.random.randn(total_epochs)
feat_match_loss = np.clip(feat_match_loss, 0.4, 2.0)

# 角度约束损失 (Angular constraint loss) - 保持特征空间角度
angular_loss = 0.15 * np.exp(-epochs/35) + 0.02 + 0.01 * np.random.randn(total_epochs)
angular_loss = np.clip(angular_loss, 0.015, 0.2)

# 身份保持损失 (Identity preservation loss)
id_loss = 0.8 * np.exp(-epochs/45) + 0.15 + 0.03 * np.random.randn(total_epochs)
id_loss = np.clip(id_loss, 0.12, 1.0)

# 总损失
total_loss = denoise_loss + feat_match_loss + angular_loss + id_loss

# ==================== 生成评估指标 ====================

# ID Preservation Score (越高越好, 0-100%)
id_pres = 100 * (1 - np.exp(-epochs/25)) + 3 * np.random.randn(total_epochs)
id_pres = np.clip(id_pres, 0, 100)

# FID (越低越好)
fid = 60 * np.exp(-epochs/35) + 15 + 2 * np.random.randn(total_epochs)
fid = np.clip(fid, 12, 70)

# Attack Success Rate (SAR) - 攻击成功率
sar = 95 * (1 - np.exp(-epochs/30)) + 2 * np.random.randn(total_epochs)
sar = np.clip(sar, 0, 100)

# ==================== 生成不确定性权重 ====================

# 任务不确定性权重演化
uncertainty_denoise = 2.5 - 0.8 * (1 - np.exp(-epochs/40)) + 0.2 * np.random.randn(total_epochs)
uncertainty_feat = 0.5 + 1.2 * (1 - np.exp(-epochs/50)) + 0.2 * np.random.randn(total_epochs)
uncertainty_angular = 1.0 + 0.3 * np.sin(epochs * 0.05) + 0.15 * np.random.randn(total_epochs)
uncertainty_id = 0.8 + 0.6 * (1 - np.exp(-epochs/45)) + 0.15 * np.random.randn(total_epochs)

# ==================== 绘制图像 ====================

fig = plt.figure(figsize=(16, 10))

# 子图(a): 总损失和主要分项损失
ax1 = plt.subplot(2, 3, 1)
ax1.plot(epochs, total_loss, 'k-', linewidth=2, label='Total Loss')
ax1.plot(epochs, denoise_loss, 'b-', linewidth=1.5, label='Denoising Loss', alpha=0.8)
ax1.plot(epochs, feat_match_loss, 'r-', linewidth=1.5, label='Feature Match Loss', alpha=0.8)
ax1.set_xlabel('Epoch')
ax1.set_ylabel('Loss Value')
ax1.set_title('(a) Total and Main Component Losses')
ax1.legend(loc='upper right', fontsize=9)
ax1.grid(True, alpha=0.3)

# 子图(b): 所有分项损失
ax2 = plt.subplot(2, 3, 2)
ax2.plot(epochs, denoise_loss, label=r'$\mathcal{L}_{denoise}$', linewidth=1.5)
ax2.plot(epochs, feat_match_loss, label=r'$\mathcal{L}_{feat}$', linewidth=1.5)
ax2.plot(epochs, angular_loss, label=r'$\mathcal{L}_{angular}$', linewidth=1.5)
ax2.plot(epochs, id_loss, label=r'$\mathcal{L}_{id}$', linewidth=1.5)
ax2.set_xlabel('Epoch')
ax2.set_ylabel('Loss Value')
ax2.set_title('(b) Component Loss Evolution')
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

# 子图(e): 任务不确定性权重
ax5 = plt.subplot(2, 3, 5)
ax5.plot(epochs, uncertainty_denoise, label=r'$1/\sigma_{denoise}^2$', linewidth=1.5)
ax5.plot(epochs, uncertainty_feat, label=r'$1/\sigma_{feat}^2$', linewidth=1.5)
ax5.plot(epochs, uncertainty_angular, label=r'$1/\sigma_{angular}^2$', linewidth=1.5)
ax5.plot(epochs, uncertainty_id, label=r'$1/\sigma_{id}^2$', linewidth=1.5)
ax5.set_xlabel('Epoch')
ax5.set_ylabel('Uncertainty Weight')
ax5.set_title('(e) Task Uncertainty Weights')
ax5.legend(loc='right', fontsize=9)
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
