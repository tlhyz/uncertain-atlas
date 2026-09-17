# 模式：点名 ProcessProposal 对付这种行为 not already CheckTx / not already Finalize / not already settled 正式三事（339 余量）

**层次**：实现 / CheckTx 弱过滤器。  
**分类**：建议（产品）。  
**对应例**：[worked-example-checktx-weak-notproc-vs-bundled.md](../../tracks/implementation/worked-example-checktx-weak-notproc-vs-bundled.md)。

ProcessProposal 对付这种行为 not already CheckTx / not already Finalize / not already settled 正式三事（339 余量） 要先数清问的是哪一件，再决定要不要同一次发布。

- **ProcessProposal 对付这种行为 不是已经是 CheckTx：** 看见有 ProcessProposal，不是已经是 CheckTx interchangeable / 931 checktx-weak-notproc interchangeable。
- **看见点名了这道门 不是已经是 Finalize：** 看见点名了这道门，不是已经 Finalize interchangeable。
- **看见会拒提案 不是已经交差：** 看见会拒提案，不是已经在池子里挡完 interchangeable。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 ProcessProposal 对付这种行为 正式三事（339 余量），先数清问的是是不是已经是 CheckTx、是不是已经是 Finalize、还是看见会拒提案是不是已经交差，再决定要不要同一次发布。339 checktx-weak vs process bundled unbundling 在本页 item 3 完成。
