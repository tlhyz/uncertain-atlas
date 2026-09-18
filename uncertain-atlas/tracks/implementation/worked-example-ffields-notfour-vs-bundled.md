# 例：看见 Finalize just-decided-fields is not already four-gates interchangeable / not already processed interchangeable / not already settled interchangeable

**层次**：实现 / Finalize just-decided-fields not already four-gates / not already processed / not already settled 正式三事（407 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) FinalizeBlock Usage / Info Usage。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「Finalize just-decided-fields not already four-gates / not already processed / not already settled 正式三事（407 余量）/ not 1109 ffields-notfour interchangeable / not 407 finfields-vs-equiv bundled interchangeable」，不是 Finalize 字段余量 bundled（407），也不是 Finalize 等价于 ABCI 1.0 那三步就已经是四门已经结算（363），也不是 Finalize height/time 对上就已经是刚决定那块的字段（1099）。不要另写怎样写 Finalize 字段余量。

## 官方三件事

1. **看见 Finalize 含刚决定那块的字段 / 看见填了字段 这份栏 is not already 已经是四门已经结算 interchangeable，也不是已经 Finalize 字段余量 bundled（407） interchangeable / 1109 ffields-notfour interchangeable / 1110 ffields-notprep interchangeable / 407 finfields item 2 must-det interchangeable，也不是已经 Finalize just-decided-fields not already four-gates / not already processed / not already settled 正式三事 bundled（407 item 1 余量） interchangeable / 407 finfields item 1 interchangeable。**  
   官方写：FinalizeBlock 含刚决定那块的字段。看见填了字段，不是已经是四门已经结算 interchangeable——本页从 407 item 1 侧钉 not already four-gates 单句。407 finfields vs equiv bundled unbundling 在本页 item 1 启动。

2. **看见有刚决定那块 / 看见填了字段 / 这份栏 is not already 已经跑过 Process interchangeable，也不是已经 Finalize 字段余量 bundled（407） interchangeable / 1109 ffields-notfour interchangeable / 407 finfields item 3 info-not-handshake interchangeable / 1111 ffields-notinfo interchangeable，也不是已经 Finalize 等价于 ABCI 1.0 那三步就已经是四门已经结算 interchangeable / 363 finresp interchangeable。**  
   官方把有刚决定那块和已经跑过 Process 分开。看见有刚决定那块，不是已经跑过 Process interchangeable。本页钉 not already processed 单句。

3. **看见能填 / 看见填了字段 / 这份栏 is not already 已经交差 interchangeable，也不是已经 Finalize 字段余量 bundled（407） interchangeable / 1109 ffields-notfour interchangeable / 1110 ffields-notprep interchangeable，也不是已经 Finalize height/time 对上就已经是刚决定那块的字段 interchangeable / 1099 htmt-notdec interchangeable。**  
   官方把能填和已经交差分开。看见能填，不是已经交差 interchangeable。407 finfields vs equiv bundled unbundling 在本页 item 1 启动。

怎样写 Finalize 字段余量、怎样写确定性、怎样回 Info 是规范里的做法，本页不抄。

## 官方为什么这样拆

- **Finalize just-decided-fields not already four-gates ≠ 已经是四门已经结算 interchangeable：** 官方把刚决定那块的字段和收成一门的三步分开。
- **看见有刚决定那块 not already processed ≠ 已经跑过 Process interchangeable：** 官方把有刚决定那块和已经跑过 Process 分开。
- **看见能填 not already settled ≠ 已经交差 interchangeable：** 官方把能填和已经交差分开；407 finfields vs equiv bundled unbundling 在本页 item 1 启动。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| Finalize 含刚决定那块的字段 | 不是已经是四门已经结算 | 不是 Finalize 等价于 ABCI 1.0 那三步就已经是四门已经结算（363） |
| 看见有刚决定那块 | 不是已经跑过 Process | 不是 Finalize height/time 对上就已经是刚决定那块的字段（1099） |
| 看见能填 | 不是已经交差 | 不是必须确定就已经可以像 Prepare 那样（1110） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Finalize just-decided-fields not already four-gates / not already processed / not already settled 正式三事（407 余量），必须分开是不是已经是四门已经结算、是不是已经跑过 Process、是不是已经交差。可以跳过「看见填了 Finalize 字段余量就已经是四门已经结算」。不要另写怎样写 Finalize 字段余量。407 finfields vs equiv bundled unbundling 在本页 item 1 启动；续 [`worked-example-ffields-notprep-vs-bundled.md`](worked-example-ffields-notprep-vs-bundled.md)（不变量 1110 item 2）。

## 本页不抄

- 怎样写 Finalize 字段余量、怎样写确定性、怎样回 Info。
- Finalize 字段余量 bundled。那是不变量 407。
- Finalize 等价于 ABCI 1.0 那三步就已经是四门已经结算。那是不变量 363。
- Finalize height/time 对上就已经是刚决定那块的字段。那是不变量 1099。
