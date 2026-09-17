# 例：看见 CheckTx Guardian of the mempool is not already Technically optional interchangeable / not already four gates settled interchangeable / not already validate-no-apply bundled interchangeable

**层次**：实现 / CheckTx Usage Guardian of the mempool not Technically optional / not four gates settled / not validate-no-apply bundled 正式三事（490 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) CheckTx Usage。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「CheckTx Usage Guardian of the mempool not Technically optional / not four gates settled / not validate-no-apply bundled 正式三事（490 余量）/ not 689 chktxguardusage-notoptional interchangeable / not 490 chktxguardusage-vs-optional bundled interchangeable」，不是 CheckTx Usage Guardian 正式三事 bundled（490），也不是 CheckTx 技术上可选（373）或 validate-no-apply（486）。不要另写怎样写内存池守卫、怎样挑邻居。

## 官方三件事

规范把 CheckTx Usage 里 Guardian of the mempool 和「已经 Technically optional - not involved in processing blocks（373） interchangeable / 已经可以不跑 CheckTx / 已经四门已经结算（33） interchangeable / 已经 CheckTx Usage validate-no-apply（486） bundled 第三件事 interchangeable」分开写成三件独立的实现事，不是「看见 Guardian 就已经 optional interchangeable / 就已经四门已经结算 interchangeable / 就已经 validate-no-apply bundled interchangeable」一件事：

1. **看见 Guardian of the mempool / 看见内存池守卫 / Guardian is not already 已经 Technically optional - not involved in processing blocks（373） interchangeable / 373 checktxopt interchangeable / 已经可以不跑 CheckTx interchangeable，也不是已经 CheckTx Usage Guardian 正式三事 bundled（490） interchangeable / 689 chktxguardusage-notoptional interchangeable / 690 chktxguardusage-notgates interchangeable / 490 chktxguardusage item 2 every node interchangeable，也不是已经 Guardian of the mempool not Technically optional / not four gates settled / not validate-no-apply bundled 正式三事 bundled（490 item 1 余量） interchangeable / 490 chktxguardusage item 1 interchangeable。**  
   官方 Usage 写：Guardian of the mempool。看见 Guardian，不是已经 Technically optional 那种 optional 就等于可以不跑 interchangeable——373 钉 optional vs block processing，本页从 490 item 1 侧钉 not optional 单句。490 chktxguardusage vs optional bundled unbundling 在本页 item 1 启动。

2. **看见 Guardian of the mempool / 看见内存池守卫 / 看见 Usage 这句 is not already 已经可以不跑 CheckTx / 已经四门已经结算（33） interchangeable / 33 four gates interchangeable / 已经 Check 通过就是已进提案 interchangeable，也不是已经 CheckTx Usage Guardian 正式三事 bundled（490） interchangeable / 689 chktxguardusage-notoptional interchangeable / 490 chktxguardusage item 3 before letting interchangeable / 691 chktxguardusage-notsource interchangeable。**  
   官方把 Usage Guardian 单句和四门结算路径分开——490 bundled 第一件事常与 33 混成「看见内存池守卫 就已经四门已经结算 interchangeable」，本页钉 not four gates settled 单句。看见 Guardian，不是已经 Check 通过就是已进提案 interchangeable——33 钉四门，本页钉 Usage Guardian。

3. **看见 Guardian of the mempool / 看见 Usage 这句 / 看见内存池守卫 is not already 已经 CheckTx Usage validate-no-apply（486） bundled 第三件事 interchangeable / 486 chktxvalidate interchangeable / 682 chktxvalidate-notoptional interchangeable / 已经 Technically optional + Code≠0 正式三事 bundled interchangeable，也不是已经 CheckTx Usage Guardian 正式三事 bundled（490） interchangeable / 689 chktxguardusage-notoptional interchangeable / 690 chktxguardusage-notgates interchangeable。**  
   官方把 Usage Guardian 单句和 validate-no-apply bundled 第三件事分开——490 bundled 第一件事常与 486 混成「看见 Guardian 就已经 validate-no-apply bundled interchangeable」，本页钉 not validate-no-apply bundled 单句。看见 Usage 这句，不是已经 486 item 3 interchangeable——486 钉 validate-no-apply 全段，本页钉 Guardian 单句。490 chktxguardusage vs optional bundled unbundling 在本页 item 1 启动。

怎样做内存池守卫、怎样挑邻居、怎样写 CheckTx 重放谓词是规范里的做法，本页不抄。CheckTx Usage Guardian 正式三事 bundled（490）、every node runs CheckTx（490 item 2 余量 / 690）、before letting into local mempool（490 item 3 余量 / 691）、Technically optional（373）、validate-no-apply（486）是另外那套，本页不抄。

## 官方为什么这样拆

- **Guardian not Technically optional ≠ 373 checktxopt interchangeable：** 官方把 Methods Usage Guardian 和 optional 就等于可以不跑路径分开。
- **Guardian not four gates settled ≠ 33 four gates interchangeable：** 官方把 Usage Guardian 单句和四门已经结算路径分开。
- **Guardian not validate-no-apply bundled ≠ 486 / 682 interchangeable：** 官方把 Usage Guardian 单句和 validate-no-apply bundled 第三件事分开；490 chktxguardusage vs optional bundled unbundling 在本页 item 1 启动。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| Guardian of the mempool | 不是 Technically optional（373） | 不是 every node runs CheckTx（690/490 item 2） |
| 看见内存池守卫 | 不是四门已经结算（33） | 不是 CheckTx 守卫余量（405） |
| 看见 Usage 这句 | 不是 validate-no-apply bundled（486） | 不是 before letting in（691/490 item 3） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 CheckTx Usage Guardian of the mempool not Technically optional / not four gates settled / not validate-no-apply bundled 正式三事（490 余量），必须分开 Guardian 是不是 optional interchangeable / 373、是不是四门已经结算 interchangeable / 33、是不是 validate-no-apply bundled interchangeable / 486。可以跳过「看见每条节点先跑 CheckTx 就已经是 optional」。不要另写怎样写内存池守卫。490 chktxguardusage vs optional bundled unbundling 在本页 item 1 启动；续 [`worked-example-chktxguardusage-notgates-vs-bundled.md`](worked-example-chktxguardusage-notgates-vs-bundled.md)（不变量 690 item 2）。

## 本页不抄

- 怎样做内存池守卫、怎样挑邻居、怎样写 CheckTx 重放谓词。
- CheckTx Usage Guardian 正式三事 bundled。那是不变量 490。
- every node runs CheckTx before letting into local mempool。那是不变量 490 item 2 余量 / 690。
- before letting into its local mempool。那是不变量 490 item 3 余量 / 691。
- CheckTx 技术上可选。那是不变量 373。
- CheckTx Usage validate-no-apply。那是不变量 486。
