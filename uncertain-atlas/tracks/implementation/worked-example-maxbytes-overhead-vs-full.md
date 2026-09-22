# 例：看见 MaxBytes 减去头集合证据才是交易上限不是已经整块都能装交易；看见诚实验证者 MAY 出满 MaxBytes 不是已经只会出默认 21 MB；看见 timeout 必须按满块投递延迟算不是已经填了 TimeoutPropose 就装得下这次 Prepare 执行

**层次**：实现 / BlockParams.MaxBytes 开销与投递。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) List of Parameters / BlockParams.MaxBytes。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5。本页是「MaxBytes 减去头集合证据才是交易上限不是已经整块都能装交易 / 诚实验证者 MAY 出满 MaxBytes 不是已经只会出默认 21 MB / timeout 必须按满块投递延迟算不是已经填了 TimeoutPropose 就装得下这次 Prepare 执行」，不是 -1 就按 100 MB 验已经没有上限，也不是证据 MaxBytes 已经是块 MaxBytes。不要另写怎样算头和证据开销。344 maxbytesoverhead vs full bundled unbundling 完成（785+786+787）；精读 [`worked-example-maxbytes-notfulltx-vs-bundled.md`](worked-example-maxbytes-notfulltx-vs-bundled.md)（不变量 785 item 1）、[`worked-example-maxbytes-notonly21-vs-bundled.md`](worked-example-maxbytes-notonly21-vs-bundled.md)（不变量 786 item 2）、[`worked-example-maxbytes-nottimeoutfit-vs-bundled.md`](worked-example-maxbytes-nottimeoutfit-vs-bundled.md)（不变量 787 item 3）。

## 官方三件事

规范把完整块上限写成三件独立的实现事，不是「看见填了 MaxBytes 就已经整块都能装交易、已经只会出默认 21 MB、已经装得下这次 Prepare 执行」一件事：

1. **看见 MaxBytes 减去头 / 集合 / 证据才是交易上限 / 看见完整块上限 不是已经整块都能装交易，也不是已经是证据 MaxBytes。**  
   官方写：这是一份完整 Protobuf 编码块的最大体积，由共识算法强制。**这蕴涵**单笔交易上限等于这份 `MaxBytes`，再减去头、验证人集合和块里证据的预期体积。看见填了块上限，不是交易已经能占满整块。看见能装交易，不是已经是证据那把尺。看见扣了开销，不是已经算出那几个字节。
2. **看见诚实验证者 MAY 出满 MaxBytes / 看见能广播到配置上限 不是已经只会出默认 21 MB，也不是已经没有上限。**  
   官方写：应用应当知道，**诚实验证者可以**造出并广播达到配置 `MaxBytes` 的块。看见默认能接到 21 MB，不是诚实者已经只会出那一档。看见写了 MAY，不是已经打满。看见能打到配置上限，不是已经写成 -1、已经没有上限。
3. **看见 timeout 必须按满块投递延迟算 / 看见最坏投递延迟 不是已经填了 TimeoutPropose 就装得下这次 Prepare 执行，也不是已经是立刻整块执行离开关键路径。**  
   官方写：因此节点采用的共识超时参数，应当按把一份 **满 `MaxBytes` 的块投递给所有验证者** 的最坏延迟来配。看见填了 TimeoutPropose，不是已经按满块投递算过。看见超时在，不是已经装得下这次 Prepare 里立刻整块执行。看见投递延迟，不是已经离开关键路径。

怎样算头 / 集合 / 证据开销、默认秒数、怎样设 `MaxBytes` 是规范里的取值或做法，本页不抄。-1 就按 100 MB 验不是已经没有上限是不变量 337，本页不抄。

## 官方为什么这样拆

- **MaxBytes 减去头集合证据才是交易上限 ≠ 已经整块都能装交易：** 官方把完整块上限和扣掉开销之后的交易上限分开。
- **诚实验证者 MAY 出满 MaxBytes ≠ 已经只会出默认 21 MB：** 官方把配置上限和默认 21 MB 那一档分开。
- **timeout 必须按满块投递延迟算 ≠ 已经填了 TimeoutPropose 就装得下这次 Prepare 执行：** 官方把满块投递延迟和 Prepare 执行超时分开。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| MaxBytes 减去头集合证据才是交易上限 | 不是已经整块都能装交易 | 不是证据 MaxBytes 已经是块 MaxBytes（331） |
| 诚实验证者 MAY 出满 MaxBytes | 不是已经只会出默认 21 MB | 不是 -1 就按 100 MB 验已经没有上限（337） |
| timeout 必须按满块投递延迟算 | 不是已经填了 TimeoutPropose 就装得下这次 Prepare 执行 | 不是立刻整块执行已经离开关键路径（327） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看「看见填了 MaxBytes 就已经整块都能装交易、已经只会出默认 21 MB、已经装得下这次 Prepare 执行」，必须分开 MaxBytes 减去头集合证据才是交易上限是不是已经整块都能装交易、诚实验证者 MAY 出满 MaxBytes 是不是已经只会出默认 21 MB、timeout 必须按满块投递延迟算是不是已经填了 TimeoutPropose 就装得下这次 Prepare 执行。可以跳过「看见填了 MaxBytes 就已经整块都能装交易」。不要另写怎样算头和证据开销。344 maxbytesoverhead vs full bundled unbundling 完成（785+786+787）。

## 本页不抄

- 怎样算头 / 集合 / 证据开销、默认秒数、怎样设 `MaxBytes`。
- -1 就按 100 MB 验已经没有上限。那是不变量 337。
- 证据 MaxBytes 已经是块 MaxBytes。那是不变量 331。
- 立刻整块执行已经离开关键路径。那是不变量 327。
