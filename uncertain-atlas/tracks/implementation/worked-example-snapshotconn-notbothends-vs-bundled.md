# 例：看见用来给人快照 / 看见用来给自己装回 / 看见写了「和 / 或」 is not already already both-ends interchangeable / already restored interchangeable / already and-or-done interchangeable

**层次**：实现 / 给人快照或给自己装回不是已经必须两头都做 not already both-ends / not already restored / not already and-or-done 正式三事（334 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Snapshot Connection。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「给人快照或给自己装回不是已经必须两头都做 not already both-ends / not already restored / not already and-or-done 正式三事（334 余量）/ not 759 snapshotconn-notbothends interchangeable / not 334 snapshotconn bundled interchangeable」，不是 Snapshot Connection bundled（334），也不是四门里有 Snapshot Connection 不是已经必须实现快照（758 item 1 余量）或应用选择不实现不是已经没有 state sync 这条对象（760 item 3 余量）。不要另写怎样实现快照方法或怎样配 state sync。

## 官方三件事

规范把 Requirements 里 Snapshot Connection 用来给人快照和 / 或给自己装回 和「已经是用来给人快照就必须两头都做 interchangeable / 已经是用来给自己装回就已经装完 interchangeable / 已经是写了和或就已经两头都做了 interchangeable / 已经是 snapshotconn bundled interchangeable」分开写成三件独立的实现事，不是「看见给人快照或给自己装回就已经必须两头都做 interchangeable / 就已经装完 interchangeable / 就已经两头都做了 interchangeable」一件事：

1. **看见这条连接用来给人快照 / 看见能给人 / 看见给人快照 is not already 已经必须两头都做 interchangeable / 已经 both-ends interchangeable / 已经必须给自己装交差 interchangeable / 334 snapshotconn bundled interchangeable / 33 four gates interchangeable / snapshotconn-sold-as-required interchangeable，也不是已经 Snapshot Connection bundled（334） interchangeable / 759 snapshotconn-notbothends interchangeable / 334 snapshotconn item 2 interchangeable，也不是已经给人快照或给自己装回不是已经必须两头都做 not already both-ends / not already restored / not already and-or-done 正式三事 bundled（334 item 2 余量） interchangeable / 334 snapshotconn item 2 interchangeable，也不是已经四门里有 Snapshot Connection 不是已经必须实现（758） interchangeable / 760 snapshotconn-notgone interchangeable / 321 snapshotrestore interchangeable，也不是已经四门已经结算（33） interchangeable。**  
   官方写：Snapshot Connection 用来给别的节点提供 state sync 快照，**和 / 或** 给正在引导的本节点装回。看见能给人，不是已经必须给自己装。看见用来给人快照，不是已经 both-ends interchangeable——334 钉 bundled 三事，本页从 item 2 侧钉 not already both-ends 单句。看见给人快照，不是已经 Snapshot Connection bundled（334） interchangeable——334 钉 bundled，本页钉 item 2 第一件事。看见能给人，不是已经 Offer 收下已经装完（321） interchangeable——321 另钉。334 snapshotconn vs required bundled unbundling 在本页 item 2 续。

2. **看见这条连接用来给自己装回 / 看见能装回 / 看见装回口 is not already 已经装完 interchangeable / 已经 restored interchangeable / 已经装回交差 interchangeable / 334 snapshotconn bundled interchangeable / 321 snapshotrestore interchangeable，也不是已经 Snapshot Connection bundled（334） interchangeable / 759 snapshotconn-notbothends interchangeable / 334 snapshotconn item 1 必须实现 interchangeable / 334 snapshotconn item 3 可选 interchangeable，也不是已经给人快照或给自己装回不是已经必须两头都做 not already both-ends / not already restored / not already and-or-done 正式三事 bundled（334 item 2 余量） interchangeable / 334 snapshotconn item 2 interchangeable，也不是已经必须两头都做（本页第一件事） interchangeable。**  
   官方写：看见能装回，不是已经必须对外提供。看见用来给自己装回，不是已经 restored interchangeable——本页钉 not already restored 单句（不是已经装完）。看见装回口，不是已经必须两头都做（本页第一件事） interchangeable——三件事分开钉。334 snapshotconn vs required bundled unbundling 在本页 item 2 续。

3. **看见写了「和 / 或」 / 看见和或写法 / 看见两头写法 is not already 已经两头都做了 interchangeable / 已经 and-or-done interchangeable / 已经和或交差 interchangeable / 334 snapshotconn bundled interchangeable / 321 snapshotrestore interchangeable，也不是已经 Snapshot Connection bundled（334） interchangeable / 759 snapshotconn-notbothends interchangeable / 334 snapshotconn item 1 / 334 snapshotconn item 3，也不是已经给人快照或给自己装回不是已经必须两头都做 not already both-ends / not already restored / not already and-or-done 正式三事 bundled（334 item 2 余量） interchangeable / 334 snapshotconn item 2 interchangeable，也不是已经必须两头都做（本页第一件事） interchangeable / 已经装完（本页第二件事） interchangeable。**  
   官方写：看见写了「和 / 或」，不是已经两头都做了。看见和或写法，不是已经 and-or-done interchangeable——本页钉 not already and-or-done 单句。看见两头写法，不是已经必须两头都做（本页第一件事） interchangeable——三件事分开钉。334 snapshotconn vs required bundled unbundling 在本页 item 2 续。

怎样实现 `ListSnapshots` / `OfferSnapshot` / `LoadSnapshotChunk` / `ApplySnapshotChunk`、怎样配 state sync 是规范里的做法，本页不抄。Snapshot Connection bundled（334）、四门里有 Snapshot Connection 不是已经必须实现快照（334 item 1 余量 / 758）、应用选择不实现不是已经没有 state sync 这条对象（334 item 3 余量 / 760）、Offer 收下已经装完（321）、四门已经结算（33）是另外那套，本页不抄。

## 官方为什么这样拆

- **用来给人快照 not already both-ends ≠ 334 / 33 interchangeable：** 官方把「和 / 或」写成可以只做一头。
- **用来给自己装回 not already restored ≠ 已经装完 interchangeable：** 官方把能装回和已经装完分开。
- **写了「和 / 或」 not already and-or-done ≠ 已经两头都做了 interchangeable：** 官方把和或写法和已经两头都做了分开；334 snapshotconn vs required bundled unbundling 在本页 item 2 续。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 用来给人快照 | 不是 already both-ends | 不是门在必须实现 alone（758） |
| 用来给自己装回 | 不是 already restored | 不是 Offer 收下已经装完 alone（321） |
| 写了「和 / 或」 | 不是 already and-or-done | 不是可选就没有对象 alone（760） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看给人快照或给自己装回不是已经必须两头都做 not already both-ends / not already restored / not already and-or-done 正式三事（334 余量），必须分开用来给人快照 是不是 already both-ends interchangeable / 334 snapshotconn bundled interchangeable / snapshotconn-sold-as-required interchangeable、用来给自己装回 是不是 already restored interchangeable、写了「和 / 或」 是不是 already and-or-done interchangeable。可以跳过「看见给人快照或给自己装回就已经必须两头都做 interchangeable / 就已经装完 interchangeable / 就已经两头都做了 interchangeable」。不要另写怎样实现快照方法。334 snapshotconn vs required bundled unbundling 在本页 item 2 续（758 + 759）；续 [`worked-example-snapshotconn-notgone-vs-bundled.md`](worked-example-snapshotconn-notgone-vs-bundled.md)（不变量 760 item 3）已写；完成见 760。

## 本页不抄

- 怎样实现 `ListSnapshots` / `OfferSnapshot` / `LoadSnapshotChunk` / `ApplySnapshotChunk`、怎样配 state sync。
- Snapshot Connection bundled。那是不变量 334。
- 四门里有 Snapshot Connection 不是已经必须实现快照。那是不变量 334 item 1 余量 / 758。
- 应用选择不实现不是已经没有 state sync 这条对象。那是不变量 334 item 3 余量 / 760。
- Offer 收下已经装完。那是不变量 321。
- 四门已经结算。那是不变量 33。
