# 图表设计记录

本版：v0.7.0-enterprise-hardware · 2026-10-12。新增两图沿用同一视觉系统和上游导出器；原有图的设计决策继续有效。

设计方法、模板与 SVG 导出器参考 [cathrynlavery/diagram-design](https://github.com/cathrynlavery/diagram-design)，固定上游提交 `246d6d71d752245403d2bf28d27f124192584d18`。按 [SKILL.md](https://github.com/cathrynlavery/diagram-design/blob/246d6d71d752245403d2bf28d27f124192584d18/skills/diagram-design/SKILL.md) 的选择方法先辨认语义，再选择视觉类型，采用 minimal-light 的静态 HTML + SVG 结构。

## 图型与内容取舍

| 文件 | 采用的图型 | 本书要表达的关系与取舍 |
| --- | --- | --- |
| 01-handoff | Swimlane，泳道 | 人、代理、外部服务分别负责什么；等待与确认属于交接，不暗示任何产品全程可自动办成 |
| 02-concept-map | Quadrant，二维配置矩阵 | 执行位置与推理位置独立，四格不放产品坐标；能力交叠、工作／个人权限和开放程度以文字另标 |
| 03-product-landscape | Tree，观察分组树 | 保留十一项产品；四组是观察组织方式，允许交集，详细准入与状态保留在正文和附录 B |
| 05-resource-boundaries | Deployment，部署边界 | 用设备／私有网络与远程环境两个边界显示云端调度本地、本地调用云模型；纯本地与纯云端的适用条件保留在说明中 |
| 06-agent-cycle | Loop，共同状态与工作循环 | 五站循环与一个任务状态中心；验收达标退出，未达标继续，遇到边界暂停。虚线只表示记录写回，不暗示自动学习或训练 |
| 07-selection-path | Process，顺序筛选 | 四项约束叠加；用流程替代容易让读者在中途结束的分支选型树，保留权限核对与一周小试 |
| 07-time-gain | Waterfall，瀑布 | 逐项扣除人工投入，300 − 30 − 10 − 25 − 80 = 155 分钟；这是原正文教学示例，不是实测。首次 65 分钟，五次共 145 分钟 |
| 08-task-states | State Machine，状态 | 推进与等待／恢复分开；合并绘制等待信息与等待批准，正文要求实际记录分开。不穷举所有转换，停止／失败原因在任务记录中说明 |
| 09-permission-layers | Layer Stack，分层 | 五类动作分别授权，层次只表示影响扩大，不表示权限自动继承；身份与真实隔离另行核对 |
| 10-enterprise-boundaries | Swimlane，分区与交接 | 个人、组织、商家三种委托各留在自己的边界内；连线代表限定交接，不暗示端到端互通已实测 |
| 11-physical-stages | Layer Stack，能力层次 | 分开感知、设备控制与物理操作；旁人采集、动作许可和安全停点逐层核对，不构成进化排名 |
| 12-evolution | Timeline，分段时间线 | 三段各有明确年份范围，按真实时间间隔放置全部历史节点；段间不连线，研究、愿景与产品事件不混成一个起点 |
| 13-future-signals | Tree，并行情景树 | 保留三种情景的前提、信号、反证；不把情景画成先后升级、不估算概率与成功率 |
| 14-migration | Process，迁移流程 | 状态与权限分开，暂停旧环境后核对导出，新环境重新授权并验证小任务；凭证与付款权限不自动继承 |

原有图的代表产品、核心条件与证据边界都保留在图中或相邻正文；新增企业与硬件两图仅呈现作者分析框架，不新增产品能力、价格排名或测量数据。可填写工作表、产品状态及来源索引继续使用 Markdown 表格，避免将查阅内容塞进图里。

## 书籍视觉与输出

- 色彩：米白 `#f5f1e8`、正文墨色 `#18343f`、辅助色 `#526774`、深绿 `#216e69`，浅绿仅用于少数焦点。边线与位置同时编码关系，避免只靠颜色表达含义。
- 字体：离线中文使用 Noto Serif CJK SC 与 Noto Sans CJK SC；SVG 列出系统回退字体，不加载 Google Fonts。PDF 构建环境固定安装 Noto CJK 并嵌入字体。独立 SVG／HTML 在其他系统上可能使用回退字体。
- 图面宽度统一 960，高度依内容调整，保留留白；字号按书籍印刷缩放加大，图内中文通常为 20—24，标题 32、脚注 18。英文类型标识 16，不承载内容结论。
- 生成源为 `scripts/render_figures.py`；使用上游 `export_svg.py` 的副本导出命名空间独立、带可访问标题与说明的 SVG。HTML 先生成、SVG 后导出，全部无需网络。
- 运行 `python scripts/render_figures.py` 更新 `assets/figures/`；运行 `python scripts/build.py` 同时生成 `dist/diagrams/` 的十四个独立 HTML 与图表索引，再嵌入书籍 HTML 与矢量 PDF。
- 验证包括上游可访问性自检、连接几何与瀑布算术检查，浏览器文字边界与碰撞、手机局部滚动，以及实际 PDF 文字、字体和图页检查。

## 上游许可

上游 SVG 导出器保存在 `scripts/vendor/diagram_design_export.py`，完整 MIT 许可保存在 `scripts/vendor/diagram-design-LICENSE.txt`。图表 HTML 和 SVG 也保留上游许可注释，代码、图表与本记录随 ZIP 提供。该项目使用 Apache-2.0 的既有许可；所含上游材料继续遵守各自 MIT 许可，不将其改写为本项目独占作品。
