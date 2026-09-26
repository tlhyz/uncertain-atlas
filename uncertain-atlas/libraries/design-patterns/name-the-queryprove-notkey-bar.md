# 模式：把 Query 回包 proof_ops 是按请求回的、要对这一高 AppHash 验的序列化证明不是已经是按键查 not already key / not already matched / not already settled 正式三事（383 余量）说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) Query Request / Query Response。  
**例**：[回了证明 not already key ≠ bundled（383）](../../tracks/implementation/worked-example-queryprove-notkey-vs-bundled.md)。

## 三个名字

1. **回了证明 不是 already key：** 看见回了证明 / Query 回包 proof_ops 是按请求回的、要对这一高 AppHash 验的序列化证明 / proof_ops 是按请求回的，不是已经是按键查 interchangeable / 已经 key interchangeable / 已经按 /store 按键查交差 interchangeable，不是 383 queryprove bundled interchangeable / queryprove-sold-as-proof interchangeable。

2. **有序列化证明 不是 already matched：** 看见有序列化证明 / 有要对这一高 AppHash 验的序列化证明 / 用来验这份值的证明，不是已经对上 AppHash interchangeable / 已经 matched interchangeable / 已经对上 AppHash 交差 interchangeable，不是 325 queryproof interchangeable / 896 queryprove-notmatched interchangeable。

3. **能回 不是 already settled：** 看见能回 / 能回 proof_ops / 按请求回了证明，不是已经交差 interchangeable / 已经 settled interchangeable / 已经交差交差 interchangeable，不是 316 txresults interchangeable / 383 queryprove item 3 interchangeable。

官方把回了证明、不是已经对上 AppHash、不是已经交差写成三个名字。把它们叫成一个「看见回了证明就已经是按键查 interchangeable / 就已经对上 AppHash interchangeable / 就已经交差 interchangeable」，会把 not already key、not already matched、not already settled 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Query 回包 proof_ops 是按请求回的、要对这一高 AppHash 验的序列化证明不是已经是按键查 not already key / not already matched / not already settled 正式三事（383 余量），先数清问的是回了证明 是不是 already key / 383 / queryprove-sold-as-proof，是不是有序列化证明 是不是 already matched，还是能回 是不是 already settled，再决定要不要同一次发布。383 queryprove-vs-proof bundled unbundling 在本页 item 2 续。
