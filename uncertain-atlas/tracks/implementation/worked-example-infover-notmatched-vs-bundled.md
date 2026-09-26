# 例：看见填了两列 / 看见有块版本 / 看见有 P2P 版本 is not already already matched interchangeable / already history interchangeable / already settled interchangeable

**层次**：实现 / block_version / p2p_version 是引擎块版本和 P2P 版本不是已经版本也对上 not already matched / not already history / not already settled 正式三事（379 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) Info Request。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「block_version / p2p_version 是引擎块版本和 P2P 版本不是已经版本也对上 not already matched / not already history / not already settled 正式三事（379 余量）/ not 885 infover-notmatched interchangeable / not 379 infover bundled interchangeable」，不是 infover bundled（379），也不是 Info 请求 version 是 CometBFT 软件语义版本不是已经是 app_version（379 item 1 余量 / 884）或 abci_version 是 ABCI 语义版本、按 X.X.x 显示不是已经是握手对齐（379 item 3 余量）。不要另写怎样写 Info 请求版本。

## 官方三件事

规范把 Methods 里 block_version / p2p_version 是引擎块版本和 P2P 版本 和「已经是填了两列就已经版本也对上 interchangeable / 已经是有块版本就已经有完整历史 interchangeable / 已经是有 P2P 版本就已经交差 interchangeable / 已经是 infover bundled interchangeable」分开写成三件独立的实现事，不是「看见填了两列就已经版本也对上 interchangeable / 就已经有完整历史 interchangeable / 就已经交差 interchangeable」一件事：

1. **看见填了两列 / 看见 block_version / p2p_version 是引擎块版本和 P2P 版本 / 看见填了 block_version 与 p2p_version is not already 已经版本也对上 interchangeable / 已经 matched interchangeable / 已经版本也对上交差 interchangeable / 379 infover bundled interchangeable / 323 transition interchangeable / infover-sold-as-appversion interchangeable，也不是已经 infover bundled（379） interchangeable / 885 infover-notmatched interchangeable / 379 infover item 2 interchangeable，也不是已经 block_version / p2p_version 是引擎块版本和 P2P 版本不是已经版本也对上 not already matched / not already history / not already settled 正式三事 bundled（379 item 2 余量） interchangeable / 379 infover item 2 interchangeable，也不是已经填了 version 就已经是 app_version（884） interchangeable / 写了语义版本就已经是握手对齐（379 item 3） interchangeable / 323 snapshotswitch interchangeable，也不是已经 Info 的 AppHash 对上就已经是版本也对上（323） interchangeable。**  
   官方写：`block_version` 是 CometBFT 的块版本。`p2p_version` 是 CometBFT 的 P2P 版本。看见填了两列，不是已经是快照装完后又对上了应用版本。看见填了两列，不是已经 matched interchangeable——379 钉 bundled 三事，本页从 item 2 侧钉 not already matched 单句。看见 block_version / p2p_version 是引擎块版本和 P2P 版本，不是已经 infover bundled（379） interchangeable——379 钉 bundled，本页钉 item 2 第一件事。看见填了 block_version 与 p2p_version，不是已经 Info 的 AppHash 对上就已经是版本也对上（323） interchangeable——323 另钉。379 infover-vs-appversion bundled unbundling 在本页 item 2 续。

2. **看见有块版本 / 看见有 CometBFT 块版本 / 看见有 block_version is not already 已经有完整历史 interchangeable / 已经 history interchangeable / 已经有从创世的完整历史交差 interchangeable / 379 infover bundled interchangeable / 323 transition interchangeable，也不是已经 infover bundled（379） interchangeable / 885 infover-notmatched interchangeable / 379 infover item 1 填了 version interchangeable / 379 infover item 3 写了语义版本 interchangeable，也不是已经 block_version / p2p_version 是引擎块版本和 P2P 版本不是已经版本也对上 not already matched / not already history / not already settled 正式三事 bundled（379 item 2 余量） interchangeable / 379 infover item 2 interchangeable，也不是已经版本也对上（本页第一件事） interchangeable。**  
   官方写：看见有块版本，不是已经有从创世的完整历史。看见有 CometBFT 块版本，不是已经 history interchangeable——本页钉 not already history 单句。看见有 block_version，不是已经版本也对上（本页第一件事） interchangeable——三件事分开钉。379 infover-vs-appversion bundled unbundling 在本页 item 2 续。

3. **看见有 P2P 版本 / 看见有 CometBFT P2P 版本 / 看见有 p2p_version is not already 已经交差 interchangeable / 已经 settled interchangeable / 已经交差交差 interchangeable / 379 infover bundled interchangeable / 884 infover-notappversion interchangeable，也不是已经 infover bundled（379） interchangeable / 885 infover-notmatched interchangeable / 379 infover item 1 / 379 infover item 3，也不是已经 block_version / p2p_version 是引擎块版本和 P2P 版本不是已经版本也对上 not already matched / not already history / not already settled 正式三事 bundled（379 item 2 余量） interchangeable / 379 infover item 2 interchangeable，也不是已经版本也对上（本页第一件事） interchangeable / 已经有完整历史（本页第二件事） interchangeable。**  
   官方写：看见有 P2P 版本，不是已经交差。看见有 CometBFT P2P 版本，不是已经 settled interchangeable——本页钉 not already settled 单句。看见有 p2p_version，不是已经有完整历史（本页第二件事） interchangeable——三件事分开钉。379 infover-vs-appversion bundled unbundling 在本页 item 2 续。

怎样写 Info 请求、怎样对版本、怎样显示 X.X.x 是规范里的做法，本页不抄。infover bundled（379）、Info 请求 version 是 CometBFT 软件语义版本不是已经是 app_version（379 item 1 余量 / 884）、abci_version 是 ABCI 语义版本、按 X.X.x 显示不是已经是握手对齐（379 item 3 余量）、Info 用来握手对齐就已经是快照重放（370）、Info 的 AppHash 对上就已经是版本也对上（323）、没定义 lane_priorities 就已经排了优先（367）是另外那套，本页不抄。

## 官方为什么这样拆

- **填了两列 not already matched ≠ 379 / 323 interchangeable：** 官方把请求里的引擎版本和快照装完后对版本分开。
- **有块版本 not already history ≠ 已经有完整历史 interchangeable：** 官方把有块版本和已经有从创世的完整历史分开。
- **有 P2P 版本 not already settled ≠ 已经交差 interchangeable：** 官方把有 P2P 版本和已经交差分开；379 infover-vs-appversion bundled unbundling 在本页 item 2 续。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 填了两列 | 不是 already matched | 不是 Info 的 AppHash 对上就已经是版本也对上 alone（323） |
| 有块版本 | 不是 already history | 不是填了 version already appversion alone（884） |
| 有 P2P 版本 | 不是 already settled | 不是写了语义版本 already handshake alone（379 item 3） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 block_version / p2p_version 是引擎块版本和 P2P 版本不是已经版本也对上 not already matched / not already history / not already settled 正式三事（379 余量），必须分开填了两列 是不是 already matched interchangeable / 379 infover bundled interchangeable / infover-sold-as-appversion interchangeable、有块版本 是不是 already history interchangeable、有 P2P 版本 是不是 already settled interchangeable。可以跳过「看见填了两列就已经版本也对上 interchangeable / 就已经有完整历史 interchangeable / 就已经交差 interchangeable」。不要另写怎样写 Info 请求版本。379 infover-vs-appversion bundled unbundling 在本页 item 2 续（884 + 885）。

## 本页不抄

- 怎样写 Info 请求、怎样对版本、怎样显示 X.X.x。
- infover bundled。那是不变量 379。
- Info 请求 version 是 CometBFT 软件语义版本不是已经是 app_version。那是不变量 379 item 1 余量 / 884。
- abci_version 是 ABCI 语义版本、按 X.X.x 显示不是已经是握手对齐。那是不变量 379 item 3 余量。
- Info 用来握手对齐就已经是快照重放。那是不变量 370。
- Info 的 AppHash 对上就已经是版本也对上。那是不变量 323。
- 没定义 lane_priorities 就已经排了优先。那是不变量 367。
