# 模式：点名 整池可见 not already only subset that fits / not already no limit / not already settled 正式三事（345 余量）

**层次**：实现 / PrepareProposal 回包上限。  
**分类**：建议（产品）。  
**对应例**：[worked-example-prepare-return-notsubset-vs-bundled.md](../../tracks/implementation/worked-example-prepare-return-notsubset-vs-bundled.md)。

整池可见 not already only subset that fits / not already no limit / not already settled 正式三事（345 余量） 要先数清问的是哪一件，再决定要不要同一次发布。

- **整池可见 不是已经只能看见装得进一块的子集：** 看见整池都来了，不是已经只能看见装得进一块的子集 interchangeable / 878 prepare-return-notsubset interchangeable。
- **看见能看见全部 不是已经没有上限：** 看见能看见全部，不是已经没有上限 interchangeable。
- **看见 MaxBytes 写成 -1 不是已经交差：** 看见 MaxBytes 写成 -1，不是已经交差 interchangeable。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看整池可见 正式三事（345 余量），先数清问的是是不是已经只能看见装得进一块的子集、是不是已经没有上限、还是看见 MaxBytes 写成 -1 是不是已经交差，再决定要不要同一次发布。345 prepare-return vs pool bundled unbundling 在本页 item 1 启动。
