#!/usr/bin/env python3
"""
绘制MIA方法渐进式三阶段训练的损失变化曲线图
基于第四章和第五章的方法描述生成模拟训练数据
"""

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Rectangle
import matplotlib.patches as mpatches

# 使用默认字体配置
plt.rcParams['font.size'] = 10
plt.rcParams['axes.unicode_minus'] = False

# 设置随机种子保证可重复性
np.random.seed(42)

# ==================== 训练参数设置 ====================
# 三个阶段的epoch数
stage0_epochs = 30   # 阶段1: 图像条件预热
stage1_epochs = 50   # 阶段2: 混合条件过渡
stage2_epochs = 70   # 阶段3: 纯标签条件适配
total_epochs = stage0_epochs + stage1_epochs + stage2_epochs

# 生成epoch序列
epochs = np.arange(1, total_epochs + 1)

# ==================== 定义各阶段的损失模拟函数 ====================

def simulate_stage0_losses(epochs):
    """阶段0: 图像条件预热 - 仅优化prior和perc损失"""
    # 扩散先验损失: 快速下降后趋于稳定
    prior_loss = 0.8 * np.exp(-epochs/8) + 0.15 + 0.02 * np.random.randn(len(epochs))

    # 感知质量损失: 类似下降趋势
    perc_loss = 0.6 * np.exp(-epochs/10) + 0.12 + 0.015 * np.random.randn(len(epochs))

    # 其他损失在阶段0不参与优化,设为None
    cls_loss = np.full(len(epochs), np.nan)
    id_loss = np.full(len(epochs), np.nan)
    preg_loss = np.full(len(epochs), np.nan)

    return prior_loss, perc_loss, cls_loss, id_loss, preg_loss

def simulate_stage1_losses(epochs, stage0_final_prior, stage0_final_perc):
    """阶段1: 混合条件过渡 - 通过余弦退火逐步引入攻击损失"""
    n = len(epochs)

    # 余弦退火系数: lambda(t) = 0.5 * (1 - cos(pi * t / T_anneal))
    t_normalized = np.linspace(0, 1, n)
    lambda_t = 0.5 * (1 - np.cos(np.pi * t_normalized))

    # Prior损失: 轻微上升后稳定(因为开始适配标签嵌入)
    prior_loss = stage0_final_prior + 0.05 * lambda_t + 0.02 * np.random.randn(n)

    # 感知质量损失: 继续小幅优化
    perc_loss = stage0_final_perc * np.exp(-epochs/30) + 0.02 * np.random.randn(n)

    # 分类引导损失: 从高值逐步下降(初期模型不会分类)
    cls_loss = 2.5 * (1 - lambda_t) + 0.3 + 0.1 * np.random.randn(n)

    # 身份一致性损失: 从高值下降(初期标签嵌入与生成图像不匹配)
    id_loss = 1.8 * (1 - lambda_t) + 0.25 + 0.08 * np.random.randn(n)

    # P-reg损失: 逐步下降
    preg_loss = 0.5 + 0.4 * (1 - lambda_t) + 0.05 * np.random.randn(n)

    return prior_loss, perc_loss, cls_loss, id_loss, preg_loss, lambda_t

def simulate_stage2_losses(epochs, stage1_final_losses):
    """阶段2: 纯标签条件适配 - 完整损失优化"""
    n = len(epochs)
    prior_s1, perc_s1, cls_s1, id_s1, preg_s1 = stage1_final_losses

    # 各损失继续优化,逐步收敛
    prior_loss = prior_s1 * np.exp(-epochs/25) + 0.18 + 0.015 * np.random.randn(n)
    perc_loss = perc_s1 * np.exp(-epochs/20) + 0.10 + 0.01 * np.random.randn(n)
    cls_loss = cls_s1 * np.exp(-epochs/15) + 0.25 + 0.05 * np.random.randn(n)
    id_loss = id_s1 * np.exp(-epochs/18) + 0.20 + 0.04 * np.random.randn(n)
    preg_loss = preg_s1 * np.exp(-epochs/20) + 0.15 + 0.03 * np.random.randn(n)

    return prior_loss, perc_loss, cls_loss, id_loss, preg_loss

# ==================== 生成完整训练曲线 ====================

# 阶段0的epoch范围
stage0_range = np.arange(stage0_epochs)
prior_s0, perc_s0, cls_s0, id_s0, preg_s0 = simulate_stage0_losses(stage0_range)

# 阶段1的epoch范围
stage1_range = np.arange(stage1_epochs)
prior_s1, perc_s1, cls_s1, id_s1, preg_s1, lambda_curve = simulate_stage1_losses(
    stage1_range, prior_s0[-1], perc_s0[-1]
)

# 阶段2的epoch范围
stage2_range = np.arange(stage2_epochs)
prior_s2, perc_s2, cls_s2, id_s2, preg_s2 = simulate_stage2_losses(
    stage2_range, (prior_s1[-1], perc_s1[-1], cls_s1[-1], id_s1[-1], preg_s1[-1])
)

# 合并三个阶段的数据
prior_full = np.concatenate([prior_s0, prior_s1, prior_s2])
perc_full = np.concatenate([perc_s0, perc_s1, perc_s2])
cls_full = np.concatenate([cls_s0, cls_s1, cls_s2])
id_full = np.concatenate([id_s0, id_s1, id_s2])
preg_full = np.concatenate([preg_s0, preg_s1, preg_s2])

# ==================== 生成评估指标曲线 ====================

# Acc1: 从低逐步提升
acc1 = np.zeros(total_epochs)
acc1[:stage0_epochs] = np.nan  # 阶段0不评估
acc1[stage0_epochs:stage0_epochs+stage1_epochs] = 20 + 40 * lambda_curve + 5 * np.random.randn(stage1_epochs)
acc1[stage0_epochs+stage1_epochs:] = 60 + 35 * (1 - np.exp(-stage2_range/20)) + 3 * np.random.randn(stage2_epochs)
acc1 = np.clip(acc1, 0, 100)

# Acc5: 比Acc1更高且更快饱和
acc5 = np.zeros(total_epochs)
acc5[:stage0_epochs] = np.nan
acc5[stage0_epochs:stage0_epochs+stage1_epochs] = 40 + 50 * lambda_curve + 4 * np.random.randn(stage1_epochs)
acc5[stage0_epochs+stage1_epochs:] = 90 + 8 * (1 - np.exp(-stage2_range/15)) + 2 * np.random.randn(stage2_epochs)
acc5 = np.clip(acc5, 0, 100)

# FID: 从高逐步下降
fid = np.zeros(total_epochs)
fid[:stage0_epochs] = 80 - 30 * (1 - np.exp(-stage0_range/8)) + 5 * np.random.randn(stage0_epochs)
fid[stage0_epochs:stage0_epochs+stage1_epochs] = 50 - 15 * lambda_curve + 4 * np.random.randn(stage1_epochs)
fid[stage0_epochs+stage1_epochs:] = 35 * np.exp(-stage2_range/25) + 20 + 3 * np.random.randn(stage2_epochs)
fid = np.clip(fid, 15, 100)

# KNN距离: 类似FID的下降趋势
knn_dist = np.zeros(total_epochs)
knn_dist[:stage0_epochs] = np.nan
knn_dist[stage0_epochs:stage0_epochs+stage1_epochs] = 1300 - 200 * lambda_curve + 20 * np.random.randn(stage1_epochs)
knn_dist[stage0_epochs+stage1_epochs:] = 1100 * np.exp(-stage2_range/30) + 900 + 15 * np.random.randn(stage2_epochs)

# ==================== 生成不确定性权重曲线 ====================

# 任务不确定性权重 1/sigma^2 的演化
# 初期各任务不确定性较大,随训练逐步学习权重
uncertainty_prior = np.ones(total_epochs)
uncertainty_prior[:stage0_epochs] = 2.0 + 0.5 * np.random.randn(stage0_epochs)
uncertainty_prior[stage0_epochs:stage0_epochs+stage1_epochs] = 1.8 - 0.3 * lambda_curve + 0.3 * np.random.randn(stage1_epochs)
uncertainty_prior[stage0_epochs+stage1_epochs:] = 1.5 - 0.3 * (1 - np.exp(-stage2_range/20)) + 0.2 * np.random.randn(stage2_epochs)

uncertainty_cls = np.zeros(total_epochs)
uncertainty_cls[:stage0_epochs] = np.nan
uncertainty_cls[stage0_epochs:stage0_epochs+stage1_epochs] = 0.3 + 1.2 * lambda_curve + 0.2 * np.random.randn(stage1_epochs)
uncertainty_cls[stage0_epochs+stage1_epochs:] = 1.5 + 0.5 * (1 - np.exp(-stage2_range/15)) + 0.2 * np.random.randn(stage2_epochs)

uncertainty_id = np.zeros(total_epochs)
uncertainty_id[:stage0_epochs] = np.nan
uncertainty_id[stage0_epochs:stage0_epochs+stage1_epochs] = 0.2 + 0.8 * lambda_curve + 0.15 * np.random.randn(stage1_epochs)
uncertainty_id[stage0_epochs+stage1_epochs:] = 1.0 + 0.3 * (1 - np.exp(-stage2_range/18)) + 0.15 * np.random.randn(stage2_epochs)

uncertainty_perc = np.ones(total_epochs) * 1.2
uncertainty_perc += 0.2 * np.random.randn(total_epochs)

uncertainty_preg = np.zeros(total_epochs)
uncertainty_preg[:stage0_epochs] = np.nan
uncertainty_preg[stage0_epochs:] = 0.8 + 0.1 * np.random.randn(stage1_epochs + stage2_epochs)

# ==================== 绘制图像 ====================

fig = plt.figure(figsize=(18, 10))

# Define three stage colors
stage_colors = ['#FFE6E6', '#E6F3FF', '#E6FFE6']
stage_labels = ['Stage 1: Image-conditional', 'Stage 2: Mixed-conditional', 'Stage 3: Label-conditional']

# 子图(a): 总损失与主要损失曲线
ax1 = plt.subplot(2, 3, 1)
# 添加阶段背景色
ax1.axvspan(0, stage0_epochs, alpha=0.2, color=stage_colors[0])
ax1.axvspan(stage0_epochs, stage0_epochs+stage1_epochs, alpha=0.2, color=stage_colors[1])
ax1.axvspan(stage0_epochs+stage1_epochs, total_epochs, alpha=0.2, color=stage_colors[2])

# Calculate total loss (simplified as weighted sum)
total_loss = prior_full + perc_full + np.nan_to_num(cls_full, 0) + np.nan_to_num(id_full, 0) + np.nan_to_num(preg_full, 0)
ax1.plot(epochs, total_loss, 'k-', linewidth=2, label='Total Loss')
ax1.plot(epochs, prior_full, 'b-', linewidth=1.5, label='Prior Loss', alpha=0.8)
ax1.plot(epochs, cls_full, 'r-', linewidth=1.5, label='Classification Loss', alpha=0.8)

# 添加阶段分界线
ax1.axvline(stage0_epochs, color='gray', linestyle='--', linewidth=1, alpha=0.6)
ax1.axvline(stage0_epochs+stage1_epochs, color='gray', linestyle='--', linewidth=1, alpha=0.6)

ax1.set_xlabel('Epoch')
ax1.set_ylabel('Loss Value')
ax1.set_title('(a) Total and Main Component Losses')
ax1.legend(loc='upper right', fontsize=9)
ax1.grid(True, alpha=0.3)

# 子图(b): 所有分项损失
ax2 = plt.subplot(2, 3, 2)
ax2.axvspan(0, stage0_epochs, alpha=0.2, color=stage_colors[0])
ax2.axvspan(stage0_epochs, stage0_epochs+stage1_epochs, alpha=0.2, color=stage_colors[1])
ax2.axvspan(stage0_epochs+stage1_epochs, total_epochs, alpha=0.2, color=stage_colors[2])

ax2.plot(epochs, prior_full, label=r'$\mathcal{L}_{prior}$', linewidth=1.5)
ax2.plot(epochs, cls_full, label=r'$\mathcal{L}_{cls}$', linewidth=1.5)
ax2.plot(epochs, id_full, label=r'$\mathcal{L}_{id}$', linewidth=1.5)
ax2.plot(epochs, perc_full, label=r'$\mathcal{L}_{perc}$', linewidth=1.5)
ax2.plot(epochs, preg_full, label=r'$\mathcal{L}_{p-reg}$', linewidth=1.5)

ax2.axvline(stage0_epochs, color='gray', linestyle='--', linewidth=1, alpha=0.6)
ax2.axvline(stage0_epochs+stage1_epochs, color='gray', linestyle='--', linewidth=1, alpha=0.6)

ax2.set_xlabel('Epoch')
ax2.set_ylabel('Loss Value')
ax2.set_title('(b) Component Loss Evolution')
ax2.legend(loc='upper right', fontsize=9)
ax2.grid(True, alpha=0.3)

# 子图(c): 攻击准确率
ax3 = plt.subplot(2, 3, 3)
ax3.axvspan(0, stage0_epochs, alpha=0.2, color=stage_colors[0])
ax3.axvspan(stage0_epochs, stage0_epochs+stage1_epochs, alpha=0.2, color=stage_colors[1])
ax3.axvspan(stage0_epochs+stage1_epochs, total_epochs, alpha=0.2, color=stage_colors[2])

ax3.plot(epochs, acc1, 'g-', linewidth=2, label='Acc1', marker='o', markersize=2, markevery=10)
ax3.plot(epochs, acc5, 'm-', linewidth=2, label='Acc5', marker='s', markersize=2, markevery=10)

ax3.axvline(stage0_epochs, color='gray', linestyle='--', linewidth=1, alpha=0.6)
ax3.axvline(stage0_epochs+stage1_epochs, color='gray', linestyle='--', linewidth=1, alpha=0.6)

ax3.set_xlabel('Epoch')
ax3.set_ylabel('Accuracy (%)')
ax3.set_title('(c) Attack Accuracy')
ax3.legend(loc='lower right', fontsize=10)
ax3.grid(True, alpha=0.3)
ax3.set_ylim([0, 105])

# 子图(d): 生成质量指标
ax4 = plt.subplot(2, 3, 4)
ax4.axvspan(0, stage0_epochs, alpha=0.2, color=stage_colors[0])
ax4.axvspan(stage0_epochs, stage0_epochs+stage1_epochs, alpha=0.2, color=stage_colors[1])
ax4.axvspan(stage0_epochs+stage1_epochs, total_epochs, alpha=0.2, color=stage_colors[2])

ax4_twin = ax4.twinx()
ax4.plot(epochs, fid, 'b-', linewidth=2, label='FID', marker='d', markersize=2, markevery=10)
ax4_twin.plot(epochs, knn_dist, 'r-', linewidth=2, label='KNN Distance', marker='^', markersize=2, markevery=10)

ax4.axvline(stage0_epochs, color='gray', linestyle='--', linewidth=1, alpha=0.6)
ax4.axvline(stage0_epochs+stage1_epochs, color='gray', linestyle='--', linewidth=1, alpha=0.6)

ax4.set_xlabel('Epoch')
ax4.set_ylabel('FID', color='b')
ax4_twin.set_ylabel('KNN Distance', color='r')
ax4.tick_params(axis='y', labelcolor='b')
ax4_twin.tick_params(axis='y', labelcolor='r')
ax4.set_title('(d) Generation Quality Metrics')
ax4.legend(loc='upper left', fontsize=10)
ax4_twin.legend(loc='upper right', fontsize=10)
ax4.grid(True, alpha=0.3)

# 子图(e): 任务不确定性权重
ax5 = plt.subplot(2, 3, 5)
ax5.axvspan(0, stage0_epochs, alpha=0.2, color=stage_colors[0])
ax5.axvspan(stage0_epochs, stage0_epochs+stage1_epochs, alpha=0.2, color=stage_colors[1])
ax5.axvspan(stage0_epochs+stage1_epochs, total_epochs, alpha=0.2, color=stage_colors[2])

ax5.plot(epochs, uncertainty_prior, label=r'$1/\sigma_{prior}^2$', linewidth=1.5)
ax5.plot(epochs, uncertainty_cls, label=r'$1/\sigma_{cls}^2$', linewidth=1.5)
ax5.plot(epochs, uncertainty_id, label=r'$1/\sigma_{id}^2$', linewidth=1.5)
ax5.plot(epochs, uncertainty_perc, label=r'$1/\sigma_{perc}^2$', linewidth=1.5)
ax5.plot(epochs, uncertainty_preg, label=r'$1/\sigma_{p-reg}^2$', linewidth=1.5)

ax5.axvline(stage0_epochs, color='gray', linestyle='--', linewidth=1, alpha=0.6)
ax5.axvline(stage0_epochs+stage1_epochs, color='gray', linestyle='--', linewidth=1, alpha=0.6)

ax5.set_xlabel('Epoch')
ax5.set_ylabel('Uncertainty Weight')
ax5.set_title('(e) Task Uncertainty Weights')
ax5.legend(loc='right', fontsize=9)
ax5.grid(True, alpha=0.3)

# 子图(f): 混合系数lambda(t)余弦退火曲线
ax6 = plt.subplot(2, 3, 6)
ax6.axvspan(0, stage0_epochs, alpha=0.2, color=stage_colors[0])
ax6.axvspan(stage0_epochs, stage0_epochs+stage1_epochs, alpha=0.2, color=stage_colors[1])
ax6.axvspan(stage0_epochs+stage1_epochs, total_epochs, alpha=0.2, color=stage_colors[2])

# 绘制lambda曲线(仅在阶段1有意义)
lambda_full = np.zeros(total_epochs)
lambda_full[:stage0_epochs] = 0
lambda_full[stage0_epochs:stage0_epochs+stage1_epochs] = lambda_curve
lambda_full[stage0_epochs+stage1_epochs:] = 1.0

ax6.plot(epochs, lambda_full, 'purple', linewidth=2.5, label=r'$\lambda(t)$')
ax6.fill_between(epochs, 0, lambda_full, alpha=0.3, color='purple')

ax6.axvline(stage0_epochs, color='gray', linestyle='--', linewidth=1, alpha=0.6)
ax6.axvline(stage0_epochs+stage1_epochs, color='gray', linestyle='--', linewidth=1, alpha=0.6)

ax6.set_xlabel('Epoch')
ax6.set_ylabel(r'Annealing Coefficient $\lambda(t)$')
ax6.set_title('(f) Cosine Annealing Schedule')
ax6.legend(loc='center right', fontsize=10)
ax6.grid(True, alpha=0.3)
ax6.set_ylim([-0.05, 1.1])

# Add stage annotations
ax6.text(stage0_epochs/2, 0.95, 'Stage 1\n(Image-cond)', ha='center', va='top', fontsize=9,
         bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.5))
ax6.text(stage0_epochs + stage1_epochs/2, 0.95, 'Stage 2\n(Mixed-cond)', ha='center', va='top', fontsize=9,
         bbox=dict(boxstyle='round', facecolor='lightblue', alpha=0.5))
ax6.text(stage0_epochs + stage1_epochs + stage2_epochs/2, 0.95, 'Stage 3\n(Label-cond)', ha='center', va='top', fontsize=9,
         bbox=dict(boxstyle='round', facecolor='lightgreen', alpha=0.5))

plt.tight_layout()

# Save figure
output_path = 'mia_training_curves.pdf'
plt.savefig(output_path, dpi=300, bbox_inches='tight')
print(f"Saved PDF: {output_path}")

# Save as EPS format (for LaTeX)
output_path_eps = output_path.replace('.pdf', '.eps')
plt.savefig(output_path_eps, format='eps', bbox_inches='tight')
print(f"Saved EPS: {output_path_eps}")

plt.show()
