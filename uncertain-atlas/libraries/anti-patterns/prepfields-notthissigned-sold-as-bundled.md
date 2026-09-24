# 反模式：把 local_last_commit 是上一高度的预提交带扩展不是已经是本高度刚签的扩展 not already this-signed / not already ve-at-h / not already settled 正式三事（359 余量）说成已经是本高度刚签的扩展 / 已经到了 H 就已经 Prepare 带了扩展 / 已经交差

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[local_last_commit 上一高 not already this-signed ≠ bundled（359）](../../tracks/implementation/worked-example-prepfields-notthissigned-vs-bundled.md)。

## 卖法

把有上一高的票 / `local_last_commit` 是上一高度的预提交带扩展 / 有上一高的票 写成已经是本高度刚签的扩展 interchangeable / 已经 this-signed interchangeable / 已经是本高度刚签的 *e* 交差 interchangeable / 359 preparefields bundled interchangeable / preparefields-sold-as-same interchangeable；把带了扩展 / 上一高的预提交带投票扩展 写成已经到了 H 就已经 Prepare 带了扩展 interchangeable / 已经 ve-at-h interchangeable / 已经到了 H 交差 interchangeable；把能用上一高 / 能用上一高度的预提交 / 上一高的票能进请求 写成已经交差 interchangeable / 已经 settled interchangeable / 已经交差交差 interchangeable，或已经和 359 preparefields bundled / preparefields-sold-as-same interchangeable / 831 prepfields-notthissigned interchangeable。

## 为什么错

官方把有上一高的票、不是已经到了 H、不是已经交差写成三件独立的实现事。把它们卖成 already this-signed interchangeable / already ve-at-h interchangeable / already settled interchangeable，会把 not already this-signed、not already ve-at-h、not already settled 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 local_last_commit 是上一高度的预提交带扩展不是已经是本高度刚签的扩展 not already this-signed / not already ve-at-h / not already settled 正式三事（359 余量），必须分开 not already this-signed、not already ve-at-h、not already settled 三件事，不要和 359 / 330 / 351 / 830 / 832 糊成一句。

## 和相邻反模式

- [preparefields-sold-as-same](preparefields-sold-as-same.md) 是 Prepare 请求字段 bundled 全段，不是本页有上一高的票 item 2 单句边界。
- [veheight-sold-as-prepared](veheight-sold-as-prepared.md) 是到了 H 就已经 Prepare 带了扩展（330），不是本页 not already this-signed 边界。
- [prepfields-notprocess-sold-as-bundled](prepfields-notprocess-sold-as-bundled.md) 是同一套字段 not already ran-process（359 item 1），不是本页 not already settled 边界。
