# 模式：把装完又对上不是已经在装回当中验过 not already incremental-verified / not already in-network / not already consensus-entered 正式三事（332 余量）说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Snapshot Verification。  
**例**：[装完又对上 not already incremental-verified ≠ bundled（332）](../../tracks/implementation/worked-example-snapshotverify-notduringrestore-vs-bundled.md)。

## 三个名字

1. **装完又对上 不是 already incremental-verified：** 看见装完又叫了 Info / LastBlockAppHash 对上轻客户端那份 / 装完又对上，不是已经在装回当中增量验过 interchangeable / 已经装回当中验过交差 interchangeable，不是 332 snapshotverify bundled interchangeable / 33 four gates interchangeable / snapshotverify-sold-as-early interchangeable。

2. **Info 绿了 不是 already in-network：** 看见 Info 绿了 / 进网前核对绿了 / 应用有效确认，不是已经进了网 interchangeable / 已经进网交差 interchangeable，不是 323 snapshotswitch interchangeable / 332 snapshotverify item 2 interchangeable。

3. **高度对上 不是 already consensus-entered：** 看见高度对上 / LastBlockHeight 对上 / 快照高度对上，不是已经切进共识 interchangeable / 已经切进共识交差 interchangeable，不是 323 snapshotswitch interchangeable / 332 snapshotverify item 3 interchangeable。

官方把装完又对上单句、already incremental-verified、already in-network、already consensus-entered 写成三个名字。把它们叫成一个「看见装完又对上就已经在装回当中验过 interchangeable / 就已经进了网 interchangeable / 就已经切进共识 interchangeable」，会把 not already incremental-verified、not already in-network、not already consensus-entered 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看装完又对上不是已经在装回当中验过 not already incremental-verified / not already in-network / not already consensus-entered 正式三事（332 余量），先数清问的是装完又对上 是不是 already incremental-verified / 332 / snapshotverify-sold-as-early，是不是 Info 绿了 是不是 already in-network，还是高度对上 是不是 already consensus-entered，再决定要不要同一次发布。332 snapshotverify vs early bundled unbundling 在本页 item 1 启动。
