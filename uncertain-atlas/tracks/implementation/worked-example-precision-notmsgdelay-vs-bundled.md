# 例：看见填了 Precision / 看见钟偏有界 / 看见能出合法提案 is not already already message-delay interchangeable / already delay-bounded interchangeable / already timely interchangeable

**层次**：实现 / 填了 Precision 不是已经是 MessageDelay not already message-delay / not already delay-bounded / not already timely 正式三事（336 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) List of Parameters / SynchronyParams.Precision / SynchronyParams.MessageDelay。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「填了 Precision 不是已经是 MessageDelay not already message-delay / not already delay-bounded / not already timely 正式三事（336 余量）/ not 761 precision-notmsgdelay interchangeable / not 336 precision bundled interchangeable」，不是 Precision bundled（336），也不是填了两个不是已经启用 PBTS（762 item 2 余量）或用于 PBTS 不是已经是永恒常数（763 item 3 余量）。不要另写怎样设 PRECISION / MSGDELAY 或怎样选启用高度。

## 官方三件事

规范把 Requirements 里填了 `SynchronyParams.Precision`、钟偏有界 和「已经是填了 Precision 就已经是 MessageDelay interchangeable / 已经是钟偏有界就已经延迟有界 interchangeable / 已经是能出合法提案就已经 timely interchangeable / 已经是 precision bundled interchangeable」分开写成三件独立的实现事，不是「看见填了 Precision 就已经是 MessageDelay interchangeable / 就已经延迟有界 interchangeable / 就已经 timely interchangeable」一件事：

1. **看见填了 Precision / 看见 `SynchronyParams.Precision` / 看见钟偏那一栏 is not already 已经是 MessageDelay interchangeable / 已经 message-delay interchangeable / 已经填了延迟那一栏交差 interchangeable / 336 precision bundled interchangeable / 40 block-time interchangeable / precision-sold-as-msgdelay interchangeable，也不是已经 Precision bundled（336） interchangeable / 761 precision-notmsgdelay interchangeable / 336 precision item 1 interchangeable，也不是已经填了 Precision 不是已经是 MessageDelay not already message-delay / not already delay-bounded / not already timely 正式三事 bundled（336 item 1 余量） interchangeable / 336 precision item 1 interchangeable，也不是已经填了两个不是已经启用 PBTS（762） interchangeable / 763 precision-noteternal interchangeable / 330 veheight interchangeable，也不是已经块时间必须点名算法（40） interchangeable。**  
   官方写：`Precision` 限制提议者的钟相对网上任一验证者可以偏多少，而仍能出合法提案。`MessageDelay` 限制一份提案消息可以走多久还算合法。看见填了 Precision，不是已经 message-delay interchangeable——336 钉 bundled 三事，本页从 item 1 侧钉 not already message-delay 单句。看见填了 Precision，不是已经 Precision bundled（336） interchangeable——336 钉 bundled，本页钉 item 1 第一件事。看见填了 Precision，不是已经块时间必须点名算法（40） interchangeable——40 另钉。336 precision vs msgdelay bundled unbundling 在本页 item 1 启动。

2. **看见钟偏有界 / 看见提议者钟偏有界 / 看见还能出合法提案的钟偏 is not already 已经延迟有界 interchangeable / 已经 delay-bounded interchangeable / 已经消息延迟有界交差 interchangeable / 336 precision bundled interchangeable / 327 preparetimeout interchangeable，也不是已经 Precision bundled（336） interchangeable / 761 precision-notmsgdelay interchangeable / 336 precision item 2 填了两个 interchangeable / 336 precision item 3 永恒常数 interchangeable，也不是已经填了 Precision 不是已经是 MessageDelay not already message-delay / not already delay-bounded / not already timely 正式三事 bundled（336 item 1 余量） interchangeable / 336 precision item 1 interchangeable，也不是已经是 MessageDelay（本页第一件事） interchangeable。**  
   官方写：看见钟偏有界，不是延迟已经有界。看见提议者钟偏有界，不是已经 delay-bounded interchangeable——本页钉 not already delay-bounded 单句。看见还能出合法提案的钟偏，不是已经是 MessageDelay（本页第一件事） interchangeable——三件事分开钉。336 precision vs msgdelay bundled unbundling 在本页 item 1 启动。

3. **看见能出合法提案 / 看见仍能出合法提案 / 看见钟偏有界仍能提案 is not already 已经 timely interchangeable / 已经 timely interchangeable / 已经及时交差 interchangeable / 336 precision bundled interchangeable / 40 block-time interchangeable，也不是已经 Precision bundled（336） interchangeable / 761 precision-notmsgdelay interchangeable / 336 precision item 2 / 336 precision item 3，也不是已经填了 Precision 不是已经是 MessageDelay not already message-delay / not already delay-bounded / not already timely 正式三事 bundled（336 item 1 余量） interchangeable / 336 precision item 1 interchangeable，也不是已经是 MessageDelay（本页第一件事） interchangeable / 已经延迟有界（本页第二件事） interchangeable。**  
   官方写：看见能出合法提案，不是已经 timely。看见仍能出合法提案，不是已经 timely interchangeable——本页钉 not already timely 单句。看见钟偏有界仍能提案，不是已经到了 H 已经 Prepare 带了扩展（330） interchangeable——330 另钉。看见能出合法提案，不是已经延迟有界（本页第二件事） interchangeable——三件事分开钉。336 precision vs msgdelay bundled unbundling 在本页 item 1 启动。

怎样设 `PRECISION` / `MSGDELAY`、默认毫秒、怎样选 `PbtsEnableHeight` 是规范里的取值或做法，本页不抄。Precision bundled（336）、填了两个不是已经启用 PBTS（336 item 2 余量 / 762）、用于 PBTS 不是已经是永恒常数（336 item 3 余量 / 763）、块时间必须点名算法（40）、到了 H 已经 Prepare 带了扩展（330）、立刻整块执行已经离开关键路径（327）是另外那套，本页不抄。

## 官方为什么这样拆

- **填了 Precision not already message-delay ≠ 336 / 40 interchangeable：** 官方把钟偏那一栏和消息延迟那一栏分开。
- **钟偏有界 not already delay-bounded ≠ 已经延迟有界 interchangeable：** 官方把钟偏有界和消息延迟已经有界分开。
- **能出合法提案 not already timely ≠ 已经 timely interchangeable：** 官方把能出合法提案和已经 timely 分开；336 precision vs msgdelay bundled unbundling 在本页 item 1 启动。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 填了 Precision | 不是 already message-delay | 不是块时间必须点名算法 alone（40） |
| 钟偏有界 | 不是 already delay-bounded | 不是立刻整块执行已经离开关键路径 alone（327） |
| 能出合法提案 | 不是 already timely | 不是到了 H 已经 Prepare 带了扩展 alone（330） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看填了 Precision 不是已经是 MessageDelay not already message-delay / not already delay-bounded / not already timely 正式三事（336 余量），必须分开填了 Precision 是不是 already message-delay interchangeable / 336 precision bundled interchangeable / precision-sold-as-msgdelay interchangeable、钟偏有界 是不是 already delay-bounded interchangeable、能出合法提案 是不是 already timely interchangeable。可以跳过「看见填了 Precision 就已经是 MessageDelay interchangeable / 就已经延迟有界 interchangeable / 就已经 timely interchangeable」。可以跳过「看见填了同步参数就已经是 PBTS」。不要另写怎样设 PRECISION / MSGDELAY 或怎样选启用高度。336 precision vs msgdelay bundled unbundling 在本页 item 1 启动；续 [`worked-example-precision-notpbts-vs-bundled.md`](worked-example-precision-notpbts-vs-bundled.md)（不变量 762 item 2）。

## 本页不抄

- 怎样设 `PRECISION` / `MSGDELAY`、默认毫秒、怎样选 `PbtsEnableHeight`。
- Precision bundled。那是不变量 336。
- 填了两个不是已经启用 PBTS。那是不变量 336 item 2 余量 / 762。
- 用于 PBTS 不是已经是永恒常数。那是不变量 336 item 3 余量 / 763。
- 块时间必须点名算法。那是不变量 40。
- 到了 H 已经 Prepare 带了扩展。那是不变量 330。
- 立刻整块执行已经离开关键路径。那是不变量 327。
