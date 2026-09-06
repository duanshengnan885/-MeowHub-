# PRD Template

## Contents

- Template structure
- Optional sections (activated by project type)
- Section guidelines
- Acceptance criteria format
- Responsibility matrix

---

## Template structure

```markdown
# PRD — {PROJECT_TITLE}

> Version: V0.1
> Date: {DATE}
> Author: {AUTHOR}
> Related: {Link to Problem Framing / SRD if exists}

---

## 1. 修订记录

| 版本号 | 修改时间 | 修改人 | 修改内容 |
|--------|----------|--------|----------|
| V0.1 | {DATE} | {NAME} | 初稿 |

## 2. 需求背景

{Project background and business motivation.
Reference or summarize Problem Framing / SRD conclusions.}

## 3. 概要说明

| 项目 | 内容 |
|------|------|
| 对应需求 | {需求编号/链接} |
| 设计稿 | {Figma 链接} |
| 平台 | PC / iOS / Android / H5 |
| 语言 | {支持的语言} |
| 页面 | {涉及的页面} |
| 核心功能 | {一句话描述} |

## 4. 产品需求

### 4.0 用户流程概览（如适用 — 跨页面项目）

{User flow description or link to flow diagram}

| 流程节点 | 页面 | 用户行为 | 关键指标 | 分支条件 |
|---------|------|---------|---------|---------|
| ... | ... | ... | ... | ... |

页面间数据传递：
- 页面A → 页面B：传递 {参数}，用于 {目的}

### 4.0 用户群定义与差异化策略（如适用 — 分群项目）

**用户群细分标准：**

| 用户群 | 定义/判定规则 | 占比 |
|--------|-------------|------|
| ... | ... | ... |

**各群体差异化策略：**

| 维度 | 群体A | 群体B | 群体C |
|------|-------|-------|-------|
| ... | ... | ... | ... |

**群体切换/降级逻辑：**
- {切换条件和行为}

### 4.1 前端需求

#### 4.1.1 PC 端

{组件样式、展示规则、交互行为}

**验收标准（可选）：**
- [ ] {可验证的验收条件}

#### 4.1.2 APP / H5 端

{组件样式、展示规则、交互行为}

**验收标准（可选）：**
- [ ] {可验证的验收条件}

#### 4.1.3 跨平台差异汇总

| 维度 | PC 端 | APP / H5 端 |
|------|-------|-------------|
| 展示数量 | ... | ... |
| 交互方式 | ... | ... |
| 特殊差异 | ... | ... |

### 4.2 数据/业务逻辑

{数据源、排序规则、筛选逻辑、托底策略}

### 4.3 后台/CMS 需求

{后台配置页面、管理界面、字段说明、操作流程}

### 4.4 后端/接口需求

**PM 填写 — 业务概要：**
- 需要哪些新接口或改动（自然语言描述）
- 数据来源与业务规则
- 性能预期

**开发补充 — 技术细节：**
> ⚠️ 以下内容由开发 lead 补充
- 接口设计（路径、入参、出参、协议）
- 技术实现方案
- 缓存策略
- 依赖的外部服务

### 4.5 多语言/本地化（如适用）

- 各语言站差异化逻辑
- 内容回退/托底策略
- 翻译需求

### 4.6 内容/素材规范（如适用）

- 上传素材格式、尺寸、文件大小限制
- 内容审核规则
- 素材更新频率

## 5. 数据需求

### 5.1 数据埋点

{曝光、点击、加购等事件埋点需求}

### 5.2 A/B Testing

| 项目 | 内容 |
|------|------|
| Test Owner | {负责人} |
| Background | {测试背景} |
| Hypothesis | {测试假设} |
| 触发时机 | {何时触发分组} |
| 分组说明 | V0：... / V1：... |
| Metrics（核心指标） | ... |
| Observation Metrics | ... |

## 6. 非功能性需求

### 6.1 性能要求

{页面加载时间、接口响应时间、图片/视频加载策略}

### 6.2 降级/容错策略

{数据获取失败时的降级方案、组件加载失败的兜底展示}

### 6.3 无障碍 (ADA)

{ARIA 标签、键盘导航、屏幕阅读器兼容性}

### 6.4 SEO 影响

{新组件对 SEO 的影响、是否需要 SSR、结构化数据}

### 6.5 安全要求

{输入校验、上传文件类型限制、XSS 防护}

## 7. 上线策略

| 项目 | 内容 |
|------|------|
| 发布方式 | 全量 / 灰度 / 分批 |
| 依赖关系 | {前置条件和依赖项} |
| 回滚方案 | {异常时如何回滚} |
| 上线时间 | {目标日期} |
```

---

## Optional sections

These sections are only included when the project type warrants them.
They are NOT boilerplate to fill for every project.

| Section | Activated when | Project type |
|---------|---------------|-------------|
| §4.0 用户流程概览 | Multiple pages, funnel, conversion path | Cross-page flow |
| §4.0 用户群定义 | Different segments, personalization | Segmented |
| §4.5 多语言/本地化 | Multi-language support needed | Any with i18n |
| §4.6 内容/素材规范 | User-uploaded or managed content | Content-heavy |
| SRD §5.4 Phasing | Multi-phase delivery | Holistic optimization |

If a section is not activated, omit it entirely from the output.
Do not include empty optional sections.

---

## Section guidelines

**§2 需求背景:** Keep this to 1-2 paragraphs. Its job is to provide
context, not to re-argue the case (that's what the SRD is for).

**§4.4 后端/接口需求:** Split into two layers by design.
PM fills business-level description; dev lead fills technical details.
Mark the dev section with `> ⚠️ 以下内容由开发 lead 补充`.

**§6 非功能性需求:** For US-facing products, always include §6.3 ADA.
For homepage/high-traffic pages, always include §6.1 and §6.4.

**§7 上线策略:** Keep it brief. If there's an A/B test, the launch
strategy should reference §5.2.

---

## Acceptance criteria format

When including acceptance criteria in §4.1, use testable checkbox items:

Good: `- [ ] 当视频数量为 6 个时，左右翻页按钮置灰不可点击`
Bad: `- [ ] 翻页按钮正常工作`

Each criterion should be independently verifiable by QA.

---

## Responsibility matrix

| Section | PM | Design | Dev |
|---------|:--:|:------:|:---:|
| 1. 修订记录 | R | — | — |
| 2. 需求背景 | R | C | I |
| 3. 概要说明 | R | C | I |
| 4.0 用户流程/用户群 | R | C | C |
| 4.1 前端需求 | R | R | C |
| 4.2 数据/业务逻辑 | R | I | C |
| 4.3 后台/CMS | R | C | C |
| 4.4 后端（业务层） | R | I | C |
| 4.4 后端（技术层） | I | I | R |
| 4.5 多语言/本地化 | R | C | C |
| 4.6 内容/素材规范 | R | R | I |
| 5.1 数据埋点 | R | I | C |
| 5.2 A/B Testing | R | I | C |
| 6.1 性能 | C | I | R |
| 6.2 降级/容错 | C | I | R |
| 6.3 ADA | C | R | C |
| 6.4 SEO | R | C | C |
| 6.5 安全 | I | I | R |
| 7. 上线策略 | R | I | C |

R = 负责撰写 · C = 参与评审 · I = 知会
