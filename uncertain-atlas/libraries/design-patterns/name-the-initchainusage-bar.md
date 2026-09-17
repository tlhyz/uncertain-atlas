# 模式：把 InitChain Usage 正式三事说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) InitChain Usage。  
**例**：[Called once upon genesis ≠ 崩溃后再调 InitChain](../../tracks/implementation/worked-example-initchainusage-vs-bundled.md)。

## 三个名字

1. **Called once upon genesis 不是崩溃后再调 InitChain：** 看见 Methods InitChain Usage 创世只调一次，不是崩溃恢复再调 interchangeable。
2. **Response Validators empty → Request Validators 不是空名单就没有集合：** 看见 empty response 规则，不是 InitChain 空名单 interchangeable。
3. **Response Validators not empty → Response regardless of Request 不是应用 can decide bundled interchangeable：** 看见 not empty 无视 request，不是 412 bundled 第二件事 interchangeable。

## 为什么要分开叫

官方把 InitChain Usage 三条核心句、InitChain Usage 余量 bundled（412）、InitChain 空名单（318）、崩溃恢复再调（320）写成三个名字。把它们叫成一个「看见 InitChain 了就已经崩溃后再调、已经没有集合、已经改了集合」，会把 genesis 只调一次、empty response 规则、not empty 无视 request 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 InitChain Usage 正式三事，先数清问的是 Called once upon genesis 是不是崩溃后再调 InitChain interchangeable / 已经交差、Response Validators empty → Request Validators 是不是空名单就没有集合 interchangeable、Response Validators not empty → Response regardless of Request 是不是应用 can decide bundled interchangeable / 已经改了集合，再决定要不要同一次发布。
