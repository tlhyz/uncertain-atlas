# 例：看见 Info 请求 version 是 CometBFT 软件语义版本不是已经是 app_version；看见 block_version / p2p_version 是引擎块版本和 P2P 版本不是已经版本也对上；看见 abci_version 是 ABCI 语义版本、按 X.X.x 显示不是已经是握手对齐

**层次**：实现 / Info 请求版本。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) Info Request。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5。本页是「Info 请求 version 是 CometBFT 软件语义版本不是已经是 app_version / block_version / p2p_version 是引擎块版本和 P2P 版本不是已经版本也对上 / abci_version 是 ABCI 语义版本、按 X.X.x 显示不是已经是握手对齐」，不是 Info 用来握手对齐就已经是快照重放，也不是 Info 的 AppHash 对上就已经是版本也对上。不要另写怎样写 Info 请求版本。379 infover-vs-appversion bundled unbundling 完成（884+885+886）；精读 [`worked-example-infover-notappversion-vs-bundled.md`](worked-example-infover-notappversion-vs-bundled.md)（不变量 884 item 1）；精读 [`worked-example-infover-notmatched-vs-bundled.md`](worked-example-infover-notmatched-vs-bundled.md)（不变量 885 item 2）；精读 [`worked-example-infover-nothandshake-vs-bundled.md`](worked-example-infover-nothandshake-vs-bundled.md)（不变量 886 item 3）。

## 官方三件事

规范把 Info 请求 `version` 是 CometBFT 软件语义版本、`block_version` / `p2p_version` 是引擎块版本和 P2P 版本、`abci_version` 是 ABCI 语义版本写成三件独立的实现事，不是「看见 Info 请求带了版本就已经是 app_version、已经版本也对上、已经是握手对齐」一件事：

1. **看见 Info 请求 `version` 是 CometBFT 软件语义版本 / 看见填了 `version` 不是已经是 `app_version`，也不是已经印进本头 AppHash。**  
   官方写：请求里的 `version` 是 CometBFT 软件的语义版本。看见填了 `version`，不是已经是回包里的 `app_version`。看见有软件版本，不是已经印进每块头。看见能回，不是已经交差。
2. **看见 `block_version` / `p2p_version` 是引擎块版本和 P2P 版本 / 看见填了两列 不是已经版本也对上，也不是已经有完整历史。**  
   官方写：`block_version` 是 CometBFT 的块版本。`p2p_version` 是 CometBFT 的 P2P 版本。看见填了两列，不是已经是快照装完后又对上了应用版本。看见有块版本，不是已经有从创世的完整历史。看见有 P2P 版本，不是已经交差。
3. **看见 `abci_version` 是 ABCI 语义版本、按 X.X.x 显示 / 看见写了语义版本 不是已经是握手对齐，也不是已经排了优先。**  
   官方写：`abci_version` 是 CometBFT 的 ABCI 语义版本。脚注写：语义版本指向 semver；Info 里的语义版本会显示成 X.X.x。看见写了 ABCI 版本，不是已经握手对齐。看见显示成 X.X.x，不是已经排了优先。看见有脚注，不是已经交差。

怎样写 Info 请求、怎样对版本、怎样显示 X.X.x 是规范里的做法，本页不抄。Info 用来握手对齐就已经是快照重放是不变量 370，本页不抄。

## 官方为什么这样拆

- **Info 请求 version 是 CometBFT 软件语义版本 ≠ 已经是 app_version：** 官方把引擎软件版本和应用 app_version 分开。
- **block_version / p2p_version 是引擎块版本和 P2P 版本 ≠ 已经版本也对上：** 官方把请求里的引擎版本和快照装完后对版本分开。
- **abci_version 是 ABCI 语义版本、按 X.X.x 显示 ≠ 已经是握手对齐：** 官方把 ABCI 语义版本和握手对齐分开。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| Info 请求 version 是 CometBFT 软件语义版本 | 不是已经是 app_version | 不是 Info 用来握手对齐就已经是快照重放（370） |
| block_version / p2p_version 是引擎块版本和 P2P 版本 | 不是已经版本也对上 | 不是 Info 的 AppHash 对上就已经是版本也对上（323） |
| abci_version 是 ABCI 语义版本、按 X.X.x 显示 | 不是已经是握手对齐 | 不是没定义 lane_priorities 就已经排了优先（367） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看「看见 Info 请求带了版本就已经是 app_version、已经版本也对上、已经是握手对齐」，必须分开 Info 请求 version 是 CometBFT 软件语义版本是不是已经是 app_version、block_version / p2p_version 是引擎块版本和 P2P 版本是不是已经版本也对上、abci_version 是 ABCI 语义版本、按 X.X.x 显示是不是已经是握手对齐。可以跳过「看见 Info 请求带了版本就已经是 app_version」。不要另写怎样写 Info 请求版本。379 infover-vs-appversion bundled unbundling 完成（884+885+886）。

## 本页不抄

- 怎样写 Info 请求、怎样对版本、怎样显示 X.X.x。
- Info 用来握手对齐就已经是快照重放。那是不变量 370。
- Info 的 AppHash 对上就已经是版本也对上。那是不变量 323。
- 没定义 lane_priorities 就已经排了优先。那是不变量 367。
