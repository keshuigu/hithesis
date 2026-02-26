# 图片资源说明

本目录用于存放答辩PPT中使用的图片资源。

## 图片命名规范

建议按照以下规范命名图片文件：

### TIA相关图片
- `template1.jpg`, `template2.jpg` - 目标特征模板示例
- `ours_tia1.jpg`, `ours_tia2.jpg` - 本文TIA方法结果
- `gafar1.jpg`, `gafar2.jpg` - GMI-GaFaR方法结果
- `nbnet1.jpg`, `nbnet2.jpg` - NBNet方法结果

### MIA相关图片  
- `ours_mia1.jpg`, `ours_mia2.jpg` - 本文MIA方法结果
- `plgmi1.jpg`, `plgmi2.jpg` - PLG-MI方法结果
- `kedmi1.jpg`, `kedmi2.jpg` - KED-MI方法结果

### 架构图和流程图
- `tia_architecture.png` - TIA方法架构图
- `mia_architecture.png` - MIA方法架构图
- `diffusion_process.png` - 扩散过程示意图
- `angular_loss.png` - 角度损失几何示意图
- `training_pipeline.png` - 训练流程图

### 实验结果图
- `success_rate_chart.png` - 攻击成功率对比图
- `fid_comparison.png` - FID指标对比图
- `ablation_study.png` - 消融实验结果图

## 图片格式要求

- **推荐格式**: PNG（适合图表）、JPG（适合照片）
- **分辨率**: 至少300 DPI，推荐600 DPI以上
- **尺寸**: 宽度建议1920px以上，便于在大屏幕上显示
- **文件大小**: 单个文件不超过5MB，保证编译效率

## 使用方法

在PPT中插入图片：

```latex
% 单个图片
\includegraphics[width=0.5\textwidth]{figures/your_image.png}

% 并排图片
\begin{columns}
\begin{column}{0.5\textwidth}
\includegraphics[width=\textwidth]{figures/image1.png}
\end{column}
\begin{column}{0.5\textwidth}
\includegraphics[width=\textwidth]{figures/image2.png}
\end{column>
\end{columns>

% 图片with标题
\begin{figure}
\centering
\includegraphics[width=0.8\textwidth]{figures/result.png}
\caption{实验结果对比}
\end{figure>
```

## 注意事项

1. **版权问题**: 确保所有图片拥有使用权限
2. **清晰度**: 图片在投影时应保持清晰可读
3. **对比度**: 确保图片在投影环境下对比度足够
4. **一致性**: 保持同类图片的风格和色彩统一
5. **文件路径**: 避免中文路径和特殊字符

## 示例图片制作工具

- **矢量图**: Inkscape, Adobe Illustrator
- **位图处理**: GIMP, Adobe Photoshop  
- **图表制作**: Python matplotlib, R ggplot2
- **架构图**: Draw.io, Visio, Lucidchart
- **学术图表**: MATLAB, Origin, TikZ/PGF

## 占位符图片

如果暂时没有实际图片，可以使用占位符：

```latex
% 创建占位符
\begin{tikzpicture}
\draw[thick] (0,0) rectangle (4,3);
\node at (2,1.5) {图片占位符};
\node at (2,1) {\small 400×300px};
\end{tikzpicture}
```