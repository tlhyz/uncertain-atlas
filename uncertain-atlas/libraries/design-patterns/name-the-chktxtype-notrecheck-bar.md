# 模式：把 CheckTx Request type CheckTx_New default full check not CheckTx_Recheck / not tx field means Recheck / not CheckTx forever valid 正式三事（484 余量） 说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) CheckTx Request `type`。  
**例**：[type ≠ bundled（484）](../../tracks/implementation/worked-example-chktxtype-notrecheck-vs-bundled.md)。

## 三个名字

1. **CheckTx_New 不是 CheckTx_Recheck：** 看见 default full check，不是已经 Recheck interchangeable / 707 chktxtype-notrecheck interchangeable。
2. **看见 New 不是 tx 栏就等于 Recheck：** 看见 type 栏 New，不是已经 391 interchangeable。
3. **看见 Usage 这句 不是 CheckTx 过了就永远有效：** 看见 full check required，不是已经 301 interchangeable。

官方把 CheckTx Request type 三条核心句拆成三个名字。把它们叫成一个「看见填了 CheckTx 请求就已经是 Recheck」，会把三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 CheckTx Request type CheckTx_New 正式三事（484 余量），先数清问的是 New 是不是 Recheck、是不是 tx 栏就等于 Recheck / 391、还是看见 Usage 是不是过了就永远有效 / 301，再决定要不要同一次发布。484 chktxtype vs recheck bundled unbundling 在本页 item 1 启动。
