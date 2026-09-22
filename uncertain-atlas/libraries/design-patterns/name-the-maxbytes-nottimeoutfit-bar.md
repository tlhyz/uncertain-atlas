# 模式：把 timeout 必须按满块投递延迟算不是已经填了 TimeoutPropose 就装得下这次 Prepare 执行 not already timeoutpropose-fit / not already prepare-exec / not already critical-path 正式三事（344 余量）说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) List of Parameters / BlockParams.MaxBytes。  
**例**：[timeout 必须按满块投递 not already timeoutpropose-fit ≠ bundled（344）](../../tracks/implementation/worked-example-maxbytes-nottimeoutfit-vs-bundled.md)。

## 三个名字

1. **timeout 必须按满块投递 不是 already timeoutpropose-fit：** 看见 timeout 必须按满块投递延迟算 / 最坏投递延迟 / 填了 TimeoutPropose，不是已经填了 TimeoutPropose 就装得下这次 Prepare 执行 interchangeable / 已经 timeoutpropose-fit interchangeable / 已经装得下交差 interchangeable，不是 344 maxbytesoverhead bundled interchangeable / 738 preparetimeout-notfit interchangeable / maxbytesoverhead-sold-as-full interchangeable。

2. **超时在 不是 already prepare-exec：** 看见超时在 / 有共识超时 / TimeoutPropose 初值在，不是已经装得下这次 Prepare 执行 interchangeable / 已经 prepare-exec interchangeable / 已经 Prepare 执行交差 interchangeable，不是 327 preparetimeout interchangeable / preparetimeout-sold-as-liveness interchangeable。

3. **投递延迟 不是 already critical-path：** 看见投递延迟 / 满块投递延迟 / 最坏投递，不是已经离开关键路径 interchangeable / 已经 critical-path interchangeable / 已经离开关键路径交差 interchangeable，不是 737 preparetimeout-notcriticalpath interchangeable / 327 preparetimeout interchangeable。

官方把满块投递延迟、有超时参数、不是已经离开关键路径写成三个名字。把它们叫成一个「看见 timeout 必须按满块投递就已经装得下 Prepare interchangeable / 就已经是 Prepare 执行超时 interchangeable / 就已经离开关键路径 interchangeable」，会把 not already timeoutpropose-fit、not already prepare-exec、not already critical-path 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 timeout 必须按满块投递延迟算不是已经填了 TimeoutPropose 就装得下这次 Prepare 执行 not already timeoutpropose-fit / not already prepare-exec / not already critical-path 正式三事（344 余量），先数清问的是 timeout 必须按满块投递 是不是 already timeoutpropose-fit / 344 / maxbytesoverhead-sold-as-full，是不是超时在 是不是 already prepare-exec，还是投递延迟 是不是 already critical-path，再决定要不要同一次发布。344 maxbytesoverhead vs full bundled unbundling 在本页 item 3 完成。
