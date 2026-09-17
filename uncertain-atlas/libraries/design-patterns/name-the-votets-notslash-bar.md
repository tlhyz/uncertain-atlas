# 模式：点名 votets-notslash 杠

**层次**：共识 / 断开 not already slashed / not already on-chain / not already doublesign 正式三事（304 余量）。  
**分类**：建议（产品）。  
**来源**：CometBFT 官方 [Validator Signing](https://github.com/cometbft/cometbft/blob/main/spec/consensus/signing.md) validator signing / vote timestamp。  
**对应**：[`../tracks/consensus/worked-example-votets-notslash-vs-bundled.md`](../tracks/consensus/worked-example-votets-notslash-vs-bundled.md)。

- **断开 不是已经罚了签的人：** 看见被断开，不是已经罚了 interchangeable / 1000 votets-notslash interchangeable。
- **看见非法 不是已经上链：** 看见非法，不是已经上链 interchangeable。
- **看见没过基本校验 不是已经是双签：** 看见没过基本校验，不是已经是双签 interchangeable。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看断开 正式三事（304 余量），先数清问的是是不是已经罚了、是不是已经上链、还是看见没过基本校验是不是已经是双签，再决定要不要同一次发布。304 vote-ts vs checked bundled unbundling 在本页 item 3 完成。
