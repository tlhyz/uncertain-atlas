# 模式：把 CheckTx Usage Technically optional + Code≠0 rejected not four gates settled / not Check passed is in proposal / not forever valid 正式三事（486 余量）说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) CheckTx Usage。  
**例**：[Technically optional + Code≠0 not four gates settled ≠ bundled（486）](../../tracks/implementation/worked-example-chktxvalidate-notoptional-vs-bundled.md)。

## 三个名字

1. **Technically optional 不是四门已经结算：** 看见 Usage optional / 不参与处理块，不是已经可以不跑 CheckTx / 已经四门已经结算 interchangeable，不是 373 checktx-optional interchangeable / 682 chktxvalidate-notoptional interchangeable。
2. **Code≠0 rejected 不是 Check 通过就是已进提案：** 看见不会广播、不会进提案块，不是已经 Check 通过就是已进提案 interchangeable，不是 33 four gates interchangeable / 489 chktxcodereject interchangeable。
3. **Code 语义 不是 forever valid：** 看见引擎对回包码不再赋予别的含义，不是已经 CheckTx 过了就永远有效 interchangeable，不是 301 proposed-vs-removed interchangeable / 405 checktxguard interchangeable。

官方把 CheckTx Usage optional+Code、四门结算、forever valid 写成三个名字。把它们叫成一个「看见跑了 CheckTx 就已经交差」，会把 not four gates settled、not Check passed is in proposal、not forever valid 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 CheckTx Usage Technically optional + Code≠0 正式三事（486 余量），先数清问的是 optional 是不是四门已经结算 / 373、Code≠0 是不是已进提案 / 33，还是 Code 语义 是不是 forever valid / 301，再决定要不要同一次发布。486 chktxvalidate vs apply bundled unbundling 在本页 item 3 完成。
