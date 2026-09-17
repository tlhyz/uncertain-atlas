# 例：看见 block_version / p2p_version 是引擎块版本和 P2P 版本 is not already versions aligned interchangeable / not already full history interchangeable / not already settled interchangeable

**层次**：实现 / block_version / p2p_version not already versions aligned / not already full history / not already settled 正式三事（379 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) Info Request。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「block_version / p2p_version not already versions aligned / not already full history / not already settled 正式三事（379 余量）/ not 792 infover-notaligned interchangeable / not 379 infover-vs-appversion bundled interchangeable」，不是 Info 请求版本 bundled（379），也不是 Info 的 AppHash 对上就已经是版本也对上（323），也不是 syncing_to_height 就已经有完整历史（382/782）。不要另写怎样写 Info 请求版本。

## 官方三件事

1. **看见 `block_version` / `p2p_version` 是引擎块版本和 P2P 版本 / 看见填了两列 / Info 这份引擎版本 is not already 已经是快照装完后又对上了应用版本 interchangeable / 323 snapid interchangeable，也不是已经 Info 请求版本 bundled（379） interchangeable / 792 infover-notaligned interchangeable / 791 infover-notappver interchangeable / 379 infover item 1 version interchangeable，也不是已经 block_version / p2p_version not already versions aligned / not already full history / not already settled 正式三事 bundled（379 item 2 余量） interchangeable / 379 infover item 2 interchangeable。**  
   官方写：`block_version` 是 CometBFT 的块版本。`p2p_version` 是 CometBFT 的 P2P 版本。看见填了两列，不是已经是快照装完后又对上了应用版本 interchangeable——本页从 379 item 2 侧钉 not already versions aligned 单句。379 infover vs appversion bundled unbundling 在本页 item 2 续。

2. **看见填了两列 / 看见有块版本 / Info 这份引擎版本 is not already 已经有从创世的完整历史 interchangeable / 323 snapid interchangeable，也不是已经 Info 请求版本 bundled（379） interchangeable / 792 infover-notaligned interchangeable / 379 infover item 3 abci_version interchangeable / 793 infover-nothandshake interchangeable，也不是已经 syncing_to_height 就已经有完整历史 interchangeable / 382 syncingheight / 782 syncingheight-nothistory interchangeable。**  
   官方把有块版本和已经有完整历史分开——379 bundled 第二件事常与 323 / 382 混成「看见填了两列就已经版本也对上或已经有完整历史 interchangeable」，本页钉 not already full history 单句。

3. **看见填了两列 / 看见有 P2P 版本 / Info 这份引擎版本 is not already 已经交差 interchangeable，也不是已经 Info 请求版本 bundled（379） interchangeable / 792 infover-notaligned interchangeable / 791 infover-notappver interchangeable。**  
   官方把有 P2P 版本和已经交差分开。看见有 P2P 版本，不是已经交差 interchangeable。379 infover vs appversion bundled unbundling 在本页 item 2 续。

怎样写 Info 请求、怎样对版本、怎样显示 X.X.x 是规范里的做法，本页不抄。

## 官方为什么这样拆

- **block_version / p2p_version not already versions aligned ≠ 323 interchangeable：** 官方把请求里的引擎版本和快照装完后对版本分开。
- **block_version / p2p_version not already full history ≠ 323 interchangeable：** 官方把有块版本和已经有完整历史分开。
- **block_version / p2p_version not already settled ≠ 已经交差 interchangeable：** 官方把有 P2P 版本和已经交差分开；379 infover vs appversion bundled unbundling 在本页 item 2 续。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| block_version / p2p_version 是引擎块版本和 P2P 版本 | 不是已经版本也对上（323） | 不是 Info 请求 version（791/379 item 1） |
| 看见填了两列 | 不是已经有完整历史 | 不是 syncing_to_height（382/782） |
| 看见有 P2P 版本 | 不是已经交差 | 不是 Info 请求版本 bundled（379） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 block_version / p2p_version not already versions aligned / not already full history / not already settled 正式三事（379 余量），必须分开两列是不是已经版本也对上 interchangeable / 323、是不是已经有完整历史、是不是已经交差。可以跳过「看见填了两列就已经版本也对上」。不要另写怎样写 Info 请求版本。379 infover vs appversion bundled unbundling 在本页 item 2 续；完成 [`worked-example-infover-nothandshake-vs-bundled.md`](worked-example-infover-nothandshake-vs-bundled.md)（不变量 793 item 3）。

## 本页不抄

- 怎样写 Info 请求、怎样对版本、怎样显示 X.X.x。
- Info 请求版本 bundled。那是不变量 379。
- Info 请求 version。那是不变量 379 item 1 余量 / 791。
- abci_version。那是不变量 379 item 3 余量 / 793。
- Info 的 AppHash 对上就已经是版本也对上。那是不变量 323。
- syncing_to_height 就已经有完整历史。那是不变量 382 / 782。
