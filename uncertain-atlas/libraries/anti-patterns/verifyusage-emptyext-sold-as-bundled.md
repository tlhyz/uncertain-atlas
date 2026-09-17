# 反模式：把 VerifyVoteExtension Usage empty extension still calls Verify 正式三事卖成 Verify Usage bundled / 已经跳过 Verify / 已经 0 长就不叫 Verify

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[empty extension still calls Verify ≠ bundled](../../tracks/implementation/worked-example-verifyusage-emptyext-vs-bundled.md)。

## 卖法

- 「看见空扩展（0 长度）就已经跳过 Verify interchangeable / 已经 0 长就不叫 Verify interchangeable。」
- 「看见发送方选择不扩 就已经不用调 VerifyVoteExtension interchangeable / 已经不会叫 ExtendVote interchangeable。」
- 「看见 even for 0-length 就已经 Verify Usage bundled interchangeable / 已经本地票也 Verify interchangeable。」

## 为什么错

官方把 even for 0-length still calls Verify、empty extension means sender chose not to extend、still calls Verify is not skip Verify 写成三件独立的实现事。把它们卖成 Verify Usage bundled、已经跳过 Verify、已经 0 长就不叫 Verify，会把 0 长仍会 call、选择不扩语义、仍会调 Verify 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 VerifyVoteExtension Usage empty extension still calls Verify 正式三事，必须分开 even for 0-length、sender chose not to extend、still calls Verify 三个名字，不要把它们卖成 Verify Usage bundled / 已经跳过 Verify / 已经 0 长就不叫 Verify。

## 和相邻反模式

- [verifywhen-sold-as-skipped](verifywhen-sold-as-skipped.md) 是 353 bundled 专用；本页是 Verify Usage empty extension still calls 单句边界。
- [verifywhen-discard-sold-as-bundled](verifywhen-discard-sold-as-bundled.md) 是 When step 1 discard，不是本页 Usage 侧 0 长仍会 call 边界。
- [extusage-sold-as-deterministic](extusage-sold-as-deterministic.md) 是 ExtendVote Usage 437 bundled，不是本页 Verify Usage 空扩展边界。
