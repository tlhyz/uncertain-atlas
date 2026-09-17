# 反模式：把 If all nodes remove historical blocks not retain_height defaults to 0 retain all / not bootstrap from genesis unless state sync / not Historical blocks required for auditing replay light client 正式三事（491 余量）说成已经 retain_height 默认 0 全留 / 已经能从创世再装 / 已经 Historical blocks required

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[If all nodes remove historical blocks not retain_height defaults to 0 retain all ≠ bundled（491）](../../tracks/implementation/worked-example-commitretaincaution-notbootstrap-vs-bundled.md)。

## 卖法

把 If all nodes in the network remove historical blocks / all nodes remove / permanently lost 写成已经 retain_height defaults to 0 retain all interchangeable / 366 retain-height bundled interchangeable / 677 commitretaincaution-notdefaultzero interchangeable / 335 finpersist interchangeable / 已经 default 0 全留 interchangeable；把 no new nodes will be able to join and bootstrap / unless state sync is enabled on the chain 写成已经能从创世再装 interchangeable / 323 full-history interchangeable / 38 genesis-replay interchangeable / 366 retain bundled item 3 interchangeable / 已经 retain_height 回了非零就等于已经在剪 interchangeable / 已经 unless state sync 就等于已经能给轻客户端验 interchangeable；把 all nodes remove 段落 写成已经 Historical blocks required for auditing / replay / light client interchangeable / 481 commitpersist bundled interchangeable / 679 commitretaincaution-notpersist interchangeable / 已经 persist signal 就代表 caution 已经验完 interchangeable，或已经和 491 commitretaincaution-vs-kept bundled / commitretaincaution-sold-as-pruning interchangeable / 678 commitretaincaution-notbootstrap interchangeable。

## 为什么错

官方把 Commit Usage all nodes remove 段落、retain_height defaults to 0 retain all（366）、bootstrap from genesis / full history（323 / 38）、Historical blocks required for auditing / replay / light client（481 / 679）写成三件独立的实现事。把它们卖成 retain_height defaults to 0 retain all interchangeable / bootstrap from genesis interchangeable / Historical blocks required interchangeable，会把 not retain_height defaults to 0 retain all、not bootstrap from genesis unless state sync、not Historical blocks required 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 If all nodes remove historical blocks not retain_height defaults to 0 retain all / not bootstrap from genesis unless state sync / not Historical blocks required for auditing replay light client 正式三事（491 余量），必须分开 not retain_height defaults to 0 retain all、not bootstrap from genesis unless state sync、not Historical blocks required 三件事，不要和 491 / 366 / 481 / 677 / 679 / 323 / 38 / 335 糊成一句。

## 和相邻反模式

- [commitretaincaution-notdefaultzero-sold-as-bundled](commitretaincaution-notdefaultzero-sold-as-bundled.md) 是 with caution 单句 vs defaults to 0 / blocks below / persist signal，不是本页 all nodes remove 段落边界。
- [commitretaincaution-sold-as-pruning](commitretaincaution-sold-as-pruning.md) 是 Commit Usage retain_height caution 正式三事 bundled 全段，不是本页 item 2 all nodes remove 单句边界。
- [retain-sold-as-pruned](retain-sold-as-pruned.md) 是 Commit 保留高度 bundled 全段，不是本页 no bootstrap unless state sync vs genesis replay 边界。
