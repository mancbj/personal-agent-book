# Personal Agent：从会回答，到能办事，再到值得托付

一本面向中文读者的开源书，帮助你理解个人智能体、辨认产品差异，并决定把哪些事情交给 AI。

我们从今天的真实问题出发：AI 能接手查找、串联、等待和跟进，但它是否真的减少了你的操心？全书先鸟瞰当下，再展开选择与使用，简短回溯过去，最后讨论有条件的未来。

**当前版本：v0.1.0-part1 · 第一篇审阅版 · 2026-10-10。** 本版包含第一篇三章及阅读说明；第二篇将在作者审阅确认后继续，历史、未来与全书附录尚未写作。

## 阅读与下载

- **现在阅读 Markdown**：[阅读说明](book/00-introduction.md) → [第 1 章](book/01-what-agents-take-over.md) → [第 2 章](book/02-concepts-and-runtimes.md) → [第 3 章](book/03-product-landscape.md)。
- **版本与全套下载**：[v0.1.0-part1 发布页](https://github.com/mancbj/personal-agent-book/releases/tag/v0.1.0-part1)，已提供 [HTML](https://github.com/mancbj/personal-agent-book/releases/download/v0.1.0-part1/personal-agent-book.html)、[PDF](https://github.com/mancbj/personal-agent-book/releases/download/v0.1.0-part1/personal-agent-book.pdf)、[完整 Markdown](https://github.com/mancbj/personal-agent-book/releases/download/v0.1.0-part1/personal-agent-book.md) 与[全套 ZIP](https://github.com/mancbj/personal-agent-book/releases/download/v0.1.0-part1/personal-agent-book-v0.1.0-part1.zip)。
- **在线 HTML**：当前仓库尚未首次启用 Pages，下载版已发布。部署状态见[出版工作流](https://github.com/mancbj/personal-agent-book/actions/workflows/publish.yml)；可访问地址将在实际部署并验证后公布。
- **全书规划**：[已确认目录](TOC.md)；**编辑依据**：[分歧与写作约定](research/README.md)、[第一篇来源记录](research/part1-sources.md)。

单页 HTML 内嵌样式与图像，可单独下载后断网阅读。PDF 提供独立分页、封面、目录、书签、页码和矢量图。完整 Markdown 的图片随 ZIP 提供；只下载 `.md` 文件时，图片资源需要一起保存。

## 这本书适合谁

如果你已经用过 AI，却还在不同软件之间复制内容、重复解释背景，或不停提醒它下一步，这本书从你的问题讲起。读者不需要编程背景；需要部署细节的人，后续可以阅读自托管章节和附录。

本书关注可持续的分工，而非品牌排行。理解“运行在哪里、能访问什么、由谁控制”，比记住某个短期套餐或模型型号更耐用。

## 两条贯穿全书的线

**一条是从答案到委托。** 个人代理是否能保留必要上下文、跨工具行动、跨时间跟进，在授权边界内办事，并给出可核验结果？衡量它时，也计入设置、监督、纠错、审批和维护所增加的工作。

**另一条是本地派与云端派的生态及地位。** OpenClaw、Hermes 的本地部署（Local Runtime）靠近本机应用、私有文件、内网和硬件，具有纯云端执行不能直接替代的场景；Muse、Dot（Dots）等托管服务提供持续在线、跨设备和运维便利。云端托管开放运行时、云端调度本地执行等交集也会讨论。

代理在本地、模型在本地、软件开源是三件不同的事。混合部署需要说明数据流与权限，不以“本地”或“云端”标签代替实际条件。

## 当前内容与后续规划

| 篇 | 内容 | 当前进度 |
| --- | --- | --- |
| 第一篇：先看今天 | 行程案例、概念与部署地图、产品版图 | 已写成审阅版，第 1—3 章 |
| 第二篇：再看细节 | 云端、本地、工作循环、选购、使用、授权 | 目录已确认，待第一篇审阅后写作 |
| 第三篇：简短回望 | 从数字助理到持续代理的演进历程 | 规划，第 10 章 |
| 第四篇：最后看未来 | 情景、验证信号与数字生活控制权 | 规划，第 11—12 章 |
| 附录 | 术语、产品快照、工作表、入门路径、来源 | 规划 |

第一篇的章首图包括任务交接、概念范围与代表产品、产品及生态版图。全书计划中的演进历程、选型决策树等图，将随对应章节完成。

代表产品覆盖 Meta **Muse**、xAI **Grok Bot**、OpenAI **Dot（Dots）**、Manus **Cue**、腾讯 **LightVela**、字节 **Spell**、阿里 **千问的 Personal Agent**、**Instinct**、Today AI 的 **Today**，以及 **OpenClaw、Hermes**。进入版图不代表它们处于相同开放阶段：媒体曝光、路线宣布、邀请测试与实际可用分别标注。

## 资料与更正原则

初始输入包括三份 AI 深度研究报告和一份博主分类、选购观点摘要。它们提供问题与线索，不能直接作为已验证事实。三份报告重复一个说法，也不等于三份独立证据。

本书珍视观点分歧，分析它们的适用条件；事实冲突则查出处并校正，无法解决时保留边界。官方描述、厂商演示、媒体报道、个体体验、作者分析和实测结果分别呈现。

第一篇资料观察截至 **2026-10-10**，主要核对公开公告和文档，没有统一产品实机测评。Instinct 的约 10% 日增长保留为有出处的访谈说法，未独立核实基数、区间与完整指标定义。价格、平台和地区范围，以读者尝试时的最新官方信息为准。

发现错误时，请在 [Issues](https://github.com/mancbj/personal-agent-book/issues) 提供章节、原说法、建议修正及可核对来源。涉及体验时，补充日期、版本和具体任务，有助于分清事实变化与不同使用条件。

## 仓库结构

```text
README.md                 阅读、下载与维护入口
TOC.md                    已确认的全书目录
book.json                 版本、出版元数据与章节顺序
book/                     唯一正文源稿：章节 Markdown
assets/                   共用 SVG 信息图、HTML 样式和 PDF 排版
research/                 来源、分歧、核查与更正记录
scripts/                  构建与成品检查
.github/workflows/        构建、版本发布和 Pages 部署
dist/                     自动生成的成品，默认不提交到源码分支
```

改正文时只改 `book/`；改图时编辑 `assets/figures/` 的 SVG；版本和章节顺序改 `book.json`。各格式由同一份源稿生成，避免三份内容分别维护。

## 本地构建

使用 Python 3.11+、Pandoc 3+、XeLaTeX、Noto CJK 字体和 Poppler。Ubuntu/Debian 上可先安装系统依赖：

```bash
sudo apt-get update
sudo apt-get install -y pandoc texlive-xetex texlive-latex-extra fonts-noto-cjk poppler-utils libcairo2
python -m venv .venv
. .venv/bin/activate
python -m pip install -r requirements.txt
python scripts/build.py
python scripts/check.py
```

成品位于 `dist/`：

| 文件 | 用途 |
| --- | --- |
| `index.html` | Pages 的单页阅读入口 |
| `personal-agent-book.html` | 相同内容的独立离线 HTML |
| `personal-agent-book.pdf` | 排版阅读与一般打印 |
| `personal-agent-book.md` | 当前已完成内容的完整 Markdown |
| `personal-agent-book-v0.1.0-part1.zip` | 成品、分章 Markdown 和图片资源 |
| `SHA256SUMS.txt` | 下载文件的校验值 |

PDF 默认提供出版排版的阅读版。印厂所需开本、出血、色彩空间及 PDF/X 等参数，待具体出版需求确定后另行配置。

## 发布与贡献

提交到 `main` 会运行构建、成品检查与 Pages 部署；Pull Request 运行构建和检查；推送与 `book.json` 版本一致的 `v*` 标签会生成 GitHub Release 并上传全套成品。历史版本保存在发布页，在线版跟随 `main`。

**Pages 首次开启**：仓库管理员在 [Settings → Pages](https://github.com/mancbj/personal-agent-book/settings/pages) 的 **Build and deployment → Source** 选择 **GitHub Actions**，随后在出版工作流中重新运行失败的 Pages 作业，或推送一次 `main` 更新。部署步骤成功并实际访问后，再公布阅读网址。工作流的默认 `GITHUB_TOKEN` 可以部署已启用的站点，不能承担首次启用所需的管理操作。

欢迎提交勘误、可靠来源、可复现的任务体验与图表改进。正文使用中文，首次出现的必要术语附英文；引用放在邻近段落，并在章末记录出处与日期。贡献应围绕已确认目录与当前审阅范围展开，较大结构调整先通过 Issue 说明。

仓库沿用 [Apache-2.0 许可证](LICENSE)，涵盖本项目原创正文、图表及代码。第三方资料、商标和被引用内容的权利归其原权利人；输入附件的提供不意味着其全文在本仓库重新授权。本项目与文中厂商无隶属关系。
