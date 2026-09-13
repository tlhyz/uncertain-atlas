# 反模式：把 InitChain Usage app decide / ValidatorUpdate from empty set 正式三事卖成 Response 规则 interchangeable / 已经改了集合 / 空名单就没有集合

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[app decide accept or different one ≠ Response 规则](../../tracks/implementation/worked-example-initchainusage-decide-vs-emptyset.md)。

## 卖法

- 「看见 This allows the app to decide to accept the initial validator set or use a different one / 应用可以决定接受创世验证者集合或用创世应用信息算出另一套 就已经 Response Validators empty/not empty 规则 interchangeable / 已经用了创世文件里的验证者 / InitChain Usage 余量 bundled interchangeable。」
- 「看见 Both InitChainRequest.Validators and InitChainResponse.Validators are ValidatorUpdate structs / Request 和 Response 都是 ValidatorUpdate 就已经 ValidatorUpdate 用公钥认人就已经改了集合 / 已经带了公钥 interchangeable。」
- 「看见 So, technically, they both are updating the validator set from the empty set / 技术上是从空集合更新 就已经 InitChain 回了空名单就没有集合 / Response empty → Request interchangeable / app decide 就已经改了集合 interchangeable。」

## 为什么错

官方把 InitChain Usage 后三条核心句写成三件独立的实现事。把它们卖成 Response 规则 interchangeable / 已经改了集合 / 空名单就没有集合，会把 app decide、ValidatorUpdate 结构、empty set 更新三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 InitChain Usage app decide / ValidatorUpdate from empty set 正式三事，必须分开 app decide accept or different one、Both Validators are ValidatorUpdate structs、updating from empty set 三个名字，不要把它们卖成 Response 规则 interchangeable / 已经改了集合 / 空名单就没有集合。

## 和相邻反模式

- [initchainusage-sold-as-bundled](initchainusage-sold-as-bundled.md) 是 InitChain Usage 正式三事 part 1 就等于崩溃后再调 / 空名单 / bundled，不是本页 app decide / empty set 专用边界。
- [initonce-sold-as-crash](initonce-sold-as-crash.md) 是 InitChain Usage 余量 bundled 三事，不是本页 app decide 单句专用边界。
