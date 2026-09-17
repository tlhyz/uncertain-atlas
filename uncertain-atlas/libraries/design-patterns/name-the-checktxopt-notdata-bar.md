# 模式：点名 回包码不再另有含义 not already Data used / not already consensus order / not already forked 正式三事（373 余量）

**层次**：实现 / CheckTx 可选。  
**分类**：建议（产品）。  
**对应例**：[worked-example-checktxopt-notdata-vs-bundled.md](../../tracks/implementation/worked-example-checktxopt-notdata-vs-bundled.md)。

回包码不再另有含义 not already Data used / not already consensus order / not already forked 正式三事（373 余量） 要先数清问的是哪一件，再决定要不要同一次发布。

- **回包码 不是已经被引擎用了 Data：** 看见有码，不是已经 317 interchangeable / 808 checktxopt-notdata interchangeable。
- **看见码在 不是已经是共识顺序：** 看见有码，不是已经是共识顺序 interchangeable。
- **看见拒了 不是已经分叉：** 看见回包码，不是已经分叉 interchangeable。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看回包码不再另有含义 正式三事（373 余量），先数清问的是是不是已经被引擎用了 Data / 317、是不是已经是共识顺序、还是看见拒了是不是已经分叉，再决定要不要同一次发布。373 checktxopt vs block bundled unbundling 在本页 item 3 完成。
