# 模式：点名 ionce-notchg 杠

**层次**：实现 / InitChain Validators-as-update not already set-changed / not already has-key / not already no-set 正式三事（412 余量）。  
**分类**：建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) InitChain Usage。  
**对应**：[`../tracks/implementation/worked-example-ionce-notchg-vs-bundled.md`](../tracks/implementation/worked-example-ionce-notchg-vs-bundled.md)。

- **Validators-as-update 不是已经改了集合：** 看见两边都是 ValidatorUpdate，不是已经改了集合 interchangeable / 1093 ionce-notchg interchangeable。
- **看见从空集合更新 不是已经带了公钥：** 看见技术上是从空集合更新，不是已经带了公钥 interchangeable。
- **看见有更新结构 不是已经没有集合：** 看见有更新结构，不是已经没有集合 interchangeable。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Validators-as-update 正式三事（412 余量），先数清问的是是不是已经改了集合、是不是已经带了公钥、还是看见有更新结构是不是已经没有集合，再决定要不要同一次发布。412 initonce vs crash bundled unbundling 在本页 item 3 完成。
