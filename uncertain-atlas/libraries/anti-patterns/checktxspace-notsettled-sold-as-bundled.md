# 反模式：把 CheckTx 回包 events 是给索引用的类型键值不是已经交差 not already settled / not already excluded / not already ordered 正式三事（381 余量）说成已经交差 / 已经没进块 / 已经是共识顺序

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[回了事件 not already settled ≠ bundled（381）](../../tracks/implementation/worked-example-checktxspace-notsettled-vs-bundled.md)。

## 卖法

把回了事件 / CheckTx 回包 events 是给索引用的类型键值 / 回了 events 写成已经交差 interchangeable / 已经 settled interchangeable / 已经交差交差 interchangeable / 381 checktxspace bundled interchangeable / checktxspace-sold-as-code interchangeable；把能按账户查 / 能按账户建索引 / 有账户索引 写成已经没进块 interchangeable / 已经 excluded interchangeable / 已经没进块交差 interchangeable；把有类型键值 / 有索引类型键值 / 有 events 类型键值 写成已经是共识顺序 interchangeable / 已经 ordered interchangeable / 已经是共识顺序交差 interchangeable，或已经和 381 checktxspace bundled / checktxspace-sold-as-code interchangeable / 891 checktxspace-notsettled interchangeable。

## 为什么错

官方把回了事件、不是已经没进块、不是已经是共识顺序写成三件独立的实现事。把它们卖成 already settled interchangeable / already excluded interchangeable / already ordered interchangeable，会把 not already settled、not already excluded、not already ordered 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 CheckTx 回包 events 是给索引用的类型键值不是已经交差 not already settled / not already excluded / not already ordered 正式三事（381 余量），必须分开 not already settled、not already excluded、not already ordered 三件事，不要和 381 / 316 / 890 / 373 糊成一句。

## 和相邻反模式

- [checktxspace-sold-as-code](checktxspace-sold-as-code.md) 是 checktxspace bundled 全段，不是本页回了事件 item 2 单句边界。
- [checktxspace-notcode-sold-as-bundled](checktxspace-notcode-sold-as-bundled.md) 是写了空间 not already code（381 item 1），不是本页 not already settled 边界。
- [exectxresult-sold-as-consensus](exectxresult-sold-as-consensus.md) 是结果列表就已经同一顺序（316），不是本页 not already settled 单句。
- [checktxopt-sold-as-block](checktxopt-sold-as-block.md) 是引擎对回包码不再赋予别的含义就已经被引擎用了 Data（373），不是本页 not already excluded 边界。
