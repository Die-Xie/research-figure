# research-figure

科研绘图 Codex skill：从论文和实现梳理科学依据，设计图的内容与提示词，生成和迭代位图，并在需要时复刻为可编辑的 draw.io 图。

## 项目结构

- `skills/research-figure/SKILL.md`：技能入口与工作流程。
- `skills/research-figure/references/`：提示词模板、设计审阅、draw.io 工作流和参考来源。
- `skills/research-figure/agents/openai.yaml`：Codex 技能展示信息。
- `tests/test_skill.py`：检查技能结构和本地 Markdown 引用。

## 使用与安装

将 `skills/research-figure` 复制到 Codex 的技能目录（通常是 `~/.codex/skills/research-figure`）即可安装。复制前请备份或比较目标目录中的既有版本；项目副本与已安装副本不会自动同步。安装或更新后，重新加载 Codex 会话以发现更改。

在对话中使用 `$research-figure`，并提供论文、代码或已有图等材料。技能也可根据科研绘图任务自动触发。数值和实验结果图应使用真实数据及绘图库生成。

## 开发与检查

直接修改 `skills/research-figure/` 中的文件，并保持 `SKILL.md` 与引用资料一致。项目没有第三方运行依赖；使用 Python 3 运行检查：

```sh
uv run --no-project python -m unittest discover -s tests -v
```

检查覆盖技能入口、基本元数据和 Markdown 相对链接是否存在；它不能替代实际绘图任务中的科学内容和视觉质量审阅。

当前项目从本机已有技能复制而来，保留了原有内容和参考资料。项目内的更改不会自动更新原位置的技能。
