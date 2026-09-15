# 模式：把 CheckTx Usage tx source 正式三事说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) CheckTx Usage。  
**例**：[may come from external user ≠ CheckTx_Recheck](../../tracks/implementation/worked-example-chktxsource-vs-recheck.md)。

## 三个名字

1. **may come from external user 不是 CheckTx_Recheck / tx 栏就知道 New：** 看见 Methods Usage 侧外部用户来源，不是 Request type Recheck 或 tx 栏 bundled interchangeable。
2. **may come from another node 不是已经从池里删掉 / CheckTx 过了就永远有效：** 看见邻居来源，不是 mempool 交接或 forever valid interchangeable。
3. **external user or another node 不是已经保证不重放 / CheckTx 守卫 bundled interchangeable：** 看见 Usage tx source，不是 Replay Protection 或 405 bundled 第二句 interchangeable。

## 为什么要分开叫

官方把 CheckTx Usage 里 may come from external user、may come from another node、external user or another node 和 Request type（484）、Replay Protection（313）、CheckTx 守卫余量（405）写成三个名字。把它们叫成一个「看见送来了就已经是 Recheck、已经从池里删掉、已经保证不重放」，会把外部用户来源、邻居来源、不重放保证三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 CheckTx Usage tx source，先数清问的是 may come from external user 是不是 CheckTx_Recheck、may come from another node 是不是已经从池里删掉 / CheckTx 过了就永远有效、external user or another node 是不是已经保证不重放 / CheckTx 守卫 bundled interchangeable，再决定要不要同一次发布。
