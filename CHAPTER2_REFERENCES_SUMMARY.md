# 第二章《理论基础》参考文献补充总结

## 概述
为第二章《理论基础》中的核心概念系统地添加了学术引用，共新增13个BibTeX条目，覆盖深度学习、人脸识别、扩散模型和参数高效微调等领域的关键文献。

## 新增引用列表

### 1. 深度学习与网络架构

| 概念 | BibTeX Key | 引用信息 |
|------|-----------|--------|
| ResNet残差网络 | `he2016deep` | He, K., et al. (2016) - Identity Mappings in Deep Residual Networks |
| Vision Transformer | `dosovitskiy2020image` | Dosovitskiy, A., et al. (2021) - An Image is Worth 16x16 Words |
| MobileNet | `howard2017mobilenets` | Howard, A. G., et al. (2017) - MobileNets: Efficient CNNs |
| EfficientNet | `tan2019efficientnet` | Tan, M. & Le, Q. V. (2019) - EfficientNet |

### 2. 人脸识别与度量学习

| 概念 | BibTeX Key | 引用信息 |
|------|-----------|--------|
| 对比损失 | `hadsell2006dimensionality` | Hadsell, R., et al. (2006) - Dimensionality Reduction by Learning |
| 三元组损失与FaceNet | `schroff2015facenet` | Schroff, F., et al. (2015) - FaceNet |
| ArcFace | `deng2019arcface` | Deng, J., et al. (2019) - ArcFace |
| CosFace | `wang2018cosface` | Wang, H., et al. (2018) - CosFace |
| SphereFace | `liu2017sphereface` | Liu, W., et al. (2017) - SphereFace |
| Adam优化器 | `kingma2014adam` | Kingma, D. P. & Ba, J. (2015) - Adam |

### 3. 扩散模型基础

| 概念 | BibTeX Key | 引用信息 |
|------|-----------|--------|
| DDPM去噪扩散 | `hoDenoisingDiffusionProbabilistic2020` | Ho, J., et al. (2020) - Denoising Diffusion Probabilistic Models |
| Score-based SDE | `songScoreBasedGenerativeModeling2021` | Song, Y., et al. (2021) - Score-based Generative Modeling |
| LDM隐空间扩散 | `rombachHighResolutionImageSynthesis2022` | Rombach, R., et al. (2022) - High-Resolution Image Synthesis with LDM |
| 生成对抗网络GAN | `goodfellowGenerativeAdversarialNetworks2014` | Goodfellow, I., et al. (2014) - Generative Adversarial Nets |

### 4. 扩散模型引导与采样

| 概念 | BibTeX Key | 引用信息 |
|------|-----------|--------|
| 分类器引导 | `dhariwalDiffusionModelsBeat2021` | Dhariwal, P. & Nichol, A. (2021) - Diffusion Models Beat GANs |
| 无分类器引导 | `ho2022classifierfree` | Ho, J. & Salimans, T. (2021) - Classifier-free Diffusion Guidance |
| DDIM确定性采样 | `song2021denoising` | Song, J., et al. (2021) - Denoising Diffusion Implicit Models |
| EDM清晰扩散设计 | `karrasEluvidatingDiffusionModels2022` | Karras, T., et al. (2022) - Elucidating Diffusion Models |

### 5. 参数高效微调

| 概念 | BibTeX Key | 引用信息 |
|------|-----------|--------|
| LoRA低秩适配 | `huLowRankAdaptation2021` | Hu, E. J., et al. (2022) - LoRA: Low-rank Adaptation |
| 任务适配维度 | `aghajanyanIntrinsicDimensionality2020` | Aghajanyan, A., et al. (2020) - Intrinsic Dimensionality |

## 第二章中的引用位置

### 第1节 - 人脸识别模型
- **深度学习发展背景**：引用了ResNet（he2016deep）和优化器（kingma2014adam）
- **度量学习方法**：引用了对比损失（hadsell2006dimensionality）、三元组损失（schroff2015facenet）、角度边距损失（deng2019arcface, wang2018cosface, liu2017sphereface）
- **骨干网络架构**：引用了ResNet（he2016deep）、Vision Transformer（dosovitskiy2020image）、MobileNet（howard2017mobilenets）、EfficientNet（tan2019efficientnet）

### 第2节 - 扩散模型基础
- **扩散模型概述**：引用了DDPM（hoDenoisingDiffusionProbabilistic2020）、Score-based SDE（songScoreBasedGenerativeModeling2021）、GAN基准（goodfellowGenerativeAdversarialNetworks2014）
- **采样策略**：引用了分类器引导（dhariwalDiffusionModelsBeat2021）、无分类器引导（ho2022classifierfree）、DDIM（song2021denoising）、EDM（karrasEluvidatingDiffusionModels2022）
- **隐空间扩散**：引用了LDM（rombachHighResolutionImageSynthesis2022）

### 第3节 - 低秩适配技术
- **参数高效微调背景**：引用了LoRA（huLowRankAdaptation2021）
- **理论基础**：引用了任务适配维度假设（aghajanyanIntrinsicDimensionality2020）

## 编译验证
✅ 所有新增引用已成功集成
✅ 编译无错误和警告
✅ PDF输出：74页
✅ 所有BibTeX条目正确格式化

## 学术质量改进
1. **完整性**：覆盖了所有关键概念的原始文献出处
2. **可追溯性**：读者可直接查阅原始论文验证理论基础
3. **专业性**：符合学位论文学术规范
4. **可信度**：建立了理论与实验的学术支撑链条

## 使用说明
所有新增的引用都采用标准格式：
```latex
\cite{key_name}
```

例如在文中引用ResNet：
```latex
残差网络\cite{he2016deep}通过引入残差连接...
```

## 后续建议
1. 继续为第3章（模板逆向重建方法）添加相关引用
2. 为第4章（模型反演方法）补充LoRA和扩散换脸相关文献
3. 为第5章（实验结果）添加评估指标相关文献
