# 例：看见Prepare 实现可以非确定不是已经必须确定；看见MAY be non-deterministic不是已经和 Process / Finalize 同一把尺；看见Prepare 实现可以非确定不是已经 Process MUST deterministic

**层次**：实现 / 规范对象。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) PrepareProposal Usage。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「PrepareNochecks nondet not already must-deterministic / not already same-ruler / not already Process-MUST-det 正式三事（504 余量）/ not 1309 nochecks-notdet interchangeable / not 504 prepareusage-nochecks-vs-bundled bundled interchangeable」，不是 prepareusage nochecks vs bundled bundled（504），也不是已经 Prepare 没有确定性要求（338），也不是已经 Process MUST deterministic（430）。不要另写 怎样再验 Prepare 回包、怎样查重复、怎样写 Prepare 确定性。

## 官方三件事

1. **看见Prepare 实现可以非确定 / 看见Prepare 实现可以非确定 这份对象 is not already 已经必须确定 interchangeable，也不是已经 prepareusage nochecks vs bundled bundled（504） interchangeable / 1309 nochecks-notdet interchangeable / 1307 nochecks-notdup interchangeable，也不是已经 PrepareNochecks nondet not already must-deterministic / not already same-ruler / not already Process-MUST-det 正式三事 bundled（504 item 3 余量） interchangeable / 504 nochecks item 3 interchangeable。**  
   官方把Prepare 实现可以非确定和已经必须确定写成两件。看见Prepare 实现可以非确定，不是已经必须确定。

2. **看见MAY be non-deterministic / 看见Prepare 实现可以非确定 / 这份对象 is not already 已经和 Process / Finalize 同一把尺 interchangeable，也不是已经 prepareusage nochecks vs bundled bundled（504） interchangeable / 1309 nochecks-notdet interchangeable / 1308 nochecks-notcrash interchangeable，也不是已经 Prepare 没有确定性要求 interchangeable / 338 Prepare 没有确定性要求 interchangeable。**  
   官方把MAY be non-deterministic和已经和 Process / Finalize 同一把尺写成两件。看见MAY be non-deterministic，不是已经和 Process / Finalize 同一把尺。

3. **看见Prepare 实现可以非确定 / 看见MAY be non-deterministic / 这份对象 is not already 已经 Process MUST deterministic interchangeable，也不是已经 prepareusage nochecks vs bundled bundled（504） interchangeable / 1309 nochecks-notdet interchangeable / 1307 nochecks-notdup interchangeable，也不是已经 Process MUST deterministic interchangeable / 430 Process MUST deterministic interchangeable。**  
   官方把Prepare 实现可以非确定和已经 Process MUST deterministic写成两件。看见Prepare 实现可以非确定，不是已经 Process MUST deterministic。

栈怎么写、分隔符、例串是规范里的取值，本页不抄。不要另写 怎样再验 Prepare 回包、怎样查重复、怎样写 Prepare 确定性。

## 官方为什么这样拆

- **MAY be non-deterministic 不是必须确定 interchangeable：官方把 Prepare Usage MAY nondet 单句和 Process MUST deterministic 分开。**
- **看见可以非确定 不是已经和 Process / Finalize 同一把尺：本页钉 Usage MAY，不是已经同一把尺。**
- **看见 MAY nondet 不是已经 Process MUST deterministic：那是不变量 430。**

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 已经必须确定 | 不是已经必须确定 | 不是已经Prepare 没有确定性要求（338） |
| 已经和 Process / Finalize 同一把尺 | 不是已经和 Process / Finalize 同一把尺 | 不是已经Process MUST deterministic（430） |
| 已经 Process MUST deterministic | 不是已经 Process MUST deterministic | 不是已经1307 nochecks-notdup |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 PrepareNochecks nondet not already must-deterministic / not already same-ruler / not already Process-MUST-det 正式三事（504 余量），必须分开是不是已经必须确定、是不是已经和 Process / Finalize 同一把尺、是不是已经 Process MUST deterministic。可以跳过「看见回了 Prepare 回包就已经验过重复、已经是 Process REJECT、已经必须确定 interchangeable」。不要另写 怎样再验 Prepare 回包、怎样查重复、怎样写 Prepare 确定性。504 PrepareProposal Usage nochecks bundled unbundling 在本页 item 3 完成；本页收束本批。

## 本页不抄

- 怎样做再验 Prepare 回包、怎样查重复、怎样写 Prepare 确定性。
- 怎样再验 Prepare 回包、怎样查重复、怎样写 Prepare 确定性。
