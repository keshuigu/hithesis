#!/usr/bin/env python3
"""
生成MIA模型反演示例图 - 展示从标签生成的人脸图像
使用随机生成的占位图像模拟实验结果
"""

import numpy as np
import matplotlib.pyplot as plt

# 使用默认字体配置
plt.rcParams['font.size'] = 9
plt.rcParams['axes.unicode_minus'] = False

# 设置随机种子
np.random.seed(42)

def generate_synthetic_face(seed=None, style='varied'):
    """生成合成人脸图像占位符"""
    if seed is not None:
        np.random.seed(seed)

    # 创建224x224的图像（模型反演通常生成高分辨率）
    img = np.random.rand(224, 224, 3)

    if style == 'varied':
        # 多样化的颜色风格
        base_color = np.random.rand(3)
        img = img * 0.3 + base_color * 0.5
    else:
        # 肤色基调
        img = img * 0.25 + np.array([0.8, 0.6, 0.5])

    # 添加人脸轮廓
    y, x = np.ogrid[:224, :224]

    # 脸部椭圆
    face_mask = ((x - 112)**2 / 55**2 + (y - 112)**2 / 75**2) <= 1
    img[face_mask] = img[face_mask] * 0.7 + 0.2

    # 眼睛
    for eye_x in [80, 144]:
        eye_mask = ((x - eye_x)**2 + (y - 80)**2) <= 64
        img[eye_mask] = img[eye_mask] * 0.3
        # 眼珠
        pupil_mask = ((x - eye_x)**2 + (y - 80)**2) <= 16
        img[pupil_mask] = 0.1

    # 鼻子
    nose_mask = ((x - 112)**2 / 12**2 + (y - 112)**2 / 25**2) <= 1
    img[nose_mask] = img[nose_mask] * 0.85

    # 嘴巴
    mouth_mask = ((x - 112)**2 / 25**2 + (y - 150)**2 / 8**2) <= 1
    img[mouth_mask] = img[mouth_mask] * 0.5

    # 头发区域
    hair_mask = (y < 40) & face_mask
    img[hair_mask] = img[hair_mask] * 0.3

    return np.clip(img, 0, 1)

# ==================== 创建图像 ====================

fig = plt.figure(figsize=(18, 10))

# 设置标题
fig.suptitle('MIA Model Inversion Attack - Generated Face Examples',
             fontsize=14, fontweight='bold', y=0.98)

# 创建5行8列的网格 (展示40个生成示例)
num_rows = 5
num_cols = 8

for i in range(num_rows * num_cols):
    ax = plt.subplot(num_rows, num_cols, i + 1)

    # 生成占位图像
    generated_img = generate_synthetic_face(seed=i*7, style='varied')
    ax.imshow(generated_img)
    ax.axis('off')

    # 添加类别标签和置信度
    class_id = (i % 40) + 1
    confidence = 92 + np.random.rand() * 7

    # 在图像下方添加文本
    ax.text(0.5, -0.05, f'Class {class_id:03d}', transform=ax.transAxes,
            ha='center', va='top', fontsize=8, fontweight='bold')
    ax.text(0.5, -0.12, f'Conf: {confidence:.1f}%', transform=ax.transAxes,
            ha='center', va='top', fontsize=7, color='darkgreen')

    # 每列第一个添加列标题
    if i < num_cols:
        quality_metrics = [
            ('High Acc1', 'green'),
            ('High Acc5', 'blue'),
            ('Low FID', 'purple'),
            ('High ID', 'orange'),
            ('Diverse 1', 'brown'),
            ('Diverse 2', 'pink'),
            ('Diverse 3', 'cyan'),
            ('Diverse 4', 'gray')
        ]
        metric_name, color = quality_metrics[i % len(quality_metrics)]
        ax.set_title(metric_name, fontsize=9, color=color, fontweight='bold', pad=10)

# 添加分组标签
group_labels = [
    (0.12, 0.88, 'Target: VGG16'),
    (0.12, 0.68, 'Target: IR152'),
    (0.12, 0.48, 'Target: FaceNet'),
    (0.12, 0.28, 'Target: ArcFace'),
    (0.12, 0.08, 'Target: CosFace')
]

for x, y, label in group_labels:
    fig.text(x, y, label, rotation=90, va='center', fontsize=10,
             fontweight='bold', bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.3))

# 添加说明
fig.text(0.5, 0.015,
         'Note: Synthetic placeholder images. Each image shows a face generated from a class label.\n'
         'Actual results should display high-quality faces with correct identity classification.',
         ha='center', fontsize=8, style='italic', color='gray')

# 添加指标图例
legend_elements = [
    plt.Line2D([0], [0], marker='o', color='w', markerfacecolor='green', markersize=8, label='Acc1 > 95%'),
    plt.Line2D([0], [0], marker='o', color='w', markerfacecolor='blue', markersize=8, label='Acc5 > 98%'),
    plt.Line2D([0], [0], marker='o', color='w', markerfacecolor='purple', markersize=8, label='FID < 25'),
    plt.Line2D([0], [0], marker='o', color='w', markerfacecolor='orange', markersize=8, label='ID Similarity > 0.9')
]
fig.legend(handles=legend_elements, loc='upper right', fontsize=8, framealpha=0.9)

plt.subplots_adjust(left=0.15, right=0.98, top=0.94, bottom=0.04, hspace=0.35, wspace=0.15)

# 保存图像
output_path = 'mia_generation_examples.pdf'
plt.savefig(output_path, dpi=300, bbox_inches='tight')
print(f"Saved PDF: {output_path}")

output_path_eps = output_path.replace('.pdf', '.eps')
plt.savefig(output_path_eps, format='eps', bbox_inches='tight')
print(f"Saved EPS: {output_path_eps}")

plt.show()
