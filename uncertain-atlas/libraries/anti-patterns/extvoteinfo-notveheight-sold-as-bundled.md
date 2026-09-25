# 反模式：把扩展关掉则字段全空不是已经到了启用高度 not already ve-height / not already settled / not already from-block 正式三事（369 余量）说成已经到了启用高度 / 已经交差 / 已经从块里抽出

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[空着 not already ve-height ≠ bundled（369）](../../tracks/implementation/worked-example-extvoteinfo-notveheight-vs-bundled.md)。

## 卖法

把空着 / 扩展关掉则 `vote_extension` / `non_rp_vote_extension` 和对应的签都空 / 扩展字段空 写成已经到了启用高度 interchangeable / 已经 ve-height interchangeable / 已经到了启用高度交差 interchangeable / 369 extvoteinfo bundled interchangeable / extvoteinfo-sold-as-local interchangeable；把关掉了 / 投票扩展关掉 / 扩展关 写成已经交差 interchangeable / 已经 settled interchangeable / 已经交差交差 interchangeable；把字段在 / 扩展字段仍在报文里 / 字段还在 写成已经从块里抽出 interchangeable / 已经 from-block interchangeable / 已经从块里抽出交差 interchangeable，或已经和 369 extvoteinfo bundled / extvoteinfo-sold-as-local interchangeable / 856 extvoteinfo-notveheight interchangeable。

## 为什么错

官方把空着、不是已经交差、不是已经从块里抽出写成三件独立的实现事。把它们卖成 already ve-height interchangeable / already settled interchangeable / already from-block interchangeable，会把 not already ve-height、not already settled、not already from-block 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看扩展关掉则字段全空不是已经到了启用高度 not already ve-height / not already settled / not already from-block 正式三事（369 余量），必须分开 not already ve-height、not already settled、not already from-block 三件事，不要和 369 / 330 / 854 / 855 糊成一句。

## 和相邻反模式

- [extvoteinfo-sold-as-local](extvoteinfo-sold-as-local.md) 是 extvoteinfo bundled 全段，不是本页空着 item 3 单句边界。
- [extvoteinfo-notfromblock-sold-as-bundled](extvoteinfo-notfromblock-sold-as-bundled.md) 是从本进程抽出 not already from-block（369 item 1），不是本页 not already ve-height 边界。
- [extvoteinfo-notraw-sold-as-bundled](extvoteinfo-notraw-sold-as-bundled.md) 是把验过的签交给应用 not already raw（369 item 2），不是本页 not already settled 边界。
- [veheight-sold-as-prepared](veheight-sold-as-prepared.md) 是到了 H 就已经 Prepare 带了扩展（330），不是本页 not already ve-height 单句。
