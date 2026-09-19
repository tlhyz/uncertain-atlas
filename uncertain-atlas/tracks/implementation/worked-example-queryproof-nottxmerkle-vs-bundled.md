# 例：看见头上有 AppHash / 看见和另外两份并列 / 看见交易在 is not already already tx-merkle interchangeable / already validators-hash interchangeable / already separate-app-state interchangeable

**层次**：实现 / 头上有 AppHash 不是已经是交易默克尔 not already tx-merkle / not already validators-hash / not already separate-app-state 正式三事（325 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Query Proofs。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「头上有 AppHash 不是已经是交易默克尔 not already tx-merkle / not already validators-hash / not already separate-app-state 正式三事（325 余量）/ not 731 queryproof-nottxmerkle interchangeable / not 325 queryproof bundled interchangeable」，不是 Query Proofs bundled（325），也不是 Query 回了 Proof 不是已经对上 AppHash（732 item 2 余量）或一层 ProofOp 的根不是已经对上最终 AppHash（733 item 3 余量）。不要另写怎样编证明或怎样种树。

## 官方三件事

规范把 Requirements 里头上有好几份哈希、各自锚一类证明（`ValidatorsHash` / `DataHash` / 应用自己的 `AppHash`）和「已经是头上有 AppHash 就已经是交易默克尔 interchangeable / 已经是和另外两份并列就已经是验证者集合锚 interchangeable / 已经是交易在就已经有分开的应用状态 interchangeable / 已经是 Query Proofs bundled interchangeable」分开写成三件独立的实现事，不是「看见头上有 AppHash 就已经是 DataHash interchangeable / 就已经是 ValidatorsHash interchangeable / 就已经有分开的应用状态 interchangeable」一件事：

1. **看见头上有 AppHash / 看见 AppHash 字段在 / 看见头上有应用根 is not already 已经是交易默克尔 interchangeable / 已经 tx-merkle interchangeable / 已经是 DataHash interchangeable / 325 queryproof bundled interchangeable / 33 four gates interchangeable / queryproof-sold-as-apphash interchangeable，也不是已经 Query Proofs bundled（325） interchangeable / 731 queryproof-nottxmerkle interchangeable / 325 queryproof item 1 interchangeable，也不是已经头上有 AppHash 不是已经是交易默克尔 not already tx-merkle / not already validators-hash / not already separate-app-state 正式三事 bundled（325 item 1 余量） interchangeable / 325 queryproof item 1 interchangeable，也不是已经 Query 回了 Proof 不是已经对上（732） interchangeable / 733 queryproof-notfinalapphash interchangeable / 147 apphash-this-block interchangeable，也不是已经四门已经结算（33） interchangeable。**  
   官方写：`DataHash` 用来快验块里的交易；`AppHash` **是应用自己的**。看见头上有 AppHash，不是已经是 DataHash / tx-merkle interchangeable——325 钉 bundled 三事，本页从 item 1 侧钉 not already tx-merkle 单句。看见 AppHash 字段在，不是已经 Query Proofs bundled（325） interchangeable——325 钉 bundled，本页钉 item 1 第一件事。看见头上有应用根，不是已经本头 AppHash 已经是本高度交差（147） interchangeable——147 另钉本头交差。325 queryproof vs apphash bundled unbundling 在本页 item 1 启动。

2. **看见和另外两份并列 / 看见和 ValidatorsHash、DataHash 并列 / 看见头上好几份哈希 is not already 已经是验证者集合锚 interchangeable / 已经 validators-hash interchangeable / 已经同一种锚 interchangeable / 325 queryproof bundled interchangeable / 38 apphash interchangeable，也不是已经 Query Proofs bundled（325） interchangeable / 731 queryproof-nottxmerkle interchangeable / 325 queryproof item 2 Proof 回了 interchangeable / 325 queryproof item 3 一层根 interchangeable，也不是已经头上有 AppHash 不是已经是交易默克尔 not already tx-merkle / not already validators-hash / not already separate-app-state 正式三事 bundled（325 item 1 余量） interchangeable / 325 queryproof item 1 interchangeable，也不是已经是 DataHash（本页第一件事） interchangeable。**  
   官方写：`ValidatorsHash` 用来快验验证者集合；头上好几份哈希各自锚一类证明。看见和另外两份并列，不是已经 validators-hash interchangeable——并列不等于已经是验证者集合那一类锚。看见头上好几份哈希，不是已经同一种锚 interchangeable——三种锚分开。看见和 ValidatorsHash、DataHash 并列，不是已经只有 AppHash 可信任（38） interchangeable——38 另钉信任边界。325 queryproof vs apphash bundled unbundling 在本页 item 1 启动。

3. **看见交易在 / 看见块里有交易 / 看见相关状态就在交易里 is not already 已经有分开的应用状态 interchangeable / 已经 separate-app-state interchangeable / 已经从交易确定算出但不在交易里交差 interchangeable / 325 queryproof bundled interchangeable / 314 querystate interchangeable，也不是已经 Query Proofs bundled（325） interchangeable / 731 queryproof-nottxmerkle interchangeable / 325 queryproof item 2 / 325 queryproof item 3，也不是已经头上有 AppHash 不是已经是交易默克尔 not already tx-merkle / not already validators-hash / not already separate-app-state 正式三事 bundled（325 item 1 余量） interchangeable / 325 queryproof item 1 interchangeable，也不是已经是 DataHash（本页第一件事） interchangeable / 已经是 ValidatorsHash（本页第二件事） interchangeable。**  
   官方写：有的应用把相关状态就放在交易里；有的应用另有一份从交易**确定算出来、但不在交易里**的状态，后一种才靠 `AppHash` 给轻客户端更省地验。看见交易在，不是已经 separate-app-state interchangeable——本页钉 not already separate-app-state 单句。看见块里有交易，不是已经是 DataHash（本页第一件事） interchangeable——三件事分开钉。看见相关状态就在交易里，不是已经 QueryState 已经是 ExecuteTxState（314） interchangeable——314 另钉查询状态。325 queryproof vs apphash bundled unbundling 在本页 item 1 完成。

怎样编 `ProofOp`、怎样种多层树、怎样从 `FinalizeBlockResponse.Data` 写出下一头是规范里的取值或做法，本页不抄。Query Proofs bundled（325）、Query 回了 Proof 不是已经对上 AppHash（325 item 2 余量 / 732）、一层 ProofOp 的根不是已经对上最终 AppHash（325 item 3 余量 / 733）、本头 AppHash 已经是本高度交差（147）、只有 AppHash 可信任（38）、QueryState 已经是 ExecuteTxState（314）是另外那套，本页不抄。

## 官方为什么这样拆

- **头上有 AppHash not already tx-merkle ≠ 325 / 33 interchangeable：** 官方把 AppHash 和 DataHash 交易默克尔分成两种锚。
- **并列 not already validators-hash ≠ 已经是验证者集合锚 interchangeable：** 官方把并列和 ValidatorsHash 那一类锚分开。
- **交易在 not already separate-app-state ≠ 已经有分开的应用状态 interchangeable：** 官方把交易里状态和另算但不在交易里的状态分开；325 queryproof vs apphash bundled unbundling 在本页 item 1 完成。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 头上有 AppHash | 不是 already tx-merkle | 不是本头交差 alone（147） |
| 和另外两份并列 | 不是 already validators-hash | 不是 Only AppHash alone（38） |
| 交易在 | 不是 already separate-app-state | 不是 QueryState alone（314） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看头上有 AppHash 不是已经是交易默克尔 not already tx-merkle / not already validators-hash / not already separate-app-state 正式三事（325 余量），必须分开头上有 AppHash 是不是 already tx-merkle interchangeable / 325 queryproof bundled interchangeable / queryproof-sold-as-apphash interchangeable、并列 是不是 already validators-hash interchangeable、交易在 是不是 already separate-app-state interchangeable。可以跳过「看见头上有 AppHash 就已经是交易默克尔 interchangeable / 就已经是验证者集合锚 interchangeable / 就已经有分开的应用状态 interchangeable」。不要另写怎样编证明。325 queryproof vs apphash bundled unbundling 在本页 item 1 启动；续 [`worked-example-queryproof-notverified-vs-bundled.md`](worked-example-queryproof-notverified-vs-bundled.md)（不变量 732 item 2）。

## 本页不抄

- 怎样编 `ProofOp`、怎样种多层树、怎样从 FinalizeBlockResponse.Data 写出下一头。
- Query Proofs bundled。那是不变量 325。
- Query 回了 Proof 不是已经对上 AppHash。那是不变量 325 item 2 余量 / 732。
- 一层 ProofOp 的根不是已经对上最终 AppHash。那是不变量 325 item 3 余量 / 733。
- 本头 AppHash 已经是本高度交差。那是不变量 147。
- 只有 AppHash 可信任。那是不变量 38。
- QueryState 已经是 ExecuteTxState。那是不变量 314。
