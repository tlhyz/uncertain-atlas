# 模式：把装完不是已经有了 ChainID not already has-ChainID / not already can-propose / not already genesis-RPC-checked 正式三事（323 余量）说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Transition to Consensus。  
**例**：[装完 not already has-ChainID ≠ bundled（323）](../../tracks/implementation/worked-example-snapshotswitch-notchainid-vs-bundled.md)。

## 三个名字

1. **装完 不是 already has-ChainID：** 看见快照已经装完 / 状态机已经恢复，不是已经有了 ChainID、参数、集合和头 interchangeable / 已经引导信息交差 interchangeable，不是 323 snapshotswitch bundled interchangeable / 33 four gates interchangeable / snapshotswitch-sold-as-full-history interchangeable。

2. **状态机在 不是 already can-propose：** 看见状态机已经恢复 / 装完之后，不是已经能出块 interchangeable / 已经能当全节点出块 interchangeable，不是 323 snapshotswitch item 3 interchangeable / 727 snapshotswitch-nothistory interchangeable。

3. **有创世文件 不是 already genesis-RPC-checked：** 看见要从创世文件再凑 / 还要轻客户端 RPC，不是已经和轻客户端那份对过 interchangeable / 已经创世与 RPC 対上交差 interchangeable，不是 38 apphash interchangeable / 323 snapshotswitch item 2 interchangeable。

官方把装完单句、already has-ChainID、already can-propose、already genesis-RPC-checked 写成三个名字。把它们叫成一个「看见快照已经装完就已经有了这些 interchangeable / 就已经能出块 interchangeable / 就已经和轻客户端对过 interchangeable」，会把 not already has-ChainID、not already can-propose、not already genesis-RPC-checked 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看装完不是已经有了 ChainID not already has-ChainID / not already can-propose / not already genesis-RPC-checked 正式三事（323 余量），先数清问的是装完 是不是 already has-ChainID / 323 / snapshotswitch-sold-as-full-history，是不是状态机在 是不是 already can-propose，还是有创世文件 是不是 already genesis-RPC-checked，再决定要不要同一次发布。323 snapshotswitch vs history bundled unbundling 在本页 item 1 启动。
