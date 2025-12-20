#!/usr/bin/env python3
"""
生成TIA模板重建示例图 - 展示从ArcFace特征模板重建的人脸图像
使用随机生成的占位图像模拟实验结果
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

# 使用默认字体配置
plt.rcParams['font.size'] = 9
plt.rcParams['axes.unicode_minus'] = False

# 设置随机种子
np.random.seed(42)

def generate_placeholder_face(seed=None):
    """生成占位人脸图像"""
    if seed is not None:
        np.random.seed(seed)
    
    # 创建112x112的图像
    img = np.random.rand(112, 112, 3) * 0.3 + 0.4
    
    # 添加椭圆形人脸轮廓
    y, x = np.ogrid[:112, :112]
    mask = ((x - 56)**2 / 30**2 + (y - 56)**2 / 40**2) <= 1
    img[mask] = img[mask] * 0.7 + 0.2
    
    # 添加眼睛区域（暗色）
    for eye_x in [40, 72]:
        eye_mask = ((x - eye_x)**2 + (y - 40)**2) <= 36
        img[eye_mask] = img[eye_mask] * 0.4
    
    # 添加鼻子区域
    nose_mask = ((x - 56)**2 / 8**2 + (y - 56)**2 / 15**2) <= 1
    img[nose_mask] = img[nose_mask] * 0.8 + 0.1
    
    # 添加嘴巴区域
    mouth_mask = ((x - 56)**2 / 15**2 + (y - 75)**2 / 5**2) <= 1
    img[mouth_mask] = img[mouth_mask] * 0.5
    
    return np.clip(img, 0, 1)

def generate_heatmap(seed=None):
    """生成Grad-CAM热力图"""
    if seed is not None:
        np.random.seed(seed)
    
    # 创建热力图
    y, x = np.ogrid[:112, :112]
    
    # 中心点（面部关键区域）
    centers = [(56, 40), (40, 40), (72, 40), (56, 75)]
    heatmap = np.zeros((112, 112))
    
    for cx, cy in centers:
        dist = np.sqrt((x - cx)**2 + (y - cy)**2)
        heatmap += np.exp(-dist**2 / 200)
    
    # 归一化
    heatmap = (heatmap - heatmap.min()) / (heatmap.max() - heatmap.min())
    
    return heatmap

# ==================== 创建图像 ====================

fig = plt.figure(figsize=(16, 10))

# 设置标题
fig.suptitle('TIA Template Reconstruction Examples', fontsize=14, fontweight='bold', y=0.98)

# 创建3行9列的网格 (3个示例 x 3种显示)
num_examples = 9
num_cols = 9

for i in range(num_examples):
    # 真实图像（模拟）
    ax1 = plt.subplot(3, num_cols, i + 1)
    real_img = generate_placeholder_face(seed=i*3)
    ax1.imshow(real_img)
    ax1.axis('off')
    if i == 0:
        ax1.set_title('Real Image', fontsize=10, fontweight='bold')
    ax1.text(0.5, -0.1, f'ID-{i+1:02d}', transform=ax1.transAxes, 
             ha='center', va='top', fontsize=8)
    
    # 重建图像（模拟）
    ax2 = plt.subplot(3, num_cols, i + 1 + num_cols)
    recon_img = generate_placeholder_face(seed=i*3+1)
    # 添加轻微差异模拟重建
    recon_img = recon_img * 0.95 + np.random.rand(112, 112, 3) * 0.05
    recon_img = np.clip(recon_img, 0, 1)
    ax2.imshow(recon_img)
    ax2.axis('off')
    if i == 0:
        ax2.set_title('Reconstructed', fontsize=10, fontweight='bold')
    
    # 添加指标文本
    id_pres = 92 + np.random.rand() * 6
    fid = 15 + np.random.rand() * 5
    ax2.text(0.5, -0.1, f'ID-Pres: {id_pres:.1f}%', transform=ax2.transAxes,
             ha='center', va='top', fontsize=7)
    ax2.text(0.5, -0.18, f'FID: {fid:.1f}', transform=ax2.transAxes,
             ha='center', va='top', fontsize=7)
    
    # Grad-CAM热力图
    ax3 = plt.subplot(3, num_cols, i + 1 + 2*num_cols)
    heatmap = generate_heatmap(seed=i*3+2)
    ax3.imshow(recon_img, alpha=0.5)
    ax3.imshow(heatmap, cmap='jet', alpha=0.5)
    ax3.axis('off')
    if i == 0:
        ax3.set_title('Grad-CAM', fontsize=10, fontweight='bold')

# 添加行标签
fig.text(0.02, 0.75, 'Original', rotation=90, va='center', fontsize=11, fontweight='bold')
fig.text(0.02, 0.50, 'Reconstruction', rotation=90, va='center', fontsize=11, fontweight='bold')
fig.text(0.02, 0.25, 'Attention Map', rotation=90, va='center', fontsize=11, fontweight='bold')

# 添加说明文本
fig.text(0.5, 0.02, 'Note: Placeholder images for demonstration. Replace with actual experimental results.', 
         ha='center', fontsize=8, style='italic', color='gray')

plt.subplots_adjust(left=0.05, right=0.98, top=0.95, bottom=0.05, hspace=0.3, wspace=0.15)

# 保存图像
output_path = 'tia_reconstruction_examples.pdf'
plt.savefig(output_path, dpi=300, bbox_inches='tight')
print(f"Saved PDF: {output_path}")

output_path_eps = output_path.replace('.pdf', '.eps')
plt.savefig(output_path_eps, format='eps', bbox_inches='tight')
print(f"Saved EPS: {output_path_eps}")

plt.show()
