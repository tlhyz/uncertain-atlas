# 例：看见 H+1 带了扩展 is not already this-height just-signed interchangeable / not already this-height e interchangeable / not already settled interchangeable

**层次**：实现 / H+1 带了扩展 not already this-height just-signed / not already this-height e / not already settled 正式三事（330 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) List of Parameters / Application configuration required to switch to ABCI 2.0。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行。本页是「H+1 带了扩展 not already this-height just-signed / not already this-height e / not already settled 正式三事（330 余量）/ not 927 ve-height-notthis interchangeable / not 330 ve-height-vs-prepare bundled interchangeable」，不是扩展启用 bundled（330），也不是治理改 enable-height 会让未升级节点 panic（58），也不是验证人集合 H+1 / H+2 / H+3（35）。不要另写怎样设 VoteExtensionsEnableHeight 或怎样写空扩展。

## 官方三件事

1. **看见 H+1 的 PrepareProposal 带了扩展 / 看见 Prepare 列表里有扩展 这份列表 is not already 已经是本高度刚签的扩展 interchangeable，也不是已经扩展启用 bundled（330） interchangeable / 927 ve-height-notthis interchangeable / 926 ve-height-notprep interchangeable / 330 ve-height item 1 到了 H interchangeable，也不是已经 H+1 带了扩展 not already this-height just-signed / not already this-height e / not already settled 正式三事 bundled（330 item 2 余量） interchangeable / 330 ve-height item 2 interchangeable。**  
   官方写：到 H+1，PrepareProposal 才带高度 H 的扩展。看见 H+1 带了扩展，不是已经是本高度刚签的那份 interchangeable——本页从 330 item 2 侧钉 not already this-height just-signed 单句。330 ve-height vs prepare bundled unbundling 在本页 item 2 续。

2. **看见 Prepare 列表里有扩展 / 看见 H+1 带了扩展 / 这份列表 is not already 已经是这一高的 e interchangeable，也不是已经扩展启用 bundled（330） interchangeable / 927 ve-height-notthis interchangeable / 330 ve-height item 3 h < H interchangeable / 928 ve-height-notlegal interchangeable，也不是已经治理改 enable-height 会让未升级节点 panic interchangeable / 58 enable-height-panic interchangeable。**  
   官方把 Prepare 列表里有扩展和已经是这一高的 e 分开——330 bundled 第二件事常与 58 混成「看见 H+1 带了扩展就已经是本高度刚签的或已经是治理切换 interchangeable」，本页钉 not already this-height e 单句。

3. **看见 Prepare 列表里有扩展 / 看见 H+1 带了扩展 / 这份列表 is not already 已经交差 interchangeable，也不是已经扩展启用 bundled（330） interchangeable / 927 ve-height-notthis interchangeable / 926 ve-height-notprep interchangeable，也不是已经验证人集合 H+1 / H+2 / H+3 interchangeable / 35 valset-delay interchangeable。**  
   官方把列表里有扩展和已经交差分开。看见列表里有扩展，不是已经交差 interchangeable。330 ve-height vs prepare bundled unbundling 在本页 item 2 续。

怎样设 VoteExtensionsEnableHeight、默认 0、怎样写空扩展是规范里的取值或做法，本页不抄。

## 官方为什么这样拆

- **H+1 带了扩展 not already this-height just-signed ≠ 已经是本高度刚签的 interchangeable：** 官方把带进来的扩展和本高度刚签的扩展分开。
- **看见 Prepare 列表里有扩展 not already this-height e ≠ 已经是这一高的 e interchangeable：** 官方把列表里有扩展和已经是这一高的 e 分开。
- **看见 Prepare 列表里有扩展 not already settled ≠ 已经交差 interchangeable：** 官方把列表里有扩展和已经交差分开；330 ve-height vs prepare bundled unbundling 在本页 item 2 续。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| H+1 带了扩展 | 不是已经是本高度刚签的 | 不是治理改 enable-height 会让未升级节点 panic（58） |
| 看见 Prepare 列表里有扩展 | 不是已经是这一高的 e | 不是验证人集合 H+1 / H+2 / H+3（35） |
| 看见 H+1 带了扩展 | 不是已经交差 | 不是到了 H 就已经 Prepare 带了扩展（926） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 H+1 带了扩展 not already this-height just-signed / not already this-height e / not already settled 正式三事（330 余量），必须分开是不是已经是本高度刚签的、是不是已经是这一高的 e、是不是已经交差。可以跳过「看见 H+1 带了扩展就已经是本高刚签的」。不要另写怎样设 VoteExtensionsEnableHeight 或怎样写空扩展。330 ve-height vs prepare bundled unbundling 在本页 item 2 续；续 [`worked-example-ve-height-notlegal-vs-bundled.md`](worked-example-ve-height-notlegal-vs-bundled.md)（不变量 928 item 3）。

## 本页不抄

- 怎样设 VoteExtensionsEnableHeight、默认 0、怎样写空扩展。
- 扩展启用 bundled。那是不变量 330。
- 到了 H 就已经 Prepare 带了扩展。那是不变量 330 item 1 余量 / 926。
- 治理改 enable-height 会让未升级节点 panic。那是不变量 58。
- 验证人集合 H+1 / H+2 / H+3。那是不变量 35。
