# 例：看见 h < H 带了扩展 is not already legal interchangeable / not already enabled interchangeable / not already settled interchangeable

**层次**：实现 / h < H 带了扩展 not already legal / not already enabled / not already settled 正式三事（330 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) List of Parameters / Application configuration required to switch to ABCI 2.0。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行。本页是「h < H 带了扩展 not already legal / not already enabled / not already settled 正式三事（330 余量）/ not 928 ve-height-notlegal interchangeable / not 330 ve-height-vs-prepare bundled interchangeable」，不是扩展启用 bundled（330），也不是验签拒收整张预提交、空扩展仍验签（34），也不是 ABCI 2.0 升级已经切完（346）。不要另写怎样设 VoteExtensionsEnableHeight 或怎样写空扩展。

## 官方三件事

1. **看见 h < H 的预提交带了扩展 / 看见字段在 这份票 is not already 已经合法 interchangeable，也不是已经扩展启用 bundled（330） interchangeable / 928 ve-height-notlegal interchangeable / 926 ve-height-notprep interchangeable / 330 ve-height item 1 到了 H interchangeable，也不是已经 h < H 带了扩展 not already legal / not already enabled / not already settled 正式三事 bundled（330 item 3 余量） interchangeable / 330 ve-height item 3 interchangeable。**  
   官方写：对所有高度 h < H，带投票扩展的预提交被当成畸形拒收。H 之后不能关，扩展必须签过且在场。看见 h < H 的票带了扩展，不是已经合法 interchangeable——本页从 330 item 3 侧钉 not already legal 单句。330 ve-height vs prepare bundled unbundling 在本页 item 3 完成。

2. **看见字段在 / 看见 h < H 的票带了扩展 / 这份票 is not already 已经启用 interchangeable，也不是已经扩展启用 bundled（330） interchangeable / 928 ve-height-notlegal interchangeable / 330 ve-height item 2 H+1 interchangeable / 927 ve-height-notthis interchangeable，也不是已经 ABCI 2.0 升级已经切完 interchangeable / 346 abci20-upgrade interchangeable。**  
   官方把字段在和已经切到 ABCI 2.0 分开——330 bundled 第三件事常与 346 混成「看见 h < H 带了扩展就已经合法或已经切到 ABCI 2.0 interchangeable」，本页钉 not already enabled 单句。

3. **看见字段在 / 看见 h < H 的票带了扩展 / 这份票 is not already 已经交差 interchangeable，也不是已经扩展启用 bundled（330） interchangeable / 928 ve-height-notlegal interchangeable / 926 ve-height-notprep interchangeable，也不是已经验签拒收整张预提交 interchangeable / 34 verify-reject interchangeable。**  
   官方把字段在和已经交差分开。看见字段在，不是已经交差 interchangeable。330 ve-height vs prepare bundled unbundling 在本页 item 3 完成。

怎样设 VoteExtensionsEnableHeight、默认 0、怎样写空扩展是规范里的取值或做法，本页不抄。

## 官方为什么这样拆

- **h < H 带了扩展 not already legal ≠ 已经合法 interchangeable：** 官方把启用前带扩展的预提交和启用后必须在场的扩展分开。
- **看见字段在 not already enabled ≠ 已经启用 interchangeable：** 官方把字段在和已经切到 ABCI 2.0 分开。
- **看见字段在 not already settled ≠ 已经交差 interchangeable：** 官方把字段在和已经交差分开；330 ve-height vs prepare bundled unbundling 在本页 item 3 完成。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| h < H 带了扩展 | 不是已经合法 | 不是验签拒收整张预提交、空扩展仍验签（34） |
| 看见字段在 | 不是已经启用 | 不是 ABCI 2.0 升级已经切完（346） |
| 看见 h < H 的票带了扩展 | 不是已经交差 | 不是到了 H 就已经 Prepare 带了扩展（926） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 h < H 带了扩展 not already legal / not already enabled / not already settled 正式三事（330 余量），必须分开是不是已经合法、是不是已经启用、是不是已经交差。可以跳过「看见字段在就已经切到 ABCI 2.0」。不要另写怎样设 VoteExtensionsEnableHeight 或怎样写空扩展。330 ve-height vs prepare bundled unbundling 在本页 item 3 完成。

## 本页不抄

- 怎样设 VoteExtensionsEnableHeight、默认 0、怎样写空扩展。
- 扩展启用 bundled。那是不变量 330。
- 到了 H 就已经 Prepare 带了扩展。那是不变量 330 item 1 余量 / 926。
- 验签拒收整张预提交、空扩展仍验签。那是不变量 34。
- ABCI 2.0 升级已经切完。那是不变量 346。
