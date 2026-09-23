# 反模式：把请求里的 hash 不是已经对该块跑过 Process not already ran-process / not already this-process / not already processalso 正式三事（353 余量）说成已经 Process 过 / 已经对上这次 Process / 已经是提议者那边也会叫 Process

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[请求里的 hash not already ran-process ≠ bundled（353）](../../tracks/implementation/worked-example-hash-notprocess-vs-bundled.md)。

## 卖法

把请求里的 `hash` / 有 hash / 指向某块 写成已经对该块跑过 `ProcessProposal` interchangeable / 已经 ran-process interchangeable / 已经 Process 过交差 interchangeable / 353 verifywhen bundled interchangeable / verifywhen-sold-as-skipped interchangeable；把是同一块 / hash 指向同一块 写成已经对上这次 Process interchangeable / 已经 this-process interchangeable / 已经对上这次 Process 交差 interchangeable；把不保证 / 不保证已经暴露给应用 / 规范说不保证 写成已经是提议者那边也会叫 Process interchangeable / 已经 processalso interchangeable / 已经 processalso 交差 interchangeable，或已经和 353 verifywhen bundled / verifywhen-sold-as-skipped interchangeable / 814 hash-notprocess interchangeable。

## 为什么错

官方把有 hash、不是已经对上这次 Process、不是已经是提议者那边也会叫 Process 写成三件独立的实现事。把它们卖成 already ran-process interchangeable / already this-process interchangeable / already processalso interchangeable，会把 not already ran-process、not already this-process、not already processalso 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看请求里的 hash 不是已经对该块跑过 Process not already ran-process / not already this-process / not already processalso 正式三事（353 余量），必须分开 not already ran-process、not already this-process、not already processalso 三件事，不要和 353 / 34 / 348 / 812 / 813 糊成一句。

## 和相邻反模式

- [verifywhen-sold-as-skipped](verifywhen-sold-as-skipped.md) 是 Verify 何时调用 bundled 全段，不是本页有 hash item 3 单句边界。
- [empty-notlocal-sold-as-bundled](empty-notlocal-sold-as-bundled.md) 是不对本进程自己发出的 Precommit 调用 not already self-verified（353 item 2），不是本页 not already ran-process 边界。
- [empty-notskip-sold-as-bundled](empty-notskip-sold-as-bundled.md) 是空扩展仍会调 Verify not already skip-verify（353 item 1），不是本页 not already processalso 边界。
