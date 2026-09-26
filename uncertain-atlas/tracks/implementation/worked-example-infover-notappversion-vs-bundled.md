# 例：看见填了 version / 看见有软件版本 / 看见能回 is not already already appversion interchangeable / already matched interchangeable / already settled interchangeable

**层次**：实现 / Info 请求 version 是 CometBFT 软件语义版本不是已经是 app_version not already appversion / not already matched / not already settled 正式三事（379 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) Info Request。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「Info 请求 version 是 CometBFT 软件语义版本不是已经是 app_version not already appversion / not already matched / not already settled 正式三事（379 余量）/ not 884 infover-notappversion interchangeable / not 379 infover bundled interchangeable」，不是 infover bundled（379），也不是 block_version / p2p_version 是引擎块版本和 P2P 版本不是已经版本也对上（379 item 2 余量）或 abci_version 是 ABCI 语义版本、按 X.X.x 显示不是已经是握手对齐（379 item 3 余量）。不要另写怎样写 Info 请求版本。

## 官方三件事

规范把 Methods 里 Info 请求 version 是 CometBFT 软件语义版本 和「已经是填了 version 就已经是 app_version interchangeable / 已经是有软件版本就已经印进本头 AppHash interchangeable / 已经是能回就已经交差 interchangeable / 已经是 infover bundled interchangeable」分开写成三件独立的实现事，不是「看见填了 version 就已经是 app_version interchangeable / 就已经印进本头 AppHash interchangeable / 就已经交差 interchangeable」一件事：

1. **看见填了 version / 看见 Info 请求 version 是 CometBFT 软件语义版本 / 看见填了 version 字段 is not already 已经是 app_version interchangeable / 已经 appversion interchangeable / 已经是 app_version 交差 interchangeable / 379 infover bundled interchangeable / 370 info-handshake interchangeable / infover-sold-as-appversion interchangeable，也不是已经 infover bundled（379） interchangeable / 884 infover-notappversion interchangeable / 379 infover item 1 interchangeable，也不是已经 Info 请求 version 是 CometBFT 软件语义版本不是已经是 app_version not already appversion / not already matched / not already settled 正式三事 bundled（379 item 1 余量） interchangeable / 379 infover item 1 interchangeable，也不是已经填了两列就已经版本也对上（379 item 2） interchangeable / 写了语义版本就已经是握手对齐（379 item 3） interchangeable / 370 Info 握手 interchangeable，也不是已经 Info 用来握手对齐就已经是快照重放（370） interchangeable。**  
   官方写：请求里的 `version` 是 CometBFT 软件的语义版本。看见填了 `version`，不是已经是回包里的 `app_version`。看见填了 version，不是已经 appversion interchangeable——379 钉 bundled 三事，本页从 item 1 侧钉 not already appversion 单句。看见 Info 请求 version 是 CometBFT 软件语义版本，不是已经 infover bundled（379） interchangeable——379 钉 bundled，本页钉 item 1 第一件事。看见填了 version 字段，不是已经 Info 用来握手对齐就已经是快照重放（370） interchangeable——370 另钉。379 infover-vs-appversion bundled unbundling 在本页 item 1 启动。

2. **看见有软件版本 / 看见有 CometBFT 软件语义版本 / 看见有版本字符串 is not already 已经印进本头 AppHash interchangeable / 已经 matched interchangeable / 已经印进每块头交差 interchangeable / 379 infover bundled interchangeable / 147 apphash-this-block interchangeable，也不是已经 infover bundled（379） interchangeable / 884 infover-notappversion interchangeable / 379 infover item 2 填了两列 interchangeable / 379 infover item 3 写了语义版本 interchangeable，也不是已经 Info 请求 version 是 CometBFT 软件语义版本不是已经是 app_version not already appversion / not already matched / not already settled 正式三事 bundled（379 item 1 余量） interchangeable / 379 infover item 1 interchangeable，也不是已经是 app_version（本页第一件事） interchangeable。**  
   官方写：看见有软件版本，不是已经印进每块头。看见有 CometBFT 软件语义版本，不是已经 matched interchangeable——本页钉 not already matched 单句。看见有版本字符串，不是已经是 app_version（本页第一件事） interchangeable——三件事分开钉。379 infover-vs-appversion bundled unbundling 在本页 item 1 启动。

3. **看见能回 / 看见能回 Info / 看见有回包 is not already 已经交差 interchangeable / 已经 settled interchangeable / 已经交差交差 interchangeable / 379 infover bundled interchangeable / 323 transition interchangeable，也不是已经 infover bundled（379） interchangeable / 884 infover-notappversion interchangeable / 379 infover item 2 / 379 infover item 3，也不是已经 Info 请求 version 是 CometBFT 软件语义版本不是已经是 app_version not already appversion / not already matched / not already settled 正式三事 bundled（379 item 1 余量） interchangeable / 379 infover item 1 interchangeable，也不是已经是 app_version（本页第一件事） interchangeable / 已经印进本头 AppHash（本页第二件事） interchangeable。**  
   官方写：看见能回，不是已经交差。看见能回 Info，不是已经 settled interchangeable——本页钉 not already settled 单句。看见有回包，不是已经印进本头 AppHash（本页第二件事） interchangeable——三件事分开钉。379 infover-vs-appversion bundled unbundling 在本页 item 1 启动。

怎样写 Info 请求、怎样对版本、怎样显示 X.X.x 是规范里的做法，本页不抄。infover bundled（379）、block_version / p2p_version 是引擎块版本和 P2P 版本不是已经版本也对上（379 item 2 余量）、abci_version 是 ABCI 语义版本、按 X.X.x 显示不是已经是握手对齐（379 item 3 余量）、Info 用来握手对齐就已经是快照重放（370）、Info 的 AppHash 对上就已经是版本也对上（323）、没定义 lane_priorities 就已经排了优先（367）是另外那套，本页不抄。

## 官方为什么这样拆

- **填了 version not already appversion ≠ 379 / 370 interchangeable：** 官方把引擎软件版本和应用 app_version 分开。
- **有软件版本 not already matched ≠ 已经印进本头 AppHash interchangeable：** 官方把有软件版本和已经印进每块头分开。
- **能回 not already settled ≠ 已经交差 interchangeable：** 官方把能回和已经交差分开；379 infover-vs-appversion bundled unbundling 在本页 item 1 启动。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 填了 version | 不是 already appversion | 不是 Info 用来握手对齐就已经是快照重放 alone（370） |
| 有软件版本 | 不是 already matched | 不是本头 AppHash alone（147） |
| 能回 | 不是 already settled | 不是填了两列 already matched alone（379 item 2） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Info 请求 version 是 CometBFT 软件语义版本不是已经是 app_version not already appversion / not already matched / not already settled 正式三事（379 余量），必须分开填了 version 是不是 already appversion interchangeable / 379 infover bundled interchangeable / infover-sold-as-appversion interchangeable、有软件版本 是不是 already matched interchangeable、能回 是不是 already settled interchangeable。可以跳过「看见填了 version 就已经是 app_version interchangeable / 就已经印进本头 AppHash interchangeable / 就已经交差 interchangeable」。不要另写怎样写 Info 请求版本。379 infover-vs-appversion bundled unbundling 在本页 item 1 启动（884）。

## 本页不抄

- 怎样写 Info 请求、怎样对版本、怎样显示 X.X.x。
- infover bundled。那是不变量 379。
- block_version / p2p_version 是引擎块版本和 P2P 版本不是已经版本也对上。那是不变量 379 item 2 余量。
- abci_version 是 ABCI 语义版本、按 X.X.x 显示不是已经是握手对齐。那是不变量 379 item 3 余量。
- Info 用来握手对齐就已经是快照重放。那是不变量 370。
- Info 的 AppHash 对上就已经是版本也对上。那是不变量 323。
- 没定义 lane_priorities 就已经排了优先。那是不变量 367。
