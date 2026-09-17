# 反模式：把 Prepare 回包校验 crash not Process REJECT / not must Accept / not ProposalStatus REJECT 正式三事（357 余量） 说成已经是 Process REJECT / 已经必须 Accept / 已经 ProposalStatus REJECT

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[crash ≠ bundled（357）](../../tracks/implementation/worked-example-prepvalid-notcrash-vs-bundled.md)。

## 卖法

把 Prepare 回包校验这句写成已经已经是 Process REJECT / 已经必须 Accept / 已经 ProposalStatus REJECT interchangeable，或已经和 357 prepare-valid-vs-checked bundled / prepvalid-notcrash-sold-as-bundled interchangeable。

## 为什么错

官方把 Prepare 回包校验三条核心句写成三件独立的实现事。把它们卖成已经是 Process REJECT / 已经必须 Accept / 已经 ProposalStatus REJECT，会把三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Prepare 回包校验 crash 正式三事（357 余量），必须分开 not Process REJECT、not must Accept、not ProposalStatus REJECT 三件事，不要和 357 / 347 / 376 / 504 / 716 / 718 糊成一句。

## 和相邻反模式

- [preparevalid-sold-as-checked](preparevalid-sold-as-checked.md) 是 Prepare 回包校验 bundled（357），不是本页 item 2 单句边界。
- [prepvalid-notchecked-sold-as-bundled](prepvalid-notchecked-sold-as-bundled.md) 是 no checks 单句边界（716 item 1），不是本页 crash 边界。
