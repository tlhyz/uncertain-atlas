# 反模式：把 CheckTx Usage will not broadcast or in proposal not Check passed is in proposal / not forever valid / not Finalize Code≠0 still in block 正式三事（489 余量）说成已经进提案 / 已经 forever valid / 已经 Finalize Code≠0 仍在块里

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[will not be in proposal not Check passed is in proposal ≠ bundled（489）](../../tracks/implementation/worked-example-chktxcodereject-notproposal-vs-bundled.md)。

## 卖法

把 will not be broadcast / or included in a proposal block / 不会进提案块 写成已经 Check 通过就是已进提案 interchangeable / 33 four gates interchangeable；把不会广播写成已经 CheckTx 过了就永远有效 interchangeable / 301 forever valid interchangeable；把看见 Code 非零写成已经 Finalize Code≠0 仍在块里 interchangeable / 316 exectxresult interchangeable，或已经和 489 chktxcodereject-vs-proposal bundled / chktxcodereject-notproposal-sold-as-bundled interchangeable / 687 chktxcodereject-notproposal interchangeable。

## 为什么错

官方把 CheckTx Usage 不会进提案块、四门结算、forever valid、Finalize Code≠0 仍在块里写成三件独立的实现事。把它们卖成 Check passed is in proposal interchangeable / forever valid interchangeable / Finalize Code≠0 still in block interchangeable，会把 not Check passed is in proposal、not forever valid、not Finalize Code≠0 still in block 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 CheckTx Usage will not be in proposal 正式三事（489 余量），必须分开 not Check passed is in proposal、not forever valid、not Finalize Code≠0 still in block 三件事，不要和 489 / 33 / 301 / 316 / 686 / 688 糊成一句。

## 和相邻反模式

- [chktxcodereject-sold-as-proposal](chktxcodereject-sold-as-proposal.md) 是 CheckTx Usage Code≠0 rejected bundled（489），不是本页 item 2 单句边界。
- [chktxcodereject-notgossip-sold-as-bundled](chktxcodereject-notgossip-sold-as-bundled.md) 是 Code≠0 rejected 单句边界（686 item 1），不是本页 proposal 边界。
