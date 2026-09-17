# 反模式：把 InitChain Usage Response Validators not empty regardless of Request not app can decide bundled / not empty list means no set / not duplicate pubkeys already recoverable 正式三事（495 余量）说成已经 can decide bundled / 已经空名单就没有集合 / 已经重复公钥就能恢复

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[not empty regardless of Request not can decide ≠ bundled（495）](../../tracks/implementation/worked-example-initchainusage-notnonempty-vs-bundled.md)。

## 卖法

把 If InitChainResponse.Validators is not empty it will be the initial set regardless of InitChainRequest.Validators / Response 非空就用 Response 写成已经 The application can decide to accept bundled interchangeable / 412 / 496 interchangeable；把看见 not empty → Response 写成已经 InitChain 回了空名单就没有集合 interchangeable / 318 interchangeable；把看见 Usage 这句写成已经同一批重复公钥就已经能恢复 interchangeable，或已经和 495 initchainusage-vs-bundled / initchainusage-notnonempty-sold-as-bundled interchangeable / 697 initchainusage-notnonempty interchangeable。

## 为什么错

官方把 InitChain Usage not empty 规则、应用 can decide bundled、空名单语义、重复公钥就已经能恢复写成三件独立的实现事。把它们卖成 can decide bundled interchangeable / empty list means no set interchangeable / duplicate pubkeys already recoverable interchangeable，会把三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 InitChain Usage not empty 正式三事（495 余量），必须分开 not app can decide bundled、not empty list means no set、not duplicate pubkeys already recoverable 三件事，不要和 495 / 412 / 496 / 318 / 695 / 696 糊成一句。

## 和相邻反模式

- [initchainusage-sold-as-bundled](initchainusage-sold-as-bundled.md) 是 InitChain Usage 正式三事 bundled（495），不是本页 item 3 单句边界。
- [initchainusage-notempty-sold-as-bundled](initchainusage-notempty-sold-as-bundled.md) 是 empty → Request 单句边界（696 item 2），不是本页 not empty 边界。
