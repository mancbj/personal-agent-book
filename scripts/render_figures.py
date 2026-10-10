#!/usr/bin/env python3
"""Render the book's editorial diagrams: one HTML source, portable SVG exports.

Layouts adapt diagram-design's minimal-light templates to offline Chinese
publishing. Run this file to redraw SVGs; build.py also produces HTML previews.
Only the stdlib and the MIT-licensed upstream exporter are needed.
"""
from pathlib import Path
import html
import math
import sys

from vendor.diagram_design_export import export_svg_document

ROOT = Path(__file__).resolve().parents[1]
PAPER, INK, MUTED = "#f5f1e8", "#18343f", "#526774"
ACCENT, TINT, RULE, WHITE = "#216e69", "#e5eee9", "#c5d0ca", "#fffdf8"
SANS = "Noto Sans CJK SC, PingFang SC, Microsoft YaHei, sans-serif"
SERIF = "Noto Serif CJK SC, Songti SC, serif"
UPSTREAM = "246d6d71d752245403d2bf28d27f124192584d18"


def attrs(values):
    return " ".join(f'{k.replace("_", "-")}="{html.escape(str(v), quote=True)}"'
                    for k, v in values.items() if v is not None)


class Figure:
    def __init__(self, slug, title, description, kind, height=720, subtitle=""):
        self.slug, self.title, self.description = slug, title, description
        self.kind, self.height, self.parts = kind, height, []
        self.rect(0, 0, 960, height, PAPER, stroke=None)
        self.text(40, 48, "PERSONAL AGENT  /  " + kind.upper(), 16, MUTED)
        self.text(40, 100, title, 32, INK, 600, family=SERIF)
        if subtitle:
            self.text(40, 140, subtitle, 20, MUTED)

    def rect(self, x, y, w, h, fill=WHITE, stroke=RULE, rx=0, **extra):
        self.parts.append("<rect " + attrs(dict(x=x, y=y, width=w, height=h,
                          rx=rx, fill=fill, stroke=stroke, stroke_width=1.2, **extra)) + "/>")

    def text(self, x, y, value, size=22, color=INK, weight=400,
             anchor="start", family=SANS, **extra):
        self.parts.append("<text " + attrs(dict(x=x, y=y, fill=color, font_size=size,
                          font_weight=weight, font_family=family, text_anchor=anchor,
                          **extra)) + ">" + html.escape(value) + "</text>")

    def lines(self, x, y, values, size=20, gap=32, color=MUTED, **extra):
        for n, value in enumerate(values):
            self.text(x, y + n * gap, value, size, color, **extra)

    def path(self, d, color=MUTED, arrow=True, dashed=False, **extra):
        marker = "accent" if color == ACCENT else "neutral"
        self.parts.append("<path " + attrs(dict(d=d, fill="none", stroke=color,
                          stroke_width=1.6, stroke_linecap="round", stroke_linejoin="round",
                          marker_end=f"url(#{self.slug}-{marker})" if arrow else None,
                          stroke_dasharray="5 5" if dashed else None, **extra)) + "/>")

    def line(self, x1, y1, x2, y2, color=RULE, **extra):
        self.parts.append("<line " + attrs(dict(x1=x1, y1=y1, x2=x2, y2=y2,
                          stroke=color, stroke_width=1.2, **extra)) + "/>")

    def circle(self, x, y, radius=4, fill=INK, **extra):
        self.parts.append("<circle " + attrs(dict(cx=x, cy=y, r=radius,
                          fill=fill, **extra)) + "/>")

    def label(self, x, y, value, color=MUTED):
        # Chinese labels use sans, with an opaque plate clear of the connector.
        width = 4 * math.ceil((len(value) * 20 + 16) / 4)
        self.rect(x - width / 2, y - 21, width, 28, PAPER, stroke=None)
        self.text(x, y, value, 20, color, anchor="middle")

    def node(self, x, y, w, h, title, notes=(), focal=False, dark=False, tag=None):
        fill = INK if dark else TINT if focal else WHITE
        stroke = INK if dark else ACCENT if focal else MUTED
        self.rect(x, y, w, h, fill, stroke, 6)
        color = PAPER if dark else ACCENT if focal else INK
        offset = 32 if tag is None else 60
        if tag:
            self.text(x + 20, y + 28, tag, 16, PAPER if dark else MUTED)
        self.text(x + 20, y + offset, title, 24, color, 600)
        self.lines(x + 20, y + offset + 36, notes, 20, 32,
                   PAPER if dark else MUTED)

    def footer(self, first, second=None):
        y = self.height - (100 if second else 68)
        self.line(40, y, 920, y)
        self.text(40, y + 36, first, 18, MUTED)
        if second:
            self.text(40, y + 68, second, 18, MUTED)

    def document(self):
        markers = "\n".join(
            f'<marker id="{self.slug}-{name}" markerWidth="8" markerHeight="6" '
            f'refX="8" refY="3" orient="auto" markerUnits="userSpaceOnUse">'
            f'<path d="M0 0 L8 3 L0 6 Z" fill="{color}"/></marker>'
            for name, color in (("neutral", MUTED), ("accent", ACCENT)))
        license_text = (ROOT / "scripts/vendor/diagram-design-LICENSE.txt").read_text()
        svg = (f'<svg xmlns="http://www.w3.org/2000/svg" width="960" height="{self.height}" '
               f'viewBox="0 0 960 {self.height}" role="img" '
               f'aria-labelledby="{self.slug}-title {self.slug}-desc">\n'
               f'<title id="{self.slug}-title">{html.escape(self.title)}</title>\n'
               f'<desc id="{self.slug}-desc">{html.escape(self.description)}</desc>\n'
               f'<!-- Layout adapted from cathrynlavery/diagram-design @ {UPSTREAM}.\n'
               f'{license_text}-->\n<defs>{markers}</defs>\n'
               + "\n".join(self.parts) + "\n</svg>")
        # Minimal-light template: local scroller, no JS, no remote font fetches.
        return (f'<!doctype html>\n<html lang="zh-CN"><head><meta charset="utf-8">'
                f'<meta name="viewport" content="width=device-width,initial-scale=1">'
                f'<title>{html.escape(self.title)} · Personal Agent</title><style>'
                f'*{{box-sizing:border-box}}body{{margin:0;background:{PAPER};color:{INK};'
                f'font-family:{SANS};padding:24px}}.frame{{max-width:100%;min-width:0;'
                f'width:960px;margin:auto}}.diagram-container{{width:100%;overflow-x:auto}}'
                'svg{display:block;width:100%;min-width:960px;height:auto}'
                '@media print{body{padding:0}.diagram-container{overflow:visible}'
                'svg{min-width:0}}</style></head><body><main class="frame">'
                f'<div class="diagram-container">{svg}</div></main></body></html>\n')


def handoff():
    f = Figure("01-handoff", "从一封通知，到一件办完的事",
               "人设定目标和边界，代理整理航班变更的影响并等待回复，重要动作须确认，结果经核验后才交付。",
               "swimlane", 840, "三条泳道区分责任；等待回复与交还决定都属于任务。")
    for y in (184, 364, 584):
        f.line(40, y, 920, y)
    f.lines(40, 244, ["你", "目标与决定"], 20, 32, INK, weight=600)
    f.lines(40, 436, ["代理", "准备与跟进"], 20, 32, INK, weight=600)
    f.lines(40, 652, ["外部服务", "实际回应"], 20, 32, INK, weight=600)
    # Ordered handoffs, drawn before the boxes.
    f.path("M268 320 V396")
    f.path("M380 448 H424")
    f.path("M536 508 V612", dashed=True)
    f.path("M648 656 H680 Q688 656 688 648 V488 Q688 480 696 480 H720", dashed=True)
    f.path("M824 404 V336", ACCENT)
    f.label(744, 568, "收到回复")
    f.label(776, 376, "需确认", ACCENT)
    f.node(156, 208, 224, 112, "目标与边界", ["保留原订单", "先准备，不付款"])
    f.node(156, 396, 224, 112, "察觉变化", ["航班推迟三小时", "找出关联安排"])
    f.node(424, 396, 224, 112, "整理与等待", ["酒店 · 接机 · 会议", "记录草稿与待办"])
    f.node(424, 612, 224, 88, "真实回应", ["客服确认或拒绝"])
    f.node(720, 208, 200, 128, "重要决定", ["发送、改签、付款", "分别确认"], focal=True)
    f.node(720, 404, 200, 128, "核对并交付", ["获准后再行动", "完成／等待／待定"])
    f.footer("按获准范围推进；请求已发出，不代表外部结果已生效。", "作者教学示意，不是某一产品的完整实测流程。")
    return f


def concept():
    f = Figure("02-concept-map", "把执行、推理与开放分开看",
               "执行位置与模型推理位置形成四种示意配置，软件开放程度另行核对，对话、任务和个人代理的能力可以重叠。",
               "quadrant", 840, "两个独立的位置维度；四格是配置示意，不是产品能力排名。")
    for x, title, note in [(40, "对话助手", "解释 · 建议 · 草稿"),
                           (344, "任务代理", "计划 · 工具 · 交付"),
                           (648, "个人代理", "个人上下文 · 持续跟进")]:
        f.text(x, 196, title, 24, INK, 600)
        f.text(x, 232, note, 20, MUTED)
    f.text(40, 280, "能力可以重叠；工作／个人是组织重点，权限分别管理。", 20, MUTED)
    f.text(40, 352, "模型推理", 20, INK, 600)
    f.text(364, 336, "本地执行", 22, INK, 600, anchor="middle")
    f.text(740, 336, "远程执行", 22, INK, 600, anchor="middle")
    f.rect(180, 360, 368, 160, TINT, stroke=None)
    f.line(176, 360, 920, 360)
    f.line(176, 528, 920, 528, MUTED)
    f.line(176, 704, 920, 704)
    f.line(552, 360, 552, 704, MUTED)
    f.text(144, 432, "本地", 22, INK, anchor="end")
    f.text(144, 604, "远程", 22, INK, anchor="end")
    cells = [(204, 404, "全本地链路", ["本机运行时 + 本机模型", "离线还需全部工具可用"], True),
             (576, 404, "远程任务，回接本地推理", ["需获准的推理连接", "仍有跨界传输"], False),
             (204, 576, "本地运行，调用云模型", ["工具靠近本机资源", "获准上下文会发往远程"], False),
             (576, 576, "远程运行与推理", ["托管运行时 + 远程模型", "仍需确认资源与权限"], False)]
    for x, y, name, lines, focal in cells:
        f.text(x, y, name, 23, ACCENT if focal else INK, 600)
        f.lines(x, y + 36, lines, 20, 32)
    f.footer("第三个维度：软件是否开放、配置由谁管理、状态能否迁移。", "本地安装不等于离线；开放运行时也可以部署在云端。")
    return f


def landscape():
    f = Figure("03-product-landscape", "产品版图：看入口，也看开放状态",
               "个人代理分为海外托管、国内动向、创业路线和开放运行时四个观察组，十一项产品全部列出，开放运行时连接本地与云端。",
               "tree", 920, "截至 2026-10-10 的观察分组；分组之间存在交集。")
    f.path("M224 480 H256", arrow=False)
    f.line(256, 236, 256, 740, MUTED)
    for y in (236, 404, 572, 740):
        f.line(256, y, 304, y, MUTED)
    f.node(40, 416, 184, 128, "个人代理", ["入口与运行环境", "分别核对"], focal=True)
    groups = [
        (172, "海外托管平台", ["Meta Muse · xAI Grok Bot", "OpenAI Dot（Dots） · Manus Cue"], "发布／文档／邀请体验；开放资格另查"),
        (340, "国内平台动向", ["腾讯 LightVela：官方产品文档", "字节 Spell：媒体曝光；千问：路线宣布"], "生态入口不等于全面开放"),
        (508, "创业公司路线", ["Instinct：通信中的私人助理", "Today AI 的 Today：生活记忆与提议"], "增长说法与产品定位不等于实测效果"),
        (676, "开放运行时与本地生态", ["OpenClaw · Hermes", "本地执行／自托管远程／平台托管"], "交集示例：LightVela 云端托管 Hermes"),
    ]
    for y, title, notes, bottom in groups:
        f.text(304, y + 28, title, 24, INK, 600)
        f.lines(304, y + 64, notes, 22, 32)
        f.text(304, y + 132, bottom, 18, MUTED)
        f.line(304, y + 148, 920, y + 148)
    f.footer("本地与云端生态并行；具体功能、地区、费用和准入见正文及附录 B。")
    return f


def resources():
    f = Figure("05-resource-boundaries", "混合部署：跨界的两条路线",
               "本地运行时靠近设备与私有资源，云端可调度获准的本地执行，本地运行时也可调用远程模型，两条路线须分别确认数据传输和权限。",
               "deployment", 840, "纯本地、纯云端与混合各有位置；连接不等于无限访问。")
    for x, title, note in [(40, "用户设备／私有网络", "本机应用 · 私有文件 · NAS · 硬件"),
                           (544, "远程基础设施", "平台托管／自托管；维护责任不同")]:
        f.rect(x, 184, 376, 424, fill=PAPER, stroke=MUTED, rx=8, stroke_dasharray="4 5")
        f.text(x + 20, 224, title, 24, INK, 600)
        f.text(x + 20, 260, note, 18, MUTED)
    f.path("M584 332 H376", dashed=True)
    f.path("M212 400 V460")
    f.path("M376 368 H464 Q472 368 472 376 V504 Q472 512 480 512 H584", ACCENT, dashed=True)
    f.label(480, 318, "获准任务")
    f.label(404, 452, "获准上下文", ACCENT)
    f.label(268, 440, "工具动作")
    f.node(80, 296, 296, 104, "本地运行时", ["工具与状态留在这端"])
    f.node(80, 460, 296, 104, "本地资源", ["访问范围由配置限定"])
    f.node(584, 296, 296, 104, "云端调度", ["连接获准的本地组件"])
    f.node(584, 460, 296, 104, "远程模型", ["可收到被允许的输入"], focal=True)
    f.text(40, 660, "四项核对", 24, INK, 600)
    f.lines(232, 660, ["原资料在哪里？模型收到什么？", "工具能动什么？日志与副本在哪里？"], 22, 36)
    f.footer("全本地路线还需本地模型与工具；纯云端须能合法触及目标资源。", "严格不外发或离线任务，应核对推理、工具、索引、日志与完整依赖链。")
    return f


def cycle():
    f = Figure("06-agent-cycle", "工作在循环中推进，状态持续留下",
               "代理在计划、行动、观察、修正和验收之间推进，每一步把必要记录写回共同任务状态，验收达标则结束，越界或不确定时暂停。",
               "loop", 848, "模型参与判断，工具实施动作，运行时保存状态并控制执行。")
    cx, cy, radius, w, h = 480, 448, 240, 200, 112
    stations = []
    for k in range(5):
        theta = -math.pi / 2 + k * 2 * math.pi / 5
        ux, uy = math.cos(theta), math.sin(theta)
        x = 4 * round((cx + radius * ux - w / 2) / 4)
        y = 4 * round((cy + radius * uy - h / 2) / 4)
        stations.append((x, y, theta, ux, uy))

    def intersections(box):
        x, y, theta, _, _ = box
        points = []
        for xe in (x, x + w):
            remainder = radius ** 2 - (xe - cx) ** 2
            if remainder >= 0:
                for ye in (cy - math.sqrt(remainder), cy + math.sqrt(remainder)):
                    if y <= ye <= y + h:
                        points.append((xe, ye))
        for ye in (y, y + h):
            remainder = radius ** 2 - (ye - cy) ** 2
            if remainder >= 0:
                for xe in (cx - math.sqrt(remainder), cx + math.sqrt(remainder)):
                    if x <= xe <= x + w:
                        points.append((xe, ye))
        return sorted(points, key=lambda p: (math.atan2(p[1] - cy, p[0] - cx) - theta + math.pi) % (2 * math.pi) - math.pi)

    for k, station in enumerate(stations):
        start = intersections(station)[-1]
        end = intersections(stations[(k + 1) % 5])[0]
        f.path(f"M{start[0]:.3f} {start[1]:.3f} A{radius} {radius} 0 0 1 {end[0]:.3f} {end[1]:.3f}")
        x, y, _, ux, uy = station
        # Use the rounded station centre for a true inward spoke.
        sx, sy = x + w / 2, y + h / 2
        dx, dy = sx - cx, sy - cy
        distance = math.hypot(dx, dy)
        vx, vy = dx / distance, dy / distance
        box_dist = min(w / 2 / abs(vx) if abs(vx) > 1e-9 else math.inf,
                       h / 2 / abs(vy) if abs(vy) > 1e-9 else math.inf)
        hub_dist = min(104 / abs(vx) if abs(vx) > 1e-9 else math.inf,
                       52 / abs(vy) if abs(vy) > 1e-9 else math.inf) + 6
        f.path(f"M{sx - box_dist * vx:.3f} {sy - box_dist * vy:.3f} "
               f"L{cx + hub_dist * vx:.3f} {cy + hub_dist * vy:.3f}",
               dashed=True, **{"class": "spoke"})
    names = [("1 计划", "条件与下一步"), ("2 行动", "获准工具与请求"),
             ("3 观察", "结果与外部状态"), ("4 修正", "变化与原有边界"),
             ("5 验收", "依据标准核对")]
    for (x, y, *_), (title, note) in zip(stations, names):
        f.node(x, y, w, h, title, [note], focal=title.startswith("5"))
    f.node(376, 396, 208, 104, "共同任务状态", ["证据 · 待办 · 回执"], dark=True)
    f.text(40, 728, "输入：目标、背景、资源、授权与验收标准。", 20, MUTED)
    f.footer("实线：推进工作；虚线：记录写回。达到验收则结束，否则继续核查。", "碰到边界或条件未知时暂停，交回人的决定，不自行扩大权限。")
    return f


def selection():
    f = Figure("07-selection-path", "选型是约束叠加，不是一题定阵营",
               "依次核对资料边界、执行资源、持续性和维护责任，任何条件都不能被后续偏好覆盖，再以权限范围及一周小试验证候选方案。",
               "process", 1000, "四次筛选都要做；右侧是缩小候选的条件，不是提前结束。")
    rows = [(184, "01", "资料可以去哪里？", "离线或不得外发", ["离线：全本地依赖", "不外发：受控链路"]),
            (348, "02", "动作发生在哪里？", "依赖本机／内网／硬件", ["保留本地执行", "或含本地端的混合"]),
            (512, "03", "需要跨时间跟进吗？", "检查触发与状态", ["一次性：工具／规则", "持续性：等待与恢复"]),
            (676, "04", "谁承担长期维护？", "前面硬约束仍有效", ["托管：核对服务边界", "自托管：记录维护成本"])]
    for y, _, _, _, _ in rows[:-1]:
        f.path(f"M268 {y + 112} V{y + 164}")
    f.path("M268 788 V836 Q268 844 276 844 H480 V864")
    for y, tag, question, condition, notes in rows:
        f.path(f"M496 {y + 56} H584", arrow=False)
        f.text(516, y + 44, "筛选", 18, MUTED)
    for y, tag, question, condition, notes in rows:
        f.node(40, y, 456, 112, question, [condition], tag=None)
        f.text(460, y + 28, tag, 16, MUTED, anchor="end")
        f.lines(604, y + 48, notes, 22, 36)
    f.node(40, 864, 880, 68, "权限能否缩小？再用一周小试验收候选方案", [], focal=True)
    f.footer("同等任务、同等验收：结果、主动分钟、等待、介入、金钱与维护。")
    return f


def time_gain():
    f = Figure("07-time-gain", "第一次未省时，五次合计才见收益",
               "教学示例中五次同等任务手工需要三百分钟，代理配置三十分钟、首次交代十分钟、首次验收纠错二十五分钟、后续四次各二十分钟，净节省一百五十五分钟。",
               "waterfall", 760, "沿用第 7 章的教学数字；单位为人的主动分钟，不是产品实测。")
    baseline, scale = 580, 1.1
    values = [("手工基线", "total", 300), ("首次配置", "delta", -30),
              ("首次交代", "delta", -10), ("验收纠错", "delta", -25),
              ("后续四次", "delta", -80), ("净省时间", "total", 155)]
    for value in (0, 100, 200, 300):
        y = baseline - value * scale
        f.line(96, y, 920, y)
        f.text(76, y + 6, str(value), 18, MUTED, anchor="end")
    f.text(40, 196, "主动分钟", 18, MUTED)
    running, positions = 300, []
    for k, (name, role, value) in enumerate(values):
        x, width = 112 + k * 136, 104
        if role == "delta":
            before, after = running, running + value
            top, bottom = baseline - max(before, after) * scale, baseline - min(before, after) * scale
            running = after
        else:
            top, bottom = baseline - value * scale, baseline
        positions.append((x, width, top, bottom, running))
        if k < len(values) - 1:
            f.line(x + width, baseline - running * scale, x + 136, baseline - running * scale,
                   MUTED, data_carry=running)
    for k, ((name, role, value), (x, width, top, bottom, _)) in enumerate(zip(values, positions)):
        focal = k == len(values) - 1
        f.rect(x, top, width, bottom - top, TINT if focal else WHITE,
               ACCENT if focal else MUTED, data_role=role,
               data_value=f"{value:+}" if role == "delta" else value, data_name=name)
        label = f"−{abs(value)}" if value < 0 else str(value)
        f.text(x + width / 2, bottom + 12 if role == "delta" else top - 8,
               label, 23, ACCENT if focal else INK, 600, anchor="middle",
               dominant_baseline="hanging" if role == "delta" else "text-after-edge")
        f.text(x + width / 2, 624, name, 20, INK, 600, anchor="middle")
    f.footer("首次代理投入 65 分钟，多于手工的 60 分钟；五次投入合计 145 分钟。", "比较前提：任务数量、规模与结果质量可比；等待、订阅与用量另记。")
    return f


def task_states():
    f = Figure("08-task-states", "等待是状态，恢复要先核对事实",
               "任务从准备、执行到核验与完成，缺信息或缺批准则进入等待；恢复前确认已发生动作、当前状态和授权，不能继续则停止。",
               "state machine", 776, "状态告诉你下一步由谁负责；请求超时不能当作从未执行。")
    f.text(40, 196, "正常推进", 20, MUTED)
    for start, end in [(200, 280), (440, 520), (680, 760)]:
        f.path(f"M{start} 272 H{end}")
    f.label(240, 255, "已具备")
    f.label(480, 255, "有回执")
    f.label(720, 255, "达标")
    f.path("M372 324 V432", dashed=True)
    f.path("M440 492 H520", dashed=True)
    f.path("M612 432 V392 Q612 384 604 384 H432 Q424 384 424 376 V324", dashed=True)
    f.path("M612 552 V632", dashed=True)
    f.label(414, 396, "缺信息／批准")
    f.label(480, 475, "可恢复")
    f.label(528, 372, "重新核对")
    f.label(664, 604, "无法继续")
    f.node(40, 220, 160, 104, "准备中", ["目标与边界"])
    f.node(280, 220, 160, 104, "执行中", ["记录请求"])
    f.node(520, 220, 160, 104, "核验中", ["查真实状态"])
    f.node(760, 220, 160, 104, "已完成", ["验收达标"])
    f.text(40, 420, "中断／恢复", 20, MUTED)
    f.node(280, 432, 160, 120, "等待中", ["等信息／批准", "说明期限"], focal=True)
    f.node(520, 432, 184, 120, "恢复核对", ["已发生动作", "授权仍有效？"])
    f.node(520, 632, 184, 64, "已停止")
    f.lines(40, 636, ["任一阶段可暂停。", "停止新动作不撤回历史动作。"], 20, 32)
    f.footer("本图为状态总览；等待信息和等待批准在实际任务中应分别记录。")
    return f


def permissions():
    f = Figure("09-permission-layers", "每一层动作，都要单独授权",
               "读取、起草、修改、发送以及付款承诺五类动作分别限定对象、资源与有效期，工作、生活、财务和公开表达的身份权限另行隔离。",
               "layer stack", 800, "动作影响逐步加大；已有低层权限不自动获得更高层权限。")
    rows = [("01", "读取", "获准资料；同时核对模型与外发"),
            ("02", "起草", "方案与草稿；不改变外部状态"),
            ("03", "修改", "限定文件与动作；保留差异与恢复"),
            ("04", "发送", "核对账号、对象、渠道与正文"),
            ("05", "付款／承诺", "金额、订单、对象；防止重复执行")]
    for k, (tag, title, note) in enumerate(rows):
        y, focal = 184 + k * 80, k == 4
        f.rect(40, y, 880, 76, TINT if focal else WHITE, ACCENT if focal else RULE)
        f.text(60, y + 46, tag, 18, MUTED)
        f.text(128, y + 46, title, 24, ACCENT if focal else INK, 600)
        f.text(352, y + 46, note, 22, MUTED)
    f.text(40, 640, "身份另设", 24, INK, 600)
    f.text(232, 640, "工作  /  生活  /  财务  /  公开表达", 24, INK)
    f.text(232, 680, "角色名称不等于权限隔离，按真实共享范围检查。", 20, MUTED)
    f.footer("每层限定资源、对象、动作、额度、时间与有效期。", "异常时：停止新动作 → 收回访问 → 保存事实 → 核对结果。")
    return f


def evolution():
    f = Figure("10-evolution", "组件逐步汇合，路线继续并行",
               "三个分段时间轴按真实年份间隔列出概念愿景、代理研究、消费产品以及行动和工具协议节点；分段采用各自刻度，不代表连续或单线演进。",
               "timeline", 1040, "日期对应不同类型的事件；三段独立刻度，间隔按真实年份绘制。")
    # Three labelled ranges prevent a compressed recent cluster from faking time.
    panels = [
        (1987, 2003, 320, [(1987, "愿景", ["Knowledge Navigator", "对话与协作的概念影片"], -1),
                           (1994, "研究", ["Maes：个人软件代理", "减轻工作与信息过载"], 1),
                           (2003, "研究启动", ["CALO", "学习、组织与执行"], -1)]),
        (2011, 2015, 584, [(2011, "产品", ["Siri / iPhone 4S"], -1),
                           (2012, "产品", ["Google Now", "主动提示"], 1),
                           (2014, "产品", ["Echo / Alexa"], -1),
                           (2015, "产品试验", ["Messenger M", "真人与 AI 共同代办"], 1)]),
        (2022, 2024, 848, [(2022, "研究", ["ReAct", "行动与观察"], -1),
                           (2023, "接口", ["模型函数调用"], 1),
                           (2024, "能力／协议", ["电脑操作测试 · MCP"], -1)])]
    for start, end, baseline, events in panels:
        f.text(40, baseline - 128, f"{start}—{end}", 18, MUTED)
        f.line(80, baseline, 880, baseline, MUTED)
        for year, kind, notes, side in events:
            x = 80 + (year - start) / (end - start) * 800
            f.circle(x, baseline, 5, ACCENT if year == 2024 else INK)
            f.line(x, baseline, x, baseline + side * 24, MUTED)
            anchor = "start" if x < 260 else "end" if x > 700 else "middle"
            text_x = x if anchor == "middle" else max(40, x - 8) if anchor == "start" else min(920, x + 8)
            y = baseline - 96 if side == -1 else baseline + 44
            f.text(text_x, y, f"{year} · {kind}", 22, INK, 600, anchor)
            f.lines(text_x, y + 32, notes, 20, 28, anchor=anchor)
    f.footer("本地派、云端派与混合部署，是当下资源分工，不是技术优劣的终点排序。", "研究目标不等于消费产品能力；人机混合不等于本地／云端混合。")
    return f


def future():
    f = Figure("11-future-signals", "未来不靠押注，用信号持续检验",
               "大众生活助手、专业工作代理、自主可迁移环境三种情景各有前提、观察信号与反证，可以并行存在，不能用产品定位代替实际验证。",
               "tree", 888, "三种并行情景；每种判断都保留可以推翻自己的证据。")
    f.line(224, 456, 264, 456, MUTED)
    f.line(264, 248, 264, 664, MUTED)
    for y in (248, 456, 664):
        f.line(264, y, 312, y, MUTED)
    f.node(40, 392, 184, 128, "可验证未来", ["前提", "信号与反证"], focal=True)
    rows = [(184, "01  大众生活助手", ["前提：服务可连，提醒与授权克制", "信号：少催促，净省心持续增加", "反证：打断增加，仍需逐步重查"]),
            (392, "02  专业工作代理", ["前提：工具权限、规则与验收明确", "信号：成果可验收，异常能交回", "反证：复核返工吞掉收益"]),
            (600, "03  自主可迁移的代理环境", ["前提：配置状态能恢复，维护可承担", "信号：换环境后，小任务可继续", "反证：只能导出聊天，升级常破坏流程"])]
    for y, title, notes in rows:
        f.text(312, y + 24, title, 24, INK, 600)
        f.lines(312, y + 64, notes, 22, 36)
        f.line(312, y + 164, 920, y + 164)
    f.footer("本地、云端与混合按资源和数据条件分工；位置、开放程度、控制权分别判断。", "作者情景分析，不承诺普及时间、产品成功率或单一获胜路线。")
    return f


def migration():
    f = Figure("12-migration", "能导出记录，还要能安全地继续",
               "迁移先暂停旧环境，核对和导出任务状态，在新环境检查上下文并重新授权，最后用低风险任务验证恢复，凭证与付款权限不自动继承。",
               "process", 720, "把状态与行动权限分开：搬走必要上下文，重新决定能做什么。")
    xs = [40, 220, 400, 580, 760]
    for x in xs[:-1]:
        f.path(f"M{x + 152} 372 H{x + 180}")
    steps = [("01", "暂停旧环境", ["任务与触发器", "停止新动作"], False),
             ("02", "核对与导出", ["已完成／待办", "未知状态另列"], False),
             ("03", "导入并检查", ["来源与适用范围", "状态是否可用"], False),
             ("04", "重新授权", ["范围与对象", "期限与额度"], True),
             ("05", "小任务验证", ["核对回执", "防止重复执行"], False)]
    for x, (tag, title, notes, focal) in zip(xs, steps):
        f.text(x, 252, tag, 20, MUTED)
        f.rect(x, 284, 152, 176, TINT if focal else WHITE, ACCENT if focal else MUTED, 6)
        f.text(x + 12, 328, title, 22, ACCENT if focal else INK, 600)
        f.lines(x + 12, 376, notes, 18, 32)
    f.line(40, 516, 920, 516)
    f.text(40, 564, "不自动继承", 24, INK, 600)
    f.text(264, 564, "登录凭证  /  付款权限  /  长期授权", 23, INK)
    f.text(40, 608, "旧环境的已发消息、已提交订单仍需核对；不要让两端重复行动。", 20, MUTED)
    f.footer("作者迁移验收框架；导出功能不等于完整恢复能力，按实际产品验证。")
    return f


BUILDERS = [handoff, concept, landscape, resources, cycle, selection,
            time_gain, task_states, permissions, evolution, future, migration]


def render(output_dir=None):
    preview = Path(output_dir) if output_dir else Path("/tmp/personal-agent-diagrams")
    preview.mkdir(parents=True, exist_ok=True)
    figures = []
    for builder in BUILDERS:
        figure = builder()
        document = figure.document()
        source = preview / (figure.slug + ".html")
        source.write_text(document)
        exported = export_svg_document(document, source, system_fonts=True)
        target = ROOT / "assets/figures" / (figure.slug + ".svg")
        if not target.exists() or target.read_text() != exported:
            target.write_text(exported)
        figures.append(figure)
    links = "\n".join(f'<li><a href="{f.slug}.html">{html.escape(f.title)}</a>'
                       f' <small>{html.escape(f.kind)}</small></li>' for f in figures)
    (preview / "index.html").write_text(
        '<!doctype html><html lang="zh-CN"><meta charset="utf-8">'
        '<meta name="viewport" content="width=device-width,initial-scale=1">'
        f'<title>全书图表 · Personal Agent</title><style>body{{max-width:780px;'
        f'margin:48px auto;padding:0 24px;background:{PAPER};color:{INK};'
        f'font:18px/2 "Noto Sans CJK SC",sans-serif}}a{{color:{ACCENT}}}'
        'small{display:block;color:#526774}</style><h1>全书图表</h1><p>'
        '图表可以独立打开；宽图在手机上可左右滑动。</p><ol>' + links + '</ol>'
        '<p>设计参考 <a href="https://github.com/cathrynlavery/diagram-design">'
        'Diagram Design</a>（MIT），内容与书籍配色由本项目编写。</p></html>\n')
    return figures


if __name__ == "__main__":
    results = render(sys.argv[1] if len(sys.argv) > 1 else None)
    print(f"Rendered {len(results)} diagrams: HTML sources and standalone SVG exports")
