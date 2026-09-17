# 例：看见 Merkle proof self-describing type is not already ProofOp key lookup interchangeable / not already CheckTx guard remainder interchangeable / not already Snapshot height remainder interchangeable

**层次**：实现 / Query Usage Merkle proof self-describing type not ProofOp 按键查 / not CheckTx 守卫余量 / not Snapshot 高度余量 正式三事（487 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) Query Usage。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「Query Usage Merkle proof self-describing type not ProofOp 按键查 / not CheckTx 守卫余量 / not Snapshot 高度余量 正式三事（487 余量）/ not 679 queryusage-notprooftype interchangeable / not 487 queryusage-vs-querystate bundled interchangeable」，不是 Query Usage 正式三事 bundled（487），也不是 Query Usage Query for data at current or past height not QueryState（677）或 Optionally return Merkle proof not prove 栏（678）。不要另写怎样写 Query 路径、怎样勾 prove、怎样编 proof_ops。

## 官方三件事

规范把 Query Usage 里 Merkle proof includes self-describing `type` field to support many types of Merkle trees and encoding formats 和「已经是 `ProofOp.type` 那种按键查（325） interchangeable / 已经 CheckTx 守卫余量（405） bundled 第三句 interchangeable / 已经 Snapshot 高度余量（406） bundled 第三句 interchangeable / 已经 Query 回了 Proof 就对上 AppHash interchangeable」分开写成三件独立的实现事，不是「看见 Merkle proof self-describing type 就已经 ProofOp 按键查 interchangeable / 就已经 CheckTx 守卫余量 interchangeable / 就已经 Snapshot 高度余量 interchangeable」一件事：

1. **看见 Merkle proof includes self-describing `type` field to support many types of Merkle trees and encoding formats / 看见证明带自描述 type、好支持多种默克尔树和编码 / self-describing `type` is not already 已经是 `ProofOp.type` 那种按键查（325） interchangeable / 325 proofop interchangeable / 已经 Query 回了 Proof 就对上 AppHash interchangeable / 已经 ProofOp.key 就已经是 Query 回包键 interchangeable / 已经 ProofOp.data 就已经是 proof_ops interchangeable，也不是已经 Query Usage 正式三事 bundled（487） interchangeable / 679 queryusage-notprooftype interchangeable / 677 queryusage-notquerystate interchangeable / 487 queryusage item 1 QueryState interchangeable，也不是已经 Merkle proof self-describing type not ProofOp 按键查 / not CheckTx 守卫余量 / not Snapshot 高度余量 正式三事 bundled（487 item 3 余量） interchangeable / 487 queryusage item 3 interchangeable，也不是已经 Optionally return Merkle proof bundled（487 item 2 余量 / 678） interchangeable / 383 queryproof interchangeable / 487 queryusage bundled interchangeable。**  
   官方 Usage 写：Merkle proof includes self-describing `type` field to support many types of Merkle trees and encoding formats。看见 self-describing `type`，不是已经是 ProofOp.type 那种按键查 interchangeable——325 钉 ProofOp.type / AppHash，本页从 487 item 3 侧钉 not ProofOp 按键查 单句。看见 support many types of Merkle trees and encoding formats，不是已经 Query Usage 正式三事 bundled（487） interchangeable——487 钉 bundled 三事，本页钉 Methods Query Usage proof type 单句。看见 type 字段，不是已经 Query 回了 Proof 就对上 AppHash interchangeable。487 queryusage vs querystate bundled unbundling 在本页 item 3 完成。

2. **看见 Merkle proof includes self-describing `type` field / 证明带自描述 type / 看见 Usage 这句 is not already 已经 CheckTx 守卫余量（405） bundled 第三句 interchangeable / 405 checktxguard interchangeable / checktxguard-sold-as-optional interchangeable / 已经 CheckTx 是内存池守卫 bundled 就代表 proof type 已经交差 interchangeable / 已经 Guardian 第三句 interchangeable，也不是已经 Query Usage 正式三事 bundled（487） interchangeable / 679 queryusage-notprooftype interchangeable / 487 queryusage item 2 Optionally Merkle proof interchangeable / 678 queryusage-notproof interchangeable，也不是已经 Merkle proof self-describing type not ProofOp 按键查 / not CheckTx 守卫余量 / not Snapshot 高度余量 正式三事 bundled（487 item 3 余量） interchangeable / 490 chktxguardusage interchangeable / 373 checktx optional interchangeable。**  
   官方把 Usage proof type 单句和 CheckTx 守卫余量 bundled 第三句分开——487 bundled 第三件事常与 405 混成「看见 self-describing type 就已经 CheckTx 守卫余量 bundled 第三句 interchangeable / 就已经 Guardian 交差 interchangeable」，本页钉 not CheckTx 守卫余量 单句。看见 support many types of Merkle trees，不是已经 CheckTx 守卫余量 bundled 第三句 interchangeable——405 钉 CheckTx 守卫余量语境，本页钉 Query Usage proof type 语义。看见 type 字段，不是已经 Guardian of the mempool interchangeable——490 另钉 Guardian，本页钉 item 3 第二件事。

3. **看见 Merkle proof includes self-describing `type` field / 证明带自描述 type / 看见 type 字段 is not already 已经 Snapshot 高度余量（406） bundled 第三句 interchangeable / 406 snapheight interchangeable / 已经 Snapshot.height 是拍快照的高度就已经是 Query 高度 interchangeable / 已经 Snapshot.metadata 就已经全字段对上 interchangeable / 已经 Query 可以可选回默克尔证明就已经对上 AppHash interchangeable，也不是已经 Query Usage 正式三事 bundled（487） interchangeable / 679 queryusage-notprooftype interchangeable / 677 queryusage-notquerystate interchangeable / 487 queryusage item 1 QueryState interchangeable，也不是已经 Merkle proof self-describing type not ProofOp 按键查 / not CheckTx 守卫余量 / not Snapshot 高度余量 正式三事 bundled（487 item 3 余量） interchangeable / 368 snapshot-sold-as-identical interchangeable / 324 snapshot-take interchangeable。**  
   官方把 Usage proof type 单句和 Snapshot 高度余量 bundled 第三句分开——487 bundled 第三件事常与 406 混成「看见 self-describing type 就已经 Snapshot 高度余量 bundled 第三句 interchangeable / 就已经 Query 可选回证明就已经对上 AppHash interchangeable」，本页钉 not Snapshot 高度余量 单句。看见 self-describing type，不是已经 Snapshot.height 是拍快照的高度就已经是 Query 高度 interchangeable——406 钉 Snapshot 高度余量，本页钉 Query Usage proof type。看见 type 字段，不是已经 Snapshot 全字段对上 interchangeable——368 另钉 Snapshot 类型，本页钉 item 3 第三件事。487 queryusage vs querystate bundled unbundling 在本页 item 3 完成。

怎样做 Query 路径、怎样勾 prove、怎样编 proof_ops 是规范里的做法，本页不抄。Query Usage 正式三事 bundled（487）、Query for data at current or past height not QueryState（487 item 1 余量 / 677）、Optionally return Merkle proof not prove 栏（487 item 2 余量 / 678）、ProofOp.type 按键查（325）、CheckTx 守卫余量 bundled（405）、Snapshot 高度余量 bundled（406）是另外那套，本页不抄。

## 官方为什么这样拆

- **Merkle proof self-describing type not ProofOp 按键查 ≠ 325 proofop interchangeable：** 官方把 Methods Query Usage proof type 单句和 ProofOp.type / 验 AppHash 路径分开。
- **Merkle proof self-describing type not CheckTx 守卫余量 ≠ 405 checktxguard interchangeable：** 官方把 Usage proof type 单句和 CheckTx 守卫余量 bundled 第三句分开。
- **Merkle proof self-describing type not Snapshot 高度余量 ≠ 406 snapheight interchangeable：** 官方把 Usage proof type 单句和 Snapshot 高度余量 bundled 第三句分开；487 queryusage vs querystate bundled unbundling 在本页 item 3 完成。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| Merkle proof self-describing type | 不是 ProofOp 按键查（325） | 不是 Query for data at current or past height（677/487 item 1） |
| 证明带自描述 type | 不是 CheckTx 守卫余量 bundled（405） | 不是 Optionally return Merkle proof（678/487 item 2） |
| 看见 type 字段 | 不是 Snapshot 高度余量 bundled（406） | 不是 Finalize Query proofs anchored（475/625） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Query Usage Merkle proof self-describing type not ProofOp 按键查 / not CheckTx 守卫余量 / not Snapshot 高度余量 正式三事（487 余量），必须分开 Merkle proof self-describing type 是不是 ProofOp 按键查 interchangeable / 325 proofop interchangeable / 已经 Query 回了 Proof 就对上 AppHash interchangeable、证明带自描述 type 是不是 CheckTx 守卫余量 bundled interchangeable / 405 checktxguard interchangeable、看见 type 字段 是不是 Snapshot 高度余量 bundled interchangeable / 406 snapheight interchangeable。可以跳过「看见 Merkle proof self-describing type 就已经 ProofOp 按键查 interchangeable / 就已经 CheckTx 守卫余量 interchangeable / 就已经 Snapshot 高度余量 interchangeable」。不要另写怎样写 Query。487 queryusage vs querystate bundled unbundling 在本页 item 3 完成。

## 本页不抄

- 怎样做 Query 路径、怎样勾 prove、怎样编 proof_ops。
- Query Usage 正式三事 bundled。那是不变量 487。
- Query for data at current or past height not QueryState。那是不变量 487 item 1 余量 / 677。
- Optionally return Merkle proof not prove 栏。那是不变量 487 item 2 余量 / 678。
- Query 回了 Proof 就已经对上 AppHash / ProofOp.type 按键查。那是不变量 325。
- CheckTx 守卫余量 bundled。那是不变量 405。
- Snapshot 高度余量 bundled。那是不变量 406。
