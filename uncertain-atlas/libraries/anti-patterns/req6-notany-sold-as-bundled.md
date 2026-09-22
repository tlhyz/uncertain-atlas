# 反模式：把正确进程交出的扩展必须被正确接收者 Verify Accept 不是已经是任意扩展都会 Accept not already any-extension / not already default-accept / not already settled 正式三事（348 余量）说成已经是任意扩展都会 Accept / 已经写了默认 Accept / 已经交差

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[正确进程交出的扩展必须被正确接收者 Verify Accept not already any-extension ≠ bundled（348）](../../tracks/implementation/worked-example-req6-notany-vs-bundled.md)。

## 卖法

把正确进程交出的扩展、正确接收者 Verify 必须 Accept / 正确进程之间永远过 / 正确进程交出来的必须过 写成已经是任意扩展都会 Accept interchangeable / 已经 any-extension interchangeable / 已经任意扩展过交差 interchangeable / 348 req6coherence bundled interchangeable / req6coherence-sold-as-accept interchangeable；把必须 Accept / 正确接收者 Verify 必须回 Accept 写成已经写了默认 Accept interchangeable / 已经 default-accept interchangeable / 已经默认 Accept 交差 interchangeable；把正确进程之间过 / 正确进程交出来的必须过 写成已经交差 interchangeable / 已经 settled interchangeable / 已经 Accept 交差 interchangeable，或已经和 348 req6coherence bundled / req6coherence-sold-as-accept interchangeable / 797 req6-notany interchangeable。

## 为什么错

官方把正确进程之间必须过、不是已经写了默认 Accept、不是已经交差写成三件独立的实现事。把它们卖成 already any-extension interchangeable / already default-accept interchangeable / already settled interchangeable，会把 not already any-extension、not already default-accept、not already settled 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看正确进程交出的扩展必须被正确接收者 Verify Accept 不是已经是任意扩展都会 Accept not already any-extension / not already default-accept / not already settled 正式三事（348 余量），必须分开 not already any-extension、not already default-accept、not already settled 三件事，不要和 348 / 34 / 349 / 798 / 799 糊成一句。

## 和相邻反模式

- [req6coherence-sold-as-accept](req6coherence-sold-as-accept.md) 是 Extend–Verify 一致性 bundled 全段，不是本页必须 Accept item 1 单句边界。
- [req3coherence-sold-as-accept](req3coherence-sold-as-accept.md) / [req3-notany-sold-as-bundled](req3-notany-sold-as-bundled.md) 是提案必须 Accept（347），不是本页扩展必须 Accept 边界。
- [vote-extension-sold-as-block](vote-extension-sold-as-block.md) 是验签拒收整张预提交不是已经是块非法（34），不是本页任意扩展都会 Accept 边界。
