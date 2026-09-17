# 例：看见填了 Precision is not already MessageDelay interchangeable / not already timely interchangeable / not already settled interchangeable

**层次**：实现 / 填了 Precision not already MessageDelay / not already timely / not already settled 正式三事（336 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) List of Parameters / SynchronyParams.Precision / SynchronyParams.MessageDelay。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5。本页是「填了 Precision not already MessageDelay / not already timely / not already settled 正式三事（336 余量）/ not 923 precision-notmsg interchangeable / not 336 precision-vs-msgdelay bundled interchangeable」，不是同步参数 bundled（336），也不是块时间必须点名算法（40），也不是到了 H 已经 Prepare 带了扩展（330）。不要另写怎样设 PRECISION / MSGDELAY 或怎样选启用高度。

## 官方三件事

1. **看见填了 SynchronyParams.Precision / 看见提议者钟偏有界 这份字段 is not already 已经是 MessageDelay interchangeable，也不是已经同步参数 bundled（336） interchangeable / 923 precision-notmsg interchangeable / 924 precision-noton interchangeable / 336 precision item 2 填了两个 interchangeable，也不是已经填了 Precision not already MessageDelay / not already timely / not already settled 正式三事 bundled（336 item 1 余量） interchangeable / 336 precision item 1 interchangeable。**  
   官方写：Precision 限制提议者的钟相对网上任一验证者可以偏多少，而仍能出合法提案。MessageDelay 限制一份提案消息可以走多久还算合法。看见填了 Precision，不是已经填了 MessageDelay interchangeable——本页从 336 item 1 侧钉 not already MessageDelay 单句。336 precision vs msgdelay bundled unbundling 在本页 item 1 启动。

2. **看见钟偏有界 / 看见能出合法提案 / 这份字段 is not already 已经 timely interchangeable，也不是已经同步参数 bundled（336） interchangeable / 923 precision-notmsg interchangeable / 336 precision item 3 用于 PBTS interchangeable / 925 precision-notconst interchangeable，也不是已经块时间必须点名算法 interchangeable / 40 block-time interchangeable。**  
   官方把钟偏有界和延迟已经有界 / 已经 timely 分开——336 bundled 第一件事常与 40 混成「看见填了 Precision 就已经是 MessageDelay 或已经点名算法 interchangeable」，本页钉 not already timely 单句。

3. **看见能出合法提案 / 看见填了 Precision / 这份字段 is not already 已经交差 interchangeable，也不是已经同步参数 bundled（336） interchangeable / 923 precision-notmsg interchangeable / 924 precision-noton interchangeable，也不是已经到了 H 已经 Prepare 带了扩展 interchangeable / 330 ve-height interchangeable。**  
   官方把能出合法提案和已经交差分开。看见能出合法提案，不是已经交差 interchangeable。336 precision vs msgdelay bundled unbundling 在本页 item 1 启动。

怎样设 PRECISION / MSGDELAY、默认毫秒、怎样选 PbtsEnableHeight 是规范里的取值或做法，本页不抄。

## 官方为什么这样拆

- **填了 Precision not already MessageDelay ≠ 已经是 MessageDelay interchangeable：** 官方把钟偏和消息延迟写成两把尺。
- **看见钟偏有界 not already timely ≠ 已经 timely interchangeable：** 官方把钟偏有界和延迟已经有界分开。
- **看见能出合法提案 not already settled ≠ 已经交差 interchangeable：** 官方把能出合法提案和已经交差分开；336 precision vs msgdelay bundled unbundling 在本页 item 1 启动。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 填了 Precision | 不是已经是 MessageDelay，也不是已经 timely | 不是块时间必须点名算法（40） |
| 看见钟偏有界 | 不是已经 timely | 不是到了 H 已经 Prepare 带了扩展（330） |
| 看见能出合法提案 | 不是已经交差 | 不是填了两个就已经启用 PBTS（924） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看填了 Precision not already MessageDelay / not already timely / not already settled 正式三事（336 余量），必须分开是不是已经是 MessageDelay、是不是已经 timely、是不是已经交差。可以跳过「看见填了同步参数就已经是 PBTS」。不要另写怎样设 PRECISION / MSGDELAY 或怎样选启用高度。336 precision vs msgdelay bundled unbundling 在本页 item 1 启动；续 [`worked-example-precision-noton-vs-bundled.md`](worked-example-precision-noton-vs-bundled.md)（不变量 924 item 2）。

## 本页不抄

- 怎样设 PRECISION / MSGDELAY、默认毫秒、怎样选 PbtsEnableHeight。
- 同步参数 bundled。那是不变量 336。
- 填了两个就已经启用 PBTS。那是不变量 336 item 2 余量 / 924。
- 块时间必须点名算法。那是不变量 40。
