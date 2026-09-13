# 反模式：看见 Process height/time 对上就当成已经验过块头 / 看见填了 Request height/time 就当成已经 match header / 看见 Process match header 就当成已经是 FinalizeBlockRequest 字段

**层次**：实现 / 失败模式。  
**分类**：事实（对象）+ 推断（事故）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) ProcessProposal Usage / Request。  
**例**：[Process height/time match header ≠ 已经验过块头](../../tracks/implementation/worked-example-procht-vs-header.md)。

## 塌法

1. 看见 Process 的 `height` / `time` 对上拟议块头 / 看见对上了，就当成已经验过块头，或当成已经跑过 Process。
2. 看见 `ProcessProposalRequest.height` 是拟议块的高度 / `ProcessProposalRequest.time` 是拟议块的时间戳 / 看见填了 height / time，就当成已经 Usage 那种 match the values from the header，或当成已经验过票上时间。
3. 看见 Process height / time match proposed block header / 看见 match header，就当成已经是 `FinalizeBlockRequest` 刚决定那块的字段，或当成已经 Finalize height/time match interchangeable。

## 为什么会出事

官方写：The height and time values match the values from the header of the proposed block。Request 表写 height / time 是拟议块的高度和时间戳。Finalize Usage 另写 Finalize 的 height / time match。When 另写收到 Proposal 会先验块头。这不是已经验过块头，不是 Request 栏就已经 match，也不是已经 Finalize 字段 interchangeable。

## 和相邻反模式

- [htmatch-sold-as-header](htmatch-sold-as-header.md) 是头字段对上余量 bundled，不是本页这种 ProcessProposal Usage match 单独切片。
- [procreq-sold-as-extreq](procreq-sold-as-extreq.md) 是 Process 请求栏单栏 bundled，不是本页这种 Request height / time 栏 vs Usage match。
- [proposetimeout-sold-as-process](proposetimeout-sold-as-process.md) 是收到带上头的提案会先验块头就已经跑过 Process，不是本页这种 Process match header 不是已经验过块头。
