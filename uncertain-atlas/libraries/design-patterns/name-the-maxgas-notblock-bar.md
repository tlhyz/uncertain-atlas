# 模式：点名 已提交块 not already gas-checked / not already consensus-enforced / not already settled 正式三事（315 余量）

**层次**：实现 / 气。  
**分类**：建议（产品）。  
**对应例**：[worked-example-maxgas-notblock-vs-bundled.md](../../tracks/implementation/worked-example-maxgas-notblock-vs-bundled.md)。

已提交块 not already gas-checked / not already consensus-enforced / not already settled 正式三事（315 余量） 要先数清问的是哪一件，再决定要不要同一次发布。

- **已提交块 不是已经按气验过：** 看见块已经提交，不是已经按气验过 interchangeable / 916 maxgas-notblock interchangeable。
- **看见池子守了 不是已经由共识层验过：** 看见池子守了，不是共识已经守了 interchangeable。
- **看见有了 Prepare / Process 不是已经交差：** 看见有了 Prepare / Process，不是已经交差 interchangeable。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看已提交块 正式三事（315 余量），先数清问的是是不是已经按气验过、是不是已经由共识层验过、还是看见有了 Prepare / Process 是不是已经交差，再决定要不要同一次发布。315 maxgas vs enforced bundled unbundling 在本页 item 3 完成。
