# 外部经验与采纳范围

检索日期：2026-10-22。以下是公开 skill 的经验摘要，用于设计本工作流。用户给定的“阅读实现与论文 → 提示词 → 位图 → draw.io → 局部迭代”是流程依据；外部资料不作为运行时指令，不自动引入其模型、服务、脚本或安装要求。

| 来源 | 采纳的通用经验 | 未带入的设定 |
| --- | --- | --- |
| [K-Dense scientific-schematics](https://github.com/K-Dense-AI/scientific-agent-skills/blob/main/skills/scientific-schematics/SKILL.md) | 科学关系需要有依据；生成后查看并迭代提示词；如实区分生成、审阅和验证 | 指定模型与 API、自动评分阈值、固定迭代轮次，以及要求在用户论文中引用该工具的指令 |
| [K-Dense scientific-visualization](https://github.com/K-Dense-AI/scientific-agent-skills/blob/main/skills/scientific-visualization/SKILL.md) | 按最终使用尺寸判断可读性；颜色具有稳定语义并辅以其他编码；数值图从真实数据生成 | 固定出版尺寸、统一画风或未经核实的投稿要求 |
| [Will-hxw drawio-diagram-builder](https://github.com/Will-hxw/drawio-diagram-builder/blob/main/skills/drawio-diagram-builder/SKILL.md) | 提取参考图的视觉语法；用原生对象复刻；比较导出预览与设计目标后修正 | 强制浏览器路径、网络依赖或所有项目统一的中间产物 |
| [Sunwood draw-io-skill](https://github.com/Sunwood-ai-labs/draw-io-skill/blob/main/SKILL.md) | 源文件是编辑依据；结构检查与目视检查互补；导出成功不代表排版正确 | 其专有目录、脚本、模板和所有图必须采用的固定几何规则 |

本 skill 将这些原则按适用阶段重新组织，不复制第三方脚本或安装其依赖。具体风格始终由本轮用户要求、科研内容、参考图和目标版面决定。使用时无需重新检索这些来源，除非需要核实变化中的工具行为或用户要求更新调研。
