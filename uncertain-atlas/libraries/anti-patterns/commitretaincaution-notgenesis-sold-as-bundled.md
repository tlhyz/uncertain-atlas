# 反模式：把 Commit Usage all nodes remove historical blocks not bootstrap from genesis / not non-zero retain is pruning / not entered consensus has full history 正式三事（491 余量）说成已经能从创世再装 / 已经非零高度就等于已经在剪 / 已经切进共识就有完整历史

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[all nodes remove not genesis bootstrap ≠ bundled（491）](../../tracks/implementation/worked-example-commitretaincaution-notgenesis-vs-bundled.md)。

## 卖法

把 If all nodes in the network remove historical blocks / permanently lost / unless state sync 写成已经能从创世再装 interchangeable / 366 / 323 / 38 interchangeable；把看见 permanently lost 写成已经 retain_height 回了非零高度就等于已经在剪 interchangeable；把看见 unless state sync 写成已经切进共识就已经有完整历史 interchangeable / 323 snaptransition interchangeable，或已经和 491 commitretaincaution-vs-kept bundled / commitretaincaution-notgenesis-sold-as-bundled interchangeable / 693 commitretaincaution-notgenesis interchangeable。

## 为什么错

官方把 Commit Usage 全网后果、从创世再装、非零高度就等于已经在剪、切进共识就有完整历史写成三件独立的实现事。把它们卖成 genesis bootstrap interchangeable / non-zero retain is pruning interchangeable / entered consensus has full history interchangeable，会把 not genesis bootstrap、not non-zero retain is pruning、not entered consensus has full history 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Commit Usage all nodes remove 正式三事（491 余量），必须分开 not genesis bootstrap、not non-zero retain is pruning、not entered consensus has full history 三件事，不要和 491 / 366 / 323 / 38 / 692 / 694 糊成一句。

## 和相邻反模式

- [commitretaincaution-sold-as-pruning](commitretaincaution-sold-as-pruning.md) 是 Commit Usage retain_height caution bundled（491），不是本页 item 2 单句边界。
- [commitretaincaution-notdefault-sold-as-bundled](commitretaincaution-notdefault-sold-as-bundled.md) 是 caution 单句边界（692 item 1），不是本页 all nodes 边界。
