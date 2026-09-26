# 反模式：把 CheckTx 回包 codespace 是码的命名空间不是已经是回包码 not already code / not already excluded / not already settled 正式三事（381 余量）说成已经是回包码 / 已经没进块 / 已经交差

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[写了空间 not already code ≠ bundled（381）](../../tracks/implementation/worked-example-checktxspace-notcode-vs-bundled.md)。

## 卖法

把写了空间 / CheckTx 回包 codespace 是码的命名空间 / 写了 codespace 写成已经是回包码 interchangeable / 已经 code interchangeable / 已经是回包码交差 interchangeable / 381 checktxspace bundled interchangeable / checktxspace-sold-as-code interchangeable；把有命名空间 / 有 codespace 命名空间 / 有空间名 写成已经没进块 interchangeable / 已经 excluded interchangeable / 已经没进块交差 interchangeable；把能回 / 能回 codespace / 有 codespace 回包 写成已经交差 interchangeable / 已经 settled interchangeable / 已经交差交差 interchangeable，或已经和 381 checktxspace bundled / checktxspace-sold-as-code interchangeable / 890 checktxspace-notcode interchangeable。

## 为什么错

官方把写了空间、不是已经没进块、不是已经交差写成三件独立的实现事。把它们卖成 already code interchangeable / already excluded interchangeable / already settled interchangeable，会把 not already code、not already excluded、not already settled 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 CheckTx 回包 codespace 是码的命名空间不是已经是回包码 not already code / not already excluded / not already settled 正式三事（381 余量），必须分开 not already code、not already excluded、not already settled 三件事，不要和 381 / 373 / 316 / 367 糊成一句。

## 和相邻反模式

- [checktxspace-sold-as-code](checktxspace-sold-as-code.md) 是 checktxspace bundled 全段，不是本页写了空间 item 1 单句边界。
- [checktxopt-sold-as-block](checktxopt-sold-as-block.md) 是引擎对回包码不再赋予别的含义就已经被引擎用了 Data（373），不是本页 not already code 边界。
- [lane-sold-as-priority](lane-sold-as-priority.md) 是没定义 lane_priorities 就已经排了优先（367），不是本页 not already settled 边界。
