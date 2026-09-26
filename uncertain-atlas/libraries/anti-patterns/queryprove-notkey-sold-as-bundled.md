# 反模式：把 Query 回包 proof_ops 是按请求回的、要对这一高 AppHash 验的序列化证明不是已经是按键查 not already key / not already matched / not already settled 正式三事（383 余量）说成已经是按键查 / 已经对上 AppHash / 已经交差

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[回了证明 not already key ≠ bundled（383）](../../tracks/implementation/worked-example-queryprove-notkey-vs-bundled.md)。

## 卖法

把回了证明 / Query 回包 proof_ops 是按请求回的、要对这一高 AppHash 验的序列化证明 / proof_ops 是按请求回的 写成已经是按键查 interchangeable / 已经 key interchangeable / 已经按 /store 按键查交差 interchangeable / 383 queryprove bundled interchangeable / queryprove-sold-as-proof interchangeable；把有序列化证明 / 有要对这一高 AppHash 验的序列化证明 / 用来验这份值的证明 写成已经对上 AppHash interchangeable / 已经 matched interchangeable / 已经对上 AppHash 交差 interchangeable；把能回 / 能回 proof_ops / 按请求回了证明 写成已经交差 interchangeable / 已经 settled interchangeable / 已经交差交差 interchangeable，或已经和 383 queryprove bundled / queryprove-sold-as-proof interchangeable / 897 queryprove-notkey interchangeable。

## 为什么错

官方把回了证明、不是已经对上 AppHash、不是已经交差写成三件独立的实现事。把它们卖成 already key interchangeable / already matched interchangeable / already settled interchangeable，会把 not already key、not already matched、not already settled 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Query 回包 proof_ops 是按请求回的、要对这一高 AppHash 验的序列化证明不是已经是按键查 not already key / not already matched / not already settled 正式三事（383 余量），必须分开 not already key、not already matched、not already settled 三件事，不要和 383 / 380 / 325 / 316 糊成一句。

## 和相邻反模式

- [queryprove-sold-as-proof](queryprove-sold-as-proof.md) 是 queryprove bundled 全段，不是本页回了证明 item 2 单句边界。
- [queryprove-notmatched-sold-as-bundled](queryprove-notmatched-sold-as-bundled.md) 是勾了 prove item 1 单句边界，不是本页 not already key 边界。
- [queryindex-sold-as-store](queryindex-sold-as-store.md) 是 Query 回包 value 就已经对上 AppHash（380），不是本页 not already key 单句。
- [queryproof-sold-as-apphash](queryproof-sold-as-apphash.md) 是 Query 回了 Proof 就已经对上 AppHash（325），不是本页 not already matched 边界。
- [exectxresult-sold-as-consensus](exectxresult-sold-as-consensus.md) 是结果列表就已经同一顺序（316），不是本页 not already settled 边界。
