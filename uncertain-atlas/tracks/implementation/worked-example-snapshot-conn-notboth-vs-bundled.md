# 例：看见给人快照或给自己装回 is not already must-do-both interchangeable / not already restored interchangeable / not already settled interchangeable

**层次**：实现 / 给人快照或给自己装回 not already must-do-both / not already restored / not already settled 正式三事（334 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Snapshot Connection。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5。本页是「给人快照或给自己装回 not already must-do-both / not already restored / not already settled 正式三事（334 余量）/ not 933 snapshot-conn-notboth interchangeable / not 334 snapshot-conn-vs-required bundled interchangeable」，不是快照连接 bundled（334），也不是 Offer 收下已经装完（321），也不是只有 AppHash 可信任（38）。不要另写怎样实现快照方法或怎样配 state sync。

## 官方三件事

1. **看见这条连接用来给人快照 / 看见这条连接用来给自己装回 这份用法 is not already 已经必须两头都做 interchangeable，也不是已经快照连接 bundled（334） interchangeable / 933 snapshot-conn-notboth interchangeable / 932 snapshot-conn-notmust interchangeable / 334 snapshot-conn item 1 四门 interchangeable，也不是已经给人快照或给自己装回 not already must-do-both / not already restored / not already settled 正式三事 bundled（334 item 2 余量） interchangeable / 334 snapshot-conn item 2 interchangeable。**  
   官方写：Snapshot Connection 用来给别的节点提供 state sync 快照，和 / 或 给正在引导的本节点装回。看见能给人，不是已经必须给自己装 interchangeable——本页从 334 item 2 侧钉 not already must-do-both 单句。334 snapshot-conn vs required bundled unbundling 在本页 item 2 续。

2. **看见能装回 / 看见写了「和 / 或」 / 这份用法 is not already 已经装完 interchangeable，也不是已经快照连接 bundled（334） interchangeable / 933 snapshot-conn-notboth interchangeable / 334 snapshot-conn item 3 选择不实现 interchangeable / 934 snapshot-conn-notgone interchangeable，也不是已经 Offer 收下已经装完 interchangeable / 321 offersnap interchangeable。**  
   官方把能装回和已经必须对外提供 / 已经装完分开——334 bundled 第二件事常与 321 混成「看见给人快照就已经必须两头都做或已经装完 interchangeable」，本页钉 not already restored 单句。

3. **看见写了「和 / 或」 / 看见能给人 / 这份用法 is not already 已经交差 interchangeable，也不是已经快照连接 bundled（334） interchangeable / 933 snapshot-conn-notboth interchangeable / 932 snapshot-conn-notmust interchangeable，也不是已经只有 AppHash 可信任 interchangeable / 38 apphash-trust interchangeable。**  
   官方把写了「和 / 或」和已经两头都做了 / 已经交差分开。看见写了「和 / 或」，不是已经交差 interchangeable。334 snapshot-conn vs required bundled unbundling 在本页 item 2 续。

怎样实现 ListSnapshots / OfferSnapshot / LoadSnapshotChunk / ApplySnapshotChunk、怎样配 state sync 是规范里的做法，本页不抄。

## 官方为什么这样拆

- **给人快照或给自己装回 not already must-do-both ≠ 已经必须两头都做 interchangeable：** 官方把「和 / 或」写成可以只做一头。
- **看见能装回 not already restored ≠ 已经装完 interchangeable：** 官方把能装回和已经必须对外提供 / 已经装完分开。
- **看见写了「和 / 或」 not already settled ≠ 已经交差 interchangeable：** 官方把写了「和 / 或」和已经交差分开；334 snapshot-conn vs required bundled unbundling 在本页 item 2 续。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 给人快照或给自己装回 | 不是已经必须两头都做 | 不是 Offer 收下已经装完（321） |
| 看见能装回 | 不是已经装完 | 不是只有 AppHash 可信任（38） |
| 看见写了「和 / 或」 | 不是已经交差 | 不是四门就已经必须实现（932） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看给人快照或给自己装回 not already must-do-both / not already restored / not already settled 正式三事（334 余量），必须分开是不是已经必须两头都做、是不是已经装完、是不是已经交差。可以跳过「看见能给人就已经必须两头都做」。不要另写怎样实现快照方法或怎样配 state sync。334 snapshot-conn vs required bundled unbundling 在本页 item 2 续；续 [`worked-example-snapshot-conn-notgone-vs-bundled.md`](worked-example-snapshot-conn-notgone-vs-bundled.md)（不变量 934 item 3）。

## 本页不抄

- 怎样实现 ListSnapshots / OfferSnapshot / LoadSnapshotChunk / ApplySnapshotChunk、怎样配 state sync。
- 快照连接 bundled。那是不变量 334。
- 四门就已经必须实现。那是不变量 334 item 1 余量 / 932。
- Offer 收下已经装完。那是不变量 321。
- 只有 AppHash 可信任。那是不变量 38。
