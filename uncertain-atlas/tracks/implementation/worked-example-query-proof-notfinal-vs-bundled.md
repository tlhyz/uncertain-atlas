# 例：看见一层 ProofOp 的根 is not already final-apphash interchangeable / not already next-value interchangeable / not already settled interchangeable

**层次**：实现 / 一层 ProofOp 的根 not already final-apphash / not already next-value / not already settled 正式三事（325 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Query Proofs。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行。本页是「一层 ProofOp 的根 not already final-apphash / not already next-value / not already settled 正式三事（325 余量）/ not 949 query-proof-notfinal interchangeable / not 325 query-proof-vs-apphash bundled interchangeable」，不是证明 bundled（325），也不是只有 AppHash 可信任（38），也不是本头 AppHash 已经是本高度交差（147）。不要另写怎样编证明或怎样种树。

## 官方三件事

1. **看见一层 ProofOp 的根 / 看见对上了 这份根 is not already 已经对上最终 AppHash interchangeable，也不是已经证明 bundled（325） interchangeable / 949 query-proof-notfinal interchangeable / 947 query-proof-nottx interchangeable / 948 query-proof-notmatch interchangeable / 325 query-proof item 1 头上有 AppHash interchangeable，也不是已经一层 ProofOp 的根 not already final-apphash / not already next-value / not already settled 正式三事 bundled（325 item 3 余量） interchangeable / 325 query-proof item 3 interchangeable。**  
   官方写：验整份证明时，这一条 ProofOp 的根，是下一条要验的值。最后一条的根，才该对上正在验的 AppHash。看见一层对上，不是已经对上最终 AppHash interchangeable——本页从 325 item 3 侧钉 not already final-apphash 单句。325 query-proof vs apphash bundled unbundling 在本页 item 3 完成。

2. **看见一层对上 / 看见中间根对了 / 这份根 is not already 已经交给下一层 interchangeable，也不是已经证明 bundled（325） interchangeable / 949 query-proof-notfinal interchangeable / 325 query-proof item 2 Query 回了 Proof interchangeable / 948 query-proof-notmatch interchangeable，也不是已经只有 AppHash 可信任 interchangeable / 38 apphash-only interchangeable。**  
   官方把多层根接值和最后一条对 AppHash 分开。看见一层对上，不是已经交给下一层 interchangeable。本页钉 not already next-value 单句。

3. **看见能证缺席 / 看见中间根对了 / 这份根 is not already 已经交差 interchangeable，也不是已经证明 bundled（325） interchangeable / 949 query-proof-notfinal interchangeable / 947 query-proof-nottx interchangeable，也不是已经本头 AppHash 已经是本高度交差 interchangeable / 147 apphash-commit interchangeable。**  
   官方把能证缺席和已经比对着块哈希分开。看见能证缺席，不是已经交差 interchangeable。325 query-proof vs apphash bundled unbundling 在本页 item 3 完成。

怎样编 ProofOp、怎样种多层树、怎样从 Finalize 写出下一头是规范里的取值或做法，本页不抄。

## 官方为什么这样拆

- **一层 ProofOp 的根 not already final-apphash ≠ 已经对上最终 AppHash interchangeable：** 官方把多层根接值和最后一条对 AppHash 分开。
- **看见一层对上 not already next-value ≠ 已经交给下一层 interchangeable：** 官方把这一条的根是下一条要验的值分开。
- **看见能证缺席 not already settled ≠ 已经交差 interchangeable：** 官方把能证缺席和已经比对着块哈希分开；325 query-proof vs apphash bundled unbundling 在本页 item 3 完成。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 一层 ProofOp 的根 | 不是已经对上最终 AppHash | 不是只有 AppHash 可信任（38） |
| 看见一层对上 | 不是已经交给下一层 | 不是本头 AppHash 已经是本高度交差（147） |
| 看见能证缺席 | 不是已经交差 | 不是头上有 AppHash 就已经是交易默克尔（947） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看一层 ProofOp 的根 not already final-apphash / not already next-value / not already settled 正式三事（325 余量），必须分开是不是已经对上最终 AppHash、是不是已经交给下一层、是不是已经交差。可以跳过「看见头上有 AppHash 就已经能验应用」。不要另写怎样编证明或怎样种树。325 query-proof vs apphash bundled unbundling 在本页 item 3 完成。

## 本页不抄

- 怎样编 ProofOp、怎样种多层树、怎样从 Finalize 写出下一头。
- 证明 bundled。那是不变量 325。
- 只有 AppHash 可信任。那是不变量 38。
- 本头 AppHash 已经是本高度交差。那是不变量 147。
