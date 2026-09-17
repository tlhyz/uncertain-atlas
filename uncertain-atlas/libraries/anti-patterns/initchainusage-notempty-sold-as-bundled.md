# 反模式：把 InitChain Usage Response Validators empty → Request Validators not empty list means no set / not not-empty ignores Request / not ValidatorUpdate already changed set 正式三事（495 余量）说成已经空名单就没有集合 / 已经 not empty 规则 / 已经改了集合

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[empty → Request not empty list means no set ≠ bundled（495）](../../tracks/implementation/worked-example-initchainusage-notempty-vs-bundled.md)。

## 卖法

把 If InitChainResponse.Validators is empty the initial set will be InitChainRequest.Validators / Response 空就用 Request 写成已经 InitChain 回了空名单就没有集合 interchangeable / 318 emptyset interchangeable；把看见 will be Request Validators 写成已经 not empty 就无视 Request interchangeable / 697 initchainusage-notnonempty interchangeable；把看见 initial validator set 写成已经 ValidatorUpdate 用公钥认人就已经改了集合 interchangeable / 364 interchangeable，或已经和 495 initchainusage-vs-bundled / initchainusage-notempty-sold-as-bundled interchangeable / 696 initchainusage-notempty interchangeable。

## 为什么错

官方把 InitChain Usage empty 规则、空名单语义、not empty 规则、ValidatorUpdate 已经改了集合写成三件独立的实现事。把它们卖成 empty list means no set interchangeable / not-empty ignores Request interchangeable / ValidatorUpdate already changed set interchangeable，会把三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 InitChain Usage empty 正式三事（495 余量），必须分开 not empty list means no set、not not-empty ignores Request、not ValidatorUpdate already changed set 三件事，不要和 495 / 318 / 364 / 695 / 697 糊成一句。

## 和相邻反模式

- [initchainusage-sold-as-bundled](initchainusage-sold-as-bundled.md) 是 InitChain Usage 正式三事 bundled（495），不是本页 item 2 单句边界。
- [initchainusage-notcrash-sold-as-bundled](initchainusage-notcrash-sold-as-bundled.md) 是 once 单句边界（695 item 1），不是本页 empty 边界。
