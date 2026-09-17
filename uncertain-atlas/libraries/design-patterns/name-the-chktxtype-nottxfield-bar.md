# 模式：把 CheckTx Request type field not tx field tells New vs Recheck / not Commit then recheck needs no type / not CheckTx request rest bundled 正式三事（484 余量） 说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) CheckTx Request `type`。  
**例**：[type ≠ bundled（484）](../../tracks/implementation/worked-example-chktxtype-nottxfield-vs-bundled.md)。

## 三个名字

1. **Request type 栏 不是 tx 栏就知道种类：** 看见 Type 标明，不是已经 391 interchangeable / 709 chktxtype-nottxfield interchangeable。
2. **看见 Type 标明 不是 Commit 后再验不需要读 type：** 看见 type 栏，不是已经 312 / 468 interchangeable。
3. **看见 Usage 这句 不是请求余栏 bundled：** 看见 type 栏单句，不是已经 391 bundled interchangeable。

官方把 CheckTx Request type 三条核心句拆成三个名字。把它们叫成一个「看见填了 CheckTx 请求就已经是 Recheck」，会把三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 CheckTx Request type 栏 正式三事（484 余量），先数清问的是 type 栏是不是 tx 栏就知道种类 / 391、是不是 Commit 后再验不需要读 type / 312 / 468、还是看见 Usage 是不是请求余栏 bundled，再决定要不要同一次发布。484 chktxtype vs recheck bundled unbundling 在本页 item 3 完成。
