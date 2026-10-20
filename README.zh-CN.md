# Clear Story Presentations

[English README](README.md) · [GitHub 发布指南](docs/PUBLISHING.md) · [核心 Skill](SKILL.md) · [参考资源](references/10-research-library.md) · [测试说明](docs/EVALUATION.md)

**一个教 Claude Code「怎么讲清楚一件事」的通用演讲与汇报 Skill。** 它重点解决的不是如何套 PPT 模板，而是怎样判断听众需要知道什么、怎样组织论证、怎样解释复杂内容、怎样删去噪声，以及怎样用 Slides 和视觉证据帮助理解。

适用范围：学术报告、技术分享、课堂讲解、管理层简报、项目进度汇报、产品演示、培训、Pitch，以及现有幻灯片的逻辑/视觉审查。

**核心流程：** 明确受众和目标 → 提炼主张与证据 → 构建故事主线 → 解释与删减 → 逐页 Storyboard → 视觉设计与实现 → 排练及质量检查。

### 跟普通 PPT 生成器有什么不同？

- 不把论文目录、会议纪要、周报 bullet 直接搬进 Slides，而是围绕**听众的问题**组织内容。
- 不强制将每个话题装进「背景—方法—结果」或三栏卡片模板。
- 不只讲“说什么”，还设计“为什么现在说”“先解释哪个概念”“用哪个例子最容易理解”。
- 不以华丽视觉掩盖不充分的证据，不编造数字、实验结果或引用。
- 严格区分**现场演讲**与**独立阅读的报告型 Slides**。
- 可以先只输出故事主线、讲稿或 Storyboard，不强迫生成 PPTX。

### 安装到 Claude Code

全局使用（macOS/Linux）：

```bash
git clone https://github.com/YOUR_USERNAME/clear-story-presentations.git \
  ~/.claude/skills/clear-story-presentations
```

某个项目内使用：

```bash
mkdir -p .claude/skills
git clone https://github.com/YOUR_USERNAME/clear-story-presentations.git \
  .claude/skills/clear-story-presentations
```

请在仓库发布后将 `YOUR_USERNAME` 换成实际用户名。也可以下载 ZIP，把**整个文件夹**放进对应目录。Claude Code 的官方安装与触发说明见 [文档](https://code.claude.com/docs/en/skills)。

### 怎么用？

**学术报告：**

```text
/clear-story-presentations 我需要做一个 12 分钟的论文报告。
请先阅读论文和结果，提炼最重要的主张、证据和创新点，
重组故事、设计每页要回答的听众问题及最适合的图，
再写自然的英文讲稿。先不要套 PPT 模板。
```

**技术讲解：**

```text
/clear-story-presentations 我要向非专家解释一个复杂技术。
请先分析听众的知识基础，用一个贯穿始终的例子逐步说明，
指出容易误解的环节，并设计 8 分钟的讲解主线。
```

**去 AI 味：**

```text
/clear-story-presentations 请审查这些 Slides：
重点找出重复、信息堆砌、逻辑断层、没必要的卡片和口号。
给出有证据、具体且自然的改写，并解释每页为什么这样设计。
```

看 [完整示例](examples/launch-decision-storyboard.md)，了解它如何把散乱信息改成有目的的汇报。

### 文件与能力边界

- `SKILL.md` 是主工作流；`references/` 包含 11 份按需加载的专业手册。
- `evals/evals.json` 中有 9 个测试**场景**；目前未证明它们在真实 Claude Code 评测中均通过。
- `scripts/check_skill.py` 提供无需第三方依赖的**结构检查**，并非实际模型效果评分。
- 不附带 PPTX 引擎或图片生成服务。最终 `.pptx`、PDF、渲染效果，取决于本地其他工具和配置。
- 37 条公开资源列在参考索引，**它们是阅读线索，不是本仓库自带的软件或资产**。请核对第三方许可证。

### 开源与贡献

- 贡献指南：[CONTRIBUTING.md](CONTRIBUTING.md)
- 评测与发布证据：[docs/EVALUATION.md](docs/EVALUATION.md)
- 来源和版权说明：[docs/SOURCES.md](docs/SOURCES.md)
- 此仓库原创文本及脚本按 [MIT License](LICENSE) 发布；第三方文章、仓库和图片的版权不因此改变。

**发布状态：** 结构检查可以在本地执行；正式发布前，建议使用两三个真实案例进行 Claude Code 人工评测，并在 README 中展示成果。未经测试不要宣称“已验证生成专业 PPT”或“通过所有评测”。
