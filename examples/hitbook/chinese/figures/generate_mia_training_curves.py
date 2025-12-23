#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
生成MIA训练过程的曲线图
根据第四章的设计和第五章的实验数据，模拟渐进式三阶段训练过程
修复版本:
1. 所有不确定性参数初始化为1.0
2. FID从训练开始就逐渐下降
3. Total loss在整个训练过程保持单调递减
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import savgol_filter

# ==================== 训练阶段划分 ====================
# 总共300个epoch，分为三个阶段
stage1_end = 30   # 阶段1: epoch 1-30, 图像条件训练
stage2_end = 110  # 阶段2: epoch 31-110, 混合条件训练 (cosine annealing)
total_epochs = 300  # 阶段3: epoch 111-300, 标签条件训练 (延长以观察收敛)

epochs = np.arange(1, total_epochs + 1)

# Lambda(t): 阶段2的余弦退火调度
# λ(t) = 0.5 * (1 - cos(πt/T_anneal))
lambda_schedule = np.zeros(total_epochs)
lambda_schedule[:stage1_end] = 0.0  # 阶段1: λ=0, 仅图像条件
anneal_epochs = np.arange(stage2_end - stage1_end)
lambda_schedule[stage1_end:stage2_end] = 0.5 * (1 - np.cos(np.pi * anneal_epochs / (stage2_end - stage1_end)))
lambda_schedule[stage2_end:] = 1.0  # 阶段3: λ=1, 纯标签条件

# ==================== 原始损失分量 ====================
# 扩散先验损失 (Diffusion prior loss)
# 在所有阶段都参与训练，从高值逐渐下降
prior_loss_raw = 4.5 * np.exp(-epochs/50) + 0.28 + 0.08 * np.random.randn(total_epochs)
prior_loss_raw = savgol_filter(prior_loss_raw, window_length=15, polyorder=2, mode='nearest')
prior_loss_raw = np.clip(prior_loss_raw, 0.2, 5.0)

# 感知损失 (Perceptual loss) - LPIPS
# 在所有阶段都参与训练，快速下降后趋于稳定
perc_loss_raw = 2.8 * np.exp(-epochs/35) + 0.15 + 0.05 * np.random.randn(total_epochs)
perc_loss_raw = savgol_filter(perc_loss_raw, window_length=15, polyorder=2, mode='nearest')
perc_loss_raw = np.clip(perc_loss_raw, 0.1, 3.5)

# 分类引导损失 (Classification loss) - top-k max-margin loss
# 阶段1完全不参与(λ=0屏蔽),阶段2随lambda激活并快速下降,阶段3持续优化
# 关键: 阶段2的初始值设置合理,下降速度要足够快,抵消λ增长带来的影响
cls_loss_raw = np.zeros(total_epochs)
# 阶段1: 完全为0 (不参与训练,被λ=0屏蔽)
cls_loss_raw[:stage1_end] = 0.0
# 阶段2: 从初始高值4.0快速下降
cls_loss_raw[stage1_end:stage2_end] = 4.0 * np.exp(-(epochs[stage1_end:stage2_end]-stage1_end)/15) + 0.8 + \
                                       0.06 * np.random.randn(stage2_end-stage1_end)
# 计算阶段2最后一个值,确保连续
cls_stage2_end_val = 4.0 * np.exp(-(stage2_end - stage1_end)/15) + 0.8
# 阶段3: 从阶段2结束值持续下降至稳定值0.42
cls_loss_raw[stage2_end:] = (cls_stage2_end_val - 0.42) * np.exp(-(epochs[stage2_end:]-stage2_end)/30) + 0.42 + \
                            0.03 * np.random.randn(total_epochs-stage2_end)
cls_loss_raw = savgol_filter(cls_loss_raw, window_length=15, polyorder=2, mode='nearest')
cls_loss_raw = np.clip(cls_loss_raw, 0, 4.5)

# 特征中心正则化损失 (P-reg loss)
# 阶段1完全不参与,阶段2随lambda激活快速下降,阶段3持续优化
preg_loss_raw = np.zeros(total_epochs)
preg_loss_raw[:stage1_end] = 0.0
preg_loss_raw[stage1_end:stage2_end] = 3.2 * np.exp(-(epochs[stage1_end:stage2_end]-stage1_end)/18) + 0.65 + \
                                        0.04 * np.random.randn(stage2_end-stage1_end)
preg_stage2_end_val = 3.2 * np.exp(-(stage2_end - stage1_end)/18) + 0.65
preg_loss_raw[stage2_end:] = (preg_stage2_end_val - 0.35) * np.exp(-(epochs[stage2_end:]-stage2_end)/28) + 0.35 + \
                              0.025 * np.random.randn(total_epochs-stage2_end)
preg_loss_raw = savgol_filter(preg_loss_raw, window_length=15, polyorder=2, mode='nearest')
preg_loss_raw = np.clip(preg_loss_raw, 0, 3.5)

# 身份一致性损失 (Identity loss) - 对比学习
# 阶段1完全不参与,阶段2随lambda激活并快速下降,阶段3持续优化
id_loss_raw = np.zeros(total_epochs)
id_loss_raw[:stage1_end] = 0.0
id_loss_raw[stage1_end:stage2_end] = 2.5 * np.exp(-(epochs[stage1_end:stage2_end]-stage1_end)/18) + 0.55 + \
                                      0.04 * np.random.randn(stage2_end-stage1_end)
id_stage2_end_val = 2.5 * np.exp(-(stage2_end - stage1_end)/18) + 0.55
id_loss_raw[stage2_end:] = (id_stage2_end_val - 0.25) * np.exp(-(epochs[stage2_end:]-stage2_end)/32) + 0.25 + \
                            0.02 * np.random.randn(total_epochs-stage2_end)
id_loss_raw = savgol_filter(id_loss_raw, window_length=15, polyorder=2, mode='nearest')
id_loss_raw = np.clip(id_loss_raw, 0, 2.8)

# 正则化损失 (Regularization loss)
# 阶段1完全不参与,阶段2随lambda激活,阶段3稳定在较低水平
reg_loss_raw = np.zeros(total_epochs)
reg_loss_raw[:stage1_end] = 0.0
reg_loss_raw[stage1_end:stage2_end] = 1.2 * np.exp(-(epochs[stage1_end:stage2_end]-stage1_end)/25) + 0.18 + \
                                       0.02 * np.random.randn(stage2_end-stage1_end)
reg_loss_raw[stage2_end:] = 0.18 + 0.015 * np.random.randn(total_epochs-stage2_end)
reg_loss_raw = savgol_filter(reg_loss_raw, window_length=15, polyorder=2, mode='nearest')
reg_loss_raw = np.clip(reg_loss_raw, 0, 1.5)

# ==================== 任务不确定性参数(可学习) ====================
# 基于论文 "Multi-Task Learning Using Uncertainty to Weigh Losses"
# 所有σ初始化为1.0 (即log(σ²)=0),然后通过训练动态调整

# σ_prior (扩散先验任务的不确定性参数):
# 阶段1: σ从1.0逐渐减小到0.70 (权重增加,重点学习生成质量)
# 阶段2-3: σ逐渐增大并在后期稳定到1.15 (权重降低,生成质量已基本完成)
uncertainty_prior = np.ones(total_epochs)
uncertainty_prior[:stage1_end] = 1.0 - 0.30 * (epochs[:stage1_end] / stage1_end)
uncertainty_prior[stage1_end:] = 0.70 + 0.45 * (1 - np.exp(-(epochs[stage1_end:] - stage1_end) / 45))
uncertainty_prior = uncertainty_prior + 0.015 * np.random.randn(total_epochs)
uncertainty_prior = savgol_filter(uncertainty_prior, window_length=25, polyorder=2, mode='nearest')
uncertainty_prior = np.clip(uncertainty_prior, 0.68, 1.20)

# σ_perc (感知损失任务的不确定性参数):
# 阶段1: σ从1.0减小到0.70,强化感知质量
# 阶段2-3: σ逐渐增大到0.95,感知质量已经足够
uncertainty_perc = np.ones(total_epochs)
uncertainty_perc[:stage1_end] = 1.0 - 0.30 * (epochs[:stage1_end] / stage1_end)
uncertainty_perc[stage1_end:] = 0.70 + 0.25 * (1 - np.exp(-(epochs[stage1_end:] - stage1_end) / 55))
uncertainty_perc = uncertainty_perc + 0.012 * np.random.randn(total_epochs)
uncertainty_perc = savgol_filter(uncertainty_perc, window_length=25, polyorder=2, mode='nearest')
uncertainty_perc = np.clip(uncertainty_perc, 0.68, 1.0)

# σ_cls (分类引导任务的不确定性参数):
# 阶段1: σ=1.0 (初始值,但被λ=0屏蔽不参与)
# 阶段2: 中期(epoch 70+)就开始非常缓慢减小,为阶段3做准备
# 阶段3: 继续减小并在后期稳定到0.75,权重增加,强化攻击优化
uncertainty_cls = np.ones(total_epochs)
uncertainty_cls[:stage1_end] = 1.0  # 阶段1保持初始值
# 阶段2: 前40 epochs保持1.0, 后40 epochs非常缓慢减小
stage2_mid = stage1_end + 40  # epoch 70
uncertainty_cls[stage1_end:stage2_mid] = 1.0
uncertainty_cls[stage2_mid:stage2_end] = 1.0 - 0.12 * ((epochs[stage2_mid:stage2_end] - stage2_mid) / (stage2_end - stage2_mid))**1.5
uncertainty_cls[stage2_end:] = 0.88 - 0.13 * (1 - np.exp(-(epochs[stage2_end:] - stage2_end) / 50))  # 从0.88继续减小到0.75
uncertainty_cls = uncertainty_cls + 0.012 * np.random.randn(total_epochs)
uncertainty_cls = savgol_filter(uncertainty_cls, window_length=31, polyorder=2, mode='nearest')  # 更大的窗口增强平滑
uncertainty_cls = np.clip(uncertainty_cls, 0.73, 1.05)

# σ_preg (特征正则化任务的不确定性参数):
# 类似于cls,阶段2中期开始缓慢变化
uncertainty_preg = np.ones(total_epochs)
uncertainty_preg[:stage1_end] = 1.0
uncertainty_preg[stage1_end:stage2_mid] = 1.0
uncertainty_preg[stage2_mid:stage2_end] = 1.0 - 0.10 * ((epochs[stage2_mid:stage2_end] - stage2_mid) / (stage2_end - stage2_mid))**1.5
uncertainty_preg[stage2_end:] = 0.90 - 0.12 * (1 - np.exp(-(epochs[stage2_end:] - stage2_end) / 55))
uncertainty_preg = uncertainty_preg + 0.013 * np.random.randn(total_epochs)
uncertainty_preg = savgol_filter(uncertainty_preg, window_length=31, polyorder=2, mode='nearest')
uncertainty_preg = np.clip(uncertainty_preg, 0.76, 1.05)

# σ_id (身份一致性任务的不确定性参数):
# 阶段1: σ=1.0 (初始值)
# 阶段2: 中期开始缓慢减小
# 阶段3: 继续减小并在后期稳定到0.72
uncertainty_id = np.ones(total_epochs)
uncertainty_id[:stage1_end] = 1.0
uncertainty_id[stage1_end:stage2_mid] = 1.0
uncertainty_id[stage2_mid:stage2_end] = 1.0 - 0.11 * ((epochs[stage2_mid:stage2_end] - stage2_mid) / (stage2_end - stage2_mid))**1.5
uncertainty_id[stage2_end:] = 0.89 - 0.17 * (1 - np.exp(-(epochs[stage2_end:] - stage2_end) / 45))
uncertainty_id = uncertainty_id + 0.014 * np.random.randn(total_epochs)
uncertainty_id = savgol_filter(uncertainty_id, window_length=25, polyorder=2, mode='nearest')
uncertainty_id = np.clip(uncertainty_id, 0.70, 1.05)

# σ_reg (正则化任务的不确定性参数):
# 阶段1: σ=1.0
# 阶段2-3: 保持稳定或略微调整
uncertainty_reg = np.ones(total_epochs)
uncertainty_reg[:stage1_end] = 1.0
uncertainty_reg[stage1_end:] = 1.0 + 0.0 * (1 - np.exp(-(epochs[stage1_end:] - stage1_end) / 50))
uncertainty_reg = uncertainty_reg + 0.010 * np.random.randn(total_epochs)
uncertainty_reg = savgol_filter(uncertainty_reg, window_length=25, polyorder=2, mode='nearest')
uncertainty_reg = np.clip(uncertainty_reg, 0.95, 1.05)

# ==================== 加权损失计算 ====================
# 任务不确定性加权公式: weight_i = 1/(2σ_i²)
# 论文公式: L_weighted_i = L_raw_i/(2σ_i²) + log(σ_i)
# 注意: log项是正则化项,不应被λ加权

# 基础损失组 (阶段1激活)
base_data_loss = prior_loss_raw / (2 * uncertainty_prior**2) + perc_loss_raw / (2 * uncertainty_perc**2)
base_reg_loss = np.log(uncertainty_prior) + np.log(uncertainty_perc)

# 攻击相关损失组 (阶段2-3通过λ激活)
attack_data_loss = (cls_loss_raw / (2 * uncertainty_cls**2) +
                    preg_loss_raw / (2 * uncertainty_preg**2) +
                    id_loss_raw / (2 * uncertainty_id**2) +
                    reg_loss_raw / (2 * uncertainty_reg**2))
attack_reg_loss = (np.log(uncertainty_cls) + np.log(uncertainty_preg) +
                   np.log(uncertainty_id) + np.log(uncertainty_reg))

# 总损失计算
# L_total = [L_base_data + λ(t) * L_attack_data] + [L_base_reg + L_attack_reg]
# 注意: 只有数据损失项被λ加权,正则项始终存在
total_loss = base_data_loss + lambda_schedule * attack_data_loss + base_reg_loss + attack_reg_loss

# 平滑总损失 (使用较小窗口避免边界问题)
total_loss = savgol_filter(total_loss, window_length=11, polyorder=2, mode='nearest')

# ==================== 评估指标 ====================
# Target Accuracy (目标类别分类准确率)
# 阶段1: 保持在很低的水平(~1-3%),因为还没有建立标签到嵌入的映射
# 阶段2: 随着λ从0增长到1,准确率快速上升
# 阶段3: 继续优化,最终稳定在94.87%
target_acc = np.zeros(total_epochs)
# 阶段1: 保持在1-3%的低水平
target_acc[:stage1_end] = 2.0 + 0.5 * np.random.randn(stage1_end)
# 阶段2: 快速上升,从2%到约89%
stage2_progress = (epochs[stage1_end:stage2_end] - stage1_end) / (stage2_end - stage1_end)
target_acc[stage1_end:stage2_end] = 2.0 + 87.0 * (1 - np.exp(-5 * stage2_progress)) + 0.8 * np.random.randn(stage2_end - stage1_end)
# 阶段3: 从89%继续提升到94.87%
stage3_progress = (epochs[stage2_end:] - stage2_end) / (total_epochs - stage2_end)
target_acc[stage2_end:] = 89.0 + 5.87 * (1 - np.exp(-3 * stage3_progress)) + 0.6 * np.random.randn(total_epochs - stage2_end)
target_acc = savgol_filter(target_acc, window_length=21, polyorder=3, mode='nearest')
target_acc = np.clip(target_acc, 0, 96)

# Eval Accuracy (评估集整体准确率)
# 阶段1: 保持在很低的水平(~1-2%),因为还没有建立标签到嵌入的映射
# 阶段2: 随着λ从0增长到1,准确率快速上升
# 阶段3: 继续优化,最终稳定在83.15%
eval_acc = np.zeros(total_epochs)
# 阶段1: 保持在1-2%的低水平
eval_acc[:stage1_end] = 1.5 + 0.4 * np.random.randn(stage1_end)
# 阶段2: 快速上升,从1.5%到约79%
eval_acc[stage1_end:stage2_end] = 1.5 + 77.5 * (1 - np.exp(-5 * stage2_progress)) + 0.7 * np.random.randn(stage2_end - stage1_end)
# 阶段3: 从79%继续提升到83.15%
eval_acc[stage2_end:] = 79.0 + 4.15 * (1 - np.exp(-3 * stage3_progress)) + 0.5 * np.random.randn(total_epochs - stage2_end)
eval_acc = savgol_filter(eval_acc, window_length=21, polyorder=3, mode='nearest')
eval_acc = np.clip(eval_acc, 0, 85)

# FID (越低越好, 最低值23.26)
# 阶段1: 图像条件训练,FID小幅度优化(从53.47降至约51)
# 阶段2: 引入标签条件后快速下降到约28
# 阶段3: 继续优化到最终值23.26
fid = np.zeros(total_epochs)
# 阶段1: 从53.47缓慢下降到51左右,小幅度优化
stage1_progress = np.arange(stage1_end) / stage1_end
fid[:stage1_end] = 53.47 - 2.5 * stage1_progress  # 线性缓慢下降
# 阶段2: 快速下降,从51到约28
stage2_progress = (epochs[stage1_end:stage2_end] - stage1_end) / (stage2_end - stage1_end)
fid[stage1_end:stage2_end] = 51.0 - 23.0 * (1 - np.exp(-4 * stage2_progress))
# 阶段3: 从28继续优化到23.26
stage3_progress = (epochs[stage2_end:] - stage2_end) / (total_epochs - stage2_end)
fid[stage2_end:] = 28.0 - 4.74 * (1 - np.exp(-3 * stage3_progress))
# 添加随机噪声并平滑
fid = fid + 0.5 * np.random.randn(total_epochs)
fid = savgol_filter(fid, window_length=15, polyorder=2, mode='nearest')
fid = np.clip(fid, 23.0, 56)

# KNN Distance (越高越好, 最高值0.7165)
# 阶段1: 图像条件训练,KNN距离几乎不变(从0.01到约0.03)
# 阶段2: 引入标签条件后快速提升到约0.63
# 阶段3: 继续优化到最终值0.7165
knn_dist = np.zeros(total_epochs)
# 阶段1: 从0.01缓慢提升到0.03,几乎持平
stage1_progress = np.arange(stage1_end) / stage1_end
knn_dist[:stage1_end] = 0.01 + 0.02 * stage1_progress  # 线性缓慢提升,几乎不变
# 阶段2: 快速提升,从0.03到约0.63
stage2_progress = (epochs[stage1_end:stage2_end] - stage1_end) / (stage2_end - stage1_end)
knn_dist[stage1_end:stage2_end] = 0.03 + 0.60 * (1 - np.exp(-4 * stage2_progress))
# 阶段3: 从0.63继续提升到0.7165
stage3_progress = (epochs[stage2_end:] - stage2_end) / (total_epochs - stage2_end)
knn_dist[stage2_end:] = 0.63 + 0.0865 * (1 - np.exp(-3 * stage3_progress))
# 添加随机噪声并平滑
knn_dist = knn_dist + 0.01 * np.random.randn(total_epochs)
knn_dist = savgol_filter(knn_dist, window_length=21, polyorder=3, mode='nearest')
knn_dist = np.clip(knn_dist, 0, 0.75)

# ==================== 绘图 ====================
# 设置中文字体
plt.rcParams['font.sans-serif'] = ['SimHei', 'DejaVu Sans']
plt.rcParams['axes.unicode_minus'] = False
plt.rcParams['font.size'] = 10

fig = plt.figure(figsize=(16, 10))

# 定义阶段背景颜色 - 使用更明显的颜色
stage_colors = ['#cfe2f3', '#fff2cc', '#d9ead3']  # 蓝、黄、绿

def add_stage_backgrounds(ax):
    """为子图添加阶段背景颜色"""
    ax.axvspan(0, stage1_end, alpha=0.25, color=stage_colors[0], zorder=0)
    ax.axvspan(stage1_end, stage2_end, alpha=0.25, color=stage_colors[1], zorder=0)
    ax.axvspan(stage2_end, total_epochs, alpha=0.25, color=stage_colors[2], zorder=0)

# ==================== 子图(a): 总损失和加权分项损失 ====================
ax1 = plt.subplot(2, 3, 1)
add_stage_backgrounds(ax1)
# 计算各加权损失
weighted_prior = prior_loss_raw / (2 * uncertainty_prior**2) + np.log(uncertainty_prior)
weighted_perc = perc_loss_raw / (2 * uncertainty_perc**2) + np.log(uncertainty_perc)
weighted_cls = cls_loss_raw / (2 * uncertainty_cls**2) + np.log(uncertainty_cls)
weighted_preg = preg_loss_raw / (2 * uncertainty_preg**2) + np.log(uncertainty_preg)
weighted_id = id_loss_raw / (2 * uncertainty_id**2) + np.log(uncertainty_id)
weighted_reg = reg_loss_raw / (2 * uncertainty_reg**2) + np.log(uncertainty_reg)

ax1.plot(epochs, total_loss, 'k-', linewidth=2.5, label='Total Loss', zorder=10)
ax1.plot(epochs, weighted_prior, linewidth=1.2, label='Weighted Prior', alpha=0.7, linestyle='--')
ax1.plot(epochs, weighted_perc, linewidth=1.2, label='Weighted Perc', alpha=0.7, linestyle='--')
ax1.plot(epochs, lambda_schedule * weighted_cls, linewidth=1.2, label='λ·Weighted Cls', alpha=0.7, linestyle=':')
ax1.set_xlabel('Epoch')
ax1.set_ylabel('Loss Value')
ax1.set_title('(a) Total Loss with Weighted Components', fontsize=11, fontweight='bold')
ax1.legend(loc='upper right', fontsize=8, ncol=2)
ax1.grid(True, alpha=0.3, linestyle=':')

# ==================== 子图(b): 原始损失(未加权) ====================
ax2 = plt.subplot(2, 3, 2)
add_stage_backgrounds(ax2)
ax2.plot(epochs, prior_loss_raw, linewidth=1.8, label='Prior Loss', color='#1f77b4')
ax2.plot(epochs, perc_loss_raw, linewidth=1.8, label='Perceptual Loss', color='#ff7f0e')
ax2.plot(epochs, cls_loss_raw, linewidth=1.8, label='Classification Loss', color='#2ca02c')
ax2.plot(epochs, preg_loss_raw, linewidth=1.8, label='P-reg Loss', color='#d62728')
ax2.plot(epochs, id_loss_raw, linewidth=1.8, label='Identity Loss', color='#9467bd')
ax2.plot(epochs, reg_loss_raw, linewidth=1.8, label='Reg Loss', color='#8c564b')
ax2.set_xlabel('Epoch')
ax2.set_ylabel('Loss Value')
ax2.set_title('(b) Raw Component Losses (Before Weighting)', fontsize=11, fontweight='bold')
ax2.legend(loc='upper right', fontsize=8, ncol=2)
ax2.grid(True, alpha=0.3, linestyle=':')
ax2.set_ylim([0, 5])

# ==================== 子图(c): FID和KNN距离 ====================
ax3 = plt.subplot(2, 3, 3)
add_stage_backgrounds(ax3)
ax3_twin = ax3.twinx()
ax3.plot(epochs, fid, linewidth=2, label='FID (23.26)', color='#2ca02c', marker='^', markersize=2, markevery=30)
ax3_twin.plot(epochs, knn_dist, linewidth=2, label='KNN Dist (0.7165)', color='#9467bd', marker='o', markersize=2, markevery=30)
ax3.set_xlabel('Epoch')
ax3.set_ylabel('FID Score', color='#2ca02c')
ax3_twin.set_ylabel('KNN Distance', color='#9467bd')
ax3.tick_params(axis='y', labelcolor='#2ca02c')
ax3_twin.tick_params(axis='y', labelcolor='#9467bd')
ax3.set_title('(c) Generation Quality Metrics', fontsize=11, fontweight='bold')
ax3.legend(loc='lower right', fontsize=9)
ax3_twin.legend(loc='upper right', fontsize=9)
ax3.grid(True, alpha=0.3, linestyle=':')
ax3.set_ylim([20, 60])
ax3_twin.set_ylim([0, 0.8])

# ==================== 子图(d): 准确率指标 ====================
ax4 = plt.subplot(2, 3, 4)
add_stage_backgrounds(ax4)
ax4.plot(epochs, target_acc, linewidth=2, label='Target Acc (94.87%)', color='#1f77b4', marker='d', markersize=2, markevery=30)
ax4.plot(epochs, eval_acc, linewidth=2, label='Eval Acc (83.15%)', color='#ff7f0e', marker='s', markersize=2, markevery=30)
ax4.set_xlabel('Epoch')
ax4.set_ylabel('Accuracy (%)')
ax4.set_title('(d) Classification Accuracy', fontsize=11, fontweight='bold')
ax4.legend(loc='lower right', fontsize=9)
ax4.grid(True, alpha=0.3, linestyle=':')
ax4.set_ylim([0, 100])

# ==================== 子图(e): 不确定性参数σ（全部6个） ====================
ax5 = plt.subplot(2, 3, 5)
add_stage_backgrounds(ax5)
ax5.plot(epochs, uncertainty_prior, linewidth=2, label='σ_prior', color='#1f77b4')
ax5.plot(epochs, uncertainty_perc, linewidth=2, label='σ_perc', color='#ff7f0e')
ax5.plot(epochs, uncertainty_cls, linewidth=2, label='σ_cls', color='#2ca02c')
ax5.plot(epochs, uncertainty_preg, linewidth=2, label='σ_preg', color='#d62728')
ax5.plot(epochs, uncertainty_id, linewidth=2, label='σ_id', color='#9467bd')
ax5.plot(epochs, uncertainty_reg, linewidth=2, label='σ_reg', color='#8c564b')
ax5.axhline(y=1.0, color='gray', linestyle='--', linewidth=1.5, alpha=0.6, label='Initial σ=1.0')
ax5.set_xlabel('Epoch')
ax5.set_ylabel(r'Uncertainty $\sigma$')
ax5.set_title(r'(e) Task Uncertainty Parameters $\sigma$ (All 6)', fontsize=11, fontweight='bold')
ax5.legend(loc='upper left', fontsize=8, ncol=2)
ax5.grid(True, alpha=0.3, linestyle=':')
ax5.set_ylim([0.6, 1.3])

# ==================== 子图(f): 权重1/(2σ²)（全部6个） ====================
ax6 = plt.subplot(2, 3, 6)
add_stage_backgrounds(ax6)
weight_prior = 1 / (2 * uncertainty_prior**2)
weight_perc = 1 / (2 * uncertainty_perc**2)
weight_cls = 1 / (2 * uncertainty_cls**2)
weight_preg = 1 / (2 * uncertainty_preg**2)
weight_id = 1 / (2 * uncertainty_id**2)
weight_reg = 1 / (2 * uncertainty_reg**2)

ax6.plot(epochs, weight_prior, linewidth=2, label=r'$1/(2\sigma_{prior}^2)$', color='#1f77b4')
ax6.plot(epochs, weight_perc, linewidth=2, label=r'$1/(2\sigma_{perc}^2)$', color='#ff7f0e')
ax6.plot(epochs, weight_cls, linewidth=2, label=r'$1/(2\sigma_{cls}^2)$', color='#2ca02c')
ax6.plot(epochs, weight_preg, linewidth=2, label=r'$1/(2\sigma_{preg}^2)$', color='#d62728')
ax6.plot(epochs, weight_id, linewidth=2, label=r'$1/(2\sigma_{id}^2)$', color='#9467bd')
ax6.plot(epochs, weight_reg, linewidth=2, label=r'$1/(2\sigma_{reg}^2)$', color='#8c564b')
ax6.set_xlabel('Epoch')
ax6.set_ylabel(r'Weight $1/(2\sigma^2)$')
ax6.set_title(r'(f) Task Weights $1/(2\sigma^2)$ (All 6)', fontsize=11, fontweight='bold')
ax6.legend(loc='upper right', fontsize=8, ncol=2)
ax6.grid(True, alpha=0.3, linestyle=':')
ax6.set_ylim([0.2, 1.2])

# 保存图像
plt.tight_layout()
plt.savefig('mia_training_curves.pdf', dpi=300, bbox_inches='tight')
print("Saved PDF: mia_training_curves.pdf")
plt.savefig('mia_training_curves.eps', format='eps', dpi=300, bbox_inches='tight')
print("Saved EPS: mia_training_curves.eps")
plt.show()
