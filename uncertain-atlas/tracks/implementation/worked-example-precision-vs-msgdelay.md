# 例：看见填了 Precision 不是已经是 MessageDelay；看见填了两个不是已经启用 PBTS；看见用于 PBTS 不是已经是永恒常数

**层次**：实现 / SynchronyParams。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) List of Parameters / SynchronyParams.Precision / SynchronyParams.MessageDelay。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5。本页是「填了 Precision 不是已经是 MessageDelay / 填了两个不是已经启用 PBTS / 用于 PBTS 不是已经是永恒常数」，不是块时间算法已经点名，也不是到了 H 已经 Prepare 带了扩展。不要另写怎样设 PRECISION / MSGDELAY 或怎样选启用高度。 336 precision vs msgdelay bundled unbundling 启动（761）；精读 [`worked-example-precision-notmsgdelay-vs-bundled.md`](worked-example-precision-notmsgdelay-vs-bundled.md)。

## 官方三件事

规范把同步参数写成三件独立的实现事，不是「看见填了 Precision 就已经是 MessageDelay、已经启用 PBTS、已经是永恒常数」一件事：

1. **看见填了 `SynchronyParams.Precision` / 看见提议者钟偏有界 不是已经是 `MessageDelay`，也不是已经 timely。**  
   官方写：`Precision` 限制提议者的钟相对网上任一验证者可以偏多少，而仍能出合法提案。`MessageDelay` 限制一份提案消息可以走多久还算合法。看见填了 Precision，不是已经填了 MessageDelay。看见钟偏有界，不是延迟已经有界。看见能出合法提案，不是已经 timely。
2. **看见填了两个 / 看见这两个参数用于 PBTS 不是已经启用 PBTS，也不是已经不能关。**  
   官方写：这两个参数都由 PBTS 算法使用。看见填了两个，不是已经到了 `PbtsEnableHeight`。看见写了用于 PBTS，不是已经切到 PBTS。看见参数在，不是已经不能关，也不是已经是扩展启用高度那种切换。
3. **看见用于 PBTS / 看见能出合法提案 不是已经是永恒常数，也不是已经是 BFT Time 中位数。**  
   官方把它们写成 PBTS 用的两把尺，不是未标注版本的永恒共识常数，也不是上一高度 LastCommit 的加权中位。看见用于 PBTS，不是已经抄成产品常数。看见能出合法提案，不是已经是 MTP，也不是已经是调整钟。

怎样设 `PRECISION` / `MSGDELAY`、默认毫秒、怎样选 `PbtsEnableHeight` 是规范里的取值或做法，本页不抄。块时间必须点名算法是不变量 40，本页不抄。

## 官方为什么这样拆

- **Precision ≠ 已经是 MessageDelay：** 官方把钟偏和消息延迟写成两把尺。
- **填了两个 ≠ 已经启用 PBTS：** 官方把参数存在和 PBTS 已经打开分开。
- **用于 PBTS ≠ 已经是永恒常数：** 官方把这两把尺和永恒常数、BFT Time 中位数分开。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 填了 Precision | 不是已经是 MessageDelay | 不是块时间必须点名算法 / 不得把 PRECISION / MSGDELAY 写成永恒共识（40） |
| 填了两个 / 用于 PBTS | 不是已经启用 PBTS | 不是到了 H 已经 Prepare 带了扩展（330） |
| 用于 PBTS | 不是已经是永恒常数 | 不是立刻整块执行已经离开关键路径（327） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看「填了 Precision 就已经是 MessageDelay、已经启用 PBTS、已经是永恒常数」，必须分开 Precision 是不是已经是 MessageDelay、填了两个是不是已经启用 PBTS、用于 PBTS 是不是已经是永恒常数。可以跳过「看见填了同步参数就已经是 PBTS」。不要另写怎样设 PRECISION / MSGDELAY 或怎样选启用高度。 336 precision vs msgdelay bundled unbundling 启动（761 item 1）。

## 本页不抄

- 怎样设 `PRECISION` / `MSGDELAY`、默认毫秒、怎样选 `PbtsEnableHeight`。
- 块时间必须点名算法、不 timely 不是块非法、启用后不能关。那是不变量 40。
- 到了 H 已经 Prepare 带了扩展。那是不变量 330。
- 立刻整块执行已经离开关键路径。那是不变量 327。
