# 模式：把 CheckTx Usage Guardian of the mempool not Technically optional / not four gates settled / not validate-no-apply bundled 正式三事（490 余量）说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) CheckTx Usage。  
**例**：[Guardian not Technically optional ≠ bundled（490）](../../tracks/implementation/worked-example-chktxguardusage-notoptional-vs-bundled.md)。

## 三个名字

1. **Guardian of the mempool 不是 Technically optional：** 看见 Methods Usage 内存池守卫，不是已经 optional 就等于可以不跑 interchangeable，不是 373 checktxopt interchangeable / 689 chktxguardusage-notoptional interchangeable。
2. **看见内存池守卫 不是四门已经结算：** 看见 Guardian，不是已经 Check 通过就是已进提案 interchangeable，不是 33 four gates interchangeable。
3. **看见 Usage 这句 不是 validate-no-apply bundled：** 看见 Guardian 单句，不是已经 486 bundled 第三件事 interchangeable，不是 682 chktxvalidate-notoptional interchangeable。

官方把 CheckTx Usage Guardian、optional、四门结算、validate-no-apply bundled 写成三个名字。把它们叫成一个「看见每条节点先跑 CheckTx 就已经是 optional」，会把 not optional、not four gates settled、not validate-no-apply bundled 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 CheckTx Usage Guardian 正式三事（490 余量），先数清问的是 Guardian 是不是 optional / 373、是不是四门已经结算 / 33、还是看见 Usage 是不是 validate-no-apply bundled / 486，再决定要不要同一次发布。490 chktxguardusage vs optional bundled unbundling 在本页 item 1 启动。
