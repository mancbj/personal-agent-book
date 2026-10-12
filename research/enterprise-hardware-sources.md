# 企业应用与实体设备：新增两章的来源和争议记录

核查日期：**2026-10-12**。对应新增第 10、11 章。本记录只说明这些公开资料能够支持哪些有限结论；企业产品、眼镜、家居系统和机器人均未进行统一实机测试、采购验证或安全认证。

## 企业应用：发布能力、采用阶段与身份边界

| 原始来源 | 本书采用的有限结论 | 不据此推出 |
| --- | --- | --- |
| [飞书 aily 官方介绍](https://www.feishu.cn/content/3d5z9ttt) | 企业级智能体平台提供技能、知识、调优和多渠道发布路径 | 所有客户已稳定完成跨系统任务、默认有全部企业数据权限 |
| [Microsoft 365 Agents 管理员指南](https://learn.microsoft.com/microsoft-365/copilot/agent-essentials/m365-agents-admin-guide) | 管理策略、智能体清单、分配和部署属于企业治理流程 | 系统能自行决定组织中的业务审批和法律责任 |
| [ChatGPT Workspace Agents 文档](https://help.openai.com/en/articles/20001143-chatgpt-workspace-agents-for-enterprise-and-business) | 工作区智能体可创建、分享和运行；文档警告个人连接凭证可能因发布而被他人调用 | 所有分享都会造成凭证泄露，或管理员设置能自动挡住全部误用 |
| [腾讯元器发布到企业微信](https://yuanqi.tencent.com/guide/publish-agent-work-wechat) | 企业微信是一个具体的发布渠道 | 渠道内的智能体已获得全部业务系统执行权 |
| [麦肯锡 2025 年 AI 状态调查](https://www.mckinsey.com/our-insights/the-state-of-ai-2025) | 23% 的受访者报告其组织在至少一个职能扩展智能体，另有 39% 开始实验 | 23% 的所有企业已全组织部署、已达到统一 ROI 或经过独立审计 |
| [麦肯锡 2026 年 AI 状态调查](https://www.mckinsey.com/capabilities/quantumblack/our-insights/the-state-of-ai) | 约两成受访者报告智能体在整个组织范围进入扩展阶段；37% 报告 AI 整体对 EBIT 有正向贡献 | 两年范围不同的指标可直接作增长率；37% 是智能体单独的利润率 |
| [NIST 2026 年智能体身份与授权概念文件](https://www.nist.gov/news-events/news/2026/02/new-concept-paper-identity-and-authority-software-agents) | 智能体身份与授权是标准实践尚需验证的议题 | 该概念文件是已实施的强制规定或一套完整成型的技术标准 |
| [Google A2A 公告](https://developers.googleblog.com/en/a2a-a-new-era-of-agent-interoperability/) | 提供智能体间互操作方向 | 协议授予跨组织业务许可、保证结果可信 |
| [Google AP2 公告](https://cloud.google.com/blog/products/ai-machine-learning/announcing-agents-to-payments-ap2-protocol) | 提出代理购物的意图与付款授权证据 | 所有商家已接入、退款与责任已有统一法律答案 |

麦肯锡的调查是受访者报告；2025 年口径为“至少一个业务职能”，2026 年另问“整个组织范围”，不能直接相减。企业章不使用供应商公布的客户数、收入、节省工时来推导一般 ROI。五道边界、角色划分、差旅流程与验收指标为作者分析。

## 硬件：入口、控制、物理动作和服务寿命

| 原始来源 | 本书采用的有限结论 | 不据此推出 |
| --- | --- | --- |
| [Meta Ray-Ban Display 公告](https://about.fb.com/news/2025/09/meta-ray-ban-display-ai-glasses-emg-wristband/) | 眼镜显示与 EMG 腕带作为已公布并在美国限定渠道上市的交互方式 | 完整个人智能体已驻留眼镜、全球可用、所有任务可离线完成 |
| [RealWear Navigator 520 页面](https://www.realwear.com/devices/navigator-520) | 面向工业现场的免手持远程协作、数字工作流和 AI 支持，为厂商功能描述 | 某个客户已取得特定 ROI、眼镜可自主操作生产设备 |
| [Home Assistant 本地语音指南](https://www.home-assistant.io/voice_control/voice_remote_local_assistant) | 在指定配置下语音识别、意图处理与回复可以在本地完成 | 接入云模型和远程工具以后仍零外发，或所有家居任务均离线可用 |
| [Matter 1.5 公告](https://csa-iot.org/newsroom/matter-1-5-introduces-cameras-closures-and-enhanced-energy-management-capabilities/) | 标准扩展摄像头、门窗类设备及能源管理能力 | 所有设备已经升级、标准替用户授权查看或行动 |
| [Figure 02 在 BMW 的部署报告](https://www.figure.ai/news/production-at-bmw) | 公司报告了约 11 个月的限定工业部署和操作经验 | 独立核验的全行业生产率、家用通用能力 |
| [Google DeepMind Gemini Robotics On-Device 公告](https://deepmind.google/blog/gemini-robotics-on-device-brings-ai-to-local-robotic-devices/) | 开发工具和设备端模型向选定测试者开放 | 大众消费者已可安装，整机全流程离线且安全 |
| [1X NEO 介绍](https://www.1x.tech/discover/neo-home-robot) | 家庭机器人接受早期订购，并公布计划交付安排 | 大规模实际交付、家庭任务可靠性已独立验证 |
| [NIST 机器人自主系统测量](https://www.nist.gov/programs-projects/measurement-science-robotics-and-autonomous-systems-program) | 物理机器人系统需验证操作、安全等表现 | 任何具体机器人已获安全认证 |
| [NIST SP 800-82 Rev. 4 初始公开草案](https://csrc.nist.gov/pubs/sp/800/82/r4/ipd) | 工业运行技术安全同时关注性能、可靠性与安全 | 草案是已生效的机器人法规；也不把工业指南直接套作家用认证 |
| [Humane Ai Pin 停服通知](https://support.humane.com/hc/en-us/articles/34374173951373-Important-Update-for-Consumer-Ai-Pin-Customers) | 云端服务结束后，依赖云端的语音和 AI 功能停止；说明设备服务寿命的重要性 | 所有云端设备都会同样停服或所有本地设备永续可用 |

硬件章的三层能力和四周试用表是作者的阅读框架，不是产业统一等级。产品状态分别写作**实际上市、限定工业部署、选定测试、早期预订**；联网标准、设备入口与完整个人智能体不混为一谈。

## 值得保留的分歧

| 张力 | 正文怎样处理 | 后续什么证据会改变判断 |
| --- | --- | --- |
| 助手越懂员工，企业越容易办事；员工越难保留私人边界 | 私人偏好可经选择传入，组织知识与凭证分开 | 可撤销、按任务传递资料的跨组织实际流程 |
| 智能体创建量增加，企业 ROI 却未必显现 | 以完整合格任务减去集成、复核、纠错和运维成本 | 长期、对照、可复核的任务级数据 |
| 可穿戴提供即时现场上下文，也可能记录旁人 | 分开采集、提示、保存和关闭 | 地区规则、设备版本、实际使用记录与退出机制 |
| 本地控制靠近设备，云端模型可能更强 | 区分执行、推理、工具与日志位置 | 同一任务在不同部署下的成功、成本与数据流记录 |
| 机器人演示和真实部署都在增加，通用家用仍需证据 | 工厂、测试、预订分别标记，不外推普及 | 实际交付、持续可靠性、人工接管和安全数据 |
| 接口和标准改善互通，业务授权仍由人和组织决定 | 把连接能力、行动许可和责任分开 | 可互认身份、可核查授权和真实争议处理流程 |

未对跨地区员工数据、劳动关系、机器人准入和具体交易责任作法律判断。原第三、四篇来源记录保留首次写作时的历史章节编号与版本范围；当前全书导航见附录 E 和 `TOC.md`。
