# 反模式：提议者时间被写成 MTP、中位数或墙上现在

> 真值：[PBTS 精读](../../tracks/consensus/worked-example-pbts.md)、[MTP 三把尺](../../tracks/consensus/worked-example-mtp.md)、[PBTS README](https://github.com/cometbft/cometbft/blob/main/spec/consensus/proposer-based-timestamp/README.md)、[不变式 40](../invariants/README.md#40-块时间必须点名算法)。

## 一句话

看见块头有时间，就写成「全网同意的现在」、Bitcoin MTP、或 BFT Time 中位数，不指出 PBTS 是提议者本地钟 + timely 窗。

## 正确写法

| 算法 | 能说的句子 |
|------|------------|
| PBTS | 「提议者本地钟；我按收到 Proposal 的时刻验 timely」 |
| BFT Time | 「上一高度 LastCommit 时间戳的加权中位数，可复算」 |
| MTP | 「最近若干块时间的中位等（Bitcoin）」 |
| 调整钟 | 「实现尺子；绕过上限是实现事故」 |
