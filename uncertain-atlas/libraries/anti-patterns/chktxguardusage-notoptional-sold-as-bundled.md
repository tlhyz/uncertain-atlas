# 反模式：把 CheckTx Usage Guardian of the mempool not Technically optional / not four gates settled / not validate-no-apply bundled 正式三事（490 余量）说成已经 optional / 已经四门已经结算 / 已经 validate-no-apply bundled

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[Guardian not Technically optional ≠ bundled（490）](../../tracks/implementation/worked-example-chktxguardusage-notoptional-vs-bundled.md)。

## 卖法

把 Guardian of the mempool / 内存池守卫 写成已经 Technically optional interchangeable / 373 checktxopt interchangeable / 已经可以不跑 CheckTx interchangeable；把看见内存池守卫写成已经四门已经结算 interchangeable / 33 four gates interchangeable；把看见 Usage 这句写成已经 validate-no-apply bundled 第三件事 interchangeable / 486 chktxvalidate interchangeable / 682 chktxvalidate-notoptional interchangeable，或已经和 490 chktxguardusage-vs-optional bundled / chktxguardusage-notoptional-sold-as-bundled interchangeable / 689 chktxguardusage-notoptional interchangeable。

## 为什么错

官方把 CheckTx Usage Guardian、optional、四门结算、validate-no-apply bundled 写成三件独立的实现事。把它们卖成 optional interchangeable / four gates settled interchangeable / validate-no-apply bundled interchangeable，会把 not optional、not four gates settled、not validate-no-apply bundled 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 CheckTx Usage Guardian 正式三事（490 余量），必须分开 not optional、not four gates settled、not validate-no-apply bundled 三件事，不要和 490 / 373 / 33 / 486 / 690 / 691 糊成一句。

## 和相邻反模式

- [chktxguardusage-sold-as-fourgates](chktxguardusage-sold-as-fourgates.md) 是 CheckTx Usage Guardian bundled（490），不是本页 item 1 单句边界。
- [chktxguardusage-notgates-sold-as-bundled](chktxguardusage-notgates-sold-as-bundled.md) 是 every node 单句边界（690 item 2），不是本页 Guardian 边界。
