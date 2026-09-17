# 反模式：把 CheckTx Usage Technically optional + Code≠0 rejected not four gates settled / not Check passed is in proposal / not forever valid 正式三事（486 余量）说成已经四门已经结算 / 已经进提案 / 已经 forever valid

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[Technically optional + Code≠0 not four gates settled ≠ bundled（486）](../../tracks/implementation/worked-example-chktxvalidate-notoptional-vs-bundled.md)。

## 卖法

把 Technically optional - not involved in processing blocks / Guardian of the mempool 写成已经可以不跑 CheckTx interchangeable / 373 checktx-optional interchangeable / 已经四门已经结算 interchangeable；把 Code≠0 will be rejected / will not be included in a proposal block 写成已经 Check 通过就是已进提案 interchangeable / 33 four gates interchangeable / 489 chktxcodereject interchangeable；把 no other value to the response code 写成已经 CheckTx 过了就永远有效 interchangeable / 301 proposed-vs-removed interchangeable / 405 checktxguard interchangeable，或已经和 486 chktxvalidate-vs-apply bundled / chktxvalidate-notoptional-sold-as-bundled interchangeable / 682 chktxvalidate-notoptional interchangeable。

## 为什么错

官方把 CheckTx Usage optional+Code、四门结算、Check 通过就是已进提案、forever valid 写成三件独立的实现事。把它们卖成 four gates settled interchangeable / Check passed is in proposal interchangeable / forever valid interchangeable，会把 not four gates settled、not Check passed is in proposal、not forever valid 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 CheckTx Usage Technically optional + Code≠0 正式三事（486 余量），必须分开 not four gates settled、not Check passed is in proposal、not forever valid 三件事，不要和 486 / 373 / 33 / 301 / 405 / 489 / 490 / 680 / 681 糊成一句。

## 和相邻反模式

- [chktxvalidate-sold-as-applied](chktxvalidate-sold-as-applied.md) 是 CheckTx Usage validate-no-apply bundled（486），不是本页 item 3 单句边界。
- [chktxvalidate-notexecstate-sold-as-bundled](chktxvalidate-notexecstate-sold-as-bundled.md) 是 validates against current state 单句边界（680 item 1），不是本页 optional+Code 边界。
