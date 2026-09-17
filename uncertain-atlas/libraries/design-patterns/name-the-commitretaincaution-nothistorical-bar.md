# 模式：把 Commit Usage Historical blocks required not persist signal bundled / not default 0 is pruning / not required means persist already done 正式三事（491 余量）说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) Commit Usage。  
**例**：[Historical blocks required not persist signal ≠ bundled（491）](../../tracks/implementation/worked-example-commitretaincaution-nothistorical-vs-bundled.md)。

## 三个名字

1. **Historical blocks required for auditing / replay / light client 不是 persist signal bundled：** 看见 caution 段里的 other purposes，不是已经 481 bundled 第三件事 interchangeable，不是 694 commitretaincaution-nothistorical interchangeable。
2. **看见 may also be required 不是默认 0 就等于已经在剪：** 看见 other purposes，不是已经 366 retain interchangeable。
3. **看见 Usage 这句 不是 required 就代表 persist 已经交差：** 看见 Historical blocks required，不是已经 persist signal 交差 interchangeable。

官方把 Commit Usage other purposes、persist signal Historical blocks、默认 0 就等于已经在剪、required 就代表 persist 交差写成三个名字。把它们叫成一个「看见 caution 段落就已经 persist signal 交差」，会把 not persist signal bundled、not default 0 is pruning、not required means persist already done 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Commit Usage Historical blocks required 正式三事（491 余量），先数清问的是 Historical blocks required 是不是 persist signal bundled / 481、是不是默认 0 就等于已经在剪 / 366、还是看见 Usage 是不是 required 就代表 persist 已经交差，再决定要不要同一次发布。491 commitretaincaution vs kept bundled unbundling 在本页 item 3 完成。
