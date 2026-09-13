# 反模式：把 InitChain Usage 正式三事卖成崩溃后再调 / 空名单就没有集合 / 应用 can decide bundled interchangeable

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[Called once upon genesis ≠ 崩溃后再调 InitChain](../../tracks/implementation/worked-example-initchainusage-vs-bundled.md)。

## 卖法

- 「看见 Called once upon genesis / InitChain 创世时只调一次 就已经崩溃后再调 InitChain / 已经交差 / InitChain Usage 余量 bundled interchangeable。」
- 「看见 If InitChainResponse.Validators is empty the initial set will be InitChainRequest.Validators / Response 空就用 Request 就已经 InitChain 回了空名单就没有集合 / 已经 ValidatorUpdate 改了集合 interchangeable。」
- 「看见 If InitChainResponse.Validators is not empty it will be the initial set regardless of InitChainRequest.Validators / Response 非空就用 Response 就已经 The application can decide to accept bundled（412） interchangeable / 已经用了创世文件里的验证者 / 已经 empty response 规则 interchangeable。」

## 为什么错

官方把 InitChain Usage 三条核心句写成三件独立的实现事。把它们卖成崩溃后再调 / 空名单就没有集合 / 应用 can decide bundled interchangeable，会把 genesis 只调一次、empty response 规则、not empty 无视 request 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 InitChain Usage 正式三事，必须分开 Called once upon genesis、Response Validators empty → Request Validators、Response Validators not empty → Response regardless of Request 三个名字，不要把它们卖成崩溃后再调 / 空名单就没有集合 / 应用 can decide bundled interchangeable。

## 和相邻反模式

- [initonce-sold-as-crash](initonce-sold-as-crash.md) 是 InitChain Usage 余量 bundled 三事，不是本页 InitChain Usage 正式三事专用边界。
- [validatorupdate-sold-as-set](validatorupdate-sold-as-set.md) 是 InitChain 回了空名单就没有集合，不是本页 empty response 规则专用边界。
