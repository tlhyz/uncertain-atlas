# 例：看见 abci_version 是 ABCI 语义版本、按 X.X.x 显示 is not already handshake interchangeable / not already prioritized interchangeable / not already settled interchangeable

**层次**：实现 / abci_version not already handshake / not already prioritized / not already settled 正式三事（379 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) Info Request。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「abci_version not already handshake / not already prioritized / not already settled 正式三事（379 余量）/ not 793 infover-nothandshake interchangeable / not 379 infover-vs-appversion bundled interchangeable」，不是 Info 请求版本 bundled（379），也不是 Info 用来握手对齐就已经是快照重放（370），也不是没定义 lane_priorities 就已经排了优先（367）。不要另写怎样写 Info 请求版本。

## 官方三件事

1. **看见 `abci_version` 是 ABCI 语义版本、按 X.X.x 显示 / 看见写了语义版本 / Info 这份 ABCI 版本 is not already 已经握手对齐 interchangeable / 370 handshake interchangeable，也不是已经 Info 请求版本 bundled（379） interchangeable / 793 infover-nothandshake interchangeable / 791 infover-notappver interchangeable / 379 infover item 1 version interchangeable，也不是已经 abci_version not already handshake / not already prioritized / not already settled 正式三事 bundled（379 item 3 余量） interchangeable / 379 infover item 3 interchangeable。**  
   官方写：`abci_version` 是 CometBFT 的 ABCI 语义版本。脚注写：语义版本指向 semver；Info 里的语义版本会显示成 X.X.x。看见写了 ABCI 版本，不是已经握手对齐 interchangeable——本页从 379 item 3 侧钉 not already handshake 单句。379 infover vs appversion bundled unbundling 在本页 item 3 完成。

2. **看见写了语义版本 / 看见显示成 X.X.x / Info 这份 ABCI 版本 is not already 已经排了优先 interchangeable / 367 laneprio interchangeable，也不是已经 Info 请求版本 bundled（379） interchangeable / 793 infover-nothandshake interchangeable / 379 infover item 2 block_version interchangeable / 792 infover-notaligned interchangeable。**  
   官方把显示成 X.X.x 和已经排了优先分开——379 bundled 第三件事常与 370 / 367 混成「看见写了 ABCI 版本就已经是握手对齐或已经排了优先 interchangeable」，本页钉 not already prioritized 单句。

3. **看见写了语义版本 / 看见有脚注 / Info 这份 ABCI 版本 is not already 已经交差 interchangeable，也不是已经 Info 请求版本 bundled（379） interchangeable / 793 infover-nothandshake interchangeable / 791 infover-notappver interchangeable。**  
   官方把有脚注和已经交差分开。看见有脚注，不是已经交差 interchangeable。379 infover vs appversion bundled unbundling 在本页 item 3 完成。

怎样写 Info 请求、怎样对版本、怎样显示 X.X.x 是规范里的做法，本页不抄。

## 官方为什么这样拆

- **abci_version not already handshake ≠ 370 interchangeable：** 官方把 ABCI 语义版本和握手对齐分开。
- **abci_version not already prioritized ≠ 367 interchangeable：** 官方把显示成 X.X.x 和已经排了优先分开。
- **abci_version not already settled ≠ 已经交差 interchangeable：** 官方把有脚注和已经交差分开；379 infover vs appversion bundled unbundling 在本页 item 3 完成。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| abci_version 是 ABCI 语义版本、按 X.X.x 显示 | 不是已经是握手对齐（370） | 不是 Info 请求 version（791/379 item 1） |
| 看见写了语义版本 | 不是已经排了优先（367） | 不是没定义 lane_priorities 就已经排了优先（367） |
| 看见有脚注 | 不是已经交差 | 不是 Info 请求版本 bundled（379） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 abci_version not already handshake / not already prioritized / not already settled 正式三事（379 余量），必须分开 abci_version 是不是已经是握手对齐 interchangeable / 370、是不是已经排了优先 interchangeable / 367、是不是已经交差。可以跳过「看见写了 ABCI 版本就已经是握手对齐」。不要另写怎样写 Info 请求版本。379 infover vs appversion bundled unbundling 在本页 item 3 完成。

## 本页不抄

- 怎样写 Info 请求、怎样对版本、怎样显示 X.X.x。
- Info 请求版本 bundled。那是不变量 379。
- Info 请求 version。那是不变量 379 item 1 余量 / 791。
- block_version / p2p_version。那是不变量 379 item 2 余量 / 792。
- Info 用来握手对齐就已经是快照重放。那是不变量 370。
- 没定义 lane_priorities 就已经排了优先。那是不变量 367。
