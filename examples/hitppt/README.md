# 博士学位论文答辩演示文稿

本目录包含基于 Beamer 的博士学位论文答辩演示文稿模板。

## 📁 文件结构

```
hitppt/
├── presentation.tex      # 主演示文稿文件
├── Makefile             # 编译脚本
├── README.md            # 本文件
└── figures/             # 图片目录
    ├── face_recognition_apps.pdf
    ├── tia_pipeline.pdf
    ├── mia_pipeline.pdf
    ├── tia_architecture.pdf
    ├── mia_architecture.pdf
    ├── tia_qualitative.pdf
    ├── mia_qualitative.pdf
    └── ablation_lora_rank.pdf
```

## 🚀 快速开始

### 编译演示文稿

```bash
# 完整编译（推荐）
make

# 或使用快速模式（调试时使用）
make quick

# 或使用 latexmk 自动编译
make auto
```

### 查看结果

```bash
# 编译并打开 PDF
make view
```

### 清理文件

```bash
# 清理临时文件
make clean

# 完全清理（包括 PDF）
make distclean
```

## 📋 所需软件

- **TeX 发行版**：TeX Live 2020+ 或 MiKTeX
- **编译器**：XeLaTeX（用于中文支持）
- **字体**：宋体（SimSun）或其他中文字体

### 安装依赖（Ubuntu/Debian）

```bash
sudo apt-get install texlive-xetex texlive-latex-extra texlive-fonts-recommended
sudo apt-get install texlive-lang-chinese
sudo apt-get install latexmk  # 可选，用于自动编译
```

### 安装依赖（macOS）

```bash
brew install --cask mactex
# 或安装 BasicTeX（较小）
brew install --cask basictex
```

## 🎨 自定义演示文稿

### 修改主题

在 `presentation.tex` 中修改：

```latex
\usetheme{Madrid}        % 可选: Berlin, Copenhagen, Singapore 等
\usecolortheme{default}  % 可选: dolphin, whale, beaver 等
```

常用学术主题推荐：
- **Madrid**: 简洁大方，适合正式答辩
- **Berlin**: 侧边栏导航，适合长篇内容
- **Singapore**: 顶部导航，现代感强
- **Copenhagen**: 顶部蓝色条，清爽简洁

### 修改字体

```latex
\setCJKmainfont{SimSun}  % 改为你系统中的中文字体
```

常用中文字体：
- Windows: SimSun（宋体）、SimHei（黑体）、Microsoft YaHei（微软雅黑）
- macOS: STSong（华文宋体）、STHeiti（华文黑体）
- Linux: Noto Sans CJK SC、WenQuanYi Micro Hei

### 调整幻灯片比例

```latex
\documentclass[aspectratio=169,12pt]{beamer}  % 16:9 宽屏
% aspectratio=43   # 4:3 传统比例
% aspectratio=1610 # 16:10
```

## 📊 准备图片

演示文稿中需要以下图片文件（放在 `figures/` 目录）：

1. **face_recognition_apps.pdf** - 人脸识别应用场景示意图
2. **tia_pipeline.pdf** - TIA 攻击流程图
3. **mia_pipeline.pdf** - MIA 攻击流程图
4. **tia_architecture.pdf** - TIA 方法架构图
5. **mia_architecture.pdf** - MIA 方法架构图
6. **tia_qualitative.pdf** - TIA 定性结果对比
7. **mia_qualitative.pdf** - MIA 定性结果对比
8. **ablation_lora_rank.pdf** - LoRA 秩消融研究图

### 图片准备建议

- **格式**: 优先使用 PDF 或 EPS 矢量格式，保证缩放质量
- **分辨率**: 如使用 PNG/JPG，建议 300 DPI 以上
- **尺寸**: 宽度建议 1920-2560 像素（16:9 比例）
- **工具**:
  - 流程图: draw.io, TikZ, Graphviz
  - 架构图: PowerPoint + PDF 导出, Inkscape
  - 结果图: Python (matplotlib), MATLAB

### 快速创建占位图片

如果暂时没有图片，可以创建占位符：

```bash
# 使用 ImageMagick 创建占位图
cd figures/
convert -size 1920x1080 xc:lightgray -pointsize 72 -fill black \
        -annotate +700+540 "图片占位符" face_recognition_apps.png
```

## 💡 演讲技巧

### 时间分配（30 分钟答辩）

- 研究背景与动机: 4-5 分钟
- 研究内容与方法: 10-12 分钟
- 实验结果与分析: 8-10 分钟
- 主要贡献与创新: 3-4 分钟
- 总结与展望: 2-3 分钟
- 预留提问时间: 5-10 分钟

### 演讲要点

1. **开场**: 简洁介绍研究背景和问题的重要性
2. **重点突出**: 在关键数据上停留，用动画或颜色强调
3. **逻辑清晰**: 保持故事线连贯，技术细节适度
4. **图表说话**: 少用文字堆砌，多用可视化展示
5. **控制节奏**: 平均 1-2 分钟/张，重点幻灯片可延长
6. **预留弹性**: 准备一些可跳过的辅助幻灯片

## 🔧 故障排查

### 编译错误

**问题**: `! Font ... not found`
**解决**: 检查中文字体是否安装，或更改 `\setCJKmainfont` 为系统已有字体

**问题**: `! LaTeX Error: File 'tikz.sty' not found`
**解决**: 安装缺失的宏包
```bash
sudo apt-get install texlive-latex-extra
```

**问题**: 图片无法显示
**解决**:
1. 检查 `figures/` 目录中图片文件是否存在
2. 检查文件名和路径是否正确
3. 临时注释图片命令进行编译测试

### 中文显示问题

**问题**: 中文显示为方框或乱码
**解决**:
1. 确认使用 XeLaTeX 编译（不要用 PDFLaTeX）
2. 检查字体是否正确安装
3. 尝试更换其他中文字体

```bash
# 查看系统可用中文字体
fc-list :lang=zh
```

### 编译速度慢

**建议**:
1. 开发时使用 `make quick` 快速编译
2. 图片较多时使用 `draft` 选项：
   ```latex
   \includegraphics[draft,width=\textwidth]{figures/large_image.pdf}
   ```
3. 使用 `latexmk -pvc` 开启连续编译模式

## 📚 参考资源

- [Beamer 官方文档](https://ctan.org/pkg/beamer)
- [Beamer 主题画廊](https://hartwork.org/beamer-theme-matrix/)
- [LaTeX Beamer 教程](https://www.overleaf.com/learn/latex/Beamer)
- [TikZ & PGF 手册](https://tikz.dev/)

## 📄 许可证

本模板遵循与 HIThesis 相同的许可证。

## 🤝 贡献

欢迎提出改进建议或报告问题！

---

**祝答辩顺利！🎓**
