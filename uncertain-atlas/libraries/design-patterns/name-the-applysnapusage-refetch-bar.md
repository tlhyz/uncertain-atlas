# 模式：把 ApplySnapshotChunk Usage refetch/ban 正式二事说成两个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) ApplySnapshotChunk Usage。  
**例**：[can choose refetch/ban ≠ refetch/ban bundled](../../tracks/implementation/worked-example-applysnapusage-refetch-vs-bundled.md)。

## 两个名字

1. **can choose refetch/ban 不是 refetch/ban bundled：** 看见 Methods ApplySnapshotChunk Usage can choose，不是 378 refetch_chunks / reject_senders bundled interchangeable。
2. **will not do unless instructed 不是引擎自动 refetch：** 看见 unless instructed by the application，不是 378 / 485 引擎自动 refetch interchangeable。

## 为什么要分开叫

官方把 can choose refetch/ban、will not do unless instructed、ApplySnapshotChunk 再拉 bundled（378）写成两个名字。把它们叫成一个「看见 Apply 了 chunk 回包 refetch_chunks 就已经 refetch/ban bundled interchangeable、已经引擎自动 refetch interchangeable」，会把 can choose refetch/ban、unless instructed 两条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 ApplySnapshotChunk Usage refetch/ban 正式二事，先数清问的是 can choose refetch/ban 是不是 refetch/ban bundled interchangeable / 已经 RETRY interchangeable、will not do unless instructed 是不是引擎自动 refetch interchangeable / 已经 unable retrieve 换快照 interchangeable，再决定要不要同一次发布。
