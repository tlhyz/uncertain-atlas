# 反模式：把空扩展仍会调 Verify 不是已经跳过 Verify not already skip-verify / not already no-call / not already empty-signed 正式三事（353 余量）说成已经跳过 Verify / 已经不用调 / 已经是空扩展仍验签

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[空扩展仍会调 Verify not already skip-verify ≠ bundled（353）](../../tracks/implementation/worked-example-empty-notskip-vs-bundled.md)。

## 卖法

把空扩展（0 长度）引擎仍会调 `VerifyVoteExtension` / 是空的 / 0 长度扩展 写成已经跳过 Verify interchangeable / 已经 skip-verify interchangeable / 已经跳过 Verify 交差 interchangeable / 353 verifywhen bundled interchangeable / verifywhen-sold-as-skipped interchangeable；把发送方选择不扩 / 选择不扩 写成已经不用调 interchangeable / 已经 no-call interchangeable / 已经不用调交差 interchangeable；把仍会调 / 引擎仍会调 / 仍调 `VerifyVoteExtension` 写成已经是空扩展仍验签 interchangeable / 已经 empty-signed interchangeable / 已经空扩展仍验签交差 interchangeable，或已经和 353 verifywhen bundled / verifywhen-sold-as-skipped interchangeable / 812 empty-notskip interchangeable。

## 为什么错

官方把是空的、不是已经不用调、不是已经是空扩展仍验签写成三件独立的实现事。把它们卖成 already skip-verify interchangeable / already no-call interchangeable / already empty-signed interchangeable，会把 not already skip-verify、not already no-call、not already empty-signed 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看空扩展仍会调 Verify 不是已经跳过 Verify not already skip-verify / not already no-call / not already empty-signed 正式三事（353 余量），必须分开 not already skip-verify、not already no-call、not already empty-signed 三件事，不要和 353 / 34 / 348 / 813 / 814 糊成一句。

## 和相邻反模式

- [verifywhen-sold-as-skipped](verifywhen-sold-as-skipped.md) 是 Verify 何时调用 bundled 全段，不是本页是空的 item 1 单句边界。
- [vote-extension-sold-as-block](vote-extension-sold-as-block.md) 是验签拒收整张预提交就已经是块非法（34），不是本页 not already skip-verify 边界。
- [req6coherence-sold-as-accept](req6coherence-sold-as-accept.md) 是正确进程交出的扩展必须被正确接收者 Verify Accept（348），不是本页 not already no-call 边界。
