# 反模式：把 Extend 或 Verify 里有确定 bug 会让带无效扩展的 Precommit 被丢掉不是已经只是活性问题 not already only-liveness / not already block-invalid / not already nondet 正式三事（348 余量）说成已经只是活性问题 / 已经是块非法 / 已经是非确定 bug

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[Extend 或 Verify 里有确定 bug 会让带无效扩展的 Precommit 被丢掉 not already only-liveness ≠ bundled（348）](../../tracks/implementation/worked-example-req6-notliveness-vs-bundled.md)。

## 卖法

把 Extend 或 Verify（或两边）里有确定 bug / 带无效扩展的 Precommit 会被丢掉 / 有确定 bug 写成已经只是活性问题 interchangeable / 已经 only-liveness interchangeable / 已经只伤活性交差 interchangeable / 348 req6coherence bundled interchangeable / req6coherence-sold-as-accept interchangeable；把 Precommit 被丢掉 / 带无效扩展的 Precommit 会被丢掉 写成已经是块非法 interchangeable / 已经 block-invalid interchangeable / 已经块非法交差 interchangeable；把有确定 bug / 算丢掉 写成已经是 Verify 非确定 bug interchangeable / 已经 nondet interchangeable / 已经非确定交差 interchangeable，或已经和 348 req6coherence bundled / req6coherence-sold-as-accept interchangeable / 798 req6-notliveness interchangeable。

## 为什么错

官方把确定 bug 丢掉 Precommit、不是已经是块非法、不是已经是非确定 bug写成三件独立的实现事。把它们卖成 already only-liveness interchangeable / already block-invalid interchangeable / already nondet interchangeable，会把 not already only-liveness、not already block-invalid、not already nondet 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Extend 或 Verify 里有确定 bug 会让带无效扩展的 Precommit 被丢掉不是已经只是活性问题 not already only-liveness / not already block-invalid / not already nondet 正式三事（348 余量），必须分开 not already only-liveness、not already block-invalid、not already nondet 三件事，不要和 348 / 341 / 34 / 797 / 799 糊成一句。

## 和相邻反模式

- [req6coherence-sold-as-accept](req6coherence-sold-as-accept.md) 是 Extend–Verify 一致性 bundled 全段，不是本页确定 bug 丢掉 Precommit item 2 单句边界。
- [req6-notany-sold-as-bundled](req6-notany-sold-as-bundled.md) 是正确进程交出的扩展必须 Verify Accept not already any-extension（348 item 1），不是本页 not already only-liveness 边界。
- [verifydet-sold-as-extend](verifydet-sold-as-extend.md) 是 Verify 必须只依赖扩展、这块和上一份状态（341），不是本页有确定 bug ≠ 非确定 bug 边界。
