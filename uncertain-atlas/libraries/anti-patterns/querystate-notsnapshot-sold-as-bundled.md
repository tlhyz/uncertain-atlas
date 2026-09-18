# 反模式：把启动对齐不是已经是快照重放 not already snapshot loaded / not already genesis replay / not already Snapshot connection 正式三事（314 余量）说成已经装了快照 / 已经从创世重放 / 已经是 Snapshot 连接

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[对齐 not already snapshot loaded ≠ bundled（314）](../../tracks/implementation/worked-example-querystate-notsnapshot-vs-bundled.md)。

## 卖法

把对齐 / 启动时对齐 / state sync 之后对齐 写成已经装了快照 interchangeable / 已经 snapshot loaded interchangeable / 已经是快照重放 interchangeable / 314 querystate bundled interchangeable / 38 snapshot interchangeable / querystate-sold-as-execute interchangeable；把启动握手 / Info 握手 / 启动对齐握手 写成已经从创世重放 interchangeable / 已经 genesis replay interchangeable；把 Query 门 / Info 或 Query 连接 写成已经是 Snapshot 连接 interchangeable / 已经 Snapshot connection interchangeable，或已经和 314 querystate bundled / querystate-sold-as-execute interchangeable / 703 querystate-notsnapshot interchangeable。

## 为什么错

官方把对齐单句、already snapshot loaded、already genesis replay、already Snapshot connection 写成三件独立的实现事。把它们卖成 already snapshot loaded interchangeable / already genesis replay interchangeable / already Snapshot connection interchangeable，会把 not already snapshot loaded、not already genesis replay、not already Snapshot connection 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看启动对齐不是已经是快照重放 not already snapshot loaded / not already genesis replay / not already Snapshot connection 正式三事（314 余量），必须分开 not already snapshot loaded、not already genesis replay、not already Snapshot connection 三件事，不要和 314 / 38 / 701 / 702 / 310 / 33 糊成一句。

## 和相邻反模式

- [querystate-sold-as-execute](querystate-sold-as-execute.md) 是 QueryState vs ExecuteTxState bundled 全段，不是本页对齐 item 3 单句边界。
- [querystate-notcaughtup-sold-as-bundled](querystate-notcaughtup-sold-as-bundled.md) 是上次 Commit item 2，不是本页快照重放边界。
- [querystate-notexecute-sold-as-bundled](querystate-notexecute-sold-as-bundled.md) 是能查 item 1，不是本页 Query 门是否 Snapshot 连接边界。
