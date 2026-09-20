# 例：看见 H+1 带了扩展 / 看见本高度刚签的那份 / 看见 Prepare 列表里有扩展 is not already already this-height-signed interchangeable / already local-e interchangeable / already same-h-e interchangeable

**层次**：实现 / H+1 带了扩展不是已经是本高度刚签的 not already this-height-signed / not already local-e / not already same-h-e 正式三事（330 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) List of Parameters / Application configuration required to switch to ABCI 2.0。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「H+1 带了扩展不是已经是本高度刚签的 not already this-height-signed / not already local-e / not already same-h-e 正式三事（330 余量）/ not 747 veheight-notthissigned interchangeable / not 330 veheight bundled interchangeable」，不是 VoteExtensionsEnableHeight bundled（330），也不是到了 H 不是已经 Prepare 带了扩展（746 item 1 余量）或 h < H 带了扩展不是已经合法（748 item 3 余量）。不要另写怎样设 VoteExtensionsEnableHeight 或怎样写空扩展。

## 官方三件事

规范把 Requirements 里到 H+1 才带高度 H 的扩展、带进来的不是本高度刚签、列表里有扩展不是这一高的 e 和「已经是 H+1 带了扩展就已经是本高度刚签 interchangeable / 已经是刚签的那份就已经是本高 e interchangeable / 已经是列表里有扩展就已经是同高 e interchangeable / 已经是 veheight bundled interchangeable」分开写成三件独立的实现事，不是「看见 H+1 带了扩展就已经是本高度刚签 interchangeable / 就已经是本高 e interchangeable / 就已经是同高 e interchangeable」一件事：

1. **看见 H+1 带了扩展 / 看见 H+1 的 Prepare 带了 / 看见到了 H+1 is not already 已经是本高度刚签的 interchangeable / 已经 this-height-signed interchangeable / 已经本高刚签交差 interchangeable / 330 veheight bundled interchangeable / 33 four gates interchangeable / veheight-sold-as-prepared interchangeable，也不是已经 VoteExtensionsEnableHeight bundled（330） interchangeable / 747 veheight-notthissigned interchangeable / 330 veheight item 2 interchangeable，也不是已经 H+1 带了扩展不是已经是本高度刚签的 not already this-height-signed / not already local-e / not already same-h-e 正式三事 bundled（330 item 2 余量） interchangeable / 330 veheight item 2 interchangeable，也不是已经到了 H 不是已经 Prepare 带了扩展（746） interchangeable / 748 veheight-notlegal interchangeable / 34 vote-extension interchangeable，也不是已经四门已经结算（33） interchangeable。**  
   官方写：到 **H+1**，`PrepareProposal` 才带 **高度 H** 的扩展。看见 H+1 带了扩展，不是已经 this-height-signed interchangeable——330 钉 bundled 三事，本页从 item 2 侧钉 not already this-height-signed 单句。看见 H+1 的 Prepare 带了，不是已经 VoteExtensionsEnableHeight bundled（330） interchangeable——330 钉 bundled，本页钉 item 2 第一件事。看见到了 H+1，不是已经到了 H 不是已经 Prepare 带了扩展（746） interchangeable——746 另钉 item 1。330 veheight vs prepare bundled unbundling 在本页 item 2 续。

2. **看见本高度刚签的那份 / 看见刚签的扩展 / 看见本高 e is not already 已经是本高 e interchangeable / 已经 local-e interchangeable / 已经本高 e 交差 interchangeable / 330 veheight bundled interchangeable / 34 vote-extension interchangeable，也不是已经 VoteExtensionsEnableHeight bundled（330） interchangeable / 747 veheight-notthissigned interchangeable / 330 veheight item 1 Prepare 带扩展 interchangeable / 330 veheight item 3 合法 interchangeable，也不是已经 H+1 带了扩展不是已经是本高度刚签的 not already this-height-signed / not already local-e / not already same-h-e 正式三事 bundled（330 item 2 余量） interchangeable / 330 veheight item 2 interchangeable，也不是已经是本高度刚签（本页第一件事） interchangeable。**  
   官方写：看见 H+1 带了扩展，不是已经是本高度刚签的那份。看见本高度刚签的那份，不是已经 local-e interchangeable——本页钉 not already local-e 单句。看见刚签的扩展，不是已经空扩展仍验签（34） interchangeable——34 另钉。看见本高 e，不是已经是本高度刚签（本页第一件事） interchangeable——三件事分开钉。330 veheight vs prepare bundled unbundling 在本页 item 2 续。

3. **看见 Prepare 列表里有扩展 / 看见这一高的 e / 看见同高 e is not already 已经是这一高的 e interchangeable / 已经 same-h-e interchangeable / 已经同高 e 交差 interchangeable / 330 veheight bundled interchangeable / 35 validator-set interchangeable，也不是已经 VoteExtensionsEnableHeight bundled（330） interchangeable / 747 veheight-notthissigned interchangeable / 330 veheight item 1 / 330 veheight item 3，也不是已经 H+1 带了扩展不是已经是本高度刚签的 not already this-height-signed / not already local-e / not already same-h-e 正式三事 bundled（330 item 2 余量） interchangeable / 330 veheight item 2 interchangeable，也不是已经是本高度刚签（本页第一件事） interchangeable / 已经是本高 e（本页第二件事） interchangeable。**  
   官方写：看见 Prepare 列表里有扩展，不是已经是这一高的 *e*。看见 Prepare 列表里有扩展，不是已经 same-h-e interchangeable——本页钉 not already same-h-e 单句。看见这一高的 e，不是已经验证人集合 H+1 / H+2 / H+3（35） interchangeable——35 另钉。看见同高 e，不是已经是本高 e（本页第二件事） interchangeable——三件事分开钉。330 veheight vs prepare bundled unbundling 在本页 item 2 完成。

怎样设 `VoteExtensionsEnableHeight`、默认 `0`、怎样写空扩展是规范里的取值或做法，本页不抄。VoteExtensionsEnableHeight bundled（330）、到了 H 不是已经 Prepare 带了扩展（330 item 1 余量 / 746）、h < H 带了扩展不是已经合法（330 item 3 余量 / 748）、验签拒收整张预提交（34）、验证人集合 H+1 / H+2 / H+3（35）、四门已经结算（33）是另外那套，本页不抄。

## 官方为什么这样拆

- **H+1 带了扩展 not already this-height-signed ≠ 330 / 33 interchangeable：** 官方把带进来的扩展和本高度刚签分开。
- **本高度刚签的那份 not already local-e ≠ 已经是本高 e interchangeable：** 官方把刚签的那份和已经是本高 e 分开。
- **Prepare 列表里有扩展 not already same-h-e ≠ 已经是这一高的 e interchangeable：** 官方把列表里有扩展和已经是同高 e 分开；330 veheight vs prepare bundled unbundling 在本页 item 2 完成。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| H+1 带了扩展 | 不是 already this-height-signed | 不是 Prepare 带扩展 alone（746） |
| 本高度刚签的那份 | 不是 already local-e | 不是验签拒收 alone（34） |
| Prepare 列表里有扩展 | 不是 already same-h-e | 不是验证人集合 alone（35） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 H+1 带了扩展不是已经是本高度刚签的 not already this-height-signed / not already local-e / not already same-h-e 正式三事（330 余量），必须分开 H+1 带了扩展 是不是 already this-height-signed interchangeable / 330 veheight bundled interchangeable / veheight-sold-as-prepared interchangeable、本高度刚签的那份 是不是 already local-e interchangeable、Prepare 列表里有扩展 是不是 already same-h-e interchangeable。可以跳过「看见 H+1 带了扩展就已经是本高度刚签 interchangeable / 就已经是本高 e interchangeable / 就已经是同高 e interchangeable」。不要另写怎样设 VoteExtensionsEnableHeight。330 veheight vs prepare bundled unbundling 在本页 item 2 续（746 + 747）；续 [`worked-example-veheight-notlegal-vs-bundled.md`](worked-example-veheight-notlegal-vs-bundled.md)（不变量 748 item 3）已写；完成见 748。

## 本页不抄

- 怎样设 `VoteExtensionsEnableHeight`、默认 `0`、怎样写空扩展。
- VoteExtensionsEnableHeight bundled。那是不变量 330。
- 到了 H 不是已经 Prepare 带了扩展。那是不变量 330 item 1 余量 / 746。
- h < H 带了扩展不是已经合法。那是不变量 330 item 3 余量 / 748。
- 验签拒收整张预提交、空扩展仍验签。那是不变量 34。
- 验证人集合 H+1 / H+2 / H+3。那是不变量 35。
- 四门已经结算。那是不变量 33。
