# 附录 E · 资料来源与争议索引

**资料观察截至 2026-10-10，当前版本 v0.6.1-terminology-update。** 本附录帮助你从结论回到证据，也把输入素材中的分歧与尚未解决的问题保留下来。

三份 AI 深度研究报告与一份博主观点摘要是本书的初始素材。它们提供问题和线索；相同说法出现三次，不等于三项独立证据。原始附件中的任务要求和引用格式也没有作为本书的写作指令。

## 本书怎样区分证据

| 层次 | 可以说明什么 | 仍需什么 |
| --- | --- | --- |
| 可定位的公告、论文与规范 | 某事件、定位或机制在何时被公开描述 | 对准确范围、后续修订与上下文的核对 |
| 厂商功能与安全说明 | 厂商承诺、文档规则与设计边界 | 实际账号和任务验证，必要时独立审计 |
| 原始采访或媒体报道 | 采访对象说过什么，报道记录了什么 | 指标、事件和因果的独立证据 |
| 用户体验与实测 | 在特定条件下发生了什么 | 可复现条件与样本，不能直接泛化 |
| 作者分析与教学情景 | 一种判断方法、可能分工或条件性预测 | 实际记录、反例与后续修订 |

本书主要核对公开资料，没有完成统一产品实机测评、购买准入验证或安全审计。正文中的林岚、工作案例、试用数字和观察表为教学内容，不冒充真实测试。

## 按章节寻找来源

| 位置 | 核心证据与方法 | 详细记录 |
| --- | --- | --- |
| 第 1—3 章：当下与版图 | 行程教学情景、概念归纳、十一项产品的公开资料 | [第一篇记录](https://github.com/mancbj/personal-agent-book/blob/main/research/part1-sources.md)；产品入口集中于附录 B |
| 第 4—5 章：部署生态 | 平台公告、计费、运行时模型配置和信任边界 | [第二篇记录](https://github.com/mancbj/personal-agent-book/blob/main/research/part2-sources.md) |
| 第 6 章：持续循环 | 工具规范与项目文档；作者的组件分工说明 | 第二篇记录及下方技术来源 |
| 第 7—8 章：选择与使用 | 作者的一周试用、委托模板与教学案例 | 第二篇记录；可复制版本见附录 C |
| 第 9 章：授权与托付 | 厂商审批与安全文档、OWASP、作者权限框架 | 第二篇记录；不把假设误操作写成品牌事故 |
| 第 10 章：简短历史 | 原始发布、论文、研究机构与参与者回顾 | [第三篇记录](https://github.com/mancbj/personal-agent-book/blob/main/research/part3-sources.md) |
| 第 11 章：未来观察 | 条件性情景，部署、接口与交易机制线索 | [第四篇记录](https://github.com/mancbj/personal-agent-book/blob/main/research/part4-sources.md)，列出前提和反证 |
| 第 12 章：控制权 | 记忆、商业角色、授权证据与法律一般框架 | 第四篇记录；未作个案法律判断 |
| 附录 A—C | 正文定义、产品快照、原创工作表 | [附录记录](https://github.com/mancbj/personal-agent-book/blob/main/research/appendices-sources.md) |
| 附录 D | 当前官方安装与起步说明，作者的验收路径 | 附录记录；本书未实际部署这些运行时 |

详细研究记录保留对应版本与核查范围，后续版本不会把旧版记录改写成新实测。全套 ZIP 随附这些记录，便于离线查看核查过程；引用网站的原文仍需联网访问。

## 产品与技术的主要入口

十一项产品的逐字段资料、发布或观察日期、访问限制，见附录 B。技术与授权问题主要使用以下资料：

- [Meta Muse 安全架构](https://research.meta.ai/blog/security-and-safety-for-ai-agents-our-approach-with-muse)：控制组件的位置与资料处理边界。
- [Grok Bot 审批、安全与隐私](https://docs.x.ai/grok-bot/approvals-security-and-privacy)、[技能与例行任务](https://docs.x.ai/grok-bot/skills-routines-and-automations)：权限、方法复用与触发的区别。
- [OpenClaw 信任边界](https://docs.openclaw.ai/start/why-openclaw/the-trust-boundary)、[本地与自定义模型服务](https://docs.openclaw.ai/concepts/model-providers/custom-providers)：实际配置与数据路径。
- [MCP 工具规范](https://modelcontextprotocol.io/specification/2025-06-18/server/tools)：本书明确采用 2025-06-18 版，不宣称覆盖最新全部规范。
- [OWASP LLM01:2025 提示注入](https://genai.owasp.org/llmrisk/llm01-prompt-injection/)：通用风险与防护思路，不充当品牌事故证明。
- [Google AP2 公告](https://cloud.google.com/blog/products/ai-machine-learning/announcing-agents-to-payments-ap2-protocol)，2025-09-16；[Cloudflare 代理交易说明](https://blog.cloudflare.com/secure-agentic-commerce/)，2025-10-24：授权证据与网站接待代理的基础设施方向。
- [OpenAI 赞助代理公告](https://openai.com/index/reimagining-advertising-with-ai/)，2026-09-16；[购物搜索说明](https://help.openai.com/en/articles/11128490-shopping-with-chatgpt-search)：商业角色与官方区分，未进行独立机制审计。
- [《民法典》政府公开全文](https://tjca.miit.gov.cn/zwgk/zcwj/flfg/art/2020/art_20cf1a2e1b854924b5caa744c8045d1f.html)：第 12 章采用中国大陆一般框架，不推广为全球结论。

## 历史节点的主要入口

第 10 章区分愿景、研究、能力发布与产品开放；下面的年份对应各自事件，不能合并成品类的唯一诞生日。

- **1987 愿景影片**：[制作参与者回顾](https://www.dubberly.com/articles/the-making-of-knowledge-navigator.html)、[计算机历史博物馆](https://computerhistory.org/blog/yesterdays-tomorrows-the-origins-of-the-tablet/)。
- **1994 软件代理研究**：[MIT 研究组出版目录](https://agents.media.mit.edu/publications.html)、[Maes 论文 DOI](https://doi.org/10.1145/176789.176792)。出版记录与摘要已核对，全文读取受限。
- **2003 起 CALO**：[SRI 历史回顾](https://www.sri.com/hoi/artificial-intelligence-calo/)。
- **2011 手机集成 Siri**：[Apple 当年公告](https://www.apple.com/newsroom/2011/10/04Apple-Launches-iPhone-4S-iOS-5-iCloud/)。
- **2012 Google Now**：[Android 4.1 预览公告](https://android-developers.googleblog.com/2012/06/introducing-android-41-jelly-bean.html)、[2013 官方回顾](https://android.googleblog.com/2013/02/new-google-now-more-of-information-you.html)。
- **2014—2015 Echo 与 Alexa**：[2015 扩大销售公告及首发回顾](https://press.aboutamazon.com/2015/6/amazon-echo-now-available-to-all-customers)、[云端语音服务公告](https://press.aboutamazon.com/2015/6/amazon-opens-alexa-voice-service-to-third-party-hardware-makers)。
- **2015 M**：[WIRED 原始采访](https://www.wired.com/2015/08/facebook-launches-m-new-kind-virtual-assistant/)、[2017 Facebook 回顾与建议功能](https://about.fb.com/news/2017/04/m-now-offers-suggestions-to-make-your-messenger-experience-more-useful-seamless-and-delightful/)。
- **2022 ReAct**：[原始论文与提交历史](https://arxiv.org/abs/2210.03629)；**2023 函数调用**：[OpenAI 公告](https://openai.com/index/function-calling-and-other-api-updates/)。
- **2024 电脑操作与 MCP**：[Anthropic 电脑操作公开测试](https://www.anthropic.com/news/3-5-models-and-computer-use)、[MCP 发布公告](https://www.anthropic.com/news/model-context-protocol)。

访问失败、回顾资料与原始公告的区别，详见第三篇记录；没有把无法读取的全文当作已经阅读全文。

## 观点分歧：保留条件，不强行统一

| 问题与位置 | 本书保留的不同解释 | 怎样继续判断 |
| --- | --- | --- |
| 品类从何时开始，第 2、10 章 | 愿景、研究、移动入口与常驻产品各有起点 | 先说明讨论的是哪类事件 |
| 云端是否替代本地，第 5、11 章 | 托管便利与本地资源控制各有价值 | 比较资源可达、数据约束与维护，而非排世代 |
| dots 是否连续，第 4、6 章 | 长期上下文的价值与跨工具交接负担可能同时存在 | 验证任务负责人、状态和约束是否完整交接 |
| 多代理是否省心，第 6、11 章 | 并行工作可增收益，协调也可增加管理 | 记录重复调用、人工交接与总成本 |
| 自托管是否等于数据主权，第 5、9、12 章 | 更多控制能力与更多维护责任并存 | 核对推理、工具、凭证与副本流向 |
| 长期记忆是否增加依赖，第 9、12 章 | 上下文提高便利，重新建立关系又增加迁移成本 | 验证导出、恢复与重新授权 |
| 谁站在用户一边，第 12 章 | 用户代理与商家代理都可有用，商业激励不同 | 看角色披露、比较范围、排序与拒绝路径 |

这些问题没有因初稿完成而被关闭。相同产品在不同任务、权限和维护条件下，也可能给出不同答案。

## 事实冲突与待确认项

| 核查项 | 当前处理 | 还需要的证据 |
| --- | --- | --- |
| Grok 每个 Bot 是否独立电脑 | 当前官方说明同账号共享环境；角色与隔离分开 | 架构变化时的新文档与实际版本 |
| Grok 必须最高套餐吗 | 当前计费文档有多种付费入口；不照抄旧最低价 | 读者地区、账号、套餐与有效额度 |
| dots 后台都能写入吗 | 官方主动研究受只读限制；委托与主动工作分开 | 具体触发模式与实际行动规则 |
| Muse Sentinel 是否在独立 VM | 同日安全资料说明容器外、同一 VM 主机侧 | 新架构与独立验证；不能推导零外发 |
| Cue 平台、费用与现实动作 | 保留早期邀请、免费阶段及公告中的平台条件 | 当前准入、号码、支付和额度 |
| Spell 与千问是否已全面开放 | 曝光与路线宣布各自标明 | 官方独立产品与开放安排 |
| Instinct 约 10% 日增长 | 归于访谈自报，不作独立统计或长期外推 | 指标、基数、区间与原始记录 |
| Today 平台与行动故事 | 保留文档张力，未确认版本或授权原因 | 对应平台、实际版本与任务记录 |
| 事故、融资与市场规模 | 没有把未充分核实的材料写成事实结论 | 原始记录、独立来源与清楚口径 |
| 安装要求是否仍沿用旧版本 | 附录 D 按当前官方安装文档记录依赖 | 安装时发行版、系统与实测结果 |

无法核实的部分不是“没有发生”，也不是可以用推断填补的事实。更完整的争议矩阵保存在[素材分歧记录](https://github.com/mancbj/personal-agent-book/blob/main/research/README.md)。

## 更正与版本记录

本版图表设计参考 Cathryn Lavery 的开源项目 [diagram-design](https://github.com/cathrynlavery/diagram-design)（MIT 许可）：按图意选择泳道、二维矩阵、树图、部署、循环、流程、瀑布、状态、分层和时间线模板，使用本书的深绿、米白和中文字体。图中内容由本书编写，模板不作为产品事实或研究结论的证据。

新增瀑布图沿用第 7 章的教学数字；历史图按真实年份间隔分段绘制；未来情景不赋予未经测量的概率或分数。图型选择、内容取舍、源代码与许可说明见[图表设计记录](https://github.com/mancbj/personal-agent-book/blob/main/research/diagram-design-notes.md)，随全套 ZIP 提供。

| 版本 | 可核对的变化 |
| --- | --- |
| v0.1.0-part1 | 第一篇首次审阅版；产品开放与证据口径分别记录 |
| v0.1.1-part1 | 将作者确认的封面与 Logo 加入 HTML、PDF |
| v0.2.0-part2 | 补齐实践、部署与授权；细化 Grok 计费和共享环境、Muse 控制位置、dots 主动研究边界 |
| v0.3.0-part3 | 增加历史与演进图，区分愿景、研究、能力和产品节点 |
| v0.4.0-part4 | 增加未来情景、反证与控制权讨论 |
| v0.5.0-complete-draft | 补齐五个附录、更新安装资料、提供可复用工作表，并将来源记录纳入全套 ZIP |
| v0.6.0-visual-edition | 重绘九张图并新增三张，更新全部出版格式，提供独立 HTML 图表与再生源代码；产品事实观察日期未变 |
| v0.6.1-terminology-update | 全书统一使用“个人智能体”指称 Personal Agent，更新正文、术语表、图注、Markdown、HTML 与 PDF |

后续更正应写清原说法、修改内容、适用日期与来源，区分“此前写错了”和“产品后来变化了”。历史发布文件保留在 [Releases](https://github.com/mancbj/personal-agent-book/releases)，在线版随维护更新。

欢迎在 [Issues](https://github.com/mancbj/personal-agent-book/issues) 提交章节、建议改法与可核对资料。若依据个人体验，使用附录 C 的条件记录；不要用不可核对的会话引用替代来源链接。
