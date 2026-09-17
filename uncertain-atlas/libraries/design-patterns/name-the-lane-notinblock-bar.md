# 模式：点名 优先级 0 留给不设道 not already in-block / not already deleted from pool / not already consensus order 正式三事（367 余量）

**层次**：实现 / Info 车道。  
**分类**：建议（产品）。  
**对应例**：[worked-example-lane-notinblock-vs-bundled.md](../../tracks/implementation/worked-example-lane-notinblock-vs-bundled.md)。

优先级 0 留给不设道 not already in-block / not already deleted from pool / not already consensus order 正式三事（367 余量） 要先数清问的是哪一件，再决定要不要同一次发布。

- **写了 0 不是已经进了块：** 看见写了 0，不是已经进了块 interchangeable / 826 lane-notinblock interchangeable。
- **看见空 lane_id 不是已经从池里删掉：** 看见写了 0，不是已经 301 interchangeable。
- **看见有优先级 不是已经是共识顺序：** 看见写了 0，不是已经 317 interchangeable。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看优先级 0 留给不设道 正式三事（367 余量），先数清问的是是不是已经进了块、是不是已经从池里删掉 / 301、还是看见有优先级是不是已经是共识顺序 / 317，再决定要不要同一次发布。367 lane vs priority bundled unbundling 在本页 item 3 完成。
