# 反模式：把 Commit Usage persist-context Historical blocks required not default 0 is pruning / not all-nodes-remove only statesync / not caution Historical blocks bundled 正式三事（481 余量） 说成已经默认 0 就等于已经在剪 / 已经只有 state sync / 已经 caution Historical blocks bundled

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[persist-context ≠ bundled（481）](../../tracks/implementation/worked-example-commitpersist-nothistorical-vs-bundled.md)。

## 卖法

把 Commit Usage persist signal 这句写成已经已经默认 0 就等于已经在剪 / 已经只有 state sync / 已经 caution Historical blocks bundled interchangeable，或已经和 481 commitpersist-vs-finalize bundled / commitpersist-nothistorical-sold-as-bundled interchangeable。

## 为什么错

官方把 Commit Usage persist signal 三条核心句写成三件独立的实现事。把它们卖成已经默认 0 就等于已经在剪 / 已经只有 state sync / 已经 caution Historical blocks bundled，会把三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Commit Usage persist Historical blocks 正式三事（481 余量），必须分开 not default 0 is pruning、not all-nodes-remove only statesync、not caution Historical blocks bundled 三件事，不要和 481 / 366 / 491 / 694 / 701 / 702 糊成一句。

## 和相邻反模式

- [commitpersist-sold-as-finalize](commitpersist-sold-as-finalize.md) 是 Commit Usage persist signal bundled（481），不是本页 item 3 单句边界。
- [commitretaincaution-nothistorical-sold-as-bundled](commitretaincaution-nothistorical-sold-as-bundled.md) 是 caution 段 Historical blocks（694），不是本页 persist 语境边界。
