# 模式：把 local_last_commit 是上一高度的预提交带扩展不是已经是本高度刚签的扩展 not already this-signed / not already ve-at-h / not already settled 正式三事（359 余量）说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) PrepareProposal Usage。  
**例**：[local_last_commit 上一高 not already this-signed ≠ bundled（359）](../../tracks/implementation/worked-example-prepfields-notthissigned-vs-bundled.md)。

## 三个名字

1. **有上一高的票 不是 already this-signed：** 看见有上一高的票 / `local_last_commit` 是上一高度的预提交带扩展 / 有上一高的票，不是已经是本高度刚签的扩展 interchangeable / 已经 this-signed interchangeable / 已经是本高度刚签的 *e* 交差 interchangeable，不是 359 preparefields bundled interchangeable / preparefields-sold-as-same interchangeable。

2. **带了扩展 不是 already ve-at-h：** 看见带了扩展 / 上一高的预提交带投票扩展 / 有扩展挂上，不是已经到了 H 就已经 Prepare 带了扩展 interchangeable / 已经 ve-at-h interchangeable / 已经到了 H 交差 interchangeable，不是 330 veheight interchangeable / 830 prepfields-notprocess interchangeable。

3. **能用上一高 不是 already settled：** 看见能用上一高 / 能用上一高度的预提交 / 上一高的票能进请求，不是已经交差 interchangeable / 已经 settled interchangeable / 已经交差交差 interchangeable，不是 832 prepfields-nothash interchangeable / 33 fourgates interchangeable。

官方把有上一高的票、不是已经到了 H、不是已经交差写成三个名字。把它们叫成一个「看见有上一高的票就已经是本高度刚签的扩展 interchangeable / 就已经到了 H 就已经 Prepare 带了扩展 interchangeable / 就已经交差 interchangeable」，会把 not already this-signed、not already ve-at-h、not already settled 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 local_last_commit 是上一高度的预提交带扩展不是已经是本高度刚签的扩展 not already this-signed / not already ve-at-h / not already settled 正式三事（359 余量），先数清问的是有上一高的票 是不是 already this-signed / 359 / preparefields-sold-as-same，是不是带了扩展 是不是 already ve-at-h，还是能用上一高 是不是 already settled，再决定要不要同一次发布。359 prepare-fields vs same bundled unbundling 在本页 item 2 续。
