# MIA训练曲线图插入说明

## 完成时间
2025年12月20日

## 插入位置
已将模拟的MIA训练曲线图插入到第五章"实验结果与性能分析"的以下位置：

**文件**: `body/5.Result.tex`  
**章节**: 5.4 MIA实验结果 → 5.4.3 关键模块消融分析 → 渐进式训练策略消融  
**行号**: 约323-328行

## 插入内容

### 图片文件
- **路径**: `figures/mia_training_curves.pdf` (59KB)
- **备用**: `figures/mia_training_curves.eps` (171KB, LaTeX兼容)
- **生成脚本**: `figures/generate_mia_training_curves.py`

### Figure环境
```latex
\begin{figure}[htbp]
  \centering
  \includegraphics[width=\textwidth]{figures/mia_training_curves.pdf}
  \caption{MIA三阶段渐进式训练过程的损失与指标演化曲线...}
  \label{fig:mia_training_curves}
\end{figure}
```

### 引用位置
1. **第一次引用** (行321): 详细分析三阶段训练过程的演化特征
2. **第二次引用** (行380): 引用子图(e)分析任务不确定性权重

## 图表说明

### 6个子图内容
- **(a)** Total and Main Component Losses - 总损失与主要分项
- **(b)** Component Loss Evolution - 所有5个损失分项的演化
- **(c)** Attack Accuracy - Acc1和Acc5的提升曲线
- **(d)** Generation Quality Metrics - FID和KNN距离下降
- **(e)** Task Uncertainty Weights - 5个损失项的不确定性权重$1/\sigma_i^2$
- **(f)** Cosine Annealing Schedule - 混合系数$\lambda(t)$的余弦退火

### 三阶段标注
- **Stage 1** (粉色背景): Image-conditional warmup (Epoch 1-30)
- **Stage 2** (蓝色背景): Mixed-conditional transition (Epoch 31-80)
- **Stage 3** (绿色背景): Label-conditional adaptation (Epoch 81-150)

## 编译验证

✅ 编译成功: `thesis.pdf` (76页)  
✅ 图片引用正常: `fig:mia_training_curves`已解析  
✅ 无字体警告: 所有标签使用英文  
✅ PDF包含图片: 日志确认 `figures/mia_training_curves.pdf` 已嵌入

## 后续工作

当有实际实验数据后:
1. 修改 `generate_mia_training_curves.py` 中的模拟参数
2. 重新运行脚本生成新图: `python generate_mia_training_curves.py`
3. 重新编译论文: `make thesis` 或 `latexmk -xelatex thesis.tex`

无需修改LaTeX源文件，只需替换PDF图片即可。

## 图注建议

当前图注已包含:
- ✅ 6个子图的详细说明
- ✅ 三阶段的背景色说明
- ✅ 训练策略的作用机制描述

可根据实际数据补充:
- 具体的数值范围(当前为模拟值)
- 关键拐点的epoch数
- 最终收敛的精确指标值
