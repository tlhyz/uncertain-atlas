# 例：看见 MaxBytes 减去头集合证据才是交易上限 is not already whole block holds txs interchangeable / not already evidence MaxBytes interchangeable / not already settled interchangeable

**层次**：实现 / MaxBytes 减去头集合证据才是交易上限 not already whole block holds txs / not already evidence MaxBytes / not already settled 正式三事（344 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) List of Parameters / BlockParams.MaxBytes。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「MaxBytes 减去头集合证据才是交易上限 not already whole block holds txs / not already evidence MaxBytes / not already settled 正式三事（344 余量）/ not 881 maxbytes-overhead-notfull interchangeable / not 344 maxbytes-overhead-vs-full bundled interchangeable」，不是 MaxBytes 开销与投递 bundled（344），也不是证据 MaxBytes 已经是块 MaxBytes（331），也不是 -1 就按 100 MB 验已经没有上限（337）。不要另写怎样算头和证据开销。

## 官方三件事

1. **看见 MaxBytes 减去头 / 集合 / 证据才是交易上限 / 看见完整块上限 这份扣开销 is not already 已经整块都能装交易 interchangeable，也不是已经 MaxBytes 开销与投递 bundled（344） interchangeable / 881 maxbytes-overhead-notfull interchangeable / 882 maxbytes-overhead-not21mb interchangeable / 344 maxbytes item 2 MAY 打满 interchangeable，也不是已经 MaxBytes 减去头集合证据才是交易上限 not already whole block holds txs / not already evidence MaxBytes / not already settled 正式三事 bundled（344 item 1 余量） interchangeable / 344 maxbytes item 1 interchangeable。**  
   官方写：这是一份完整 Protobuf 编码块的最大体积，由共识算法强制。这蕴涵单笔交易上限等于这份 `MaxBytes`，再减去头、验证人集合和块里证据的预期体积。看见填了块上限，不是交易已经能占满整块 interchangeable——本页从 344 item 1 侧钉 not already whole block holds txs 单句。344 maxbytes vs full bundled unbundling 在本页 item 1 启动。

2. **看见能装交易 / 看见扣了开销 / 这份扣开销 is not already 已经是证据 MaxBytes interchangeable，也不是已经 MaxBytes 开销与投递 bundled（344） interchangeable / 881 maxbytes-overhead-notfull interchangeable / 344 maxbytes item 3 timeout interchangeable / 883 maxbytes-overhead-nottimeout interchangeable，也不是已经证据 MaxBytes 已经是块 MaxBytes interchangeable / 331 evidence-max interchangeable。**  
   官方把能装交易和已经是证据那把尺分开——344 bundled 第一件事常与 331 混成「看见填了 MaxBytes 就已经整块都能装或已经是证据尺 interchangeable」，本页钉 not already evidence MaxBytes 单句。

3. **看见扣了开销 / 看见填了块上限 / 这份扣开销 is not already 已经交差 interchangeable，也不是已经 MaxBytes 开销与投递 bundled（344） interchangeable / 881 maxbytes-overhead-notfull interchangeable / 882 maxbytes-overhead-not21mb interchangeable，也不是已经 -1 就按 100 MB 验已经没有上限 interchangeable / 337 minus-one interchangeable。**  
   官方把扣了开销和已经算出那几个字节 / 已经交差分开。看见扣了开销，不是已经算出那几个字节 interchangeable。344 maxbytes vs full bundled unbundling 在本页 item 1 启动。

怎样算头 / 集合 / 证据开销、默认秒数、怎样设 `MaxBytes` 是规范里的取值或做法，本页不抄。

## 官方为什么这样拆

- **MaxBytes 减去头集合证据才是交易上限 not already whole block holds txs ≠ 已经整块都能装交易 interchangeable：** 官方把完整块上限和扣掉开销之后的交易上限分开。
- **看见能装交易 not already evidence MaxBytes ≠ 已经是证据 MaxBytes interchangeable：** 官方把能装交易和已经是证据那把尺分开。
- **看见扣了开销 not already settled ≠ 已经交差 interchangeable：** 官方把扣了开销和已经交差分开；344 maxbytes vs full bundled unbundling 在本页 item 1 启动。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| MaxBytes 减去头集合证据才是交易上限 | 不是已经整块都能装交易 | 不是证据 MaxBytes 已经是块 MaxBytes（331） |
| 看见能装交易 | 不是已经是证据 MaxBytes | 不是 -1 就按 100 MB 验已经没有上限（337） |
| 看见扣了开销 | 不是已经交差 | 不是诚实验证者 MAY 出满 MaxBytes（882） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 MaxBytes 减去头集合证据才是交易上限 not already whole block holds txs / not already evidence MaxBytes / not already settled 正式三事（344 余量），必须分开是不是已经整块都能装交易、是不是已经是证据 MaxBytes、是不是已经交差。可以跳过「看见填了 MaxBytes 就已经整块都能装交易」。不要另写怎样算头和证据开销。344 maxbytes vs full bundled unbundling 在本页 item 1 启动；续 [`worked-example-maxbytes-overhead-not21mb-vs-bundled.md`](worked-example-maxbytes-overhead-not21mb-vs-bundled.md)（不变量 882 item 2）。

## 本页不抄

- 怎样算头 / 集合 / 证据开销、默认秒数、怎样设 `MaxBytes`。
- MaxBytes 开销与投递 bundled。那是不变量 344。
- 诚实验证者 MAY 出满 MaxBytes。那是不变量 344 item 2 余量 / 882。
- 证据 MaxBytes 已经是块 MaxBytes。那是不变量 331。
- -1 就按 100 MB 验已经没有上限。那是不变量 337。
