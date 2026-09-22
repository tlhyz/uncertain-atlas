# 例：看见 MaxBytes 减去头 / 集合 / 证据才是交易上限 / 看见完整块上限 / 看见扣了开销 is not already already full-tx interchangeable / already evidence-max interchangeable / already overhead-known interchangeable

**层次**：实现 / MaxBytes 减去头集合证据才是交易上限不是已经整块都能装交易 not already full-tx / not already evidence-max / not already overhead-known 正式三事（344 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) List of Parameters / BlockParams.MaxBytes。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「MaxBytes 减去头集合证据才是交易上限不是已经整块都能装交易 not already full-tx / not already evidence-max / not already overhead-known 正式三事（344 余量）/ not 785 maxbytes-notfulltx interchangeable / not 344 maxbytesoverhead bundled interchangeable」，不是 MaxBytes 开销与投递 bundled（344），也不是诚实验证者 MAY 出满不是已经只会出默认 21 MB（786 item 2 余量）或 timeout 必须按满块投递不是已经填了 TimeoutPropose 就装得下（787 item 3 余量）。不要另写怎样算头和证据开销。

## 官方三件事

规范把 Requirements 里完整块上限蕴涵交易上限还要扣掉头 / 集合 / 证据 和「已经是填了 MaxBytes 就已经整块都能装交易 interchangeable / 已经是能装交易就已经是证据 MaxBytes interchangeable / 已经是扣了开销就已经算出那几个字节 interchangeable / 已经是 maxbytesoverhead bundled interchangeable」分开写成三件独立的实现事，不是「看见填了 MaxBytes 就已经整块都能装交易 interchangeable / 就已经是证据 MaxBytes interchangeable / 就已经算出开销字节 interchangeable」一件事：

1. **看见 MaxBytes 减去头 / 集合 / 证据才是交易上限 / 看见完整块上限 / 看见填了块上限 is not already 已经整块都能装交易 interchangeable / 已经 full-tx interchangeable / 已经整块装交易交差 interchangeable / 344 maxbytesoverhead bundled interchangeable / 331 evidencemaxbytes interchangeable / maxbytesoverhead-sold-as-full interchangeable，也不是已经 MaxBytes 开销与投递 bundled（344） interchangeable / 785 maxbytes-notfulltx interchangeable / 344 maxbytesoverhead item 1 interchangeable，也不是已经 MaxBytes 减去头集合证据才是交易上限不是已经整块都能装交易 not already full-tx / not already evidence-max / not already overhead-known 正式三事 bundled（344 item 1 余量） interchangeable / 344 maxbytesoverhead item 1 interchangeable，也不是已经诚实验证者 MAY 出满（786） interchangeable / 787 maxbytes-nottimeoutfit interchangeable / 337 maxbytescap interchangeable，也不是已经证据 MaxBytes 已经是块 MaxBytes（331） interchangeable。**  
   官方写：这是一份完整 Protobuf 编码块的最大体积，由共识算法强制。**这蕴涵**单笔交易上限等于这份 `MaxBytes`，再减去头、验证人集合和块里证据的预期体积。看见填了块上限，不是交易已经能占满整块。看见完整块上限，不是已经 full-tx interchangeable——344 钉 bundled 三事，本页从 item 1 侧钉 not already full-tx 单句。看见填了块上限，不是已经 MaxBytes 开销与投递 bundled（344） interchangeable——344 钉 bundled，本页钉 item 1 第一件事。看见填了块上限，不是已经证据 MaxBytes 已经是块 MaxBytes（331） interchangeable——331 另钉。344 maxbytesoverhead vs full bundled unbundling 在本页 item 1 启动。

2. **看见能装交易 / 看见交易上限还在 / 看见扣开销之后的上限 is not already 已经是证据 MaxBytes interchangeable / 已经 evidence-max interchangeable / 已经证据那把尺交差 interchangeable / 344 maxbytesoverhead bundled interchangeable / evidencemaxbytes-sold-as-blockmax interchangeable / 331 evidencemaxbytes interchangeable，也不是已经 MaxBytes 开销与投递 bundled（344） interchangeable / 785 maxbytes-notfulltx interchangeable / 344 maxbytesoverhead item 2 MAY 出满 interchangeable / 344 maxbytesoverhead item 3 timeout interchangeable，也不是已经 MaxBytes 减去头集合证据才是交易上限不是已经整块都能装交易 not already full-tx / not already evidence-max / not already overhead-known 正式三事 bundled（344 item 1 余量） interchangeable / 344 maxbytesoverhead item 1 interchangeable，也不是已经整块都能装交易（本页第一件事） interchangeable。**  
   官方写：看见能装交易，不是已经是证据那把尺。看见交易上限还在，不是已经 evidence-max interchangeable——本页钉 not already evidence-max 单句。看见扣开销之后的上限，不是已经整块都能装交易（本页第一件事） interchangeable——三件事分开钉。344 maxbytesoverhead vs full bundled unbundling 在本页 item 1 启动。

3. **看见扣了开销 / 看见减去头集合证据 / 看见预期体积要扣 is not already 已经算出那几个字节 interchangeable / 已经 overhead-known interchangeable / 已经开销字节交差 interchangeable / 344 maxbytesoverhead bundled interchangeable / 299 evidence-tx interchangeable，也不是已经 MaxBytes 开销与投递 bundled（344） interchangeable / 785 maxbytes-notfulltx interchangeable / 344 maxbytesoverhead item 2 / 344 maxbytesoverhead item 3，也不是已经 MaxBytes 减去头集合证据才是交易上限不是已经整块都能装交易 not already full-tx / not already evidence-max / not already overhead-known 正式三事 bundled（344 item 1 余量） interchangeable / 344 maxbytesoverhead item 1 interchangeable，也不是已经整块都能装交易（本页第一件事） interchangeable / 已经是证据 MaxBytes（本页第二件事） interchangeable。**  
   官方写：看见扣了开销，不是已经算出那几个字节。看见减去头集合证据，不是已经 overhead-known interchangeable——本页钉 not already overhead-known 单句。看见预期体积要扣，不是已经是证据 MaxBytes（本页第二件事） interchangeable——三件事分开钉。344 maxbytesoverhead vs full bundled unbundling 在本页 item 1 启动。

怎样算头 / 集合 / 证据开销、默认秒数、怎样设 `MaxBytes` 是规范里的做法，本页不抄。MaxBytes 开销与投递 bundled（344）、诚实验证者 MAY 出满不是已经只会出默认 21 MB（344 item 2 余量 / 786）、timeout 必须按满块投递不是已经填了 TimeoutPropose 就装得下（344 item 3 余量 / 787）、-1 就按 100 MB 验不是已经没有上限（337）、证据 MaxBytes 已经是块 MaxBytes（331）、立刻整块执行已经离开关键路径（327）是另外那套，本页不抄。

## 官方为什么这样拆

- **完整块上限 not already full-tx ≠ 344 / 331 interchangeable：** 官方把完整块上限和交易已经能占满整块分开。
- **能装交易 not already evidence-max ≠ 已经是证据 MaxBytes interchangeable：** 官方把交易上限和证据那把尺分开。
- **扣了开销 not already overhead-known ≠ 已经算出那几个字节 interchangeable：** 官方把要扣开销和已经算出开销字节分开；344 maxbytesoverhead vs full bundled unbundling 在本页 item 1 启动。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 完整块上限 | 不是 already full-tx | 不是证据 MaxBytes 已经是块 MaxBytes alone（331） |
| 能装交易 | 不是 already evidence-max | 不是 MAY 出满就已经默认 21 MB alone（786） |
| 扣了开销 | 不是 already overhead-known | 不是 timeout 按满块投递 alone（787） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 MaxBytes 减去头集合证据才是交易上限不是已经整块都能装交易 not already full-tx / not already evidence-max / not already overhead-known 正式三事（344 余量），必须分开完整块上限 是不是 already full-tx interchangeable / 344 maxbytesoverhead bundled interchangeable / maxbytesoverhead-sold-as-full interchangeable、能装交易 是不是 already evidence-max interchangeable、扣了开销 是不是 already overhead-known interchangeable。可以跳过「看见填了 MaxBytes 就已经整块都能装交易 interchangeable / 就已经是证据 MaxBytes interchangeable / 就已经算出开销字节 interchangeable」。不要把 21 MB 当不确定常数。不要另写怎样算头和证据开销。344 maxbytesoverhead vs full bundled unbundling 在本页 item 1 启动；续 [`worked-example-maxbytes-notonly21-vs-bundled.md`](worked-example-maxbytes-notonly21-vs-bundled.md)（不变量 786 item 2）已写；完成见 787。

## 本页不抄

- 怎样算头 / 集合 / 证据开销、默认秒数、怎样设 `MaxBytes`。
- MaxBytes 开销与投递 bundled。那是不变量 344。
- 诚实验证者 MAY 出满不是已经只会出默认 21 MB。那是不变量 344 item 2 余量 / 786。
- timeout 必须按满块投递不是已经填了 TimeoutPropose 就装得下。那是不变量 344 item 3 余量 / 787。
- -1 就按 100 MB 验已经没有上限。那是不变量 337。
- 证据 MaxBytes 已经是块 MaxBytes。那是不变量 331。
- 立刻整块执行已经离开关键路径。那是不变量 327。
