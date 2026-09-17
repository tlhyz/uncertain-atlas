# 反模式：把 Commit Usage Use retain_height with caution not defaults to 0 retain all / not blocks below may be removed / not persist signal bundled 正式三事（491 余量）说成已经默认 0 就等于已经在剪 / 已经回了高度就等于已经在剪 / 已经 persist signal bundled

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[caution not defaults to 0 ≠ bundled（491）](../../tracks/implementation/worked-example-commitretaincaution-notdefault-vs-bundled.md)。

## 卖法

把 Use `CommitResponse.retain_height` with caution / 要慎用 retain_height 写成已经 retain_height defaults to 0 (retain all) interchangeable / 366 retain interchangeable / 已经没填就等于已经在剪 interchangeable；把看见要慎用 retain_height 写成已经 blocks below this height may be removed 那种回了高度就等于已经在剪 interchangeable；把看见 Usage 这句写成已经 persist signal bundled 第三件事 interchangeable / 481 commitpersist interchangeable，或已经和 491 commitretaincaution-vs-kept bundled / commitretaincaution-notdefault-sold-as-bundled interchangeable / 692 commitretaincaution-notdefault interchangeable。

## 为什么错

官方把 Commit Usage caution、默认全留、回了高度就等于已经在剪、persist signal bundled 写成三件独立的实现事。把它们卖成 default 0 interchangeable / blocks below may be removed interchangeable / persist signal bundled interchangeable，会把 not default 0、not blocks below may be removed、not persist signal bundled 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Commit Usage caution 正式三事（491 余量），必须分开 not default 0、not blocks below may be removed、not persist signal bundled 三件事，不要和 491 / 366 / 481 / 693 / 694 糊成一句。

## 和相邻反模式

- [commitretaincaution-sold-as-pruning](commitretaincaution-sold-as-pruning.md) 是 Commit Usage retain_height caution bundled（491），不是本页 item 1 单句边界。
- [commitretaincaution-notgenesis-sold-as-bundled](commitretaincaution-notgenesis-sold-as-bundled.md) 是 all nodes remove 单句边界（693 item 2），不是本页 caution 边界。
