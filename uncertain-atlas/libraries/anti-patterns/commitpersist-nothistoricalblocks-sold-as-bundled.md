# 反模式：把 Historical blocks required for auditing replay light client not retain_height defaults to 0 retain all / not blocks below height may be removed / not full history in consensus when joined 正式三事（481 余量）说成已经 retain_height 默认 0 全留 / 已经能剪就没有历史 / 已经切进共识就有完整历史

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[Historical blocks required for auditing replay light client not retain_height defaults to 0 retain all ≠ bundled（481）](../../tracks/implementation/worked-example-commitpersist-nothistoricalblocks-vs-bundled.md)。

## 卖法

把 Historical blocks may also be required for other purposes, e.g. auditing, replay of non-persisted heights, light client verification, and so on / auditing / replay / light client 写成已经 retain_height defaults to 0 (retain all) interchangeable / 366 retain-height bundled interchangeable / 677 commitretaincaution-notdefaultzero interchangeable / 335 finpersist interchangeable / 587 finreturn interchangeable；把 may also be required / other purposes 写成已经 blocks below this height may be removed interchangeable / 366 retain bundled item 2 interchangeable / 已经 non-zero retain_height 就等于已经在剪 interchangeable / 已经能剪就等于已经没有历史 interchangeable；把 Historical blocks required 写成已经切进共识就已经有完整历史 interchangeable / 323 full-history interchangeable / 38 genesis-replay interchangeable / 647 offersnapusage-notlisted interchangeable / 已经装完切进共识 interchangeable，或已经和 481 commitpersist-vs-finalize bundled / commitpersist-sold-as-finalize interchangeable / 682 commitpersist-nothistoricalblocks interchangeable / 679 commitretaincaution-notpersist interchangeable。

## 为什么错

官方把 Commit Usage Historical blocks may also be required 单句、retain_height defaults to 0 retain all（366）、blocks below height may be removed（366 item 2）、full history in consensus when joined（323）写成三件独立的实现事。把它们卖成 retain_height 默认 0 全留 interchangeable / 能剪就没有历史 interchangeable / 切进共识就有完整历史 interchangeable，会把 not retain_height defaults to 0 retain all、not blocks below height may be removed、not full history in consensus when joined 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Historical blocks required for auditing replay light client not retain_height defaults to 0 retain all / not blocks below height may be removed / not full history in consensus when joined 正式三事（481 余量），必须分开 not retain_height defaults to 0 retain all、not blocks below height may be removed、not full history in consensus when joined 三件事，不要和 481 / 366 / 491 / 677 / 678 / 679 / 323 / 38 / 680 / 681 / 665 / 497 糊成一句。

## 和相邻反模式

- [commitretaincaution-notpersist-sold-as-bundled](commitretaincaution-notpersist-sold-as-bundled.md) 是 Historical blocks required not Use retain_height with caution / not If all nodes remove / not persist signal bundled（491 item 3），不是本页 481 item 3 retain_height default 0 / blocks below / full history 边界。
- [commitretaincaution-notdefaultzero-sold-as-bundled](commitretaincaution-notdefaultzero-sold-as-bundled.md) 是 Use retain_height with caution vs defaults to 0，不是本页 Historical blocks other purposes 单句边界。
- [commitpersist-sold-as-finalize](commitpersist-sold-as-finalize.md) 是 Commit Usage persist signal 正式三事 bundled 全段，不是本页 Historical blocks 段落单句边界。
