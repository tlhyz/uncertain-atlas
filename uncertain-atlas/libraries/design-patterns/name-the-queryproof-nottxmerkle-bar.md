# 模式：把头上有 AppHash 不是已经是交易默克尔 not already tx-merkle / not already validators-hash / not already separate-app-state 正式三事（325 余量）说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Query Proofs。  
**例**：[头上有 AppHash not already tx-merkle ≠ bundled（325）](../../tracks/implementation/worked-example-queryproof-nottxmerkle-vs-bundled.md)。

## 三个名字

1. **头上有 AppHash 不是 already tx-merkle：** 看见头上有 AppHash / AppHash 字段在 / 头上有应用根，不是已经是交易默克尔 interchangeable / 已经是 DataHash interchangeable，不是 325 queryproof bundled interchangeable / 33 four gates interchangeable / queryproof-sold-as-apphash interchangeable。

2. **并列 不是 already validators-hash：** 看见和另外两份并列 / 和 ValidatorsHash、DataHash 并列 / 头上好几份哈希，不是已经是验证者集合锚 interchangeable / 已经同一种锚 interchangeable，不是 38 apphash interchangeable / 325 queryproof item 2 interchangeable。

3. **交易在 不是 already separate-app-state：** 看见交易在 / 块里有交易 / 相关状态就在交易里，不是已经有分开的应用状态 interchangeable / 已经从交易确定算出但不在交易里交差 interchangeable，不是 314 querystate interchangeable / 325 queryproof item 3 interchangeable。

官方把头上有 AppHash 单句、already tx-merkle、already validators-hash、already separate-app-state 写成三个名字。把它们叫成一个「看见头上有 AppHash 就已经是交易默克尔 interchangeable / 就已经是验证者集合锚 interchangeable / 就已经有分开的应用状态 interchangeable」，会把 not already tx-merkle、not already validators-hash、not already separate-app-state 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看头上有 AppHash 不是已经是交易默克尔 not already tx-merkle / not already validators-hash / not already separate-app-state 正式三事（325 余量），先数清问的是头上有 AppHash 是不是 already tx-merkle / 325 / queryproof-sold-as-apphash，是不是并列 是不是 already validators-hash，还是交易在 是不是 already separate-app-state，再决定要不要同一次发布。325 queryproof vs apphash bundled unbundling 在本页 item 1 启动。
