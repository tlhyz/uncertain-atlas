# 例：看见 InitChain 请求 app_state_bytes 是序列化起步应用状态 is not already verified interchangeable / not already balances interchangeable / not already settled interchangeable

**层次**：实现 / InitChain 请求 app_state_bytes not already verified / not already balances / not already settled 正式三事（388 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) InitChain Request。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「InitChain 请求 app_state_bytes not already verified / not already balances / not already settled 正式三事（388 余量）/ not 766 initparams-notverified interchangeable / not 388 initparams-vs-empty bundled interchangeable」，不是 InitChain 请求余栏 bundled（388），也不是创世 app_state 就已经验过应用状态（303），也不是 InitChain 回包 app_hash 就已经是本头 AppHash（392/755）。不要另写怎样写 InitChain 请求余栏。

## 官方三件事

1. **看见 InitChain 请求 `app_state_bytes` 是序列化起步应用状态 / 看见填了 JSON 字节 / InitChain 这份序列化状态 is not already 已经验过创世文件里的应用段 interchangeable / 303 genesis interchangeable，也不是已经 InitChain 请求余栏 bundled（388） interchangeable / 766 initparams-notverified interchangeable / 764 initparams-notnoparams interchangeable / 388 initparams item 1 consensus_params interchangeable，也不是已经 app_state_bytes not already verified / not already balances / not already settled 正式三事 bundled（388 item 3 余量） interchangeable / 388 initparams item 3 interchangeable。**  
   官方写：`app_state_bytes` 是序列化起步应用状态，JSON 字节。看见填了 JSON 字节，不是已经验过创世文件里的应用段 interchangeable——本页从 388 item 3 侧钉 not already verified 单句。388 initparams vs empty bundled unbundling 在本页 item 3 完成。

2. **看见填了 JSON 字节 / 看见有字节 / InitChain 这份序列化状态 is not already 已经懂余额 interchangeable / 303 genesis interchangeable，也不是已经 InitChain 请求余栏 bundled（388） interchangeable / 766 initparams-notverified interchangeable / 388 initparams item 2 validators interchangeable / 765 initparams-notnoset interchangeable，也不是已经 InitChain 回包 app_hash 就已经是本头 AppHash interchangeable / 392 initapphash / 755 initapphash-notheader interchangeable。**  
   官方把请求里的序列化应用状态和已经懂余额分开——388 bundled 第三件事常与 303 / 392 混成「看见填了 JSON 字节就已经验过应用状态或已经是本头 AppHash interchangeable」，本页钉 not already balances 单句。

3. **看见填了 JSON 字节 / 看见能填 / InitChain 这份序列化状态 is not already 已经交差 interchangeable，也不是已经 InitChain 请求余栏 bundled（388） interchangeable / 766 initparams-notverified interchangeable / 764 initparams-notnoparams interchangeable。**  
   官方把能填 InitChain 请求 app_state_bytes 和已经交差分开。看见能填，不是已经交差 interchangeable。388 initparams vs empty bundled unbundling 在本页 item 3 完成。

怎样写 InitChain 请求余栏、怎样选起步参数、怎样排起步名单是规范里的做法，本页不抄。

## 官方为什么这样拆

- **app_state_bytes not already verified ≠ 303 interchangeable：** 官方把请求里的序列化应用状态和创世文件里的应用段已经验过分开。
- **app_state_bytes not already balances ≠ 303 interchangeable：** 官方把有字节和已经懂余额分开。
- **app_state_bytes not already settled ≠ 已经交差 interchangeable：** 官方把能填 JSON 字节和已经交差分开；388 initparams vs empty bundled unbundling 在本页 item 3 完成。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| InitChain 请求 app_state_bytes 是序列化起步应用状态 | 不是已经验过应用状态（303） | 不是 InitChain 请求 consensus_params（764/388 item 1） |
| 看见填了 JSON 字节 | 不是已经懂余额（303） | 不是 InitChain 回包 app_hash（392/755） |
| 看见能填 | 不是已经交差 | 不是 InitChain 请求余栏 bundled（388） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 InitChain 请求 app_state_bytes not already verified / not already balances / not already settled 正式三事（388 余量），必须分开 app_state_bytes 是不是已经验过应用状态 interchangeable / 303、是不是已经懂余额、是不是已经交差。可以跳过「看见填了 JSON 字节就已经验过应用状态」。不要另写怎样写 InitChain 请求余栏。388 initparams vs empty bundled unbundling 在本页 item 3 完成。

## 本页不抄

- 怎样写 InitChain 请求余栏、怎样选起步参数、怎样排起步名单。
- InitChain 请求余栏 bundled。那是不变量 388。
- InitChain 请求 consensus_params。那是不变量 388 item 1 余量 / 764。
- InitChain 请求 validators。那是不变量 388 item 2 余量 / 765。
- 创世 app_state 就已经验过应用状态。那是不变量 303。
- InitChain 回包 app_hash 就已经是本头 AppHash。那是不变量 392 / 755。
