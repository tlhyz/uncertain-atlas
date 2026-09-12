# 反模式：看见先装证据就当成已经装满交易 / 看见两条上限就当成已经同一条 / 看见 MaxBytes 写成 -1 就当成已经没有上限

**层次**：共识 / 失败模式。  
**分类**：事实（对象）+ 推断（事故）。  
**来源**：[Creating a proposal](https://github.com/cometbft/cometbft/blob/main/spec/consensus/creating-proposal.md)。  
**例**：[先装证据 ≠ 已经装满交易](../../tracks/consensus/worked-example-evidence-vs-reap.md)。

## 塌法

1. 看见未处理的证据优先于内存池交易 / 看见先装证据，就当成已经装满交易，或当成已经执行。
2. 看见提案按扣掉证据之后的上限收交易 / 看见内存池按假定没有证据的上限收，就当成已经同一条上限。
3. 看见 MaxBytes 写成 -1 / 看见把未处理交易全给了 Prepare，就当成已经没有上限。
4. 看见应用回了列表，就当成已经过了 Process。
5. 看见证据进了提案，就当成证据窗已经盖住解绑。

## 为什么会出事

官方写：未处理的证据比内存池交易优先。提案收交易要先扣掉头、上次 commit 和证据；进池检查假定没有证据。写成 -1 时引擎把整池交给 Prepare，应用仍不得超过这次的 `MaxTxBytes`。

## 和相邻反模式

- [wal-sold-as-signed](wal-sold-as-signed.md) 是写下 ≠ 已经 fsync，不是本页这种造提案。
- [half-written-state](half-written-state.md) 是应用半写 ≠ 已经对齐高度，不是本页。
