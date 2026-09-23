# 模式：把空扩展仍会调 Verify 不是已经跳过 Verify not already skip-verify / not already no-call / not already empty-signed 正式三事（353 余量）说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) VerifyVoteExtension Usage。  
**例**：[空扩展仍会调 Verify not already skip-verify ≠ bundled（353）](../../tracks/implementation/worked-example-empty-notskip-vs-bundled.md)。

## 三个名字

1. **是空的 不是 already skip-verify：** 看见空扩展（0 长度）引擎仍会调 `VerifyVoteExtension` / 是空的 / 0 长度扩展，不是已经跳过 Verify interchangeable / 已经 skip-verify interchangeable / 已经跳过 Verify 交差 interchangeable，不是 353 verifywhen bundled interchangeable / verifywhen-sold-as-skipped interchangeable。

2. **选择不扩 不是 already no-call：** 看见发送方选择不扩 / 选择不扩 / 不扩，不是已经不用调 interchangeable / 已经 no-call interchangeable / 已经不用调交差 interchangeable，不是 348 req6coherence interchangeable / 34 vote-extension-block interchangeable。

3. **仍会调 不是 already empty-signed：** 看见仍会调 / 引擎仍会调 / 仍调 `VerifyVoteExtension`，不是已经是空扩展仍验签 interchangeable / 已经 empty-signed interchangeable / 已经空扩展仍验签交差 interchangeable，不是 813 empty-notlocal interchangeable / 814 hash-notprocess interchangeable。

官方把是空的、不是已经不用调、不是已经是空扩展仍验签写成三个名字。把它们叫成一个「看见是空的就已经跳过 Verify interchangeable / 就已经不用调 interchangeable / 就已经是空扩展仍验签 interchangeable」，会把 not already skip-verify、not already no-call、not already empty-signed 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看空扩展仍会调 Verify 不是已经跳过 Verify not already skip-verify / not already no-call / not already empty-signed 正式三事（353 余量），先数清问的是是空的 是不是 already skip-verify / 353 / verifywhen-sold-as-skipped，是不是选择不扩 是不是 already no-call，还是仍会调 是不是 already empty-signed，再决定要不要同一次发布。353 verifywhen vs empty bundled unbundling 在本页 item 1 启动。
