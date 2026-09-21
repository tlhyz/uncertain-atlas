# 模式：把四门里有 Snapshot Connection 不是已经必须实现快照 not already must-implement / not already snapshot-taken / not already conn-name-is-snap 正式三事（334 余量）说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Snapshot Connection。  
**例**：[四门里有 Snapshot Connection not already must-implement ≠ bundled（334）](../../tracks/implementation/worked-example-snapshotconn-notrequired-vs-bundled.md)。

## 三个名字

1. **四门里有 Snapshot Connection 不是 already must-implement：** 看见四门里有 Snapshot Connection / 四条连接 / 门在，不是已经必须实现快照管理 interchangeable / 已经必须实现交差 interchangeable，不是 334 snapshotconn bundled interchangeable / 33 four gates interchangeable / snapshotconn-sold-as-required interchangeable。

2. **四门齐了 不是 already snapshot-taken：** 看见四门齐了 / 四条连接都在 / 连接表齐了，不是已经有快照 interchangeable / 已经拍过快照交差 interchangeable，不是 322 snapshotdiscover interchangeable / 334 snapshotconn item 2 interchangeable。

3. **连接名在 不是 already conn-name-is-snap：** 看见连接名在 / Snapshot Connection 这个名 / 连接名叫快照，不是已经拍过或装过 interchangeable / 已经名即快照交差 interchangeable，不是 321 snapshotrestore interchangeable / 334 snapshotconn item 3 interchangeable。

官方把四门里有 Snapshot Connection 单句、already must-implement、already snapshot-taken、already conn-name-is-snap 写成三个名字。把它们叫成一个「看见四门里有 Snapshot Connection 就已经必须实现快照 interchangeable / 就已经有快照 interchangeable / 就已经拍过或装过 interchangeable」，会把 not already must-implement、not already snapshot-taken、not already conn-name-is-snap 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看四门里有 Snapshot Connection 不是已经必须实现快照 not already must-implement / not already snapshot-taken / not already conn-name-is-snap 正式三事（334 余量），先数清问的是四门里有 Snapshot Connection 是不是 already must-implement / 334 / snapshotconn-sold-as-required，是不是四门齐了 是不是 already snapshot-taken，还是连接名在 是不是 already conn-name-is-snap，再决定要不要同一次发布。334 snapshotconn vs required bundled unbundling 在本页 item 1 启动。
