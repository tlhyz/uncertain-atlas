# 例：看见 Merkle proof self-describing-type is not already ProofOp-type interchangeable / not already apphash-aligned interchangeable / not already settled interchangeable

**层次**：实现 / Merkle proof self-describing-type not already ProofOp-type / not already apphash-aligned / not already settled 正式三事（405 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) CheckTx Usage / Query Usage。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「Merkle proof self-describing-type not already ProofOp-type / not already apphash-aligned / not already settled 正式三事（405 余量）/ not 1105 cguard-notproof interchangeable / not 405 checktxguard-vs-optional bundled interchangeable」，不是 CheckTx 守卫余量 bundled（405），也不是 ProofOp.type 就已经是按键查（325），也不是 Query 锚就已经对上 AppHash（1101）。不要另写怎样写 CheckTx 守卫余量。

## 官方三件事

1. **看见默克尔证明带自描述 type、好支持多种默克尔树和编码 / 看见写了 type 这份栏 is not already 已经是 ProofOp 类型 interchangeable，也不是已经 CheckTx 守卫余量 bundled（405） interchangeable / 1105 cguard-notproof interchangeable / 1103 cguard-notopt interchangeable / 405 checktxguard item 1 guard-not-optional interchangeable，也不是已经 Merkle proof self-describing-type not already ProofOp-type / not already apphash-aligned / not already settled 正式三事 bundled（405 item 3 余量） interchangeable / 405 checktxguard item 3 interchangeable。**  
   官方写：默克尔证明带自描述的 type 字段，好支持多种默克尔树和编码格式。看见写了 type，不是已经是 ProofOp 类型 interchangeable——本页从 405 item 3 侧钉 not already ProofOp-type 单句。405 checktxguard vs optional bundled unbundling 在本页 item 3 完成。

2. **看见能支持多种树 / 看见写了 type / 这份栏 is not already 已经对上 AppHash interchangeable，也不是已经 CheckTx 守卫余量 bundled（405） interchangeable / 1105 cguard-notproof interchangeable / 405 checktxguard item 2 source-not-replay interchangeable / 1104 cguard-notreplay interchangeable，也不是已经 ProofOp.type 就已经是按键查 interchangeable / 325 query-proof interchangeable。**  
   官方把能支持多种树和已经对上 AppHash 分开。看见能支持多种树，不是已经对上 AppHash interchangeable。本页钉 not already apphash-aligned 单句。

3. **看见能回证明 / 看见写了 type / 这份栏 is not already 已经交差 interchangeable，也不是已经 CheckTx 守卫余量 bundled（405） interchangeable / 1105 cguard-notproof interchangeable / 1103 cguard-notopt interchangeable，也不是已经 Query 锚就已经对上 AppHash interchangeable / 1101 fhash-notalign interchangeable。**  
   官方把能回证明和已经交差分开。看见能回证明，不是已经交差 interchangeable。405 checktxguard vs optional bundled unbundling 在本页 item 3 完成。

怎样写 CheckTx 守卫余量、怎样挑邻居、怎样编 type 是规范里的做法，本页不抄。

## 官方为什么这样拆

- **Merkle proof self-describing-type not already ProofOp-type ≠ 已经是 ProofOp 类型 interchangeable：** 官方把自描述 type 和按键查分开。
- **看见能支持多种树 not already apphash-aligned ≠ 已经对上 AppHash interchangeable：** 官方把能支持多种树和已经对上 AppHash 分开。
- **看见能回证明 not already settled ≠ 已经交差 interchangeable：** 官方把能回证明和已经交差分开；405 checktxguard vs optional bundled unbundling 在本页 item 3 完成。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 默克尔证明带自描述 type、好支持多种默克尔树和编码 | 不是已经是 ProofOp 类型 | 不是 ProofOp.type 就已经是按键查（325） |
| 看见能支持多种树 | 不是已经对上 AppHash | 不是 Query 锚就已经对上 AppHash（1101） |
| 看见能回证明 | 不是已经交差 | 不是先跑了就已经是技术上可选（1103） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Merkle proof self-describing-type not already ProofOp-type / not already apphash-aligned / not already settled 正式三事（405 余量），必须分开是不是已经是 ProofOp 类型、是不是已经对上 AppHash、是不是已经交差。可以跳过「看见回了 CheckTx 守卫余量就已经是技术上可选」。不要另写怎样写 CheckTx 守卫余量。405 checktxguard vs optional bundled unbundling 在本页 item 3 完成。

## 本页不抄

- 怎样写 CheckTx 守卫余量、怎样挑邻居、怎样编 type。
- CheckTx 守卫余量 bundled。那是不变量 405。
- ProofOp.type 就已经是按键查。那是不变量 325。
- Query 锚就已经对上 AppHash。那是不变量 1101。
