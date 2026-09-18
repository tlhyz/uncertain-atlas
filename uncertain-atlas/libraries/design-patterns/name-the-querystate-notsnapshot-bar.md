# 模式：把启动对齐不是已经是快照重放 not already snapshot loaded / not already genesis replay / not already Snapshot connection 正式三事（314 余量）说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Info/Query Connection。  
**例**：[对齐 not already snapshot loaded ≠ bundled（314）](../../tracks/implementation/worked-example-querystate-notsnapshot-vs-bundled.md)。

## 三个名字

1. **对齐 不是 already snapshot loaded：** 看见启动时对齐 / state sync 之后对齐，不是已经装了快照 interchangeable / 已经是快照重放 interchangeable，不是 314 querystate bundled interchangeable / 38 snapshot interchangeable / querystate-sold-as-execute interchangeable。

2. **启动握手 不是 already genesis replay：** 看见 Info 握手 / 启动对齐握手，不是已经从创世重放 interchangeable / 已经创世重放完 interchangeable，不是 314 querystate item 1 interchangeable / 701 querystate-notexecute interchangeable。

3. **Query 门 不是 already Snapshot connection：** 看见 Info 或 Query 连接 / Query 连接用途，不是已经是 Snapshot 连接 interchangeable / 已经快照连接 interchangeable，不是 314 querystate item 2 interchangeable / 702 querystate-notcaughtup interchangeable。

官方把对齐单句、already snapshot loaded、already genesis replay、already Snapshot connection 写成三个名字。把它们叫成一个「看见对齐就已经是快照重放 interchangeable / 就已经从创世重放 interchangeable / 就已经是 Snapshot 连接 interchangeable」，会把 not already snapshot loaded、not already genesis replay、not already Snapshot connection 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看启动对齐不是已经是快照重放 not already snapshot loaded / not already genesis replay / not already Snapshot connection 正式三事（314 余量），先数清问的是对齐 是不是 already snapshot loaded / 314 / 38，是不是启动握手 是不是 already genesis replay，还是 Query 门 是不是 already Snapshot connection，再决定要不要同一次发布。314 querystate vs execute bundled unbundling 在本页 item 3 完成。
