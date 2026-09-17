# 模式：点名 写成 0 不是已经启用 PBTS not already Precision is PBTS / not already field-present / not already settled 正式三事（343 余量）

**层次**：实现 / PbtsEnableHeight。  
**分类**：建议（产品）。  
**对应例**：[worked-example-pbts-height-notzero-vs-bundled.md](../../tracks/implementation/worked-example-pbts-height-notzero-vs-bundled.md)。

写成 0 不是已经启用 PBTS not already Precision is PBTS / not already field-present / not already settled 正式三事（343 余量） 要先数清问的是哪一件，再决定要不要同一次发布。

- **写成 0 不是已经启用：** 看见写成 0，不是已经启用 PBTS interchangeable / 884 pbts-height-notzero interchangeable。
- **看见填了 Precision 不是已经填了 Precision 就是 PBTS：** 看见填了 Precision / MessageDelay，不是已经填了 Precision 就是 PBTS interchangeable。
- **看见字段在 不是已经交差：** 看见字段在，不是已经交差 interchangeable。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看写成 0 不是已经启用 PBTS 正式三事（343 余量），先数清问的是是不是已经启用、是不是已经填了 Precision 就是 PBTS、还是看见字段在是不是已经交差，再决定要不要同一次发布。343 pbts vs params bundled unbundling 在本页 item 1 启动。
