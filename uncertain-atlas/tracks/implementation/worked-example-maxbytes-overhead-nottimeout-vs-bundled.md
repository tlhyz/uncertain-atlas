# 例：看见 timeout 必须按满块投递延迟算 is not already TimeoutPropose covers Prepare interchangeable / not already left critical path interchangeable / not already settled interchangeable

**层次**：实现 / timeout 必须按满块投递延迟算 not already TimeoutPropose covers Prepare / not already left critical path / not already settled 正式三事（344 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) List of Parameters / BlockParams.MaxBytes。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「timeout 必须按满块投递延迟算 not already TimeoutPropose covers Prepare / not already left critical path / not already settled 正式三事（344 余量）/ not 883 maxbytes-overhead-nottimeout interchangeable / not 344 maxbytes-overhead-vs-full bundled interchangeable」，不是 MaxBytes 开销与投递 bundled（344），也不是立刻整块执行已经离开关键路径（327），也不是 Prepare 及时性 bundled（327 余量）。不要另写怎样算头和证据开销。

## 官方三件事

1. **看见 timeout 必须按满块投递延迟算 / 看见最坏投递延迟 这份超时 is not already 已经填了 TimeoutPropose 就装得下这次 Prepare 执行 interchangeable，也不是已经 MaxBytes 开销与投递 bundled（344） interchangeable / 883 maxbytes-overhead-nottimeout interchangeable / 881 maxbytes-overhead-notfull interchangeable / 344 maxbytes item 1 扣开销 interchangeable，也不是已经 timeout 必须按满块投递延迟算 not already TimeoutPropose covers Prepare / not already left critical path / not already settled 正式三事 bundled（344 item 3 余量） interchangeable / 344 maxbytes item 3 interchangeable。**  
   官方写：因此节点采用的共识超时参数，应当按把一份满 `MaxBytes` 的块投递给所有验证者的最坏延迟来配。看见填了 TimeoutPropose，不是已经按满块投递算过 interchangeable——本页从 344 item 3 侧钉 not already TimeoutPropose covers Prepare 单句。344 maxbytes vs full bundled unbundling 在本页 item 3 完成。

2. **看见超时在 / 看见投递延迟 / 这份超时 is not already 已经是立刻整块执行离开关键路径 interchangeable，也不是已经 MaxBytes 开销与投递 bundled（344） interchangeable / 883 maxbytes-overhead-nottimeout interchangeable / 344 maxbytes item 2 MAY 打满 interchangeable / 882 maxbytes-overhead-not21mb interchangeable，也不是已经立刻整块执行已经离开关键路径 interchangeable / 327 leave-path interchangeable。**  
   官方把超时在和已经装得下这次 Prepare 里立刻整块执行分开——344 bundled 第三件事常与 327 混成「看见填了 TimeoutPropose 就已经装得下或已经离开关键路径 interchangeable」，本页钉 not already left critical path 单句。

3. **看见投递延迟 / 看见填了 TimeoutPropose / 这份超时 is not already 已经交差 interchangeable，也不是已经 MaxBytes 开销与投递 bundled（344） interchangeable / 883 maxbytes-overhead-nottimeout interchangeable / 881 maxbytes-overhead-notfull interchangeable，也不是已经四门已经结算 interchangeable / 33 four gates interchangeable。**  
   官方把投递延迟和已经离开关键路径 / 已经交差分开。看见投递延迟，不是已经离开关键路径 interchangeable。344 maxbytes vs full bundled unbundling 在本页 item 3 完成。

怎样算头 / 集合 / 证据开销、默认秒数、怎样设 `MaxBytes` 是规范里的取值或做法，本页不抄。

## 官方为什么这样拆

- **timeout 必须按满块投递延迟算 not already TimeoutPropose covers Prepare ≠ 已经填了 TimeoutPropose 就装得下这次 Prepare 执行 interchangeable：** 官方把满块投递延迟和 Prepare 执行超时分开。
- **看见超时在 not already left critical path ≠ 已经离开关键路径 interchangeable：** 官方把超时在和已经离开关键路径分开。
- **看见投递延迟 not already settled ≠ 已经交差 interchangeable：** 官方把投递延迟和已经交差分开；344 maxbytes vs full bundled unbundling 在本页 item 3 完成。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| timeout 必须按满块投递延迟算 | 不是已经填了 TimeoutPropose 就装得下这次 Prepare 执行 | 不是立刻整块执行已经离开关键路径（327） |
| 看见超时在 | 不是已经离开关键路径 | 不是四门已经结算（33） |
| 看见投递延迟 | 不是已经交差 | 不是扣了开销就已经整块都能装（881） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 timeout 必须按满块投递延迟算 not already TimeoutPropose covers Prepare / not already left critical path / not already settled 正式三事（344 余量），必须分开是不是已经填了 TimeoutPropose 就装得下这次 Prepare 执行、是不是已经离开关键路径、是不是已经交差。可以跳过「看见填了 TimeoutPropose 就已经装得下」。不要另写怎样算头和证据开销。344 maxbytes vs full bundled unbundling 在本页 item 3 完成。

## 本页不抄

- 怎样算头 / 集合 / 证据开销、默认秒数、怎样设 `MaxBytes`。
- MaxBytes 开销与投递 bundled。那是不变量 344。
- MaxBytes 减去头集合证据才是交易上限。那是不变量 344 item 1 余量 / 881。
- 立刻整块执行已经离开关键路径。那是不变量 327。
- 四门已经结算。那是不变量 33。
