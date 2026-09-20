# 例：看见 h < H 带了扩展 / 看见已经启用 / 看见切到 ABCI 2.0 is not already already legal interchangeable / already enabled interchangeable / already abci20 interchangeable

**层次**：实现 / h < H 带了扩展不是已经合法 not already legal / not already enabled / not already abci20 正式三事（330 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) List of Parameters / Application configuration required to switch to ABCI 2.0。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「h < H 带了扩展不是已经合法 not already legal / not already enabled / not already abci20 正式三事（330 余量）/ not 748 veheight-notlegal interchangeable / not 330 veheight bundled interchangeable」，不是 VoteExtensionsEnableHeight bundled（330），也不是到了 H 不是已经 Prepare 带了扩展（746 item 1 余量）或 H+1 带了扩展不是已经是本高度刚签的（747 item 2 余量）。不要另写怎样设 VoteExtensionsEnableHeight 或怎样写空扩展。

## 官方三件事

规范把 Requirements 里启用前带扩展的预提交当畸形拒收、H 之后不能关、字段在不等于已切到 ABCI 2.0 和「已经是 h < H 带了扩展就已经合法 interchangeable / 已经是字段在就已经启用 interchangeable / 已经是看见字段就已经切到 ABCI 2.0 interchangeable / 已经是 veheight bundled interchangeable」分开写成三件独立的实现事，不是「看见 h < H 带了扩展就已经合法 interchangeable / 就已经启用 interchangeable / 就已经切到 ABCI 2.0 interchangeable」一件事：

1. **看见 h < H 带了扩展 / 看见启用前带了扩展 / 看见带扩展的预提交 is not already 已经合法 interchangeable / 已经 legal interchangeable / 已经合法交差 interchangeable / 330 veheight bundled interchangeable / 33 four gates interchangeable / veheight-sold-as-prepared interchangeable，也不是已经 VoteExtensionsEnableHeight bundled（330） interchangeable / 748 veheight-notlegal interchangeable / 330 veheight item 3 interchangeable，也不是已经 h < H 带了扩展不是已经合法 not already legal / not already enabled / not already abci20 正式三事 bundled（330 item 3 余量） interchangeable / 330 veheight item 3 interchangeable，也不是已经到了 H 不是已经 Prepare 带了扩展（746） interchangeable / 747 veheight-notthissigned interchangeable / 34 vote-extension interchangeable，也不是已经四门已经结算（33） interchangeable。**  
   官方写：对所有高度 `h < H`，带投票扩展的预提交被当成畸形拒收。看见 h < H 带了扩展，不是已经 legal interchangeable——330 钉 bundled 三事，本页从 item 3 侧钉 not already legal 单句。看见启用前带了扩展，不是已经 VoteExtensionsEnableHeight bundled（330） interchangeable——330 钉 bundled，本页钉 item 3 第一件事。看见带扩展的预提交，不是已经 H+1 带了扩展不是已经是本高度刚签的（747） interchangeable——747 另钉 item 2。330 veheight vs prepare bundled unbundling 在本页 item 3 完成。

2. **看见已经启用 / 看见字段在 / 看见 H 之后不能关 is not already 已经启用交差 interchangeable / 已经 enabled interchangeable / 已经启用交差 interchangeable / 330 veheight bundled interchangeable / 58 enable-height interchangeable，也不是已经 VoteExtensionsEnableHeight bundled（330） interchangeable / 748 veheight-notlegal interchangeable / 330 veheight item 1 Prepare 带扩展 interchangeable / 330 veheight item 2 本高度刚签 interchangeable，也不是已经 h < H 带了扩展不是已经合法 not already legal / not already enabled / not already abci20 正式三事 bundled（330 item 3 余量） interchangeable / 330 veheight item 3 interchangeable，也不是已经合法（本页第一件事） interchangeable。**  
   官方写：H 之后不能关，扩展必须签过且在场；看见字段在，不是已经启用。看见已经启用，不是已经 enabled interchangeable——本页钉 not already enabled 单句。看见字段在，不是已经治理改 enable-height 会 panic（58） interchangeable——58 另钉。看见 H 之后不能关，不是已经合法（本页第一件事） interchangeable——三件事分开钉。330 veheight vs prepare bundled unbundling 在本页 item 3 完成。

3. **看见切到 ABCI 2.0 / 看见已经是 ABCI 2.0 / 看见切换完成 is not already 已经切到 ABCI 2.0 interchangeable / 已经 abci20 interchangeable / 已经切换交差 interchangeable / 330 veheight bundled interchangeable / 346 abci20-upgrade interchangeable，也不是已经 VoteExtensionsEnableHeight bundled（330） interchangeable / 748 veheight-notlegal interchangeable / 330 veheight item 1 / 330 veheight item 2，也不是已经 h < H 带了扩展不是已经合法 not already legal / not already enabled / not already abci20 正式三事 bundled（330 item 3 余量） interchangeable / 330 veheight item 3 interchangeable，也不是已经合法（本页第一件事） interchangeable / 已经启用（本页第二件事） interchangeable。**  
   官方写：看见字段在，不是已经切到 ABCI 2.0。看见切到 ABCI 2.0，不是已经 abci20 interchangeable——本页钉 not already abci20 单句。看见已经是 ABCI 2.0，不是已经必须协调升级不是已经只改 VoteExtensionsEnableHeight（346） interchangeable——346 另钉。看见切换完成，不是已经启用（本页第二件事） interchangeable——三件事分开钉。330 veheight vs prepare bundled unbundling 在本页 item 3 完成。

怎样设 `VoteExtensionsEnableHeight`、默认 `0`、怎样写空扩展是规范里的取值或做法，本页不抄。VoteExtensionsEnableHeight bundled（330）、到了 H 不是已经 Prepare 带了扩展（330 item 1 余量 / 746）、H+1 带了扩展不是已经是本高度刚签的（330 item 2 余量 / 747）、验签拒收整张预提交（34）、治理改 enable-height 会 panic（58）、必须协调升级（346）、四门已经结算（33）是另外那套，本页不抄。

## 官方为什么这样拆

- **h < H 带了扩展 not already legal ≠ 330 / 33 interchangeable：** 官方把启用前带扩展和已经合法分开。
- **字段在 not already enabled ≠ 已经启用 interchangeable：** 官方把字段在和已经启用分开。
- **看见字段 not already abci20 ≠ 已经切到 ABCI 2.0 interchangeable：** 官方把字段在和已经切到 ABCI 2.0 分开；330 veheight vs prepare bundled unbundling 在本页 item 3 完成。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| h < H 带了扩展 | 不是 already legal | 不是本高度刚签 alone（747） |
| 字段在 / 已经启用 | 不是 already enabled | 不是 enable-height panic alone（58） |
| 切到 ABCI 2.0 | 不是 already abci20 | 不是只改 VoteExtensionsEnableHeight alone（346） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 h < H 带了扩展不是已经合法 not already legal / not already enabled / not already abci20 正式三事（330 余量），必须分开 h < H 带了扩展 是不是 already legal interchangeable / 330 veheight bundled interchangeable / veheight-sold-as-prepared interchangeable、字段在 是不是 already enabled interchangeable、切到 ABCI 2.0 是不是 already abci20 interchangeable。可以跳过「看见 h < H 带了扩展就已经合法 interchangeable / 就已经启用 interchangeable / 就已经切到 ABCI 2.0 interchangeable」。不要另写怎样设 VoteExtensionsEnableHeight。330 veheight vs prepare bundled unbundling 在本页 item 3 完成（746 + 747 + 748）。

## 本页不抄

- 怎样设 `VoteExtensionsEnableHeight`、默认 `0`、怎样写空扩展。
- VoteExtensionsEnableHeight bundled。那是不变量 330。
- 到了 H 不是已经 Prepare 带了扩展。那是不变量 330 item 1 余量 / 746。
- H+1 带了扩展不是已经是本高度刚签的。那是不变量 330 item 2 余量 / 747。
- 验签拒收整张预提交、空扩展仍验签。那是不变量 34。
- 治理改 enable-height 会 panic。那是不变量 58。
- 必须协调升级不是已经只改 VoteExtensionsEnableHeight。那是不变量 346。
- 四门已经结算。那是不变量 33。
