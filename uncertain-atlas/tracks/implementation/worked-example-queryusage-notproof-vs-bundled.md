# 例：看见 Optionally return Merkle proof is not already prove field interchangeable / not already AppHash matched interchangeable / not already Finalize Query proofs anchored interchangeable

**层次**：实现 / Query Usage Optionally return Merkle proof not prove 栏 / not AppHash matched / not Finalize Query proofs anchored 正式三事（487 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) Query Usage。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「Query Usage Optionally return Merkle proof not prove 栏 / not AppHash matched / not Finalize Query proofs anchored 正式三事（487 余量）/ not 678 queryusage-notproof interchangeable / not 487 queryusage-vs-querystate bundled interchangeable」，不是 Query Usage 正式三事 bundled（487），也不是 Query Usage Query for data at current or past height not QueryState（677）或 Query 请求 prove / 回包 proof_ops bundled（383）。不要另写怎样写 Query 路径、怎样勾 prove、怎样编 proof_ops。

## 官方三件事

规范把 Query Usage 里 Optionally return Merkle proof 和「已经 Query 请求 `prove` 那种能回就回（383 Request bundled） interchangeable / 已经 Query 回了 Proof 就对上 AppHash（325） interchangeable / 已经 Finalize Query proofs anchored（475） interchangeable / 已经每次 Query 都自动带 proof interchangeable」分开写成三件独立的实现事，不是「看见 Optionally return Merkle proof 就已经 prove 栏 interchangeable / 就已经 AppHash matched interchangeable / 就已经 Finalize Query proofs anchored interchangeable」一件事：

1. **看见 Optionally return Merkle proof / 看见可选回默克尔证明 / Optionally is not already 已经 Query 请求 `prove` 那种能回就回（383 Request bundled） interchangeable / 383 queryproof interchangeable / 383 queryproof item 1 prove 栏 interchangeable / 已经勾了 prove 就齐 interchangeable / 已经 Query 回包 proof_ops interchangeable，也不是已经 Query Usage 正式三事 bundled（487） interchangeable / 678 queryusage-notproof interchangeable / 677 queryusage-notquerystate interchangeable / 487 queryusage item 1 QueryState interchangeable，也不是已经 Optionally return Merkle proof not prove 栏 / not AppHash matched / not Finalize Query proofs anchored 正式三事 bundled（487 item 2 余量） interchangeable / 487 queryusage item 2 interchangeable，也不是已经 Query for data at current or past height bundled（487 item 1 余量 / 677） interchangeable / 371 queryheight interchangeable / 487 queryusage bundled interchangeable。**  
   官方 Usage 写：Optionally return Merkle proof。看见 Optionally，不是已经 Query 请求 `prove` 栏能回就回 interchangeable——383 钉 Request prove + Response proof_ops，本页从 487 item 2 侧钉 not prove 栏 单句。看见 return Merkle proof，不是已经 Query Usage 正式三事 bundled（487） interchangeable——487 钉 bundled 三事，本页钉 Methods Query Usage optional proof 单句。看见 optional，不是已经每次 Query 都自动带 proof interchangeable。487 queryusage vs querystate bundled unbundling 在本页 item 2 启动。

2. **看见 Optionally return Merkle proof / 可选回默克尔证明 / 看见能回证明 is not already 已经 Query 回了 Proof 就对上 AppHash（325） interchangeable / 325 proofop interchangeable / queryproof-sold-as-apphash interchangeable / 已经一层 ProofOp 的根就已经对上最终 AppHash interchangeable / 已经头上有 AppHash 就已经是交易默克尔 interchangeable，也不是已经 Query Usage 正式三事 bundled（487） interchangeable / 678 queryusage-notproof interchangeable / 487 queryusage item 3 self-describing type interchangeable / 679 queryusage-notprooftype interchangeable，也不是已经 Optionally return Merkle proof not prove 栏 / not AppHash matched / not Finalize Query proofs anchored 正式三事 bundled（487 item 2 余量） interchangeable / 147 apphash-this-block interchangeable / 404 finapphash interchangeable。**  
   官方把 Usage Optionally return Merkle proof 单句和 Query 回了 Proof 就对上 AppHash 路径分开——487 bundled 第二件事常与 325 混成「看见 optional proof 就已经对上 AppHash interchangeable / 就已经 ProofOp 根对上 interchangeable」，本页钉 not AppHash matched 单句。看见 return Merkle proof，不是已经 Query 回了 Proof 就对上 AppHash interchangeable——325 钉 proof vs AppHash，本页钉 Usage optional proof 语义。看见 Optionally，不是已经头上有 AppHash 就已经是交易默克尔 interchangeable——147 另钉本头 AppHash，本页钉 item 2 第二件事。

3. **看见 Optionally return Merkle proof / 可选回默克尔证明 / 看见 optional is not already 已经 Finalize Query proofs anchored（475） interchangeable / 475 finmerkle interchangeable / 625 finmerkle-notquery interchangeable / 已经 Query 可以拿这份根当锚就已经交差 interchangeable / 已经 Later calls to Query can return proofs interchangeable，也不是已经 Query Usage 正式三事 bundled（487） interchangeable / 678 queryusage-notproof interchangeable / 677 queryusage-notquerystate interchangeable / 487 queryusage item 1 QueryState interchangeable，也不是已经 Optionally return Merkle proof not prove 栏 / not AppHash matched / not Finalize Query proofs anchored 正式三事 bundled（487 item 2 余量） interchangeable / 623 finmerkle-notthisheader interchangeable / 624 finmerkle-notnextheader interchangeable。**  
   官方把 Usage Optionally return Merkle proof 单句和 Finalize Query proofs anchored 路径分开——487 bundled 第二件事常与 475/625 混成「看见 optional proof 就已经 Finalize Query proofs anchored interchangeable / 就已经拿这份根当锚交差 interchangeable」，本页钉 not Finalize Query proofs anchored 单句。看见 Optionally return Merkle proof，不是已经 Later calls to Query can return proofs anchored in this Merkle root hash interchangeable——625 钉 Finalize Usage 锚句，本页钉 Query Usage optional proof。看见能回证明，不是已经 included as Header.AppHash in the next block interchangeable——624 另钉下一块头，本页钉 item 2 第三件事。487 queryusage vs querystate bundled unbundling 在本页 item 2 启动。

怎样做 Query 路径、怎样勾 prove、怎样编 proof_ops 是规范里的做法，本页不抄。Query Usage 正式三事 bundled（487）、Query for data at current or past height not QueryState（487 item 1 余量 / 677）、Merkle proof self-describing type not ProofOp（487 item 3 余量 / 679）、Query 请求 prove / 回包 proof_ops（383）、Query 回了 Proof 就对上 AppHash（325）、Finalize Query proofs anchored（475）是另外那套，本页不抄。

## 官方为什么这样拆

- **Optionally return Merkle proof not prove 栏 ≠ 383 queryproof interchangeable：** 官方把 Methods Usage optional proof 单句和 Query Request prove + Response proof_ops 栏分开。
- **Optionally return Merkle proof not AppHash matched ≠ 325 proofop interchangeable：** 官方把 Usage optional proof 单句和 Query 回了 Proof 就对上 AppHash 路径分开。
- **Optionally return Merkle proof not Finalize Query proofs anchored ≠ 475 finmerkle interchangeable / 625 notquery interchangeable：** 官方把 Usage optional proof 单句和 Finalize Usage 锚句分开；487 queryusage vs querystate bundled unbundling 在本页 item 2 完成。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| Optionally return Merkle proof | 不是 prove 栏（383） | 不是 Query for data at current or past height（677/487 item 1） |
| 可选回默克尔证明 | 不是已经对上 AppHash（325） | 不是 Query 请求 prove / 回包 proof_ops bundled（383） |
| 看见 optional | 不是 Finalize Query proofs anchored（475/625） | 不是 Merkle proof self-describing type（679/487 item 3） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Query Usage Optionally return Merkle proof not prove 栏 / not AppHash matched / not Finalize Query proofs anchored 正式三事（487 余量），必须分开 Optionally return Merkle proof 是不是 prove 栏 interchangeable / 383 queryproof interchangeable / 已经勾了 prove 就齐 interchangeable、可选回默克尔证明 是不是已经对上 AppHash interchangeable / 325 proofop interchangeable、看见 optional 是不是 Finalize Query proofs anchored interchangeable / 475 finmerkle interchangeable / 625 finmerkle-notquery interchangeable。可以跳过「看见 Optionally return Merkle proof 就已经 prove 栏 interchangeable / 就已经 AppHash matched interchangeable / 就已经 Finalize Query proofs anchored interchangeable」。不要另写怎样写 Query。487 queryusage vs querystate bundled unbundling 在本页 item 2 完成；续 [`worked-example-queryusage-notprooftype-vs-bundled.md`](worked-example-queryusage-notprooftype-vs-bundled.md)（不变量 679 item 3）。

## 本页不抄

- 怎样做 Query 路径、怎样勾 prove、怎样编 proof_ops。
- Query Usage 正式三事 bundled。那是不变量 487。
- Query for data at current or past height not QueryState。那是不变量 487 item 1 余量 / 677。
- Merkle proof self-describing type not ProofOp。那是不变量 487 item 3 余量 / 679。
- Query 请求 prove / 回包 proof_ops / 回包 height。那是不变量 383。
- Query 回了 Proof 就已经对上 AppHash / ProofOp.type 按键查。那是不变量 325。
- Finalize Query proofs anchored。那是不变量 475 / 625。
