# 例：看见写了 ABCI 版本 / 看见显示成 X.X.x / 看见有脚注 is not already already handshake interchangeable / already priority interchangeable / already settled interchangeable

**层次**：实现 / abci_version 是 ABCI 语义版本、按 X.X.x 显示不是已经是握手对齐 not already handshake / not already priority / not already settled 正式三事（379 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) Info Request。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「abci_version 是 ABCI 语义版本、按 X.X.x 显示不是已经是握手对齐 not already handshake / not already priority / not already settled 正式三事（379 余量）/ not 886 infover-nothandshake interchangeable / not 379 infover bundled interchangeable」，不是 infover bundled（379），也不是 Info 请求 version 是 CometBFT 软件语义版本不是已经是 app_version（379 item 1 余量 / 884）或 block_version / p2p_version 是引擎块版本和 P2P 版本不是已经版本也对上（379 item 2 余量 / 885）。不要另写怎样写 Info 请求版本。

## 官方三件事

规范把 Methods 里 abci_version 是 ABCI 语义版本、按 X.X.x 显示 和「已经是写了 ABCI 版本就已经是握手对齐 interchangeable / 已经是显示成 X.X.x 就已经排了优先 interchangeable / 已经是有脚注就已经交差 interchangeable / 已经是 infover bundled interchangeable」分开写成三件独立的实现事，不是「看见写了 ABCI 版本就已经是握手对齐 interchangeable / 就已经排了优先 interchangeable / 就已经交差 interchangeable」一件事：

1. **看见写了 ABCI 版本 / 看见 abci_version 是 ABCI 语义版本、按 X.X.x 显示 / 看见写了 abci_version is not already 已经是握手对齐 interchangeable / 已经 handshake interchangeable / 已经是握手对齐交差 interchangeable / 379 infover bundled interchangeable / 370 info-handshake interchangeable / infover-sold-as-appversion interchangeable，也不是已经 infover bundled（379） interchangeable / 886 infover-nothandshake interchangeable / 379 infover item 3 interchangeable，也不是已经 abci_version 是 ABCI 语义版本、按 X.X.x 显示不是已经是握手对齐 not already handshake / not already priority / not already settled 正式三事 bundled（379 item 3 余量） interchangeable / 379 infover item 3 interchangeable，也不是已经填了 version 就已经是 app_version（884） interchangeable / 填了两列就已经版本也对上（885） interchangeable / 370 Info 握手 interchangeable，也不是已经 Info 用来握手对齐就已经是快照重放（370） interchangeable。**  
   官方写：`abci_version` 是 CometBFT 的 ABCI 语义版本。脚注写：语义版本指向 semver；Info 里的语义版本会显示成 X.X.x。看见写了 ABCI 版本，不是已经握手对齐。看见写了 ABCI 版本，不是已经 handshake interchangeable——379 钉 bundled 三事，本页从 item 3 侧钉 not already handshake 单句。看见 abci_version 是 ABCI 语义版本、按 X.X.x 显示，不是已经 infover bundled（379） interchangeable——379 钉 bundled，本页钉 item 3 第一件事。看见写了 abci_version，不是已经 Info 用来握手对齐就已经是快照重放（370） interchangeable——370 另钉。379 infover-vs-appversion bundled unbundling 在本页 item 3 完成。

2. **看见显示成 X.X.x / 看见语义版本显示成 X.X.x / 看见有 X.X.x 显示 is not already 已经排了优先 interchangeable / 已经 priority interchangeable / 已经排了优先交差 interchangeable / 379 infover bundled interchangeable / 367 lane-priority interchangeable，也不是已经 infover bundled（379） interchangeable / 886 infover-nothandshake interchangeable / 379 infover item 1 填了 version interchangeable / 379 infover item 2 填了两列 interchangeable，也不是已经 abci_version 是 ABCI 语义版本、按 X.X.x 显示不是已经是握手对齐 not already handshake / not already priority / not already settled 正式三事 bundled（379 item 3 余量） interchangeable / 379 infover item 3 interchangeable，也不是已经是握手对齐（本页第一件事） interchangeable。**  
   官方写：看见显示成 X.X.x，不是已经排了优先。看见语义版本显示成 X.X.x，不是已经 priority interchangeable——本页钉 not already priority 单句。看见有 X.X.x 显示，不是已经是握手对齐（本页第一件事） interchangeable——三件事分开钉。379 infover-vs-appversion bundled unbundling 在本页 item 3 完成。

3. **看见有脚注 / 看见脚注写了 semver / 看见有语义版本脚注 is not already 已经交差 interchangeable / 已经 settled interchangeable / 已经交差交差 interchangeable / 379 infover bundled interchangeable / 885 infover-notmatched interchangeable，也不是已经 infover bundled（379） interchangeable / 886 infover-nothandshake interchangeable / 379 infover item 1 / 379 infover item 2，也不是已经 abci_version 是 ABCI 语义版本、按 X.X.x 显示不是已经是握手对齐 not already handshake / not already priority / not already settled 正式三事 bundled（379 item 3 余量） interchangeable / 379 infover item 3 interchangeable，也不是已经是握手对齐（本页第一件事） interchangeable / 已经排了优先（本页第二件事） interchangeable。**  
   官方写：看见有脚注，不是已经交差。看见脚注写了 semver，不是已经 settled interchangeable——本页钉 not already settled 单句。看见有语义版本脚注，不是已经排了优先（本页第二件事） interchangeable——三件事分开钉。379 infover-vs-appversion bundled unbundling 在本页 item 3 完成。

怎样写 Info 请求、怎样对版本、怎样显示 X.X.x 是规范里的做法，本页不抄。infover bundled（379）、Info 请求 version 是 CometBFT 软件语义版本不是已经是 app_version（379 item 1 余量 / 884）、block_version / p2p_version 是引擎块版本和 P2P 版本不是已经版本也对上（379 item 2 余量 / 885）、Info 用来握手对齐就已经是快照重放（370）、Info 的 AppHash 对上就已经是版本也对上（323）、没定义 lane_priorities 就已经排了优先（367）是另外那套，本页不抄。

## 官方为什么这样拆

- **写了 ABCI 版本 not already handshake ≠ 379 / 370 interchangeable：** 官方把 ABCI 语义版本和握手对齐分开。
- **显示成 X.X.x not already priority ≠ 已经排了优先 interchangeable：** 官方把 X.X.x 显示和已经排了优先分开。
- **有脚注 not already settled ≠ 已经交差 interchangeable：** 官方把有脚注和已经交差分开；379 infover-vs-appversion bundled unbundling 在本页 item 3 完成。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 写了 ABCI 版本 | 不是 already handshake | 不是 Info 用来握手对齐就已经是快照重放 alone（370） |
| 显示成 X.X.x | 不是 already priority | 不是没定义 lane_priorities 就已经排了优先 alone（367） |
| 有脚注 | 不是 already settled | 不是填了两列 already matched alone（885） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 abci_version 是 ABCI 语义版本、按 X.X.x 显示不是已经是握手对齐 not already handshake / not already priority / not already settled 正式三事（379 余量），必须分开写了 ABCI 版本 是不是 already handshake interchangeable / 379 infover bundled interchangeable / infover-sold-as-appversion interchangeable、显示成 X.X.x 是不是 already priority interchangeable、有脚注 是不是 already settled interchangeable。可以跳过「看见写了 ABCI 版本就已经是握手对齐 interchangeable / 就已经排了优先 interchangeable / 就已经交差 interchangeable」。不要另写怎样写 Info 请求版本。379 infover-vs-appversion bundled unbundling 在本页 item 3 完成（884 + 885 + 886）。

## 本页不抄

- 怎样写 Info 请求、怎样对版本、怎样显示 X.X.x。
- infover bundled。那是不变量 379。
- Info 请求 version 是 CometBFT 软件语义版本不是已经是 app_version。那是不变量 379 item 1 余量 / 884。
- block_version / p2p_version 是引擎块版本和 P2P 版本不是已经版本也对上。那是不变量 379 item 2 余量 / 885。
- Info 用来握手对齐就已经是快照重放。那是不变量 370。
- Info 的 AppHash 对上就已经是版本也对上。那是不变量 323。
- 没定义 lane_priorities 就已经排了优先。那是不变量 367。
