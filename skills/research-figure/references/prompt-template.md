# 高质量文生图提示词：先设计可视表达

用于新图设计和底图迭代。图的目标是帮助读者快速理解算法或框架及其 motivation；图形、对象变化和流程关系是主要信息载体，正文承担完整叙事与论证。提示词应规定如何把科学内容画出来，而不只是要求包含哪些概念。

## 1. 从论文内容提炼图的理解目标

依据已核对的论文和实现，用简短说明回答：

- 研究处理什么对象，图需要交代怎样的输入、输出或内部表示？
- 哪个困难、约束或缺口最直接地引出当前方法？
- 理解哪些关键操作和关系，才能明白方法为什么这样设计？
- 哪些内容必须在图中看见，哪些由图题或正文解释更合适？

按图的职责选择这些问题。框架总览应建立整体认识；局部机制图可以聚焦一个操作或关系。不要将“完整”理解为把每个组件、接口、训练设置和实验结论都放入同一张图。

将内容分为三个层次：

| 层次 | 处理方式 |
| --- | --- |
| 主体 | 用图形与关系展开中心机制及其对应的困难；读者首先看到它 |
| 必要细节 | 用局部结构、短标签、条件标记或小型图例消除理解歧义 |
| 论文解释 | 完整推导、理由展开、实现配置与实验讨论留在正文或图题 |

重要条件不能仅因占空间而删除。若它改变机制含义，应在图中用条件、边界或明确标签保留。

## 2. 将机制转成可画的对象与关系

先写可视化方案，再写完整提示词。对每个关键区域明确：**科学含义 → 可见对象 → 可见变化或关系 → 最少必要标签 → 读者能看出的信息**。方案可以是几条说明，不必为简单图额外保存文档。

根据真实机制选择画法，以下是可选的映射方式，不是必须出现的模块：

| 需要解释的内容 | 可视化方式 | 应能看出的信息 |
| --- | --- | --- |
| 结构或状态的变化 | 同一对象的前后状态，突出实际改变的部分 | 哪些内容变化，哪些保持不变 |
| 选择、过滤或组合 | 候选集合与被保留、移除或组合的对象，保留对应关系 | 操作作用于什么，结果如何形成 |
| 共享、依赖或耦合 | 共用结构、明确连接、边界或对齐的分支 | 哪些部分相互制约或共享依据 |
| 时序、迭代或反馈 | 可追踪的步骤、循环与更新对象 | 执行顺序，以及反馈具体改变什么 |
| 方法对应的困难 | 发生问题的对象、受限位置及相关条件 | 为什么需要该设计，它解除或处理什么约束 |

避免用通用图标代替机制。一个齿轮、一叠文档或“关键模块”文字框只能帮助命名，不能解释内部发生了什么。关键设计需要呈现与实际实现一致的操作或结构；次要基础设施可以简化。

尽量让同一对象跨阶段保持可辨识的形状、标记或颜色，使读者追踪其变化。示例有助于说明机制时，可使用最小且自洽的示例，集中揭示关键变化，不额外展开无关细节。

## 3. 将 motivation 接到方法上

把动机落在方法真正处理的对象和约束上。优先在相关机制附近展示困难与解法的关系，或者让输入状态、依赖结构和处理前后的差异自然说明需求。只有有助于整体阅读时，才设置独立动机区域。

需要画对比时，明确对比条件和共同对象，突出与该设计有关的差异。不能为了让图更有戏剧性而虚构基线失败、普遍不可行条件或性能优势。没有充分依据时，可以直接画约束与方法，不必画失败路径。

避免用一段“现有方法存在……因此我们提出……”代替动机图解。图应帮助读者形成直观认识，完整论证由论文完成。

## 4. 组织构图与信息密度

根据科学关系选择布局：变换适合可追踪的前后结构，依赖适合共享节点或层级，迭代适合反馈环，对比适合对齐关系。不要先固定面板数量或均分画布，再把内容塞进去。

- **主阅读路线**：让主要对象和操作有自然顺序；局部放大与辅助说明接在对应位置。
- **机制展开**：把空间留给关键区域的内部结构，压缩重复的输入框、标题、基础设施和长距离连线。
- **关系密度**：通过共享结构、对象对应、分支、条件和状态变化增加信息；每种关系都应可追踪、可解释。
- **文字负担**：短标签负责“是什么”，图形负责“怎样变化、怎样关联”；必须保留的解释句只用于图形难以准确传达的条件。
- **标题**：需要标题的整图、面板或模块使用简洁标题即可，避免“标题 + 小字副标题”的组合。删除标题下重复概括、口号和无关紧要的说明；必要技术条件放在对应对象、操作或连线附近。
- **可读性**：在目标尺寸下保留可辨文字与间距，避免靠缩小全部元素容纳更多内容。没有实际信息的空白可以收紧，必要留白保留。

对每个主要区域写清绘制动作。与“加入一个描述关键机制的模块”相比，“在该区域画出实际对象，通过与算法一致的结构变化连接前后状态，并突出决定结果的条件”更能指导生成。最终提示词中应将“实际对象”“结构变化”“条件”替换为已经核对的具体内容。

## 5. 写成可直接调用的提示词

下面是提示词的组织框架。替换字段、删除不适用内容后再提交；段落标题用于组织生成指令，除非列入可见文字，否则不要求画在图上。提示词语言适配工具，图中文字语言服从用户或论文要求。

提示词可以详细描述空间关系与绘制动作，但应把全部可见文字单独列出。不要让模型把方法说明、设计理由和约束段落一起排进成图。

用户请求完整提示词时，交付已经填入当前科学内容、可以直接调用的版本，不只返回模板或修改建议。迭代后将适用的要求合并为一致版本，删去过时布局和相互冲突的指令。

### 完整底图模板

```text
Create a scientific [figure type] for [audience and intended use].
Use diagrams, object transformations, and visible relationships as the primary
explanation. Keep on-image text to the specified labels and necessary annotations.

COMMUNICATION GOAL — instructions, not text to render
Readers should quickly understand [central mechanism or framework capability]
and why [verified difficulty or constraint] motivates it.
The visual focus is [the mechanism or relationship essential to that understanding].
Leave [derivation, extended rationale, or other nonvisual detail] to the paper.

COMPOSITION AND READING ORDER
Use [chosen arrangement and aspect ratio], suitable for [intended display size].
Guide the eye through [the actual main reading route].
Give [important region] enough space to show [its internal mechanism].
Keep [supporting elements] compact and subordinate.

WHAT TO DRAW
For each essential region:
- Position: [location relative to the main structure].
- Objects: [concrete visual objects grounded in the method].
- Operation: [how their arrangement, state, selection, or connections change].
- Relationships: [source, destination, direction, and scientific meaning].
- Invariants or conditions: [what remains shared, fixed, or conditional].
- Visual takeaway: [what readers can infer from the drawing itself].

MOTIVATION IN THE DRAWING
At [the relevant location], depict [the actual constraint or difficulty]
using [specific visible structure, condition, or state difference].
Connect it visually to [the design that addresses it].
[Include a comparison only if supported, using aligned objects and conditions.]

CROSS-REGION CONNECTIONS AND VISUAL ENCODING
- [source] -> [destination]: [meaning, direction, optional label]
- [source] -> [destination]: [meaning, direction, optional label]
Use consistent encodings for [the distinct relationship types in this figure].
Make direction, branching, and shared structure explicit.
Keep recurring objects recognizable across regions.

ON-IMAGE TEXT
Render only these specified titles, short labels, notation, and annotations:
[the actual visible-text list]
Worked-example content, confined to its illustrated context:
[example values or text, if the figure needs an example]
The communication goals and drawing instructions above are not image text.
Where a heading is needed, use a single concise title. Do not add subtitles,
taglines, or small explanatory lines beneath headings. Place essential technical
conditions beside the relevant objects, operations, or connections.

VISUAL DIRECTION
Follow [reference style or chosen visual direction].
Use [project-specific palette, font character, line weights, shapes, and spacing].
Apply the same visual encoding to the same semantic role throughout.
Build information density through meaningful structures and relationships.
Keep labels legible at the intended size, with sufficient visual separation.
Use icons as supporting cues; show the essential mechanism with actual structure.

REFERENCE AND INVARIANTS
Use the attached reference for [specific layout or style aspects].
Preserve [accepted content, protected regions, or visual relationships].
Correct [identified errors or ambiguities] rather than reproducing them.

OUTPUT
Produce a clean raster design draft for subsequent editable reconstruction.
The drawing should establish an intuitive understanding and complement the paper.
Do not add scientific claims, connections, numerical results, or symbols that
are absent from this specification.
```

局部机制图只保留相应的理解目标和内容，不强制加入完整框架、动机对照或反馈环。科学内容明确后再确定风格，不能让美术要求替代“画什么、如何变化、为何相关”。

## 6. 生成前审阅提示词

- **可视表达**：去掉解释性长句、保留短标签后，是否仍可追踪主要对象、操作和结果？图标不能只起装饰作用。
- **机制特征**：关键区域是否画出了区别于普通模块串联的内部结构？读者是否能看出该方法具体做了什么？
- **动机对应**：图的职责包含 motivation 时，困难是否可见，是否能与相关设计对应，而非依赖一段背景文案？
- **信息密度**：主要空间是否用于有意义的对象和关系？是否存在等宽空框、重复解释或长距离无信息箭头？
- **分工**：哪些长句可以留在图题或正文？删去后是否仍保留科学理解必需的条件？
- **标题**：是否在标题下额外添加了无关紧要的小字副标题或重复解释？标题足以命名时删除这些小字，必要技术条件移到对应图形附近。
- **可执行性**：绘制动作、连接关系、可见文字和保留区域是否明确，是否仍有未替换字段或相互冲突的要求？

这些检查用于改进提示词，不生成虚构的分数，也不把“隐藏所有文字后仍完全可懂”设为目标。科学术语、符号和必要标签本来就承担命名作用。

## 7. 从生成结果反推提示词修改

先判断实际图像中的问题属于内容、可视表达、构图还是局部排版，再修改相应指令：

| 生成结果的问题 | 提示词应如何调整 |
| --- | --- |
| 满屏是文字框，机制只剩模块名 | 给关键区域补充具体对象、绘制动作和状态关系；将可见文字限制为必要标签 |
| 画面稀疏，只有几条概括箭头 | 展开影响理解的内部结构与条件，建立对象对应；收紧无信息空间 |
| 密度高但不易理解 | 恢复主阅读路线，共享重复结构，减少次要信息与交叉连线 |
| Motivation 不鲜明 | 将已核实的困难画在它发生的对象与位置，并与解法对齐 |
| 参考风格相似，科学关系却错误 | 修正具体对象、方向、条件与不变量，再讨论美术细节 |

已有可编辑源图时，局部文字、对齐和连线问题优先在源文件完成。只有确实需要调整位图底图时，使用以下迭代模板：

```text
Revise the attached scientific diagram.

Preserve: [accepted regions, scientific content, labels, and style].
Change only: [target region or global issue explicitly requested].
Current issue: [observable problem and its effect on understanding].
Replace or revise: [specific visual structure and drawing instructions].
Readers should be able to see: [the intended relationship or transformation].
On-image text after the revision: [short labels and necessary annotations].
Keep these relationships accurate: [relevant semantic invariants].
Keep all unaffected regions consistent with the reference.
```

把“太空”“太乱”“不像参考图”等反馈转化为可执行修改，而不是在原提示词后不断追加“更漂亮”“更专业”“信息更丰富”。每轮改动明确针对可观察的问题，保留已经成立的科学关系和已接受区域。
