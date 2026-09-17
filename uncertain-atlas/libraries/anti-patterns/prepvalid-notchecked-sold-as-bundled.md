# 反模式：把 Prepare 回包校验 no extra checks not already checked / not app-level replay / not pool dedup 正式三事（357 余量） 说成已经验过重复 / 已经有应用级重放保护 / 已经池门去重交差

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[no ≠ bundled（357）](../../tracks/implementation/worked-example-prepvalid-notchecked-vs-bundled.md)。

## 卖法

把 Prepare 回包校验这句写成已经已经验过重复 / 已经有应用级重放保护 / 已经池门去重交差 interchangeable，或已经和 357 prepare-valid-vs-checked bundled / prepvalid-notchecked-sold-as-bundled interchangeable。

## 为什么错

官方把 Prepare 回包校验三条核心句写成三件独立的实现事。把它们卖成已经验过重复 / 已经有应用级重放保护 / 已经池门去重交差，会把三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Prepare 回包校验 no extra checks 正式三事（357 余量），必须分开 not already checked、not app-level replay、not pool dedup 三件事，不要和 357 / 313 / 504 / 717 / 718 糊成一句。

## 和相邻反模式

- [preparevalid-sold-as-checked](preparevalid-sold-as-checked.md) 是 Prepare 回包校验 bundled（357），不是本页 item 1 单句边界。
- [prepvalid-notcrash-sold-as-bundled](prepvalid-notcrash-sold-as-bundled.md) 是 crash 单句边界（717 item 2），不是本页 no checks 边界。
