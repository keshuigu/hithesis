# 第五章实验对比数据参考文档

**创建日期**: 2025年12月18日
**用途**: 为第五章实验结果提供基线方法性能数据和文献引用

---

## 目录

- [一、TIA (模板反演攻击) 基线方法](#一tia-模板反演攻击-基线方法)
- [二、MIA (模型反演攻击) 基线方法](#二mia-模型反演攻击-基线方法)
- [三、最新研究进展 (2024-2025)](#三最新研究进展-2024-2025)
- [四、技术演进时间线](#四技术演进时间线)
- [五、表格数据填充指南](#五表格数据填充指南)
- [六、完整论文列表](#六完整论文列表)
- [七、后续行动建议](#七后续行动建议)

---

## 一、TIA (模板反演攻击) 基线方法

### 1.1 GaFaR - 当前SOTA方法 ⭐

**论文信息**:
- **标题**: Template Inversion Attack against Face Recognition Systems using 3D Face Reconstruction
- **作者**: Hatef Otroshi Shahreza, Sébastien Marcel
- **发表**: ICCV 2023
- **引用次数**: 17次 (ICCV), 31次 (IEEE TIFS), 39次 (NeurIPS), 24次 (IEEE TPAMI)

**核心技术**:
- 3D人脸重建 (FLAME 3D morphable model)
- 深度生成网络从模板反演人脸
- 针对ArcFace等SOTA人脸识别系统的白盒攻击

**实验数据** (已从LaTeX文件提取):
- **MOBIO数据集**:
  - SAR = **99.83%** @ FMR = 10^-2
  - SAR = **96.5%** @ FMR = 10^-3 ✨ (当前最高性能)
- **LFW数据集**: 见ICCV论文完整表格
- **AgeDB数据集**: 见ICCV论文完整表格

**论文资源**:
- 📄 ICCV 2023 PDF: http://openaccess.thecvf.com/content/ICCV2023/papers/Shahreza_Template_Inversion_Attack_against_Face_Recognition_Systems_using_3D_Face_ICCV_2023_paper.pdf
- 📄 IEEE TIFS 2023: https://publications.idiap.ch/attachments/papers/2024/OtroshiShahreza_IEEE-TIFS_2024.pdf
- 📄 NeurIPS 2023: https://proceedings.neurips.cc/paper_files/paper/2023/file/29e4b51d45dc8f534260adc45b587363-Paper-Conference.pdf

**Shahreza系列相关论文** (2022-2025):
1. **Comprehensive vulnerability evaluation** (IEEE TIFS 2023) - 31次引用
2. **Vulnerability of SOTA models** (IEEE TPAMI 2024) - 24次引用
3. **Face reconstruction from facial templates by learning latent space** (NeurIPS 2023) - 39次引用
4. **Template inversion using synthetic face images** (IEEE TBBA 2024) - 12次引用
5. **Face reconstruction from partially leaked embeddings** (ICASSP 2024) - 5次引用
6. **Face Reconstruction using Adapter to Face Foundation Model** (CVPR 2025 Workshop) - 4次引用

---

### 1.2 NBNet

**论文信息**:
- **作者**: Mai et al.
- **年份**: 2019
- **方法**: 神经网络重建

**实验数据** (已从LaTeX文件提取):
- **MOBIO数据集**:
  - SAR = **99.67%** @ FMR = 10^-2

---

### 1.3 Dong et al. (2021)

**论文信息**:
- **标题**: Towards Generating Photorealistic 3D Faces from Biometric Embeddings
- **作者**: Dong et al.
- **年份**: 2021

**状态**: ⚠️ 需要查阅原文获取MOBIO/LFW数据集上的具体SAR/FMR数值

---

### 1.4 Vendrow et al. (2021)

**论文信息**:
- **标题**: Realistic Face Reconstruction from Deep Embeddings
- **作者**: Vendrow et al.
- **年份**: 2021

**状态**: ⚠️ 需要查阅原文获取MOBIO/LFW数据集上的具体SAR/FMR数值

---

## 二、MIA (模型反演攻击) 基线方法

### 2.1 PLG-MI - 当前SOTA方法 ⭐

**论文信息**:
- **标题**: Pseudo Label-Guided Model Inversion Attack via Conditional Generative Adversarial Network
- **作者**: Xiaojian Yuan, Kejiang Chen, Jie Zhang, Weiming Zhang, Nenghai Yu, Yang Zhang
- **发表**: AAAI 2023
- **arXiv**: https://arxiv.org/abs/2302.09814

**核心技术**:
- Conditional GAN (cGAN) 作为图像先验
- Top-n选择策略提供伪标签
- Max-margin Loss替代交叉熵损失避免梯度消失
- 为不同类别解耦搜索空间

**关键改进**:
- 在大分布偏移下性能比SOTA提升 **2~3倍**
- 显著改善攻击成功率和视觉质量

**实验数据** (已从LaTeX文件提取):
- **VGGFace2数据集**:
  - Acc1 (Top-1准确率) = **97.47%** ✨ (当前最高性能)
  - 显著超越KED-MI的63.13%和GMI的23.4%

**代码资源**:
- 💻 GitHub: https://github.com/LetheSec/PLG-MI-Attack

---

### 2.2 KED-MI

**论文信息**:
- **标题**: Knowledge-Enriched Distributional Model Inversion Attacks
- **作者**: Chen et al.
- **年份**: 2021

**核心技术**:
- 知识增强的分布式模型反演
- 利用公开数据集作为先验知识

**实验数据** (已从LaTeX文件提取):
- **VGGFace2数据集**:
  - Acc1 (Top-1准确率) = **63.13%**

---

### 2.3 GMI - 首个GAN-based MIA

**论文信息**:
- **标题**: The Secret Revealer: Generative Model-Inversion Attacks Against Deep Neural Networks
- **作者**: Zhang et al.
- **年份**: 2020

**核心技术**:
- 首个使用GAN作为图像先验的模型反演攻击
- 开创了生成式MIA的研究方向

**实验数据** (已从LaTeX文件提取):
- **VGGFace2数据集**:
  - Acc1 (Top-1准确率) = **23.4%**

**历史意义**: 虽然性能较低，但奠定了后续研究基础

---

### 2.4 Re-thinking MIA - CVPR 2023 重要工作

**论文信息**:
- **标题**: Re-thinking Model Inversion Attacks Against Deep Neural Networks
- **作者**: Ngoc-Bao Nguyen, Keshigeyan Chandrasegaran, Milad Abdollahzadeh, Ngai-Man Cheung
- **发表**: CVPR 2023
- **arXiv**: https://arxiv.org/abs/2304.01669

**核心创新**:
- ✨ 改进的优化目标函数
- ✨ 模型增强技术防止MI过拟合
- 系统性分析了传统MI攻击的局限性

**实验数据**:
- **CelebA数据集**:
  - 攻击准确率 > **90%**
  - 相比先前SOTA提升 **11.8%**

**代码与资源**:
- 🌐 项目页面: 提供Demo、预训练模型
- 💡 适用场景: CelebA等人脸数据集，需查阅论文获取VGGFace2结果

---

### 2.5 Plug & Play Attacks - ICML 2022

**论文信息**:
- **标题**: Plug & Play Attacks: Towards Robust and Flexible Model Inversion Attacks
- **作者**: Lukas Struppek, Dominik Hintersdorf, Antonio De Almeida Correira, Antonia Adler, Kristian Kersting
- **发表**: ICML 2022 (Proceedings of Machine Learning Research Vol. 162)
- **页码**: 20522-20545
- **PDF**: https://proceedings.mlr.press/v162/struppek22a/struppek22a.pdf

**核心技术**:
- 解耦目标模型与图像先验的依赖关系
- 使用公开预训练GAN进行攻击
- 只需少量调整即可攻击不同目标模型

**关键优势**:
- 时间和资源高效
- 对分布偏移鲁棒
- 灵活性强，适应性好

**适用场景**: 在数据集分布差异大的情况下仍能生成高质量图像

---

### 2.6 Variational Model Inversion - NeurIPS 2021

**论文信息**:
- **标题**: Variational Model Inversion Attacks
- **作者**: Kuan-Chieh Wang, Yan Fu, Ke Li, Ashish Khisti, Richard S. Zemel, Alireza Makhzani
- **发表**: NeurIPS 2021

**核心技术**:
- 模型反演攻击的概率解释
- 变分目标函数同时优化多样性和准确性
- 在深度生成模型的编码空间定义变分家族

**数据集**: 人脸图像 + 胸部X光图像

**关键贡献**: 提供了MIA的理论框架，强调样本多样性的重要性

---

## 三、最新研究进展 (2024-2025)

### 3.1 扩散模型在模板反演中的应用

#### LADIMO (IEEE IJCB 2024) 🔥

**论文信息**:
- **标题**: LADIMO: Face Morph Generation through Biometric Template Inversion with Latent Diffusion
- **发表**: IEEE International Joint Conference on Biometrics 2024
- **引用次数**: 7次

**核心技术**:
- **潜在扩散模型** (Latent Diffusion Model)
- 生物特征模板反演
- 人脸变形生成

**研究意义**: 展示了扩散模型在模板反演任务中的潜力

---

#### DiffUMI (arXiv 2025) 🆕

**论文信息**:
- **标题**: DiffUMI: Training-Free Universal Model Inversion via Unconditional Diffusion
- **年份**: 2025 (最新)

**核心技术**:
- **无需训练**的通用模型反演
- 使用无条件扩散模型
- 零样本攻击能力

**创新点**: 不需要针对特定目标模型进行训练，极大提高了攻击的通用性

---

#### Controllable Inversion via Diffusion (ICCV 2023 Workshop)

**论文信息**:
- **标题**: Controllable Inversion of Black-box Face Recognition Models via Diffusion
- **发表**: ICCV 2023 Workshop on Adversarial Robustness in the Real World
- **引用次数**: 34次

**核心技术**:
- 条件扩散模型
- 黑盒人脸识别系统反演
- 可控的人脸生成

---

#### Diffusion-driven GAN Inversion (CVPR 2024)

**论文信息**:
- **标题**: Diffusion-driven GAN Inversion for Multi-Modal Face Image Generation
- **发表**: CVPR 2024
- **引用次数**: 22次

**核心技术**:
- 结合GAN和扩散模型的优势
- 多模态人脸图像生成

**研究方向**: 混合架构成为新趋势

---

### 3.2 其他相关技术

#### CLIP-FTI (AAAI 2026预期)
- 基于CLIP的多模态特征用于模板反演

#### Null-text Inversion (CVPR 2023)
- **引用次数**: 1301次 (高影响力工作)
- 编辑真实图像的扩散模型反演技术
- 为后续工作提供了重要技术基础

---

## 四、技术演进时间线

### 模型反演攻击 (MIA) 发展历程

```
┌─────────────────────────────────────────────────────────────────┐
│ 2020: GAN-based时代                                              │
│ GMI: 23.4% Acc1 @ VGGFace2                                      │
│ • 首次使用GAN作为图像先验                                          │
│ • 开创生成式MIA研究方向                                            │
└─────────────────────────────────────────────────────────────────┘
                           ↓
┌─────────────────────────────────────────────────────────────────┐
│ 2021: 知识增强时代                                                │
│ KED-MI: 63.13% Acc1 @ VGGFace2 (+39.73%)                       │
│ • 利用公开数据集提供先验知识                                        │
│ • 分布式建模提高攻击效果                                            │
│                                                                 │
│ Variational MI (NeurIPS 2021)                                  │
│ • 提供概率解释和理论框架                                            │
│ • 强调多样性与准确性的平衡                                          │
└─────────────────────────────────────────────────────────────────┘
                           ↓
┌─────────────────────────────────────────────────────────────────┐
│ 2022-2023: 引导与优化时代                                         │
│ Plug & Play (ICML 2022)                                        │
│ • 解耦模型与先验依赖                                               │
│ • 提高鲁棒性和灵活性                                               │
│                                                                 │
│ PLG-MI (AAAI 2023): 97.47% Acc1 @ VGGFace2 (+34.34%) ⭐        │
│ • 伪标签引导的条件生成                                             │
│ • Max-margin loss优化                                           │
│ • 大分布偏移下提升2~3倍                                            │
│                                                                 │
│ Re-thinking MIA (CVPR 2023): 90%+ @ CelebA                     │
│ • 改进优化目标                                                    │
│ • 模型增强防止过拟合                                               │
└─────────────────────────────────────────────────────────────────┘
                           ↓
┌─────────────────────────────────────────────────────────────────┐
│ 2024-2025: 扩散模型时代 🚀                                        │
│ LADIMO (IJCB 2024)                                             │
│ • 潜在扩散模型用于模板反演                                          │
│                                                                 │
│ DiffUMI (arXiv 2025)                                           │
│ • 无需训练的通用反演                                               │
│ • 零样本攻击能力                                                   │
│                                                                 │
│ 趋势: Diffusion > GAN                                          │
│ • 更好的图像质量 (更低FID)                                         │
│ • 更强的泛化能力                                                   │
│ • 可控性更强                                                      │
└─────────────────────────────────────────────────────────────────┘
```

### 模板反演攻击 (TIA) 发展历程

```
┌─────────────────────────────────────────────────────────────────┐
│ 2019: 早期神经网络方法                                             │
│ NBNet: 99.67% SAR @ FMR=10^-2                                  │
│ • 直接神经网络重建                                                 │
└─────────────────────────────────────────────────────────────────┘
                           ↓
┌─────────────────────────────────────────────────────────────────┐
│ 2021: 2D生成方法探索                                              │
│ Dong et al., Vendrow et al.                                    │
│ • 基于2D图像生成的模板反演                                          │
└─────────────────────────────────────────────────────────────────┘
                           ↓
┌─────────────────────────────────────────────────────────────────┐
│ 2022-2023: 3D重建突破 ⭐                                          │
│ Shahreza系列 (NeurIPS 2023, ICCV 2023, IEEE TIFS/TPAMI)       │
│ GaFaR: 96.5% SAR @ FMR=10^-3 on MOBIO                         │
│ • FLAME 3D morphable model                                     │
│ • 深度生成网络                                                    │
│ • 学习生成器潜在空间                                               │
│                                                                 │
│ 引用数: 17次(ICCV), 31次(TIFS), 39次(NeurIPS), 24次(TPAMI)       │
└─────────────────────────────────────────────────────────────────┘
                           ↓
┌─────────────────────────────────────────────────────────────────┐
│ 2024-2025: 3D + Diffusion融合                                   │
│ • Shahreza继续推进3D重建技术                                       │
│ • 扩散模型开始应用于模板反演                                         │
│ • CVPR 2025: Adapter + Face Foundation Model                   │
└─────────────────────────────────────────────────────────────────┘
```

---

## 五、表格数据填充指南

### 表5.1-5.2: TIA性能对比 (MOBIO, LFW, AgeDB, IJB-C)

#### 已确认数据 ✅

| 方法 | MOBIO<br>SAR@FMR=10^-2 | MOBIO<br>SAR@FMR=10^-3 | 数据来源 |
|------|------------------------|------------------------|---------|
| NBNet (2019) | 99.67% | - | LaTeX文件注释 |
| GaFaR (2023) | 99.83% | 96.5% | LaTeX文件注释 + ICCV论文 |
| 本文方法 | **待实验** | **待实验** | **需要实验获取** |

#### 待补充数据 ⚠️

| 方法 | 状态 | 建议 |
|------|------|------|
| Dong et al. (2021) | 缺失 | 查阅原文或从GaFaR论文对比表中获取 |
| Vendrow et al. (2021) | 缺失 | 查阅原文或从GaFaR论文对比表中获取 |
| LFW数据集结果 | 缺失 | 从GaFaR ICCV 2023论文表格中提取 |
| AgeDB数据集结果 | 缺失 | 从GaFaR ICCV 2023论文表格中提取 |
| IJB-C数据集结果 | 缺失 | 从GaFaR论文或实验获取 |

**目标设定**:
- 你的方法应至少达到或超过 **GaFaR的96.5% SAR @ FMR=10^-3**
- 在保持高SAR的同时，应有更低的FID值（更好的图像质量）

---

### 表5.3-5.4: MIA性能对比 (VGGFace2)

#### 已确认数据 ✅

**表5.3: 标准性能指标**

| 方法 | Acc1 (Top-1) | Acc5 (Top-5) | KNN Distance | 数据来源 |
|------|-------------|-------------|--------------|---------|
| GMI (2020) | 23.4% | - | - | LaTeX文件注释 |
| KED-MI (2021) | 63.13% | - | - | LaTeX文件注释 |
| PLG-MI (2023) | 97.47% | - | - | LaTeX文件注释 |
| 本文方法 | **待实验** | **待实验** | **待实验** | **需要实验获取** |

**表5.4: 图像质量指标**

| 方法 | FID ↓ | PSNR ↑ | SSIM ↑ | LPIPS-Alex ↓ | LPIPS-VGG ↓ |
|------|-------|--------|--------|--------------|-------------|
| GMI | - | - | - | - | - |
| KED-MI | - | - | - | - | - |
| PLG-MI | - | - | - | - | - |
| 本文方法 | **待实验** | **待实验** | **待实验** | **待实验** | **待实验** |

#### 可选添加的最新方法 🆕

| 方法 | Acc1 | 数据集 | 说明 |
|------|------|--------|------|
| Re-thinking MIA (CVPR 2023) | >90% | CelebA | 可添加以展示研究前沿，但需注意数据集不同 |
| Plug & Play (ICML 2022) | - | - | 强调鲁棒性和灵活性的工作 |

**目标设定**:
- **Acc1**: 应保持≥97%，与PLG-MI竞争
- **FID**: 显著低于PLG-MI（如<25），体现REFace先验的优势
- **PSNR/SSIM**: 应高于基线，展示更好的视觉质量
- **LPIPS**: 应低于基线，展示更接近真实人脸的感知质量

---

### 表5.5-5.7: 消融实验

这些表格需要通过你自己的实验填充，用于验证各个模块的有效性：

**TIA消融实验**:
- ❌ 无角度约束
- ❌ 无任务不确定性加权
- ❌ 无多样性正则化
- ✅ 完整方法

**MIA消融实验**:
- ❌ 无REFace先验
- ❌ 无LoRA微调
- ❌ 非渐进训练
- ✅ 完整方法

**每个配置都需要测量完整指标集**以量化各模块的贡献。

---

## 六、完整论文列表

### TIA相关论文 (按时间排序)

1. **NBNet (2019)**
   - Mai et al., "Reconstruction of Face Images from Deep Embeddings"
   - 状态: 需查阅原文

2. **Dong et al. (2021)**
   - "Towards Generating Photorealistic 3D Faces from Biometric Embeddings"
   - 状态: 需查阅原文

3. **Vendrow et al. (2021)**
   - "Realistic Face Reconstruction from Deep Embeddings"
   - 状态: 需查阅原文

4. **Shahreza & Marcel (2022-2025系列) ⭐**

   - **[ICIP 2022]** Face Reconstruction from Deep Facial Embeddings using CNN
     - 34次引用
     - PDF: http://publications.idiap.ch/downloads/papers/2022/OtroshiShahreza_ICIP_2022.pdf

   - **[IJCB 2022]** Inversion of Deep Facial Templates using Synthetic Data
     - 3次引用
     - PDF: https://publications.idiap.ch/attachments/papers/2024/OtroshiShahreza_IJCB-2_2023.pdf

   - **[NeurIPS 2023]** Face Reconstruction from Facial Templates by Learning Latent Space of Generator Network
     - 39次引用 ⭐⭐⭐
     - PDF: https://proceedings.neurips.cc/paper_files/paper/2023/file/29e4b51d45dc8f534260adc45b587363-Paper-Conference.pdf

   - **[ICCV 2023]** Template Inversion Attack against Face Recognition Systems using 3D Face Reconstruction (GaFaR)
     - 17次引用 ⭐
     - PDF: http://openaccess.thecvf.com/content/ICCV2023/papers/Shahreza_Template_Inversion_Attack_against_Face_Recognition_Systems_using_3D_Face_ICCV_2023_paper.pdf

   - **[IEEE TIFS 2023]** Comprehensive Vulnerability Evaluation of Face Recognition Systems to Template Inversion Attacks via 3D Face Reconstruction
     - 31次引用 ⭐⭐
     - PDF: https://publications.idiap.ch/attachments/papers/2024/OtroshiShahreza_IEEE-TIFS_2024.pdf

   - **[ICASSP 2024]** Face Reconstruction from Partially Leaked Facial Embeddings
     - 5次引用
     - PDF: https://publications.idiap.ch/attachments/papers/2024/OtroshiShahreza_ICASSP-2_2024.pdf

   - **[IEEE TPAMI 2024]** Vulnerability of State-of-the-Art Face Recognition Models to Template Inversion Attack
     - 24次引用 ⭐

   - **[IEEE TBBA 2024]** Template Inversion Attack using Synthetic Face Images against Real Face Recognition Systems
     - 12次引用
     - PDF: https://publications.idiap.ch/attachments/papers/2024/OtroshiShahreza_IJCB-2_2023.pdf

   - **[FG 2024]** Breaking Template Protection: Reconstruction of Face Images from Protected Facial Templates
     - 5次引用
     - PDF: https://publications.idiap.ch/attachments/papers/2024/OtroshiShahreza_FG-2_2024.pdf

   - **[CVPR 2025 Workshop]** Face Reconstruction from Face Embeddings using Adapter to a Face Foundation Model
     - 4次引用 (最新)
     - PDF: https://openaccess.thecvf.com/content/CVPR2025W/ABAW/papers/Shahreza_Face_Reconstruction_from_Face_Embeddings_using_Adapter_to_a_Face_CVPRW_2025_paper.pdf

### MIA相关论文 (按时间排序)

1. **GMI (2020)**
   - Zhang et al., "The Secret Revealer: Generative Model-Inversion Attacks Against Deep Neural Networks"
   - CVPR 2020
   - 首个GAN-based MIA

2. **Variational MI (NeurIPS 2021)**
   - Kuan-Chieh Wang et al.
   - "Variational Model Inversion Attacks"
   - 提供概率解释框架

3. **Plug & Play Attacks (ICML 2022)**
   - Lukas Struppek et al.
   - PDF: https://proceedings.mlr.press/v162/struppek22a/struppek22a.pdf
   - 解耦模型与先验的灵活方法

4. **PLG-MI (AAAI 2023) ⭐**
   - Xiaojian Yuan et al.
   - "Pseudo Label-Guided Model Inversion Attack via Conditional GAN"
   - arXiv: https://arxiv.org/abs/2302.09814
   - GitHub: https://github.com/LetheSec/PLG-MI-Attack
   - 当前SOTA: 97.47% Acc1 @ VGGFace2

5. **Re-thinking MIA (CVPR 2023)**
   - Ngoc-Bao Nguyen et al.
   - arXiv: https://arxiv.org/abs/2304.01669
   - 90%+ accuracy on CelebA, 11.8% improvement

6. **ICCV 2023 Workshop - Controllable Inversion**
   - "Controllable Inversion of Black-box Face Recognition Models via Diffusion"
   - 34次引用
   - 条件扩散模型应用

7. **CVPR 2024 - Diffusion-driven GAN Inversion**
   - "Diffusion-driven GAN Inversion for Multi-Modal Face Image Generation"
   - 22次引用
   - 混合架构

8. **LADIMO (IEEE IJCB 2024)**
   - "Face Morph Generation through Biometric Template Inversion with Latent Diffusion"
   - 7次引用
   - 潜在扩散模型

9. **DiffUMI (arXiv 2025) 🆕**
   - "Training-Free Universal Model Inversion via Unconditional Diffusion"
   - 最新工作
   - 零样本攻击

### 重要基础工作

1. **Null-text Inversion (CVPR 2023)**
   - "Null-text Inversion for Editing Real Images using Guided Diffusion Models"
   - 1301次引用 ⭐⭐⭐
   - 扩散模型反演的奠基性工作

---

## 七、后续行动建议

### 7.1 立即行动 (优先级: 高) 🔴

1. **获取GaFaR完整实验数据**
   - 📥 下载ICCV 2023论文PDF
   - 📊 提取LFW、AgeDB、IJB-C数据集上的完整SAR/FMR表格
   - ⏰ 预计时间: 30分钟

2. **获取PLG-MI完整实验数据**
   - 📥 查看GitHub仓库是否有完整实验结果
   - 📊 获取FID、PSNR、SSIM等图像质量指标
   - ⏰ 预计时间: 30分钟

3. **开始TIA实验**
   - 🎯 目标: SAR ≥ 96.5% @ FMR=10^-3 (超过GaFaR)
   - 📈 同时优化图像质量 (FID)
   - ⏰ 预计时间: 根据实验设置

4. **开始MIA实验**
   - 🎯 目标1: Acc1 ≥ 97% (与PLG-MI竞争)
   - 🎯 目标2: FID < 25 (显著优于基线)
   - 🎯 目标3: PSNR/SSIM/LPIPS全面提升
   - ⏰ 预计时间: 根据实验设置

### 7.2 短期行动 (优先级: 中) 🟡

1. **补充基线数据**
   - 📖 查阅Dong et al. (2021)原文
   - 📖 查阅Vendrow et al. (2021)原文
   - 💡 或从GaFaR论文的对比表中直接提取

2. **获取PLG-MI图像质量数据**
   - 如果GitHub或论文中没有，考虑联系作者
   - 或基于PLG-MI代码复现实验

3. **完成消融实验**
   - TIA: 验证角度约束、任务加权、多样性正则化的贡献
   - MIA: 验证REFace先验、LoRA微调、渐进训练的贡献
   - 每个配置需要完整指标

### 7.3 论文写作建议 (优先级: 中) 🟡

1. **相关工作章节**
   ```
   建议结构:
   - 2.1 早期模板反演方法 (NBNet等)
   - 2.2 GAN-based MIA演进 (GMI → KED-MI → PLG-MI)
   - 2.3 3D重建在TIA中的突破 (Shahreza系列)
   - 2.4 最新扩散模型趋势 (LADIMO, DiffUMI) [可选]
   ```

2. **实验结果章节**
   ```
   重点对比:
   - TIA vs. GaFaR (当前SOTA)
     → 强调角度约束扩散模型的优势
     → 在保持高SAR同时改善图像质量

   - MIA vs. PLG-MI (当前SOTA)
     → 强调REFace+LoRA的创新性
     → 在保持高Acc1同时显著改善FID
   ```

3. **贡献定位**
   ```
   你的创新点:
   - TIA: 角度约束扩散模型 (vs. GaFaR的3D重建)
           ↳ 可能更简单、更高效，但性能竞争

   - MIA: REFace+LoRA渐进训练 (vs. PLG-MI的伪标签引导)
           ↳ 未见先例的组合，图像质量优势明显
   ```

### 7.4 可选的深入研究 (优先级: 低) 🟢

1. **追踪最新文献**
   - CVPR 2025可能有新的相关工作
   - NeurIPS 2024可能有理论突破

2. **探索混合架构**
   - 参考Diffusion-driven GAN Inversion
   - 考虑是否能结合3D重建+扩散模型

3. **跨领域应用**
   - 参考Variational MI的X光图像应用
   - 考虑方法的泛化性讨论

---

## 附录A: 关键数据快速查找表

### TIA快速参考

| 方法 | 年份 | MOBIO SAR@10^-2 | MOBIO SAR@10^-3 | 核心技术 |
|------|------|-----------------|-----------------|---------|
| NBNet | 2019 | 99.67% | - | 神经网络重建 |
| GaFaR | 2023 | 99.83% | **96.5%** ⭐ | 3D重建(FLAME) |
| 本文 | 2025 | **待实验** | **待实验** | 角度约束扩散 |

### MIA快速参考

| 方法 | 年份 | VGGFace2 Acc1 | 核心技术 | 性能提升 |
|------|------|--------------|---------|---------|
| GMI | 2020 | 23.4% | GAN-based | 基线 |
| KED-MI | 2021 | 63.13% | 知识增强 | +39.73% |
| PLG-MI | 2023 | **97.47%** ⭐ | 伪标签+cGAN | +34.34% |
| 本文 | 2025 | **待实验** | REFace+LoRA | 目标≥97% |

---

## 附录B: 重要PDF下载清单

### 必须获取 ✅

1. ✅ GaFaR ICCV 2023: http://openaccess.thecvf.com/content/ICCV2023/papers/Shahreza_Template_Inversion_Attack_against_Face_Recognition_Systems_using_3D_Face_ICCV_2023_paper.pdf

2. ✅ PLG-MI AAAI 2023: https://arxiv.org/pdf/2302.09814.pdf

3. ✅ Re-thinking MIA CVPR 2023: https://arxiv.org/pdf/2304.01669.pdf

### 建议获取 📚

4. 📚 Shahreza IEEE TIFS 2023: https://publications.idiap.ch/attachments/papers/2024/OtroshiShahreza_IEEE-TIFS_2024.pdf

5. 📚 Shahreza NeurIPS 2023: https://proceedings.neurips.cc/paper_files/paper/2023/file/29e4b51d45dc8f534260adc45b587363-Paper-Conference.pdf

6. 📚 Plug & Play ICML 2022: https://proceedings.mlr.press/v162/struppek22a/struppek22a.pdf

---

## 版本历史

- **v1.0** (2025-12-18): 初始版本，整理所有搜索结果和文献数据
  - 完成TIA和MIA基线方法整理
  - 添加最新研究进展(2024-2025)
  - 提供完整论文列表和资源链接
  - 制定后续行动计划

---

**文档状态**: ✅ 完成
**最后更新**: 2025年12月18日
**下次更新时机**: 实验数据获取后或发现新的相关文献时

---

*本文档为论文第五章实验部分提供数据支持，应随实验进展持续更新。*
