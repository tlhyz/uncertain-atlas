# 例：看见 InitChain 请求 validators 是起步验证者名单 is not already no set interchangeable / not already empty list interchangeable / not already settled interchangeable

**层次**：实现 / InitChain 请求 validators not already no set / not already empty list / not already settled 正式三事（388 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) InitChain Request。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「InitChain 请求 validators not already no set / not already empty list / not already settled 正式三事（388 余量）/ not 765 initparams-notnoset interchangeable / not 388 initparams-vs-empty bundled interchangeable」，不是 InitChain 请求余栏 bundled（388），也不是 InitChain 回了空名单就已经没有集合（318）。不要另写怎样写 InitChain 请求余栏。

## 官方三件事

1. **看见 InitChain 请求 `validators` 是起步验证者名单 / 看见填了起步名单 / InitChain 这份起步名单 is not already 已经没有集合 interchangeable / 318 emptyset interchangeable，也不是已经 InitChain 请求余栏 bundled（388） interchangeable / 765 initparams-notnoset interchangeable / 764 initparams-notnoparams interchangeable / 388 initparams item 1 consensus_params interchangeable，也不是已经 validators not already no set / not already empty list / not already settled 正式三事 bundled（388 item 2 余量） interchangeable / 388 initparams item 2 interchangeable。**  
   官方写：`validators` 是起步创世验证者，按投票权排序。看见填了起步名单，不是已经没有集合 interchangeable——本页从 388 item 2 侧钉 not already no set 单句。388 initparams vs empty bundled unbundling 在本页 item 2 续。

2. **看见填了起步名单 / 看见有这份请求栏 / InitChain 这份起步名单 is not already 已经是 InitChain 回了空就改用创世名单 interchangeable / 318 emptyset interchangeable，也不是已经 InitChain 请求余栏 bundled（388） interchangeable / 765 initparams-notnoset interchangeable / 388 initparams item 3 app_state_bytes interchangeable / 766 initparams-notverified interchangeable。**  
   官方把请求里的起步名单和回包空着就已经没有集合分开——388 bundled 第二件事常与 318 混成「看见填了起步名单就已经没有集合或已经用了回包空名单 interchangeable」，本页钉 not already empty list 单句。

3. **看见填了起步名单 / 看见能回 / InitChain 这份起步名单 is not already 已经交差 interchangeable，也不是已经 InitChain 请求余栏 bundled（388） interchangeable / 765 initparams-notnoset interchangeable / 764 initparams-notnoparams interchangeable。**  
   官方把能填 InitChain 请求 validators 和已经交差分开。看见能回，不是已经交差 interchangeable。388 initparams vs empty bundled unbundling 在本页 item 2 续。

怎样写 InitChain 请求余栏、怎样选起步参数、怎样排起步名单是规范里的做法，本页不抄。

## 官方为什么这样拆

- **validators not already no set ≠ 318 interchangeable：** 官方把请求里的起步名单和回包空着就已经没有集合分开。
- **validators not already empty list ≠ 318 interchangeable：** 官方把有这份请求栏和已经用了回包空名单分开。
- **validators not already settled ≠ 已经交差 interchangeable：** 官方把能填起步名单和已经交差分开；388 initparams vs empty bundled unbundling 在本页 item 2 续。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| InitChain 请求 validators 是起步验证者名单 | 不是已经没有集合（318） | 不是 InitChain 请求 consensus_params（764/388 item 1） |
| 看见填了起步名单 | 不是已经用了回包空名单（318） | 不是 InitChain 请求余栏 bundled（388） |
| 看见能回 | 不是已经交差 | 不是 InitChain 请求 app_state_bytes（766/388 item 3） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 InitChain 请求 validators not already no set / not already empty list / not already settled 正式三事（388 余量），必须分开 validators 是不是已经没有集合 interchangeable / 318、是不是已经用了回包空名单、是不是已经交差。可以跳过「看见填了起步名单就已经没有集合」。不要另写怎样写 InitChain 请求余栏。388 initparams vs empty bundled unbundling 在本页 item 2 续；完成 [`worked-example-initparams-notverified-vs-bundled.md`](worked-example-initparams-notverified-vs-bundled.md)（不变量 766 item 3）。

## 本页不抄

- 怎样写 InitChain 请求余栏、怎样选起步参数、怎样排起步名单。
- InitChain 请求余栏 bundled。那是不变量 388。
- InitChain 请求 consensus_params。那是不变量 388 item 1 余量 / 764。
- InitChain 请求 app_state_bytes。那是不变量 388 item 3 余量 / 766。
- InitChain 回了空名单就已经没有集合。那是不变量 318。
