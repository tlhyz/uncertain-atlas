# 反模式：把头字段对上余量 proposer prepare five steps not already no Process 正式三事卖成头字段对上余量 bundled / 已经不用再 Process / 已经保证是这一次

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[头字段对上余量 proposer prepare five steps not already no Process ≠ bundled](../../tracks/implementation/worked-example-htmatch-notproprocess-vs-bundled.md)。

## 卖法

- 「看见自己是提议者会先走完 Prepare 那五步 / 看见走完了 就已经不用再 Process interchangeable / 已经头字段对上余量 bundled interchangeable。」
- 「看见自己是提议者走完了 Prepare 就已经保证是这一次 interchangeable / 已经列表对得上 interchangeable。」
- 「看见先走 Prepare 就已经 Process follows Prepare interchangeable / 已经 ProcessProposalRequest.txs equals PrepareProposalResponse.txs interchangeable。」

## 为什么错

官方把 When 里若 *p* 是提议者、*p* 先执行 Prepare 那五步，和 Process 也会在提议者那边叫、通常紧跟 Prepare、列表对得上写成三件独立的实现事。把它们卖成头字段对上余量 bundled、已经不用再 Process、已经保证是这一次，会把 proposer prepare not no Process、proposer prepare not guarantee this proposal、proposer prepare not Process follows Prepare 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看头字段对上余量 proposer prepare five steps not already no Process 正式三事，必须分开 proposer prepare not no Process、proposer prepare not guarantee this proposal、proposer prepare not Process follows Prepare 三个名字，不要把它们卖成头字段对上余量 bundled / 已经不用再 Process / 已经保证是这一次。

## 和相邻反模式

- [htmatch-sold-as-header](htmatch-sold-as-header.md) 是 417 bundled 三事专用，不是本页 proposer prepare not no Process 单句边界。
- [processalso-sold-as-matched](processalso-sold-as-matched.md) 是 351 Process 也会在提议者那边叫，不是本页 When 先走 Prepare 五步边界。
