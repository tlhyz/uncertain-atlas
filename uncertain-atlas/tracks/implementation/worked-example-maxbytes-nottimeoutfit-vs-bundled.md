# 例：看见 timeout 必须按满块投递延迟算 / 看见最坏投递延迟 / 看见投递延迟 is not already already timeoutpropose-fit interchangeable / already prepare-exec interchangeable / already critical-path interchangeable

**层次**：实现 / timeout 必须按满块投递延迟算不是已经填了 TimeoutPropose 就装得下这次 Prepare 执行 not already timeoutpropose-fit / not already prepare-exec / not already critical-path 正式三事（344 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) List of Parameters / BlockParams.MaxBytes。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「timeout 必须按满块投递延迟算不是已经填了 TimeoutPropose 就装得下这次 Prepare 执行 not already timeoutpropose-fit / not already prepare-exec / not already critical-path 正式三事（344 余量）/ not 787 maxbytes-nottimeoutfit interchangeable / not 344 maxbytesoverhead bundled interchangeable」，不是 MaxBytes 开销与投递 bundled（344），也不是 MaxBytes 减去头集合证据才是交易上限不是已经整块都能装交易（785 item 1 余量）或诚实验证者 MAY 出满不是已经只会出默认 21 MB（786 item 2 余量），也不是立刻整块执行不是已经离开关键路径（737 / 327）。不要另写怎样算头和证据开销。

## 官方三件事

规范把 Requirements 里共识超时应当按把一份满 `MaxBytes` 的块投递给所有验证者的最坏延迟来配 和「已经是填了 TimeoutPropose 就已经装得下这次 Prepare 执行 interchangeable / 已经是超时在就已经装得下 Prepare 执行 interchangeable / 已经是投递延迟就已经离开关键路径 interchangeable / 已经是 maxbytesoverhead bundled interchangeable」分开写成三件独立的实现事，不是「看见 timeout 必须按满块投递就已经装得下 Prepare interchangeable / 就已经是 Prepare 执行超时 interchangeable / 就已经离开关键路径 interchangeable」一件事：

1. **看见 timeout 必须按满块投递延迟算 / 看见最坏投递延迟 / 看见填了 TimeoutPropose is not already 已经填了 TimeoutPropose 就装得下这次 Prepare 执行 interchangeable / 已经 timeoutpropose-fit interchangeable / 已经装得下交差 interchangeable / 344 maxbytesoverhead bundled interchangeable / 738 preparetimeout-notfit interchangeable / maxbytesoverhead-sold-as-full interchangeable，也不是已经 MaxBytes 开销与投递 bundled（344） interchangeable / 787 maxbytes-nottimeoutfit interchangeable / 344 maxbytesoverhead item 3 interchangeable，也不是已经 timeout 必须按满块投递延迟算不是已经填了 TimeoutPropose 就装得下这次 Prepare 执行 not already timeoutpropose-fit / not already prepare-exec / not already critical-path 正式三事 bundled（344 item 3 余量） interchangeable / 344 maxbytesoverhead item 3 interchangeable，也不是已经完整块上限不是已经整块装交易（785） interchangeable / 786 maxbytes-notonly21 interchangeable / 327 preparetimeout interchangeable，也不是已经填了 TimeoutPropose 不是已经装得下（738） interchangeable。**  
   官方写：因此节点采用的共识超时参数，应当按把一份 **满 `MaxBytes` 的块投递给所有验证者** 的最坏延迟来配。看见填了 TimeoutPropose，不是已经按满块投递算过。看见 timeout 必须按满块投递延迟算，不是已经 timeoutpropose-fit interchangeable——344 钉 bundled 三事，本页从 item 3 侧钉 not already timeoutpropose-fit 单句。看见最坏投递延迟，不是已经 MaxBytes 开销与投递 bundled（344） interchangeable——344 钉 bundled，本页钉 item 3 第一件事。看见填了 TimeoutPropose，不是已经填了 TimeoutPropose 不是已经装得下（738） interchangeable——738 另钉 327 item 2。344 maxbytesoverhead vs full bundled unbundling 在本页 item 3 完成。

2. **看见超时在 / 看见有共识超时 / 看见 TimeoutPropose 初值在 is not already 已经装得下这次 Prepare 执行 interchangeable / 已经 prepare-exec interchangeable / 已经 Prepare 执行交差 interchangeable / 344 maxbytesoverhead bundled interchangeable / 327 preparetimeout interchangeable / preparetimeout-sold-as-liveness interchangeable，也不是已经 MaxBytes 开销与投递 bundled（344） interchangeable / 787 maxbytes-nottimeoutfit interchangeable / 344 maxbytesoverhead item 1 扣开销 interchangeable / 344 maxbytesoverhead item 2 MAY 出满 interchangeable，也不是已经 timeout 必须按满块投递延迟算不是已经填了 TimeoutPropose 就装得下这次 Prepare 执行 not already timeoutpropose-fit / not already prepare-exec / not already critical-path 正式三事 bundled（344 item 3 余量） interchangeable / 344 maxbytesoverhead item 3 interchangeable，也不是已经填了 TimeoutPropose 就装得下（本页第一件事） interchangeable。**  
   官方写：看见超时在，不是已经装得下这次 Prepare 里立刻整块执行。看见有共识超时，不是已经 prepare-exec interchangeable——本页钉 not already prepare-exec 单句。看见 TimeoutPropose 初值在，不是已经填了 TimeoutPropose 就装得下（本页第一件事） interchangeable——三件事分开钉。344 maxbytesoverhead vs full bundled unbundling 在本页 item 3 完成。

3. **看见投递延迟 / 看见满块投递延迟 / 看见最坏投递 is not already 已经离开关键路径 interchangeable / 已经 critical-path interchangeable / 已经离开关键路径交差 interchangeable / 344 maxbytesoverhead bundled interchangeable / 737 preparetimeout-notcriticalpath interchangeable / 327 preparetimeout interchangeable，也不是已经 MaxBytes 开销与投递 bundled（344） interchangeable / 787 maxbytes-nottimeoutfit interchangeable / 344 maxbytesoverhead item 1 / 344 maxbytesoverhead item 2，也不是已经 timeout 必须按满块投递延迟算不是已经填了 TimeoutPropose 就装得下这次 Prepare 执行 not already timeoutpropose-fit / not already prepare-exec / not already critical-path 正式三事 bundled（344 item 3 余量） interchangeable / 344 maxbytesoverhead item 3 interchangeable，也不是已经填了 TimeoutPropose 就装得下（本页第一件事） interchangeable / 已经装得下 Prepare 执行（本页第二件事） interchangeable。**  
   官方写：看见投递延迟，不是已经离开关键路径。看见满块投递延迟，不是已经 critical-path interchangeable——本页钉 not already critical-path 单句。看见最坏投递，不是已经立刻整块执行不是已经离开关键路径（737） interchangeable——737 另钉 327 item 1。看见投递延迟，不是已经装得下 Prepare 执行（本页第二件事） interchangeable——三件事分开钉。344 maxbytesoverhead vs full bundled unbundling 在本页 item 3 完成。

怎样算头 / 集合 / 证据开销、默认秒数、怎样设 `MaxBytes` 是规范里的做法，本页不抄。MaxBytes 开销与投递 bundled（344）、MaxBytes 减去头集合证据才是交易上限不是已经整块都能装交易（344 item 1 余量 / 785）、诚实验证者 MAY 出满不是已经只会出默认 21 MB（344 item 2 余量 / 786）、立刻整块执行不是已经离开关键路径（327 / 737）、填了 TimeoutPropose 不是已经装得下（738）、又开一轮不是已经丢了活性（739）是另外那套，本页不抄。

## 官方为什么这样拆

- **timeout 必须按满块投递 not already timeoutpropose-fit ≠ 344 / 738 interchangeable：** 官方把满块投递延迟和填了 TimeoutPropose 就已经装得下 Prepare 执行分开。
- **超时在 not already prepare-exec ≠ 已经装得下 Prepare 执行 interchangeable：** 官方把有超时参数和已经装得下这次 Prepare 执行分开。
- **投递延迟 not already critical-path ≠ 已经离开关键路径 interchangeable：** 官方把满块投递延迟和立刻整块执行离开关键路径分开；344 maxbytesoverhead vs full bundled unbundling 在本页 item 3 完成。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| timeout 必须按满块投递 | 不是 already timeoutpropose-fit | 不是填了 TimeoutPropose 不是已经装得下 alone（738） |
| 超时在 | 不是 already prepare-exec | 不是诚实验证者 MAY 出满 alone（786） |
| 投递延迟 | 不是 already critical-path | 不是立刻整块执行已经离开关键路径 alone（737） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 timeout 必须按满块投递延迟算不是已经填了 TimeoutPropose 就装得下这次 Prepare 执行 not already timeoutpropose-fit / not already prepare-exec / not already critical-path 正式三事（344 余量），必须分开 timeout 必须按满块投递 是不是 already timeoutpropose-fit interchangeable / 344 maxbytesoverhead bundled interchangeable / maxbytesoverhead-sold-as-full interchangeable、超时在 是不是 already prepare-exec interchangeable、投递延迟 是不是 already critical-path interchangeable。可以跳过「看见 timeout 必须按满块投递就已经装得下 Prepare interchangeable / 就已经是 Prepare 执行超时 interchangeable / 就已经离开关键路径 interchangeable」。不要把 21 MB 当不确定常数。不要另写怎样算头和证据开销。344 maxbytesoverhead vs full bundled unbundling 在本页 item 3 完成（785 + 786 + 787）。

## 本页不抄

- 怎样算头 / 集合 / 证据开销、默认秒数、怎样设 `MaxBytes`。
- MaxBytes 开销与投递 bundled。那是不变量 344。
- MaxBytes 减去头集合证据才是交易上限不是已经整块都能装交易。那是不变量 344 item 1 余量 / 785。
- 诚实验证者 MAY 出满不是已经只会出默认 21 MB。那是不变量 344 item 2 余量 / 786。
- 立刻整块执行不是已经离开关键路径。那是不变量 327 / 737。
- 填了 TimeoutPropose 不是已经装得下。那是不变量 738。
- 又开一轮不是已经丢了活性。那是不变量 739。
