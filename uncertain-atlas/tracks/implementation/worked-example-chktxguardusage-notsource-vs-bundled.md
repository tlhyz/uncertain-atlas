# 例：看见 CheckTx before letting into its local mempool is not already tx source bundled interchangeable / not already mempool dedup interchangeable / not already Code≠0 rejected bundled interchangeable

**层次**：实现 / CheckTx Usage before letting into its local mempool not tx source bundled / not mempool dedup / not Code≠0 rejected bundled 正式三事（490 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) CheckTx Usage。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「CheckTx Usage before letting into its local mempool not tx source bundled / not mempool dedup / not Code≠0 rejected bundled 正式三事（490 余量）/ not 691 chktxguardusage-notsource interchangeable / not 490 chktxguardusage-vs-optional bundled interchangeable」，不是 CheckTx Usage Guardian 正式三事 bundled（490），也不是 tx source（488）或 Code≠0 rejected（489）。不要另写怎样写内存池守卫、怎样挑邻居。

## 官方三件事

规范把 CheckTx Usage 里 before letting a transaction into its local mempool 和「已经 may come from external user or another node（488） bundled 就代表来源已经验完 interchangeable / 已经内存池去重那种保证不重放（313） interchangeable / 已经 CheckTx Usage Code≠0 rejected（489） bundled 就代表 Guardian 已经交差 interchangeable」分开写成三件独立的实现事，不是「看见才让进本地池 就已经 tx source bundled interchangeable / 就已经 dedup interchangeable / 就已经 Code≠0 bundled interchangeable」一件事：

1. **看见 before letting a transaction into its local mempool / 看见才让进本地池 / local mempool is not already 已经 may come from external user or another node（488） bundled 就代表来源已经验完 interchangeable / 488 chktxsource interchangeable / 683 chktxsource-notrecheck interchangeable / 685 chktxsource-notreplay interchangeable，也不是已经 CheckTx Usage Guardian 正式三事 bundled（490） interchangeable / 691 chktxguardusage-notsource interchangeable / 689 chktxguardusage-notoptional interchangeable / 490 chktxguardusage item 1 Guardian interchangeable，也不是已经 before letting into local mempool not tx source bundled / not mempool dedup / not Code≠0 rejected bundled 正式三事 bundled（490 item 3 余量） interchangeable / 490 chktxguardusage item 3 interchangeable。**  
   官方把 before letting into its local mempool 和 tx source 分开写。看见才让进本地池，不是已经 may come from external user or another node interchangeable——488 钉 tx source，本页从 490 item 3 侧钉 not tx source bundled 单句。490 chktxguardusage vs optional bundled unbundling 在本页 item 3 完成。

2. **看见 before letting into its local mempool / 看见才让进本地池 / 看见 local mempool is not already 已经内存池去重那种保证不重放（313） interchangeable / 313 replay interchangeable / 已经应用级重放保护 interchangeable / 已经提案收了就从池里删掉（301） interchangeable，也不是已经 CheckTx Usage Guardian 正式三事 bundled（490） interchangeable / 691 chktxguardusage-notsource interchangeable / 490 chktxguardusage item 2 every node interchangeable / 690 chktxguardusage-notgates interchangeable。**  
   官方把 Usage 本地池入口和 Replay Protection 路径分开——490 bundled 第三件事常与 313 混成「看见才让进本地池 就已经保证不重放 interchangeable」，本页钉 not mempool dedup 单句。看见 local mempool，不是已经提案收了就从池里删掉 interchangeable——301 钉 mempool 交接，本页钉 Usage 入口。

3. **看见 before letting into its local mempool / 看见 Guardian 语境下的 before letting in / 看见 Usage 这句 is not already 已经 CheckTx Usage Code≠0 rejected（489） bundled 就代表 Guardian 已经交差 interchangeable / 489 chktxcodereject interchangeable / 686 chktxcodereject-notgossip interchangeable / 已经 validate-no-apply bundled 就代表 Guardian 已经验完 interchangeable / 486 chktxvalidate interchangeable，也不是已经 CheckTx Usage Guardian 正式三事 bundled（490） interchangeable / 691 chktxguardusage-notsource interchangeable / 689 chktxguardusage-notoptional interchangeable。**  
   官方把 Usage 本地池入口和 Code≠0 rejected bundled 路径分开——490 bundled 第三件事常与 489 混成「看见 before letting in 就已经 Code≠0 bundled 就代表 Guardian 交差 interchangeable」，本页钉 not Code≠0 rejected bundled 单句。看见 Guardian 语境下的 before letting in，不是已经 validate-no-apply bundled interchangeable——486 钉 validate-no-apply，本页钉 Usage item 3。490 chktxguardusage vs optional bundled unbundling 在本页 item 3 完成。

怎样做内存池守卫、怎样挑邻居、怎样写 CheckTx 重放谓词是规范里的做法，本页不抄。CheckTx Usage Guardian 正式三事 bundled（490）、Guardian of the mempool（490 item 1 余量 / 689）、every node runs CheckTx（490 item 2 余量 / 690）、tx source（488）、Replay Protection（313）、Code≠0 rejected（489）是另外那套，本页不抄。

## 官方为什么这样拆

- **before letting in not tx source bundled ≠ 488 chktxsource interchangeable：** 官方把 Usage 本地池入口和 tx source bundled 就代表来源验完路径分开。
- **before letting in not mempool dedup ≠ 313 replay interchangeable：** 官方把 Usage 本地池入口和去重就保证不重放路径分开。
- **before letting in not Code≠0 rejected bundled ≠ 489 interchangeable：** 官方把 Usage 本地池入口和 Code≠0 bundled 就代表 Guardian 交差路径分开；490 chktxguardusage vs optional bundled unbundling 在本页 item 3 完成。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| before letting into its local mempool | 不是 tx source bundled（488） | 不是 Guardian 单句（689/490 item 1） |
| 看见才让进本地池 | 不是内存池去重就保证不重放（313） | 不是 every node 单句（690/490 item 2） |
| 看见 Usage 这句 | 不是 Code≠0 rejected bundled（489） | 不是 CheckTx 守卫余量（405） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 CheckTx Usage before letting into its local mempool not tx source bundled / not mempool dedup / not Code≠0 rejected bundled 正式三事（490 余量），必须分开才让进本地池 是不是 tx source bundled interchangeable / 488、是不是去重就保证不重放 interchangeable / 313、是不是 Code≠0 bundled 就代表 Guardian 交差 interchangeable / 489。可以跳过「看见才让进本地池就已经保证不重放」。不要另写怎样写内存池守卫。490 chktxguardusage vs optional bundled unbundling 在本页 item 3 完成。

## 本页不抄

- 怎样做内存池守卫、怎样挑邻居、怎样写 CheckTx 重放谓词。
- CheckTx Usage Guardian 正式三事 bundled。那是不变量 490。
- Guardian of the mempool。那是不变量 490 item 1 余量 / 689。
- every node runs CheckTx before letting into local mempool。那是不变量 490 item 2 余量 / 690。
- CheckTx Usage tx source。那是不变量 488。
- 内存池去重 / 应用级重放保护。那是不变量 313。
- CheckTx Usage Code≠0 rejected。那是不变量 489。
