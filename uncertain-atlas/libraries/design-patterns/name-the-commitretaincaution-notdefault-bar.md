# 模式：把 Commit Usage Use retain_height with caution not defaults to 0 retain all / not blocks below may be removed / not persist signal bundled 正式三事（491 余量）说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) Commit Usage。  
**例**：[caution not defaults to 0 ≠ bundled（491）](../../tracks/implementation/worked-example-commitretaincaution-notdefault-vs-bundled.md)。

## 三个名字

1. **Use retain_height with caution 不是 retain_height 默认 0 就等于已经在剪：** 看见 Methods Usage caution 语气，不是已经 default 0 retain all interchangeable，不是 366 retain interchangeable / 692 commitretaincaution-notdefault interchangeable。
2. **看见要慎用 retain_height 不是回了高度就等于已经在剪：** 看见 caution，不是已经 blocks below may be removed interchangeable。
3. **看见 Usage 这句 不是 persist signal bundled：** 看见 caution 单句，不是已经 481 bundled 第三件事 interchangeable，不是 481 commitpersist interchangeable。

官方把 Commit Usage caution、默认全留、回了高度就等于已经在剪、persist signal bundled 写成三个名字。把它们叫成一个「看见 caution 段落就已经在剪」，会把 not default 0、not blocks below may be removed、not persist signal bundled 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Commit Usage caution 正式三事（491 余量），先数清问的是 caution 是不是默认 0 就等于已经在剪 / 366、是不是回了高度就等于已经在剪、还是看见 Usage 是不是 persist signal bundled / 481，再决定要不要同一次发布。491 commitretaincaution vs kept bundled unbundling 在本页 item 1 启动。
