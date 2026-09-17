# 反模式：把 Historical blocks required for auditing replay light client not Use retain_height with caution / not If all nodes remove historical blocks / not Commit Usage persist signal bundled 正式三事（491 余量）说成已经 with caution / 已经 all nodes remove / 已经 persist signal bundled

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[Historical blocks required for auditing replay light client not Commit Usage persist signal bundled ≠ bundled（491）](../../tracks/implementation/worked-example-commitretaincaution-notpersist-vs-bundled.md)。

## 卖法

把 Historical blocks may also be required for other purposes / auditing / replay / light client verification 写成已经 Use retain_height with caution interchangeable / 677 commitretaincaution-notdefaultzero interchangeable / 366 retain-height bundled interchangeable / 335 finpersist interchangeable / 已经 caution 段落就已经在剪 interchangeable；把 may also be required / other purposes 写成已经 If all nodes remove historical blocks interchangeable / 678 commitretaincaution-notbootstrap interchangeable / 323 full-history interchangeable / 38 genesis-replay interchangeable / 已经 permanently lost / no bootstrap unless state sync interchangeable；把 auditing / replay / light client 写成已经 Commit Usage persist signal bundled interchangeable / 481 commitpersist bundled interchangeable / 665 infousage-notcommitpersist interchangeable / 497 infousage-persist interchangeable / 已经 Signal persist application state interchangeable / 已经 persist signal 就代表 caution 已经验完 interchangeable，或已经和 491 commitretaincaution-vs-kept bundled / commitretaincaution-sold-as-pruning interchangeable / 679 commitretaincaution-notpersist interchangeable。

## 为什么错

官方把 Commit Usage other purposes 单句、Use retain_height with caution（677）、If all nodes remove historical blocks（678）、Commit Usage persist signal bundled（481）写成三件独立的实现事。把它们卖成 with caution interchangeable / all nodes remove interchangeable / persist signal bundled interchangeable，会把 not Use retain_height with caution、not If all nodes remove historical blocks、not Commit Usage persist signal bundled 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Historical blocks required for auditing replay light client not Use retain_height with caution / not If all nodes remove historical blocks / not Commit Usage persist signal bundled 正式三事（491 余量），必须分开 not Use retain_height with caution、not If all nodes remove historical blocks、not Commit Usage persist signal bundled 三件事，不要和 491 / 366 / 481 / 677 / 678 / 323 / 38 / 335 / 665 / 497 糊成一句。

## 和相邻反模式

- [commitretaincaution-notbootstrap-sold-as-bundled](commitretaincaution-notbootstrap-sold-as-bundled.md) 是 all nodes remove 段落 vs bootstrap，不是本页 other purposes vs persist signal 边界。
- [commitretaincaution-notdefaultzero-sold-as-bundled](commitretaincaution-notdefaultzero-sold-as-bundled.md) 是 with caution 单句 vs defaults to 0，不是本页 Historical blocks required 边界。
- [commitpersist-sold-as-finalize](commitpersist-sold-as-finalize.md) 是 persist signal 就等于已经在 Finalize 落了，不是本页 caution other purposes vs persist signal bundled 边界。
