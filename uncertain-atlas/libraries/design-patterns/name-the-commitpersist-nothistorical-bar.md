# 模式：把 Commit Usage persist-context Historical blocks required not default 0 is pruning / not all-nodes-remove only statesync / not caution Historical blocks bundled 正式三事（481 余量） 说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) Commit Usage。  
**例**：[persist-context ≠ bundled（481）](../../tracks/implementation/worked-example-commitpersist-nothistorical-vs-bundled.md)。

## 三个名字

1. **persist Historical blocks 不是默认 0 就等于已经在剪：** 看见 persist 语境 other purposes，不是已经 366 interchangeable / 703 commitpersist-nothistorical interchangeable。
2. **看见 may also be required 不是全网删了就只有 state sync：** 看见 persist other purposes，不是已经能剪就等于没有历史 interchangeable。
3. **看见 Usage 这句 不是 caution Historical blocks bundled：** 看见 persist Historical blocks，不是已经 491 / 694 interchangeable。

官方把 Commit Usage persist signal 三条核心句拆成三个名字。把它们叫成一个「看见叫了 Commit 就已经落盘」，会把三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Commit Usage persist Historical blocks 正式三事（481 余量），先数清问的是 persist 语境 Historical blocks 是不是默认 0 就等于已经在剪 / 366、是不是全网删了就只有 state sync、还是看见 Usage 是不是 caution Historical blocks bundled / 491 / 694，再决定要不要同一次发布。481 commitpersist vs finalize bundled unbundling 在本页 item 3 完成。
