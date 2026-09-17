# 模式：点名 CheckTx 可选 not already four gates settled / not already settled / not already deleted from pool 正式三事（373 余量）

**层次**：实现 / CheckTx 可选。  
**分类**：建议（产品）。  
**对应例**：[worked-example-checktxopt-notsettled-vs-bundled.md](../../tracks/implementation/worked-example-checktxopt-notsettled-vs-bundled.md)。

CheckTx 可选 not already four gates settled / not already settled / not already deleted from pool 正式三事（373 余量） 要先数清问的是哪一件，再决定要不要同一次发布。

- **可选 不是已经是四门已经结算：** 看见能回，不是已经 33 interchangeable / 806 checktxopt-notsettled interchangeable。
- **看见可选 不是已经交差：** 看见能回，不是已经交差 interchangeable。
- **看见没参与处理块 不是已经从池里删掉：** 看见可选，不是已经从池里删掉 interchangeable。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 CheckTx 可选 正式三事（373 余量），先数清问的是是不是已经是四门已经结算 / 33、是不是已经交差、还是看见没参与处理块是不是已经从池里删掉，再决定要不要同一次发布。373 checktxopt vs block bundled unbundling 在本页 item 1 启动。
