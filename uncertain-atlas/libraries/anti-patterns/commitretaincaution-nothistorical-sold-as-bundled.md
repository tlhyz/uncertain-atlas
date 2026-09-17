# 反模式：把 Commit Usage Historical blocks required not persist signal bundled / not default 0 is pruning / not required means persist already done 正式三事（491 余量）说成已经 persist signal bundled / 已经默认 0 就等于已经在剪 / 已经 required 就代表 persist 交差

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[Historical blocks required not persist signal ≠ bundled（491）](../../tracks/implementation/worked-example-commitretaincaution-nothistorical-vs-bundled.md)。

## 卖法

把 Historical blocks may also be required for auditing / replay / light client verification 写成已经 persist signal bundled 第三件事 interchangeable / 481 commitpersist interchangeable；把看见 may also be required 写成已经 retain_height 默认 0 就等于已经在剪 interchangeable / 366 retain interchangeable；把看见 Usage 这句写成已经 Historical blocks required 就代表 persist signal 已经交差 interchangeable，或已经和 491 commitretaincaution-vs-kept bundled / commitretaincaution-nothistorical-sold-as-bundled interchangeable / 694 commitretaincaution-nothistorical interchangeable。

## 为什么错

官方把 Commit Usage other purposes、persist signal Historical blocks、默认 0 就等于已经在剪、required 就代表 persist 交差写成三件独立的实现事。把它们卖成 persist signal bundled interchangeable / default 0 is pruning interchangeable / required means persist already done interchangeable，会把 not persist signal bundled、not default 0 is pruning、not required means persist already done 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Commit Usage Historical blocks required 正式三事（491 余量），必须分开 not persist signal bundled、not default 0 is pruning、not required means persist already done 三件事，不要和 491 / 481 / 366 / 692 / 693 糊成一句。

## 和相邻反模式

- [commitretaincaution-sold-as-pruning](commitretaincaution-sold-as-pruning.md) 是 Commit Usage retain_height caution bundled（491），不是本页 item 3 单句边界。
- [commitretaincaution-notgenesis-sold-as-bundled](commitretaincaution-notgenesis-sold-as-bundled.md) 是 all nodes remove 单句边界（693 item 2），不是本页 Historical blocks 边界。
