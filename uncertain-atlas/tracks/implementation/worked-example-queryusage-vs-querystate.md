# 例：看见 Query for data at current or past height 不是已经是 QueryState；看见 Optionally return Merkle proof 不是已经对上 AppHash；看见 Merkle proof self-describing type 不是已经是 ProofOp 按键查

**层次**：实现 / Query Usage 正式三事。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) Query Usage。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「Query for data at current or past height 不是已经是 QueryState / Optionally return Merkle proof 不是已经对上 AppHash / Merkle proof self-describing type 不是已经是 ProofOp 按键查」，不是 Query Request height 栏 bundled（371），也不是 Query 请求 prove / 回包 proof_ops bundled（383）。不要另写怎样写 Query 路径、怎样勾 prove、怎样编 proof_ops。

## 官方三件事

规范把 Query Usage 里 Query for data at current or past height、Optionally return Merkle proof、Merkle proof includes self-describing `type` field 写成三件独立的实现事，不是「看见能 Query 就已经是 QueryState、已经对上 AppHash、已经是 ProofOp 按键查」一件事：

1. **看见 Query for data from the application at current or past height / 看见查应用在当前或过去高度的数据 不是已经是 QueryState（371 Request bundled），也不是已经复制到各节点（329），也不是已经 QueryState 就是 ExecuteTxState（314）。**  
   官方 Usage 写：Query for data from the application at current or past height。看见 at current or past height，不是已经是 Query Request `height` 默认 0 回最新已提交（371） bundled 第二句 interchangeable——371 钉 Request 栏，本页钉 Methods Query Usage 查哪一高度。看见 for data from the application，不是已经是 QueryState 那份只读副本 interchangeable。看见能查，不是已经复制到各节点（329） interchangeable。看见 Query，不是已经 QueryState 就是 ExecuteTxState（314） interchangeable。
2. **看见 Optionally return Merkle proof / 看见可选回默克尔证明 不是已经 Query 请求 `prove` 那种能回就回（383 Request bundled），也不是已经 Query 回了 Proof 就对上 AppHash（325），也不是已经 Finalize Query proofs anchored（475） interchangeable。**  
   官方 Usage 写：Optionally return Merkle proof。看见 Optionally，不是已经 Query 请求 `prove` 栏能回就回（383） bundled 第一句 interchangeable——383 钉 Request prove + Response proof_ops，本页钉 Usage 侧 optional proof 语义。看见 return Merkle proof，不是已经 Query 回了 Proof 就对上 AppHash（325） interchangeable。看见能回证明，不是已经 FinalizeBlock Later calls to Query can return proofs anchored in this Merkle root hash（475） bundled 第三句 interchangeable。看见 optional，不是已经每次 Query 都自动带 proof interchangeable。
3. **看见 Merkle proof includes self-describing `type` field to support many types of Merkle trees and encoding formats / 看见证明带自描述 type、好支持多种默克尔树和编码 不是已经是 `ProofOp.type` 那种按键查（325），也不是已经 Query 回了 Proof 就对上 AppHash（325 bundled），也不是已经 CheckTx 守卫余量（405） / Snapshot 高度余量（406） bundled 第三句 interchangeable。**  
   官方 Usage 写：Merkle proof includes self-describing `type` field to support many types of Merkle trees and encoding formats。看见 self-describing `type`，不是已经是 ProofOp.type 那种按键查（325） interchangeable。看见 support many types of Merkle trees and encoding formats，不是已经 Query 回了 Proof 就对上 AppHash（325） bundled interchangeable。看见 Usage 这句，不是已经 CheckTx Usage / Query Usage 守卫余量（405） bundled 第三件事 interchangeable——405 钉 CheckTx 守卫余量语境，本页钉 Query Usage proof type 语义。看见 type 字段，不是已经 Snapshot 高度余量（406） bundled 第三句 interchangeable。

怎样做 Query 路径、怎样勾 prove、怎样编 proof_ops 是规范里的做法，本页不抄。Query Request height 栏（371）、Query 证明回包（383）、ProofOp.type 按键查（325）是另外那套，本页不抄。

## 官方为什么这样拆

- **Query for data at current or past height ≠ 已经是 QueryState：** 官方把 Methods Usage 查哪一高度和 app requirements QueryState / Request height 栏分开。
- **Optionally return Merkle proof ≠ 已经对上 AppHash / prove 请求栏 interchangeable：** 官方把 Usage optional proof 和 Request prove + 验 AppHash 分开。
- **Merkle proof self-describing type ≠ ProofOp 按键查 / CheckTx 守卫余量 bundled interchangeable：** 官方把 Query Usage proof type 和 ProofOp.type / 405 bundled 分开。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| Query for data at current or past height | 不是已经是 QueryState | 不是 Query Request height 栏（371） |
| Optionally return Merkle proof | 不是已经对上 AppHash | 不是 Query 请求 prove / 回包 proof_ops（383） |
| Merkle proof self-describing type | 不是 ProofOp 按键查 | 不是 CheckTx 守卫余量 bundled（405） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看「看见能 Query 就已经是 QueryState、已经对上 AppHash、已经是 ProofOp 按键查」，必须分开 Query for data at current or past height 是不是已经是 QueryState、Optionally return Merkle proof 是不是已经对上 AppHash、Merkle proof self-describing type 是不是 ProofOp 按键查。可以跳过「看见能 Query 就已经是 QueryState」。不要另写怎样写 Query 路径。487 queryusage vs querystate bundled unbundling 完成（677 item 1 / 678 item 2 / 679 item 3）；精读 [`worked-example-queryusage-notquerystate-vs-bundled.md`](worked-example-queryusage-notquerystate-vs-bundled.md)（不变量 677 item 1）。

## 本页不抄

- 怎样做 Query 路径、怎样勾 prove、怎样编 proof_ops。
- Query Request height 栏 / height 默认 0 / Height-1 提交后的状态。那是不变量 371。
- Query 请求 prove / 回包 proof_ops / 回包 height。那是不变量 383。
- Query 回了 Proof 就已经对上 AppHash / ProofOp.type 按键查。那是不变量 325。
- Query 回了就已经复制到各节点。那是不变量 329。
- QueryState 就是 ExecuteTxState。那是不变量 314。
- Finalize Query proofs anchored。那是不变量 475。
- CheckTx 守卫余量 bundled / Snapshot 高度余量 bundled。那是不变量 405 / 406。
