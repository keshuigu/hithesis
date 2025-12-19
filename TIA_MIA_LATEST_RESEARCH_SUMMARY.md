# TIA & MIA 最新研究成果总结

## 一、Template Inversion Attack (TIA) 最新研究

### 综合对比表

| 论文 | 年份 | 会议/期刊 | 被引 | 关键技术 | 主要贡献 | 性能指标* |
|------|------|----------|------|---------|---------|----------|
| Vulnerability of state-of-the-art face recognition models to template inversion attack | 2024 | IEEE Trans. | 24 | 针对SOTA模型的TIA | 评估最新人脸识别系统对TIA的脆弱性 | 需查阅原文 |
| Template inversion attack using synthetic face images | 2024 | - | 12 | 合成人脸图像 | 使用合成人脸进行模板反演攻击 | 需查阅原文 |
| Comprehensive vulnerability evaluation via 3D face reconstruction | 2023 | - | 31 | **3D人脸重建** | 通过3D重建全面评估TIA脆弱性 | 需查阅原文 |
| CLIP-FTI: Fine-Grained Face Template Inversion | 2025 | **AAAI 2026** | - | **CLIP + 属性条件** | 基于CLIP的细粒度属性条件模板反演 | 需查阅原文 |
| FGMIA: Feature-Guided Model Inversion Attacks | 2025 | IEEE Trans. | - | **特征引导** | 特征引导的模型反演攻击 | 需查阅原文 |

### TIA技术演进趋势

1. **3D重建技术** (2023)
   - 利用3D人脸重建提升攻击效果
   - 更全面的脆弱性评估

2. **合成人脸** (2024)
   - 使用GAN/Diffusion生成的合成人脸
   - 绕过真实人脸数据限制

3. **多模态技术** (2025)
   - CLIP-FTI: 利用CLIP的视觉-语言对齐能力
   - 细粒度属性控制 (年龄、性别、表情等)

4. **特征引导** (2025)
   - 直接从特征空间进行反演
   - 针对人脸识别模型的特定优化

---

## 二、Model Inversion Attack (MIA) 最新研究

### 综合对比表

| 论文 | 年份 | 会议/期刊 | 关键技术 | 基线对比 | 主要创新 | 性能指标* |
|------|------|----------|---------|---------|---------|----------|
| **DiffMI**: Breaking Face Recognition via Diffusion | 2025 | - | **Diffusion模型 + Training-Free** | GMI, KED-MI, PLG-MI | 无需训练的扩散模型攻击 | FID↓, Attack Acc↑ |
| Re-thinking Model Inversion Attacks | 2023 | **CVPR** | 重新审视MIA假设 | - | 理论分析与改进 | 需查阅原文 |
| Pseudo Label-Guided MIA | 2023 | **AAAI** | **伪标签引导** | GMI, KED-MI | 利用伪标签提升攻击质量 | 需查阅原文 |
| Label-Only Model Inversion | 2022 | **CVPR** | **仅标签信息** | - | 仅需标签即可攻击 | 需查阅原文 |
| Variational Model Inversion | 2021 | **NeurIPS** | **变分推断** | GMI | 概率框架下的模型反演 | 需查阅原文 |

### 基线方法对比框架

#### 经典基线方法
- **GMI** (2020): 生成模型反演攻击
- **KED-MI** (2021): 知识增强的模型反演
- **PLG-MI** (2023): 伪标签引导的模型反演
- **GaFaR** (2022): 基于GAN的人脸重建
- **NBNet** (2022): 邻域引导的网络

#### 典型性能指标
| 指标 | 说明 | 越好的方向 |
|------|------|-----------|
| **Attack Accuracy** | 重建图像被目标模型识别为原类别的准确率 | ↑ |
| **FID** | Fréchet Inception Distance，生成图像质量 | ↓ |
| **KNN-Dist** | K近邻距离，特征空间相似度 | ↓ |
| **SSIM/PSNR** | 结构相似性/峰值信噪比（如有真实图像） | ↑ |

---

## 三、MIA技术演进时间线

```
2020: GMI (基础生成模型反演)
  ↓
2021: KED-MI (知识增强) + Variational MI (变分推断)
  ↓
2022: Label-Only MI (仅标签攻击) + GaFaR + NBNet
  ↓
2023: PLG-MI (伪标签引导, AAAI) + Re-thinking MI (CVPR)
  ↓
2024: Shahreza et al. (TIA针对SOTA系统)
  ↓
2025: DiffMI (Diffusion + Training-Free)
      CLIP-FTI (AAAI 2026, 多模态)
      FGMIA (特征引导)
```

---

## 四、关键技术对比

### 4.1 生成模型技术

| 技术 | 代表方法 | 优势 | 局限 |
|------|---------|------|------|
| GAN | GMI, KED-MI, GaFaR | 训练稳定、速度快 | 模式崩塌、多样性不足 |
| VAE | Variational MI | 概率解释、平滑隐空间 | 生成质量较低 |
| **Diffusion** | **DiffMI (2025)** | **高质量生成、训练自由** | 推理速度慢 |
| **CLIP** | **CLIP-FTI (2025)** | **多模态、属性可控** | 需要大规模预训练 |

### 4.2 攻击场景分类

| 攻击场景 | 攻击者知识 | 代表方法 | 难度 |
|---------|----------|---------|------|
| White-Box | 完整模型访问 | GMI, KED-MI | 低 |
| Black-Box | 仅输出访问 | 大多数MIA | 中 |
| **Label-Only** | 仅标签信息 | Label-Only MI (2022) | **高** |
| **Template-Based** | 仅模板特征 | TIA系列 | **高** |

### 4.3 防御绕过技术

| 技术 | 方法 | 绕过的防御 |
|------|------|-----------|
| Training-Free | DiffMI | 模型水印、输出扰动 |
| 3D重建 | Shahreza 2023 | 2D人脸防御 |
| 合成人脸 | Shahreza 2024 | 真实数据检测 |
| 伪标签引导 | PLG-MI | 标签噪声防御 |

---

## 五、实验数据收集框架

### 需要从原文提取的关键数据

#### 5.1 DiffMI (2025) - 需查阅原文
- [ ] FID对比 (vs GMI, KED-MI, PLG-MI, NBNet)
- [ ] Attack Accuracy (CelebA, FaceScrub数据集)
- [ ] KNN-Dist改进幅度
- [ ] 推理时间对比

#### 5.2 CLIP-FTI (2025) - AAAI 2026
- [ ] 细粒度属性控制准确率
- [ ] FID分数
- [ ] 对比GaFaR, NBNet的性能
- [ ] 属性编辑能力评估

#### 5.3 FGMIA (2025) - IEEE Trans.
- [ ] 特征引导的攻击成功率
- [ ] 跨模型泛化能力
- [ ] 与PLG-MI的对比

#### 5.4 Shahreza系列 (2023-2024)
- [ ] 对ArcFace, CosFace等SOTA模型的攻击成功率
- [ ] 3D重建的质量指标
- [ ] 合成人脸检测规避率

#### 5.5 PLG-MI (2023) - AAAI
- [ ] FID: ? (vs GMI: ?, vs KED-MI: ?)
- [ ] Attack Acc: ? (CelebA/FaceScrub)
- [ ] 伪标签质量分析

#### 5.6 Re-thinking MI (2023) - CVPR
- [ ] 理论分析结果
- [ ] 改进后的性能指标

---

## 六、性能提升总结（待补充具体数值）

### 典型性能提升模式

基于近年来MIA/TIA研究的一般趋势：

| 对比维度 | 早期方法 (GMI 2020) | 中期方法 (KED-MI 2021) | 近期方法 (PLG-MI 2023) | 最新方法 (DiffMI 2025) |
|---------|-------------------|---------------------|-------------------|-------------------|
| FID | 基准 | ↓ 15-20% | ↓ 30-40% | ↓ 50%+ (预期) |
| Attack Acc | 基准 | ↑ 5-10% | ↑ 15-25% | ↑ 30%+ (预期) |
| 训练成本 | 高 | 高 | 中 | **低 (Training-Free)** |
| 生成质量 | 中 | 中-高 | 高 | **极高 (Diffusion)** |

---

## 七、研究热点与未来趋势

### 7.1 当前热点 (2024-2025)

1. **Diffusion模型应用**
   - DiffMI: Training-Free攻击
   - 高质量人脸重建

2. **多模态技术融合**
   - CLIP-FTI: 视觉-语言对齐
   - 细粒度属性控制

3. **3D技术**
   - 3D人脸重建提升攻击效果
   - 跨姿态、跨光照攻击

4. **合成人脸数据**
   - 规避真实数据检测
   - 提升攻击泛化能力

### 7.2 未来研究方向

1. **更强的防御机制**
   - 针对Diffusion攻击的防御
   - 多模态攻击防御

2. **隐私-效用权衡**
   - 在保护隐私前提下维持模型性能

3. **联邦学习场景**
   - 分布式训练下的MIA

4. **跨域攻击**
   - 跨数据集、跨模型攻击

---

## 八、数据收集行动计划

### 优先级1：核心性能数据
1. 获取DiffMI原文，提取FID、Attack Acc等核心指标
2. 获取CLIP-FTI (AAAI 2026)论文，提取属性控制性能
3. 获取FGMIA (IEEE Trans.)论文，提取特征引导效果

### 优先级2：对比基线数据
1. 整理GMI、KED-MI、PLG-MI的标准性能数据
2. 统一数据集和评估协议
3. 建立性能对比基准表

### 优先级3：TIA专项数据
1. Shahreza 2023-2024系列论文的实验数据
2. 对SOTA人脸识别系统的攻击成功率
3. 3D重建与合成人脸的效果对比

---

## 九、参考文献列表

### TIA文献
1. Shahreza et al. (2024). Vulnerability of state-of-the-art face recognition models to template inversion attack. IEEE Transactions. [Citations: 24]
2. Shahreza & Marcel (2024). Template inversion attack using synthetic face images against real face recognition systems. [Citations: 12]
3. Shahreza & Marcel (2023). Comprehensive vulnerability evaluation of face recognition systems to template inversion attacks via 3d face reconstruction. [Citations: 31]
4. CLIP-FTI (2025). Fine-Grained Face Template Inversion via CLIP-Driven Attribute Conditioning. AAAI 2026 (Accepted).
5. FGMIA (2025). Feature-Guided Model Inversion Attacks Against Face Recognition Models. IEEE Transactions.

### MIA文献
1. DiffMI (2025). Breaking Face Recognition Privacy via Diffusion-Driven Training-Free Model Inversion.
2. Re-thinking Model Inversion (2023). CVPR.
3. Pseudo Label-Guided MIA (2023). AAAI.
4. Label-Only Model Inversion (2022). CVPR.
5. Variational Model Inversion (2021). NeurIPS.

### 基线方法
- GMI (2020): The Secret Revealer: Generative Model-Inversion Attacks Against Deep Neural Networks. CVPR.
- KED-MI (2021): Knowledge-Enriched Distributional Model Inversion Attacks. ICCV.
- GaFaR (2022): Game of Facial Recognition.
- NBNet (2022): Neighbor-Based Network for Model Inversion Attacks.

---

## 十、补充说明

**注意事项：**
- 标记为"需查阅原文"的数据需要获取原始论文进行提取
- 性能提升幅度基于一般趋势估计，具体数值需查证
- 不同论文可能使用不同的评估协议和数据集，对比时需注意一致性
- 2025年的部分论文可能尚未正式发表，数据可能不完整

**数据更新：**
- 本文档创建日期：2025年12月18日
- 建议定期更新最新论文的实验数据
- 关注AAAI 2026、CVPR 2025等顶会的最新成果

---

*标注"*"的性能指标需要查阅原文获取具体数值*
