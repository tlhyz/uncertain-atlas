# 模式：把应用回了 AppHash 和各笔输出引擎哈希进 ResultHash 不是已经印进本头 not already printed / not already header / not already settled 正式三事（362 余量）说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) FinalizeBlock When。  
**例**：[回了 ResultHash not already printed ≠ bundled（362）](../../tracks/implementation/worked-example-finwhen-notprinted-vs-bundled.md)。

## 三个名字

1. **回了 不是 already printed：** 看见回了 / 应用回了 AppHash 和各笔输出 / 回了 AppHash 与各笔输出，不是已经印进本头 interchangeable / 已经 printed interchangeable / 已经印进本头交差 interchangeable，不是 362 finwhen bundled interchangeable / finalizewhen-sold-as-decided interchangeable。

2. **有 ResultHash 不是 already header：** 看见有 ResultHash / 引擎把输出哈希进 ResultHash / 有 ResultHash，不是已经是本头 AppHash interchangeable / 已经 header interchangeable / 已经是本头 AppHash 交差 interchangeable，不是 147 apphash interchangeable / 836 finwhen-notwillcall interchangeable。

3. **哈希了 不是 already settled：** 看见哈希了 / 把输出哈希进了 / 引擎哈希了，不是已经交差 interchangeable / 已经 settled interchangeable / 已经交差交差 interchangeable，不是 837 finwhen-notpersist interchangeable / 33 fourgates interchangeable。

官方把回了、不是已经是本头 AppHash、不是已经交差写成三个名字。把它们叫成一个「看见回了就已经印进本头 interchangeable / 就已经是本头 AppHash interchangeable / 就已经交差 interchangeable」，会把 not already printed、not already header、not already settled 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看应用回了 AppHash 和各笔输出引擎哈希进 ResultHash 不是已经印进本头 not already printed / not already header / not already settled 正式三事（362 余量），先数清问的是回了 是不是 already printed / 362 / finalizewhen-sold-as-decided，是不是有 ResultHash 是不是 already header，还是哈希了 是不是 already settled，再决定要不要同一次发布。362 finalize-when vs decided bundled unbundling 在本页 item 3 完成。
