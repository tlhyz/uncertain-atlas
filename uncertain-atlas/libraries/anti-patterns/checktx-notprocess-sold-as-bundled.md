# 反模式：把 ProcessProposal 对付这种行为不是已经是 CheckTx not already is-checktx / not already is-finalize / not already pool-done 正式三事（339 余量）说成已经是 CheckTx / 已经是 Finalize / 已经在池子里挡完

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[有 ProcessProposal not already is-checktx ≠ bundled（339）](../../tracks/implementation/worked-example-checktx-notprocess-vs-bundled.md)。

## 卖法

把从 ABCI 1.0 起有 ProcessProposal 对付这种行为 / 有 ProcessProposal / 这道门对付拜占庭不守 CheckTx 写成已经是 CheckTx interchangeable / 已经 is-checktx interchangeable / 已经是 CheckTx 交差 interchangeable / 339 checktxweak bundled interchangeable / 312 checktxstate interchangeable / checktxweak-sold-as-consensus interchangeable；把规范点名 ProcessProposal / 点名了这道门 / 规范写了 ProcessProposal 写成已经是 Finalize interchangeable / 已经 is-finalize interchangeable；把会拒提案 / ProcessProposal 可以拒 / 会拒 写成已经在池子里挡完 interchangeable / 已经 pool-done interchangeable，或已经和 339 checktxweak bundled / checktxweak-sold-as-consensus interchangeable / 772 checktx-notprocess interchangeable。

## 为什么错

官方把有 ProcessProposal 单句、already is-checktx、already is-finalize、already pool-done 写成三件独立的实现事。把它们卖成 already is-checktx interchangeable / already is-finalize interchangeable / already pool-done interchangeable，会把 not already is-checktx、not already is-finalize、not already pool-done 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 ProcessProposal 对付这种行为不是已经是 CheckTx not already is-checktx / not already is-finalize / not already pool-done 正式三事（339 余量），必须分开 not already is-checktx、not already is-finalize、not already pool-done 三件事，不要和 339 / 312 / 33 / 313 / 770 / 771 糊成一句。

## 和相邻反模式

- [checktxweak-sold-as-consensus](checktxweak-sold-as-consensus.md) 是 CheckTx 弱过滤器 bundled 全段，不是本页有 ProcessProposal item 3 单句边界。
- [checktx-notordering-sold-as-bundled](checktx-notordering-sold-as-bundled.md) 是不该验排序相关有效性 ≠ 已经该在 CheckTx 里验（339 item 1），不是本页有 ProcessProposal ≠ 已经是 CheckTx 边界。
- [checktx-notblocked-sold-as-bundled](checktx-notblocked-sold-as-bundled.md) 是拜占庭能提案无效块 ≠ 已经被池子挡住（339 item 2），不是本页会拒提案 ≠ 已经在池子里挡完 边界。
- [checktxstate-sold-as-execute](checktxstate-sold-as-execute.md) 是 CheckTxState ≠ 已经是 ExecuteTxState（312），不是本页点名了这道门 ≠ 已经是 Finalize 边界。
