# hithesis 哈尔滨工业大学LaTeX论文模板

[![招生](https://img.shields.io/badge/招生-进行中-green.svg)](https://dustincys.github.io/cn/2025/03/jobad/)

[![texlive-latest](https://github.com/hithesis/hithesis/actions/workflows/test_texlive_latest.yml/badge.svg?branch=master)](https://github.com/hithesis/hithesis/actions/workflows/test_texlive_latest.yml)

[![GitHub tag (latest by date)](https://img.shields.io/github/v/tag/hithesis/hithesis)](https://github.com/hithesis/hithesis/releases)
[![GitHub release (latest by date)](https://img.shields.io/github/v/release/hithesis/hithesis)](https://github.com/hithesis/hithesis/releases)
[![CTAN](https://img.shields.io/ctan/v/hithesis)](https://ctan.org/pkg/hithesis)
![GitHub repo size](https://img.shields.io/github/repo-size/hithesis/hithesis)
<!-- [![GitHub All Releases](https://img.shields.io/github/downloads/dustincys/hithesis/total)](https://github.com/dustincys/hithesis/tags)  -->

<a rel="license" href="http://creativecommons.org/licenses/by-nc/4.0/"><img alt="知识共享许可协议" style="border-width:0" src="https://i.creativecommons.org/l/by-nc/4.0/88x31.png" /></a><br />本作品采用<a rel="license" href="http://creativecommons.org/licenses/by-nc/4.0/">知识共享署名-非商业性使用 4.0 国际许可协议</a>进行许可。

## What's hithesis?

hithesis is a LaTeX thesis template package for Harbin Institute of Technology (all 3 campuses) supporting bachelor, master, doctor dissertations, postdoc report, thesis proposal and midterm report, *both Chinese and English version*.

Files/Codes in hithesis may be distributed and/or modified under the conditions of the LaTeX Project Public License, either version 1.3a of this license or (at your option) any later version. The latest version of this license is in:

[http://www.latex-project.org/lppl.txt](http://www.latex-project.org/lppl.txt)

and version 1.3a or later is part of all distributions of LaTeX version 2004/10/01 or later.

Files/Codes in hithesis also under the protection of license of [Attribution-NonCommercial 4.0 International (CC BY-NC 4.0)](http://creativecommons.org/licenses/by-nc/4.0/).

## hithesis是什么？

一个简单易用的哈尔滨工业大学学位论文LaTeX模板，现包括一校三区本科、硕士、博士开题、中期和毕业论文，包括博后出站报告和英文毕业论文格式。
hithesis 已收录在[CTAN](https://ctan.org/pkg/hithesis)中，用户安装TeXLive将自带窝工模板。

## hithesis版本更新说明

~~版本号：vX.Y.Z 中，X表示重大不兼容改进，Y表示功能改进，Z表示非功能的bug补丁。~~
由于 `\changes` 命令的排序方便，现将版本号的表示法更新，vX.Y.Z 形式的最后一版为 v3.0.22，接下来改为 v3.1a。

版本号：vX.YZ 中，X 表示重大的不兼容改进，Y 表示功能改进，Z 表示非功能的 bug 补丁。其中 X, Y 为数字，Z 为小写字母。

## 窝工规范以及模板支持

### 窝工规范

| 校区   | 学位                                   | 撰写规范                                                                                                                                                                                   | Word排版范例                                                                                                                                                                               | 更新日期   |
| ------ | -------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ---------- |
| 深圳   | 本科毕业                               | -                                                                                                                                                                                          | [关于做好2022届本科生毕业设计（论文） 答辩工作的通知](https://www.hitsz.edu.cn/article/view/id-132766.html)                                                                                |
| 深圳   | 硕士/英文版硕士暂行规定                | [哈工大（深圳）学术规范及硕士学位论文撰写文件包（2020年版）](http://due.hitsz.edu.cn/info/1211/1859.htm)                                                                                   | 同左                                                                                                                                                                                       | 2020-10-23 |
| 深圳   | 硕士中期                               | -                                                                                                                                                                                          | [硕士学位论文中期报告模板](http://due.hitsz.edu.cn/info/1210/4794.htm)<!-- http://due.hitsz.edu.cn/info/1210/1828.htm -->                                                                  | 2023-01-31 |
| 深圳   | 博士开题                               | -                                                                                                                                                                                          | [博士学位开题报告模板](http://due.hitsz.edu.cn/info/1252/1865.htm)                                                                                                                         | 2018-07-31 |
| 深圳   | 博士中期                               | -                                                                                                                                                                                          | [博士学位论文中期检查报告](http://due.hitsz.edu.cn/info/1253/1860.htm)                                                                                                                     | 2018-07-31 |
| 深圳   | 博士毕业                               | [哈尔滨工业大学研究生学位论文撰写规范（2011版）](http://due.hitsz.edu.cn/info/1243/1776.htm)                                                                                               | [哈尔滨工业大学研究生学位论文书写范例（2011版）](http://due.hitsz.edu.cn/info/1243/1777.htm)                                                                                               | 2018-07-31 |
| 深圳   | 英文版博士毕业                         | [Thesis-Tmplt(英文论文撰写规范)](http://due.hitsz.edu.cn/info/1243/1775.htm)                                                                                                               | 同左                                                                                                                                                                                       | 2018-07-31 |
| 威海   | 本科所有                               | [本科毕业论文撰写规范和相关资料](http://jwc.hitwh.edu.cn/bysj/list.htm)                                                                                                                    | 同左                                                                                                                                                                                       | 2021-11-29 |
| 威海   | 硕士                                   | [研究生学位论文撰写规范](http://yjsc.hitwh.edu.cn/2012/1217/c981a37691/page.htm)                                                                                                           | [研究生学位论文书写范例](http://yjsc.hitwh.edu.cn/2012/1217/c981a37689/page.htm)                                                                                                           | 2012-12-17 |
| 威海   | 硕士                                   | [硕士学位论文撰写规范自查表2011版](http://yjsc.hitwh.edu.cn/2015/1230/c981a37718/page.htm)                                                                                                 | 同左                                                                                                                                                                                       | 2015-12-30 |
| 哈尔滨 | 本科所有                               | [毕业论文撰写规范](http://jwc.hit.edu.cn/2014/0504/c4305a116176/page.htm)                                                                                                                  | [所有word范例](http://jwc.hit.edu.cn/2566/list.htm)                                                                                                                                        | 2022-06    |
| 哈尔滨 | 硕士开题中期                           | -                                                                                                                                                                                          | [所有word范例](http://hitgs.hit.edu.cn/2015/1210/c3359a123058/page.htm)                                                                                                                    | 2015-12-10 |
| 哈尔滨 | 博士开题中期                           | -                                                                                                                                                                                          | [所有word范例](http://hitgs.hit.edu.cn/2015/1210/c3416a123048/page.htm)                                                                                                                    | 2015-12-10 |
| 哈尔滨 | 硕博毕业论文所有（含有部分英文版说明） | [研究生学位论文书写范例（理工类）](http://hitgs.hit.edu.cn/2021/0429/c3425a253485/page.htm)[研究生学位论文书写范例（人文社科类）](http://hitgs.hit.edu.cn/2021/0429/c3425a253486/page.htm) | [研究生学位论文写作指南（理工类）](http://hitgs.hit.edu.cn/2021/0429/c3425a253487/page.htm)[研究生学位论文写作指南（人文社科类）](http://hitgs.hit.edu.cn/2021/0429/c3425a253488/page.htm) | 2021-04-29 |
| 哈尔滨 | 博后                                   | -                                                                                                                                                                                          | [出站报告以及封皮](http://rsc.hit.edu.cn/2015/1209/c10906a212031/page.htm)                                                                                                                 | 2015-12-09 |

### 歧义说明

- 规范自身歧义之处：[版芯歧义](http://yanshuo.site/cn/2017/06/hithesisregulation/)和[本科生行距歧义](http://yanshuo.site/cn/2017/06/hithesissiyuan/)。

- 规范与Word模板的歧义：
  - 在[规范](http://hitgs.hit.edu.cn/aa/fd/c3425a109309/page.htm)中规定和[研究生word排版范例](http://hitgs.hit.edu.cn/ab/1f/c3425a109343/page.htm)的中文目录中出现的“ABSTRACT”和“Abstract”的写法歧义（规格严格功夫到家！！！）。
  - [《哈尔滨工业大学本科生毕业论文撰写规范》](http://jwc.hit.edu.cn/2014/0504/c4305a116176/page.htm)与[本科生论文word排版范例](http://jwc.hit.edu.cn/2566/list.htm)中章节标题是否加粗有歧义
  - 本科生论文官方模板的页眉页码格式混乱，有的有页码横线有的没有，有的有页眉有的没有。
  - 规范规定一行33个字，Word模板34个字。

- Word模板自身歧义：
  - Contradictory font size of section title in English version of Word template

### hithesis 支持

- [x] 哈尔滨校区本科毕业设计
- [x] 哈尔滨校区硕士毕业论文
- [x] 哈尔滨校区博士毕业论文
- [x] 哈尔滨校区本科毕业设计开题
- [x] 哈尔滨校区本科毕业设计中期
- [x] 哈尔滨校区硕士毕业设计开题
- [x] 哈尔滨校区硕士毕业设计中期
- [x] 哈尔滨校区博士毕业设计开题
- [x] 哈尔滨校区博士毕业设计中期
- [x] 哈尔滨校区博后出站报告
- [x] 威海校区本科毕业设计
- [x] 威海校区硕士毕业论文
- [x] 威海校区博士毕业论文
- [x] 威海校区本科毕业设计开题
- [x] 威海校区本科毕业设计中期
- [x] 威海校区硕士毕业设计开题
- [x] 威海校区硕士毕业设计中期
- [x] 威海校区博士毕业设计开题
- [x] 威海校区博士毕业设计中期
- [x] 威海校区博后出站报告
- [x] 深圳校区硕士毕业论文
- [x] 深圳校区本科毕业设计
- [x] 深圳校区博士毕业论文
- [x] 深圳校区本科毕业设计开题
- [x] 深圳校区本科毕业设计中期
- [x] 深圳校区硕士毕业设计开题
- [x] 深圳校区硕士毕业设计中期
- [x] 深圳校区博士毕业设计开题
- [x] 深圳校区博士毕业设计中期
- [x] 深圳校区博后出站报告
- [x] English version of thesis

## 模板特点

### 呆萌的操作，傲娇的效果

- 极限程度实现了[《哈尔滨工业大学研究生学位论文撰写规范》](https://hitgs.hit.edu.cn/2025/0331/c17461a365618/page.htm)、[《哈尔滨工业大学本科生毕业论文撰写规范》](http://jwc.hit.edu.cn/2014/0504/c4305a116176/page.htm)
- 这是[PlutoThesis](https://github.com/dustincys/PlutoThesis)的终极进化，PlutoThesis废弃不再维护。
- 更傻更简单的选项，例如论文主文件，只需要在文档类的括号中填写本硕博选项，字体选项（设置弹性间距或者刚性间距），文科生选项（目录可以设成四级目录），非全日制类型等，轻松设定目标格式。
- 更聪明更简单的自适应格式，例如图题和标题，标题字号在字数超过两行时自动由五号变小五号，实现自适应（硕博规范规定，字数多时用五号）
- 自动化中英文索引（博士规范要求，有需要时候添加）
- 自动化表格和图片目录（英文版）
- 自动化生成术语词汇表（英文版）
- 图书馆提交论文级的电子版
- ……

### 矫正PlutoThesis的不足

- 纠正PlutoThesis页面向下溢出
- 纠正PlutoThesis不符合规范要求的各层次题序及标题不得置于页面的最后两行，改为不得置于最后一行（孤行），从此解决了饱受诟病的空白大的问题。
- 纠正PlutoThesis行间距与标题段前段后距离统统设置为1.6倍行距的问题
- 更强大的版芯设置，满足所有需求
- 补充了PlutoThesis没有的符号表、索引两项
- 字体设置符合CTeX的自动识别系统功能
- 纠正PlutoThesis中图片中一些距离设置
- 添加了符合规范要求的“图注在图题之上的设置”
- 纠正PlutoThesis的双语图、表题中英语的非两端对齐问题
- 添加了PlutoThesis中没有的图题最后一行居中且两端对齐格式
- 添加了所有的图形排版格式
- 纠正了附录中标题错误
- 纠正了博士论文右翻页问题
- 添加扫描替换功能，替换之后、页码目录书签自动设置
- 添加思源宋体设置，再也不用害怕奇怪字打不出来了
- 添加文科生、非全日制同等学力封面格式
- 添加PlutoThesis没有的说明文档
- ……

### 为了窝工的规格严格、功夫到家

- 行间距、段前后距离设置精确到小数后四位， 例如 1bp = 1.00374pt，1mm = 2.84526pt， 按照窝工之要求, 行距在3mm～4mm之间，换算之后为20.50398～23.33863bp，严格符合规范要求，哪怕是显微镜级别
- 规范明确规定，数字间空格要求为汉字宽度的四分之一（形式类似与 12 2345 和 0.123 456 这样多于3位以上的整数或小数）。默认情况下在LaTeX中任何人工输入的空格均不正确（“\:”为4/18汉字宽度，“\;”为5/18汉字宽度，所以PlutoThesis中的数字间宽度错误）。hithesis模板中定义了精准的数字间宽度。
- 重写了一堆重要函数，例如章节标题由原来的`BiChapter{}{}`方式进化为`chapter{}[]`，极大简化，后面方括号中为可选括号，硕本可以不用，用了自动忽略
- 严格符合（满足）两个规范要求，由于规范中有矛盾之处，例如本科生的标题段前距离有两处不一样的规定，刚性行距尽量满足行数（要求约33行）要求。
- 规范中给出了行距区间，为了规格严格，设置了弹性行距
- ……

## 关于模板的命名和其他说明

### 模板的命名

本模板对PlutoThesis中的核心代码进行了彻底深入的修改。
PlutoThesis中没有采用cls，这种文档类的模式，代码与正文内容耦合程度大难以维护，本科模板和硕博模板难以融合。
由于冥王星已经不是太阳系C9之一，所以不继续使用PlutoThesis命名。

hithesis, 既含窝工hit，也是说用的“嗨！”，读作“嗨thesis”。

### 关于模板的下载地址

模板有三个下载地址：

1. github: [https://github.com/hithesis/hithesis](https://github.com/hithesis/hithesis)
2. ~~gitee: [https://gitee.com/dustincys/hithesis](https://gitee.com/dustincys/hithesis)~~
3. CTAN: [https://ctan.org/pkg/hithesis](https://ctan.org/pkg/hithesis)

github和gitee的版本是同步且是最新的模板。
CTAN的版本一般会比较落后，但在每年年底会同步为最新版本。

### 关于hithesis的线上讨论区

- QQ群: 259959600
  ![hithesis 1群](https://github.com/user-attachments/assets/cb50f4cf-2aee-469b-97a2-15345b438020)

- 微信公众号

   ![石见石页](https://raw.githubusercontent.com/dustincys/cn/assets/qrcode_for_gh_af6e07ba273e_258.jpg)

### 关于查重

注意：窝工的论文查重可以使用pdf查重！！！！！！！

另外一点注意：查重的pdf一定要确保能够正常复制汉字。有些系统自动识别的汉字字体，
会出现无法正常复制的情况（可能是系统的字体映射出现了误差）。一般需要在主文件的
选项中明确声明使用哪一种fontset。

### 关于LaTeX软件的安装

#### 平台

- 推荐使用开源系统 Linux
- 推荐使用开源编辑器 [Spacemacs](https://www.spacemacs.org/)

#### 中文字体

- 推荐使用LaTeX安装包自带的开源中文字体集[fandol](https://www.ctan.org/pkg/fandol)

#### LaTeX安装包介绍

不推荐安装完整版TeXLive/MiKTeX/MacTeX，因为太费时间。
如果不介意在自己房子里放进一堆小破烂，那么浪费硬盘空间完全不是问题，即使99%的模板八百年都用不到。

所以推荐安装非完整版TeXLive/MiKTeX/MacTex。不完整的安装包有的支持自动安装缺失package，有的不支持，需要手动安装。

| LaTeX安装包  | 是否支持非完整安装         | 平台          | 是否支持自动安装Package | 最小满足hithesis安装脚本                                                                                                           |
| ------------ | -------------------------- | ------------- | ----------------------- | ---------------------------------------------------------------------------------------------------------------------------------- |
| TeXLive      | 是，称为BasicTeX           | WIN/Mac/Linux | 否                      | [install-TeXLive_hithesis.sh](https://github.com/dustincys/hithesis/blob/master/.github/workflows/install-TeXLive_hithesis.sh)     |
| MiKTeX       | 是                         | WIN/Mac/Linux | 是                      | [install-MiKTeX_hithesis.sh](https://github.com/dustincys/hithesis/blob/master/.github/workflows/install-MiKTeX_hithesis.sh)       |
| MacTeX       | 否，MacTeX官方推荐BasicTeX | Mac           | 否                      | [install BasicTeX on Mac](https://github.com/dustincys/hithesis/blob/mac/.github/workflows/test2.yml)                              |
| TinyTeX      | 自身就是最Mini的安装包     | Linux/Mac     | 否                      | [install-TinyTeX_hithesis.sh](https://github.com/dustincys/hithesis/blob/master/.github/workflows/install-TinyTeX_hithesis.sh)      |

<!-- 强烈推荐安装TinyTeX，只占不到300M左右，如果用开源字体集合fandol不用额外安装字体。 -->

<!-- #### docker 镜像 [tinytex-hithesis](https://hub.docker.com/r/dustincys/tinytex-hithesis)

[![Docker Image Version (latest by date)](https://img.shields.io/docker/v/dustincys/tinytex-hithesis?style=plastic)](https://hub.docker.com/r/dustincys/tinytex-hithesis)
[![Docker Image Size (latest by date)](https://img.shields.io/docker/image-size/dustincys/tinytex-hithesis?style=plastic)](https://hub.docker.com/r/dustincys/tinytex-hithesis)

[tinytex-hithesis](https://hub.docker.com/r/dustincys/tinytex-hithesis)构建策略是基于最轻量Alpine Linux（5MB）系统安装最轻量的TinyTeX和最小的hithesis依赖包集合。[还能有比这还要**更快更节省空间更方便部署更良心**的安装和使用hithesis的方法么？](https://5b0988e595225.cdn.sohucs.com/images/20171216/1f6862975513431cbb744c3f6e25c971.gif)

- 第一步，下载[tinytex-hithesis](https://hub.docker.com/r/dustincys/tinytex-hithesis)镜像，

      docker pull dustincys/tinytex-hithesis:latest

- 第二步，在hithesis根目录下执行抽取格式

      docker run --rm -i  -v $(pwd):/home/runner dustincys/tinytex-hithesis:latest latex hithesis.ins

- 第三步，在hithesis毕业论文文件夹hitbook或报告文件夹report下执行以下命令进行编译

      docker run --rm -i  -v $(pwd):/home/runner dustincys/tinytex-hithesis:latest make thesis

      docker run --rm -i  -v $(pwd):/home/runner dustincys/tinytex-hithesis:latest make report

  或者在根目录编译文档

      docker run --rm -i  -v $(pwd):/home/runner dustincys/tinytex-hithesis:latest make doc

  或者直接在hitbook或报告文件夹report下执行

      docker run --rm -i  -v $(pwd):/home/runner dustincys/tinytex-hithesis:latest latexmk

编译过程可以参照下一节模板的编译方法。

使用Docker可以使本地安装不再受平台限制、随时部署，不再受bug、字体、环境变量困扰。诸位上仙、大侠、刀客、头领可以任性地、随意地、抽象地、写实地设置别名，最终完成羽化、飞升。

    alias xelatex='docker run --rm -i  -v $(pwd):/home/runner dustincys/tinytex-hithesis:latest xelatex'
    alias splitindex='docker run --rm -i  -v $(pwd):/home/runner dustincys/tinytex-hithesis:latest splitindex'
    alias bibtex='docker run --rm -i  -v $(pwd):/home/runner dustincys/tinytex-hithesis:latest bibtex'
    alias latexmk='docker run --rm -i  -v $(pwd):/home/runner dustincys/tinytex-hithesis:latest latexmk'
    ... -->

### 模板的编译方法

1. 生成论文格式文件(第一步要生成 *.cls，*.cfg，*.ist，然后再生成论文)

   - 如果是Linux/Mac执行

         latex hithesis.ins

   - 如果是Windows执行（作者没测试过，如遇问题同上）

         lualatex hithesis.ins

   - 如果喜欢玩 make

         make cls

2. 生成好格式后，下一步进入到示例文件夹中

       examples
       ├── hitart
       │   ├── reportplus  %深圳校区博士中期报告
       │   └── reports     %除去深圳校区博士中期报告的一校三区本硕博开题、中期报告
       └── hitbook
           ├── chinese     %一校三区本硕博毕业论文以及博后出站报告
           └── english     %一校三区本硕博英文版毕业论文

3. 生成论文方式

   - 手动狙击（源文件更改后每次编译逐行命令输入一轮）

     - hitbook/chinese 文件夹中

           xelatex -shell-escape thesis.tex
           bibtex thesis
           xelatex -shell-escape thesis.tex
           xelatex -shell-escape thesis.tex
           splitindex thesis -- -s hithesis.ist  # 自动生成索引
           xelatex -shell-escape thesis.tex

     - hitbook/english 文件夹中

           xelatex -shell-escape thesis.tex
           bibtex thesis
           xelatex -shell-escape thesis.tex
           xelatex -shell-escape thesis.tex

     - hitart/{reports,reportplus}文件夹中

           xelatex -shell-escape report.tex
           bibtex report
           xelatex -shell-escape report.tex
           xelatex -shell-escape report.tex

   - 半自动精确射击（源文件更改后每次编译敲一次）

         make thesis

   - 全自动火力覆盖（只需要输入一次命令，源文件更改后自动识别更改自动编译）

         latexmk

4. 生成文档（没什么用，因为有文档也基本没人看）

   - 手动狙击（逐行命令输入一轮）

         xelatex hithesis.dtx
         makeindex -s gind.ist -o hithesis.ind hithesis.idx
         makeindex -s gglo.ist -o hithesis.gls hithesis.glo
         xelatex hithesis.dtx
         xelatex hithesis.dtx

   - 半自动精确射击（编译敲一次）

         make doc

### 打印版、电子版

注意，一般情况下，博士论文的打印版要求双面打印，本硕单面。
博士论文在双面打印成册时，规范中没有明确规定是否要右翻页（右翻页是每一章的起始位
置位于书的右侧页面），所以会出现DIY（或身不由己DIY）哪一处右翻页。
`openright`选项设置为真时，会将所有章（即所有部分，包括前文和后文）起始设置成右翻页。
如果想DIY（或身不由己DIY）在什么地方右翻页，将这个选项设置为false，然后在目标位
置添加`\cleardoublepage`命令即可。

最后向图书管提交的电子版不是右翻页且要求没有任何空白页，这时只需要设置选项`library=true`
即可，这时候会强制`openright=false`。然后什么都不用做，就会出现如同`Sirius`同学
的这种“书签还没整明白，论文居然已经通过了”的情况。

### 幻灯片

有些强迫症刀客喜欢用Beamer，推荐[progressbar主题](https://github.com/dustincys/progressbar)，
能够使用[pympress](https://github.com/Cimbali/pympress)播放双屏提示。
[progressbar主题](https://github.com/dustincys/progressbar)在幻灯片上边排列毕业论文章节链接，在下边有进度指示条，十分适合展示结构复杂的毕业论文内容。

### 关于hithesis的博客

- [2022-06-19 hithesis的二代目掌门](https://yanshuo.site/cn/2022/06/hithesis/)
- [2022-03-04 hithesis 如何使用 docker](https://yanshuo.site/cn/2022/03/hithesis/)
- [2021-11-16 如何维护hithesis（三）](https://yanshuo.site/cn/2021/11/hithesis3/)
- [2021-11-16 如何维护hithesis（二）](https://yanshuo.site/cn/2021/11/hithesis2/)
- [2021-11-15 如何维护hithesis（一）](https://yanshuo.site/cn/2021/11/hithesis/)
- [2020-05-24 hithesis v3 进化](https://yanshuo.site/cn/2020/05/hithesisv3/)
- [2020-02-09 hithesis的“昨天今天和明天”](https://yanshuo.site/cn/2020/01/hithesis/)
- [2017-08-29 发布到了CTAN](https://yanshuo.site/cn/2017/08/ctan/)
- [2017-06-22 规范的正确打开方式](https://yanshuo.site/cn/2017/06/hithesisregulation/)
- [2017-06-16 为了大唐中兴！](https://yanshuo.site/cn/2017/06/hithesissiyuan/)


### 其他说明

- hithesis的维护和创造基于开源式爱心发电精神，所以千万不要向作者提出无礼请求。
- 作者由于工作繁忙，不再无偿解决一些用户要求（例如前面文档中[已经解决的算法格式各实验室要求不一致](https://github.com/dustincys/PlutoThesis#%E6%B2%A1%E6%9C%89%E6%98%8E%E7%A1%AE%E8%A6%81%E6%B1%82%E7%9A%84%E6%A0%BC%E5%BC%8F)问题）。
- 本模板以PlutoThesis为核心基础，参考了CTAN中清华大学薛瑞尼所开发的thuthesis以及其分支重庆大学等毕业论文模板的代码开发而来
- 学校教务处和研究生院提供了规范和[研究生word模板](http://hitgs.hit.edu.cn/ab/1f/c3425a109343/page.htm)以及[本科生word模板](http://jwc.hit.edu.cn/2566/list.htm)，此模板仅为规范的参考实现，不保证格式审查老师不提意见。任何由于使用本模板而引起的论文格式审查问题均与本模板作者无关

### Apply to sponsor

We have spent a lot time and long been involved in developing/maintaining
this open source project.
I'd be humbled and grateful if you could financially support hithesis.

|                Contributer                 |                                          WeChat                                          |                                          Alipay                                          |
| :----------------------------------------: | :--------------------------------------------------------------------------------------: | :--------------------------------------------------------------------------------------: |
|    [@syvshc](https://github.com/syvshc)    | ![szh_wechat](https://raw.githubusercontent.com/hithesis/hithesis/images/szh_wechat.jpg) | ![szh_alipay](https://raw.githubusercontent.com/hithesis/hithesis/images/szh_alipay.jpg) |
| [@dustincys](https://github.com/dustincys) | ![cys_wechat](https://raw.githubusercontent.com/dustincys/hifvwm/screenshots/wechat.jpg) |     ![sys_alipay](http://wx3.sinaimg.cn/large/61dccbaaly1fizali9tafj20k00ucgos.jpg)      |

Or Zelle quick pay: yanshuoc@gmail.com

### Sponsor List

Please contact me if I missed to add any sponsor. Thank you so much.

| Time       | Name      | Comments        |
| ---------- | --------- | --------------- |
| 2020-05-06 | Li Liming |                 |
| 2020-06-16 | 航明      |                 |
| 2020-06-28 | *鑫       |                 |
| 2020-07-20 | CR        | Wechat          |
| 2020-08-13 | d*g       |                 |
| 2020-09-11 | **扬      |                 |
| 2020-11-03 | **宝      |                 |
| 2020-11-05 | **庭      |                 |
| 2021-01-04 | **杰      |                 |
| 2021-02-27 | *晰       |                 |
| 2021-04-29 | *振兴     | Alipay          |
| 2021-04-21 | *作       |                 |
| 2021-05-06 | *文陶     | Zelle quick pay |
| 2021-05-13 | *涵       |                 |
| 2021-05-13 | 慕*       |                 |
| 2021-05-28 | Y*a       |                 |
| 2021-06-19 | *淞       |                 |
| 2021-10-18 | q*q       |                 |
| 2021-11-21 | **刚      | Alipay          |
| 2022-07-06 | 初八      | Wechat          |
| 2022-07-19 | 夏日的风  | WeChat          |
| 2022-08-26 | Yang      | WeChat          |
| 2022-10-18 | cyf       | WeChat          |
| 2023-02-28 | hidadeng  | QQ              |
| 2023-04-16 | Yang      | Alipay          |
| 2023-04-28 | Lin | Alipay |
| 2023-05-11 | hzy       | WeChat          |
| 2023-09-05 | 曹世达    | Wechat          |
| 2023-11-30 | JerryLiu  | WeChat          |
| 2024-03-12 | Chuck     | Alipay          |
| 2024-04-09 | 老学水    | Alipay          |
| 2024-04-10 | csat      | WeChat          |
| 2024-04-14 | Cen       | WeChat          |
| 2025-03-10 |  xw       |Alipay           |

# CONTENT TMP
我将先写一个小型任务清单以跟踪进度，然后开始撰写学术性中文段落，内容涵盖两类人脸识别模型的技术细节、优缺点与攻防含义，最后给出可直接粘贴的论文用段落。现在我先创建/更新 todo 列表。

已创建 3 个待办事项

## 进展简短说明
已创建任务清单并把“草拟两类人脸识别模型的详尽介绍”标为进行中。下面给出学术性、可直接粘贴到论文中的中文介绍段落（包含数学表达与关键术语），并在末尾提供一段简短的插入建议与可选的 LaTeX 处理提示。

## 两类人脸识别模型的学术性介绍（可直接粘贴）

在实际的人脸识别系统研究与部署中，现有模型通常可归为两大类：一类以“特征提取 + 模板匹配”为主（以下简称模板匹配型）；另一类是在基础特征之上增加分类头以直接输出身份类别（以下简称分类头型）。这两类体系在训练目标、推理流程、开放/封闭集适应性以及隐私/攻击面上存在显著差异，理解这些差异对于后续的逆向重建与防御策略设计至关重要。

1. 模板匹配型（Feature embedding + matching）
模板匹配型系统由两部分组成：一个学习得到的特征提取器 f(·; θ)（通常为深度卷积网络或其变体）与一个相似性度量或距离函数 s(·,·)。对于任一输入人脸图像 x，特征提取器产生向量嵌入 e = f(x; θ) ∈ R^d，称为模板或特征向量。系统在登记（enrollment）阶段把每个被识别对象的模板存入数据库；在验证/识别阶段，将待测图像 x' 的嵌入 e' 与数据库中的模板集合 {e_i} 通过相似性度量比较，常见的度量包括欧氏距离 ||e' − e_i||_2、余弦相似度 cos(e', e_i) = e'·e_i/(||e'||·||e_i||) 等。基于阈值 τ 的决策可实现一对一验证（verification）或一对多识别（identification）：
- 验证：接受当 s(e', e_owner) ≥ τ（或距离 ≤ τ）；
- 识别：返回使 s(e', e_i) 最大的索引 i，或返回“未知”若最大相似度低于阈值（开放集识别）。

模板匹配型模型的训练通常采用度量学习（metric learning）范式，以直接优化嵌入空间中同类样本的紧凑性和异类样本的可分性。常见损失包括对比损失（contrastive loss）、三元组损失（triplet loss）以及带角度/余弦间隔的软最大化变体（如 ArcFace、CosFace、SphereFace），其目标可抽象为最小化/最大化嵌入间的距离或角度差异，从而使相似性的几何含义在向量空间中成立。模板匹配型的优点在于天然支持开放集识别（可对未见过的身份进行比对），且嵌入易于索引和大规模检索；但缺点包括对模板存储与保护的要求高（模板泄露即带来隐私风险），且当嵌入维度或分布发生域漂移时性能易受影响。

2. 分类头型（Feature extractor + classification head）
分类头型模型在结构上通常由共享的特征提取器 g(·; θ) 与一个线性或非线性分类头 h(·; φ) 组成，整体可表示为 ŷ = h(g(x; θ); φ)，输出为对预定义身份集合 {1,…,C} 的概率分布或置信分数，常以 softmax+交叉熵作为训练目标：
p = softmax(W · g(x; θ) + b),
L = −∑_{k} 1[y=k] log p_k.
此类模型在封闭集识别（closed-set）任务上表现优秀，尤其在训练集中每个身份都有充足样本时能学习到对类别判别特别敏感的判别边界。训练过程直接将识别问题视作多类分类问题，因此在推理时可以直接从模型输出得到类别标签与置信度。

分类头型的局限主要在于其对开放集情形的适应能力较弱：若请求识别的身份在训练集中不存在，模型往往会错误地将其归入最相近的训练类别（过度自信的预测）。此外，从隐私角度讲，分类头模型的类别输出（尤其是当返回 logits 或概率向量而非仅标签时）为攻击者提供了丰富信息，使得基于类别信息的反演攻击（model inversion attack，MIA）更易实现；在白盒或可查询 logits 的条件下，攻击者可通过优化或生成模型反向合成高置信度属于某类别的输入样本，从而导致隐私泄露。

3. 对比与联系（实用视角）
- 访问接口与攻击面：模板匹配型在攻击上主要被模板逆向重建（template inversion）或从嵌入反推原始图像；攻击者若能获取或查询到特征向量/特征提取器，则可构成强威胁；分类头型在 logits/概率可查询时则更易受到模型反演（MIA）攻击。两者在白盒、灰盒（仅能查询中间特征或 logits）、黑盒（仅得到标签）情形下的脆弱性与可行攻击方法有所不同。
- 训练目标的影响：度量学习驱动的嵌入（模板匹配型）更强调局部相似性结构与一般化到未见身份的能力；交叉熵驱动的分类头更强调训练集内类间判别。为了兼得优点，实务中常见混合策略：在主分支训练 embedding（用于检索），并在其上叠加分类头作辅助监督；或在分类训练后抽取中间特征作为可用于检索的嵌入。
- 系统工程考量：模板匹配型易于扩展到百万级数据库（借助索引结构与近似最近邻检索），而分类头型在身份数量非常大或动态变化时维护成本高（需频繁微调或增量学习）。

4. 对隐私与防御的含义（与本论文工作的关联）
理解上述体系差异能帮助明确攻击目标与防御方向：对模板匹配型，应重视模板加密/模糊化、可逆性降低与基于特征空间的对抗鲁棒性；对分类头型，应控制模型输出信息量（例如仅返回标签或对 logits 做热力学抑制）、采用差分隐私训练或引入抗反演的正则化（例如信息瓶颈）。在本论文中，针对模板逆向重建（TIA）工作的核心在于如何在已知或可查询嵌入/特征的条件下，利用高质量生成先验恢复出既具有视觉逼真性又在特征空间上与真实样本一致的图像；而针对分类模型的模型反演（MIA），则侧重于在仅给定类别标签或有限输出信息的情况下，结合生成模型与标签嵌入实现条件化重建。因此，区分这两类模型的技术细节与可访问接口是构建攻击方法与评估隐私泄露风险的基础。

5. 简短的“合同式”说明（便于论文中后续实验设计说明）
- 输入/输出：输入为人脸图像 x；模板匹配型输出为嵌入 e=f(x)（或相似性分数）；分类头型输出为类别概率/标签 ŷ。
- 成功准则：在识别任务上，模板匹配型以真阳性率与误接受率在给定阈值下评估；分类头型以 Top-1/Top-k 精度与置信度校准评估。
- 主要误差模式：域偏移（光照/姿态/年龄）、样本短缺导致的过拟合、对抗样本与遮挡/低分辨率造成的识别失败。

6. 可能的补充与延伸（供论文后文引用或实验设计使用）
- 可列举常用人脸嵌入训练方法（例如 ArcFace、CosFace）与检索加速方法（例如 FAISS、HNSW）；
- 讨论开放集识别技术（例如阈值拒识、重识别校验）和增量/持续学习在分类头型中的应用；
- 提到模板保护技术（cancelable biometrics、homomorphic encryption、secure sketch）作为防御方向。

## 插入建议（LaTeX 处理提示）
- 上述文本已以学术论文段落风格撰写，直接粘贴到章节文件（如 `chap-methods.tex` 或 `introduction.tex`）中最为合适；如果要放入 `cover.tex` 的摘要或前言部分，请酌情压缩为 1–2 段。
- 若希望在 LaTeX 中保留数学符号（例如向量 e、距离表达式），建议使用数学环境：inline math 用 $e=f(x)$、$||e-e'||_2$ 等。
- 我可以把以上内容格式化为 LaTeX 段落（含 $...$ 数学标记）并直接插入指定文件；如果需要我也可以把特定句子压缩成 200–300 字的摘要版本以放入封面摘要处。

## 后续（我接下来会做的事）
- 我目前已完成草稿（任务 1），下一步将把该任务标记为完成并更新 todo 列表，然后按需进行语言校对与 LaTeX 格式化（任务 2 与 3）。请告诉我是否需要我直接把该段插入到某个具体的文件（例如 cover.tex 或论文章节文件），或需要我生成更短的摘要版本。



我将先在仓库里快速查找常用的算法宏包（如 algorithm、algorithm2e、algorithmicx/algpseudocode）是否已在文档中被加载，这样我能给出与当前模板兼容的替换建议。随后我会给出一个具体的示例：把当前 verbatim 伪代码替换为使用 algorithm + algpseudocode 的 LaTeX 代码（带行号、注释与缩进），并说明若需要我可以直接替换该段并提交补丁。现在我去搜索已配置的宏包。

搜索 `usepackage{algorithm` (`**/*.tex`)、3 结果的文本

简短回答先行：
- verbatim 是 LaTeX 的逐字（原样）文本环境，常用于显示代码或控制字符，不做语义解析，适合展示“原样代码/输出”；
- 若要把伪代码变为学术论文常用的“algo”形式，应用 LaTeX 的算法环境（常见组合：algorithm + algorithmic 或 algorithm2e / algorithmicx+algpseudocode），这样可以获得行号、关键字高亮（IF/FOR/RETURN）、自动编号与 caption，便于引用与排版。下面我说明细节并给出可直接替换的示例（与你的模板兼容）。

1) verbatim 是什么？
- verbatim 环境（或 \verb）只是按原样渲染输入字符，不解释反斜杠等命令。它不会产生算法结构化语义（如行号、IF/FOR/RETURN）。目前你的文件中使用 verbatim 放的是高层伪代码块（供阅读），但对论文排版不够规范，也不便于交叉引用或自动编号。

2) 推荐的 algo 环境（与本仓库兼容性）
- 我在仓库中检查到你的模板已有 \usepackage{algorithm} 和 \usepackage{algorithmic}（见 report.tex 与 thesis.tex），因此最简单、兼容性最好的替换方案是使用 algorithm + algorithmic（这是标准且轻量的组合）。
- 如果你喜欢更现代的伪代码语法和 \Comment，另一个常用选择是 algorithmicx + algpseudocode 或 algorithm2e，但这会要求在模板前言中加载相应包（我可以帮你添加）。

3) 我把你 verbatim 中的三段伪代码（基础训练 / LoRA 微调 / 推理）转换为 algorithm + algorithmic 的形式示例，直接可拷贝到 `3.TIA.tex` 中替换原 verbatim 块：

- 建议替换（中文注释版，行号启用）：

\begin{algorithm}[htbp]
\caption{基础训练（可跳过）}
\label{alg:train_edm}
\begin{algorithmic}[1]
\STATE \textbf{Input:} 基础配置 base\_cfg, 数据加载器 D
\STATE 初始化模型 $M \leftarrow$ EDM(cfg=base\_cfg)
\FOR{epoch = 1 \TO E}
  \FOR{batch \textbf{in} D}
    \STATE loss $\leftarrow$ \texttt{edm\_loss}(batch)
    \STATE loss.backward(); optimizer.step(); optimizer.zero\_grad()
  \ENDFOR
\ENDFOR
\STATE 保存模型检查点
\end{algorithmic}
\end{algorithm}

\begin{algorithm}[htbp]
\caption{LoRA 微调（目标化）}
\label{alg:finetune_lora}
\begin{algorithmic}[1]
\STATE \textbf{Input:} ckpt, 模板集合 T, 步数 $N\_steps$
\STATE $M \leftarrow$ \texttt{load\_edm}(ckpt); \texttt{freeze}(M.parameters())
\STATE $L \leftarrow$ \texttt{attach\_lora\_modules}(M, r, \alpha)
\FOR{step = 1 \TO $N\_steps$}
  \STATE $(x\_batch, t\_batch) \leftarrow$ \texttt{sample\_mini\_batch}(T)
  \STATE loss\_edm $\leftarrow$ \texttt{edm\_loss\_on\_batch}(M, x\_batch)
  \STATE $x\_{\hat{}} \leftarrow$ \texttt{decode\_latent}(M, z\_sample)
  \STATE loss\_id $\leftarrow$ \texttt{id\_loss}(F(x\_{\hat{}}), t\_batch)
  \STATE loss $\leftarrow$ loss\_edm + $\lambda\_\text{id}(\text{step})$*loss\_id + ...
  \STATE loss.backward(); optimizer.step(); optimizer.zero\_grad()
\ENDFOR
\STATE 保存 LoRA 权重与元信息
\end{algorithmic}
\end{algorithm}

\begin{algorithm}[htbp]
\caption{推理（采样 + 可选投影）}
\label{alg:infer}
\begin{algorithmic}[1]
\STATE \textbf{Input:} template, ckpt\_or\_lora, guidance scale $s$, proj\_enabled
\STATE $M \leftarrow$ \texttt{load\_model}(ckpt\_or\_lora)
\STATE $z\_T \leftarrow$ \texttt{sample\_noise()}
\FOR{每个采样步 $i$ \textbf{in} schedule}
  \STATE $\epsilon\_\text{uncond} \leftarrow$ \texttt{denoiser}(z\_i, cond=None)
  \STATE $\epsilon\_\text{cond} \leftarrow$ \texttt{denoiser}(z\_i, cond=template)
  \STATE $\epsilon \leftarrow \epsilon\_\text{uncond} + s\cdot(\epsilon\_\text{cond}-\epsilon\_\text{uncond})$
  \STATE $z\_{i-1} \leftarrow$ \texttt{sampler\_step}(z\_i, \epsilon)
  \IF{proj\_enabled}
    \STATE $x \leftarrow$ \texttt{decode}(z\_{i-1})
    \STATE $g \leftarrow \nabla\_x\ \texttt{id\_loss}(F(x),template)$
    \STATE $x \leftarrow x - \eta\cdot \texttt{normalize}(g)$
    \STATE $z\_{i-1} \leftarrow$ \texttt{encode}(x)
  \ENDIF
\ENDFOR
\STATE \textbf{return} \texttt{decode}(z\_0)
\end{algorithmic}
\end{algorithm}

（注：上面使用了 algorithm + algorithmic 的基本命令：\STATE、\FOR、\IF、\ENDFOR、\ENDIF。若想要注释行（// comment）样式，可用 \STATE \texttt{// 注释} 或 \STATE \quad\%\% 注释文本。）

4) 细节与注意事项
- 包加载：你的模板中应该已经加载了 \usepackage{algorithm} 和 \usepackage{algorithmic}；若没有，我可以帮你在主 tex 文件（如 thesis.tex）前言里添加。
- 可读性：algorithmic 比较简洁但语法有限；若想使用 \Comment、\Require、\Ensure、带行内注释或更友好的关键字显示，建议切换到 algorithmicx+algpseudocode（需要把 preamble 的 \usepackage{algorithmic} 改为 \usepackage{algpseudocode}）或使用 algorithm2e（更灵活但风格不同）。我可以为你选定一种并做统一替换。
- 引用：用 \label{alg:...} 可让你在文中用 \ref{alg:...} 引用算法编号。caption 放在 algorithm 环境中即可。

5) 我可以现在帮你做哪一步？（选一项回复即可）
A. 我把 verbatim 伪代码直接替换为上面给出的 algorithm+algorithmic 代码（我会在 `3.TIA.tex` 中替换原 verbatim 段），然后提交 patch。
B. 我先把替换内容写成 patch 给你预览（不直接提交），你审阅后我再应用。
C. 改为使用更强的 algpseudocode/algorithm2e 风格，并把 preamble 中的宏包统一修改（我会修改主 tex 的 preamble 并替换伪代码）。
D. 仅给出示例，你手动替换（不需要我提交修改）。

你想让我现在直接替换（选 A），还是先预览（选 B），或改用更强方案（选 C），或者你自己替换（D）？