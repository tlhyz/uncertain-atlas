# 反模式：把 VerifyVoteExtension Usage not called for local process 正式三事卖成 Verify Usage bundled / 已经本地票也 Verify / 已经 Accept

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[not called for local process ≠ bundled](../../tracks/implementation/worked-example-verifyusage-localproc-vs-bundled.md)。

## 卖法

- 「看见是本地票 / 是自己签的 就已经自己验过 interchangeable / 已经 Accept interchangeable。」
- 「看见 VerifyVoteExtension 不对本地 Precommit 调用 就已经本地票也 Verify interchangeable / 已经 received from q≠p interchangeable。」
- 「看见 not called for local process 就已经 Verify Usage bundled interchangeable / 已经带有效签就会调 Verify interchangeable。」

## 为什么错

官方把 not called for local process、not already self-verified、not When received from q≠p 写成三件独立的实现事。把它们卖成 Verify Usage bundled、已经本地票也 Verify、已经 Accept，会把 Usage 侧本地票不调、不是已经自己验过、不是 When 收到侧 call 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 VerifyVoteExtension Usage not called for local process 正式三事，必须分开 not called for local process、not already self-verified、not When received from q≠p 三个名字，不要把它们卖成 Verify Usage bundled / 已经本地票也 Verify / 已经 Accept。

## 和相邻反模式

- [verifyusage-emptyext-sold-as-bundled](verifyusage-emptyext-sold-as-bundled.md) 是 353 item 1 / 521 边界，不是本页 local process 单句边界。
- [verifywhen-call-sold-as-bundled](verifywhen-call-sold-as-bundled.md) 是 When step 2 call received from q≠p，不是本页 Usage 侧 local process not called 边界。
- [verifywhen-sold-as-skipped](verifywhen-sold-as-skipped.md) 是 353 bundled 专用；本页是 local process not called 单句边界。
