# 例：看见 Finalize must-det state-machine is not already like-Prepare interchangeable / not already header-printed interchangeable / not already settled interchangeable

**层次**：实现 / Finalize must-det state-machine not already like-Prepare / not already header-printed / not already settled 正式三事（407 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) FinalizeBlock Usage / Info Usage。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「Finalize must-det state-machine not already like-Prepare / not already header-printed / not already settled 正式三事（407 余量）/ not 1110 ffields-notprep interchangeable / not 407 finfields-vs-equiv bundled interchangeable」，不是 Finalize 字段余量 bundled（407），也不是 Finalize 算出的状态必须只依赖上一份状态和决定块就已经可以像 Prepare 那样（342），也不是 Prepare 没有确定性要求就已经交差（338）。不要另写怎样写 Finalize 字段余量。

## 官方三件事

1. **看见 Finalize 实现必须确定、因为它在状态机复制里推进应用状态 / 看见必须确定 这份栏 is not already 已经可以像 Prepare 那样 interchangeable，也不是已经 Finalize 字段余量 bundled（407） interchangeable / 1110 ffields-notprep interchangeable / 1109 ffields-notfour interchangeable / 407 finfields item 1 fields-not-four interchangeable，也不是已经 Finalize must-det state-machine not already like-Prepare / not already header-printed / not already settled 正式三事 bundled（407 item 2 余量） interchangeable / 407 finfields item 2 interchangeable。**  
   官方写：FinalizeBlock 的实现必须确定，因为它在状态机复制的上下文里推进应用状态。看见必须确定，不是已经可以像 Prepare 那样 interchangeable——本页从 407 item 2 侧钉 not already like-Prepare 单句。407 finfields vs equiv bundled unbundling 在本页 item 2 续。

2. **看见在复制里推进 / 看见必须确定 / 这份栏 is not already 已经印进本头 interchangeable，也不是已经 Finalize 字段余量 bundled（407） interchangeable / 1110 ffields-notprep interchangeable / 407 finfields item 3 info-not-handshake interchangeable / 1111 ffields-notinfo interchangeable，也不是已经 Finalize 算出的状态必须只依赖上一份状态和决定块就已经可以像 Prepare 那样 interchangeable / 342 finalize-det interchangeable。**  
   官方把在复制里推进和已经印进本头分开。看见在复制里推进，不是已经印进本头 interchangeable。本页钉 not already header-printed 单句。

3. **看见能推进 / 看见必须确定 / 这份栏 is not already 已经交差 interchangeable，也不是已经 Finalize 字段余量 bundled（407） interchangeable / 1110 ffields-notprep interchangeable / 1109 ffields-notfour interchangeable，也不是已经 Prepare 没有确定性要求就已经交差 interchangeable / 338 prepare-nondet interchangeable。**  
   官方把能推进和已经交差分开。看见能推进，不是已经交差 interchangeable。407 finfields vs equiv bundled unbundling 在本页 item 2 续。

怎样写 Finalize 字段余量、怎样写确定性、怎样回 Info 是规范里的做法，本页不抄。

## 官方为什么这样拆

- **Finalize must-det state-machine not already like-Prepare ≠ 已经可以像 Prepare 那样 interchangeable：** 官方把 Usage 这句必须确定和 Req 11–12 那句只依赖分开。
- **看见在复制里推进 not already header-printed ≠ 已经印进本头 interchangeable：** 官方把在复制里推进和已经印进本头分开。
- **看见能推进 not already settled ≠ 已经交差 interchangeable：** 官方把能推进和已经交差分开；407 finfields vs equiv bundled unbundling 在本页 item 2 续。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| Finalize 实现必须确定、因为它在状态机复制里推进应用状态 | 不是已经可以像 Prepare 那样 | 不是 Finalize 算出的状态必须只依赖上一份状态和决定块就已经可以像 Prepare 那样（342） |
| 看见在复制里推进 | 不是已经印进本头 | 不是 Prepare 没有确定性要求就已经交差（338） |
| 看见能推进 | 不是已经交差 | 不是 Info 能回就已经是握手对齐（1111） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Finalize must-det state-machine not already like-Prepare / not already header-printed / not already settled 正式三事（407 余量），必须分开是不是已经可以像 Prepare 那样、是不是已经印进本头、是不是已经交差。可以跳过「看见填了 Finalize 字段余量就已经是四门已经结算」。不要另写怎样写 Finalize 字段余量。407 finfields vs equiv bundled unbundling 在本页 item 2 续；续 [`worked-example-ffields-notinfo-vs-bundled.md`](worked-example-ffields-notinfo-vs-bundled.md)（不变量 1111 item 3）。

## 本页不抄

- 怎样写 Finalize 字段余量、怎样写确定性、怎样回 Info。
- Finalize 字段余量 bundled。那是不变量 407。
- Finalize 算出的状态必须只依赖上一份状态和决定块就已经可以像 Prepare 那样。那是不变量 342。
- Prepare 没有确定性要求就已经交差。那是不变量 338。
