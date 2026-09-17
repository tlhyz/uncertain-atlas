# 模式：把 Query Usage Optionally return Merkle proof not prove 栏 / not AppHash matched / not Finalize Query proofs anchored 正式三事（487 余量）说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) Query Usage。  
**例**：[Optionally return Merkle proof not prove 栏 ≠ bundled（487）](../../tracks/implementation/worked-example-queryusage-notproof-vs-bundled.md)。

## 三个名字

1. **Optionally return Merkle proof 不是 prove 栏：** 看见 Usage optional proof，不是已经 Query 请求 `prove` 那种能回就回 interchangeable，不是 383 queryproof interchangeable / 678 queryusage-notproof interchangeable。

2. **可选回默克尔证明 不是已经对上 AppHash：** 看见 Optionally return Merkle proof，不是已经 Query 回了 Proof 就对上 AppHash interchangeable，不是 325 proofop interchangeable。

3. **看见 optional 不是 Finalize Query proofs anchored：** 看见 Usage optional proof，不是已经 Later calls to Query can return proofs anchored interchangeable，不是 475 finmerkle interchangeable / 625 finmerkle-notquery interchangeable。

官方把 Query Usage optional proof、Request prove 栏、Finalize Usage 锚句写成三个名字。把它们叫成一个「看见 Optionally return Merkle proof 就已经 prove 栏 interchangeable / 就已经 AppHash matched interchangeable / 就已经 Finalize Query proofs anchored interchangeable」，会把 not prove 栏、not AppHash matched、not Finalize Query proofs anchored 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Query Usage Optionally return Merkle proof not prove 栏 / not AppHash matched / not Finalize Query proofs anchored 正式三事（487 余量），先数清问的是 Optionally return Merkle proof 是不是 prove 栏 / 383、是不是已经对上 AppHash / 325，还是看见 optional 是不是 Finalize Query proofs anchored / 475 / 625，再决定要不要同一次发布。487 queryusage vs querystate bundled unbundling 在本页 item 2 完成。
