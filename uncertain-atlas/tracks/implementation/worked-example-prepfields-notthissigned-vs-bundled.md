# 例：看见有上一高的票 / 看见带了扩展 / 看见能用上一高 is not already already this-signed interchangeable / already ve-at-h interchangeable / already settled interchangeable

**层次**：实现 / local_last_commit 是上一高度的预提交带扩展不是已经是本高度刚签的扩展 not already this-signed / not already ve-at-h / not already settled 正式三事（359 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) PrepareProposal Usage。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「local_last_commit 是上一高度的预提交带扩展不是已经是本高度刚签的扩展 not already this-signed / not already ve-at-h / not already settled 正式三事（359 余量）/ not 831 prepfields-notthissigned interchangeable / not 359 preparefields bundled interchangeable」，不是 Prepare 请求字段 bundled（359），也不是 Prepare 和 Process / Finalize 同一套字段不是已经跑过 Process（830 item 1 余量）或 height / time / proposer_address 对上拟议头不是已经知道本头哈希（832 item 3 余量）。不要另写怎样填 Prepare 请求字段。

## 官方三件事

规范把 Methods 里 `local_last_commit` 是上一高度的预提交、包括促成上一块决定的那些以及对应的投票扩展 和「已经是有上一高的票就已经是本高度刚签的扩展 interchangeable / 已经是带了扩展就已经到了 H 就已经 Prepare 带了扩展 interchangeable / 已经是能用上一高就已经交差 interchangeable / 已经是 preparefields bundled interchangeable」分开写成三件独立的实现事，不是「看见有上一高的票就已经是本高度刚签的扩展 interchangeable / 就已经到了 H 就已经 Prepare 带了扩展 interchangeable / 就已经交差 interchangeable」一件事：

1. **看见有上一高的票 / 看见 `local_last_commit` 是上一高度的预提交带扩展 / 看见有上一高的票 is not already 已经是本高度刚签的扩展 interchangeable / 已经 this-signed interchangeable / 已经是本高度刚签的 *e* 交差 interchangeable / 359 preparefields bundled interchangeable / 330 veheight interchangeable / preparefields-sold-as-same interchangeable，也不是已经 Prepare 请求字段 bundled（359） interchangeable / 831 prepfields-notthissigned interchangeable / 359 preparefields item 2 interchangeable，也不是已经 local_last_commit 是上一高度的预提交带扩展不是已经是本高度刚签的扩展 not already this-signed / not already ve-at-h / not already settled 正式三事 bundled（359 item 2 余量） interchangeable / 359 preparefields item 2 interchangeable，也不是已经跑过 Process（830） interchangeable / 832 prepfields-nothash interchangeable / 330 ve-at-h interchangeable，也不是已经到了 H 就已经 Prepare 带了扩展就已经是本高度刚签的扩展（330） interchangeable。**  
   官方写：`local_last_commit` 是上一高度的预提交，包括促成上一块决定的那些，以及对应的投票扩展。看见有上一高的票，不是已经是本高度刚签的 *e*。看见有上一高的票，不是已经 this-signed interchangeable——359 钉 bundled 三事，本页从 item 2 侧钉 not already this-signed 单句。看见 `local_last_commit` 是上一高度的预提交带扩展，不是已经 Prepare 请求字段 bundled（359） interchangeable——359 钉 bundled，本页钉 item 2 第一件事。看见有上一高的票，不是已经跑过 Process（830） interchangeable——830 另钉 item 1。看见有上一高的票，不是已经到了 H 就已经 Prepare 带了扩展就已经是本高度刚签的扩展（330） interchangeable——330 另钉。359 prepare-fields vs same bundled unbundling 在本页 item 2 续。

2. **看见带了扩展 / 看见上一高的预提交带投票扩展 / 看见有扩展挂上 is not already 已经到了 H 就已经 Prepare 带了扩展 interchangeable / 已经 ve-at-h interchangeable / 已经到了 H 交差 interchangeable / 359 preparefields bundled interchangeable / 330 veheight interchangeable，也不是已经 Prepare 请求字段 bundled（359） interchangeable / 831 prepfields-notthissigned interchangeable / 359 preparefields item 1 同一套 interchangeable / 359 preparefields item 3 拟议头 interchangeable，也不是已经 local_last_commit 是上一高度的预提交带扩展不是已经是本高度刚签的扩展 not already this-signed / not already ve-at-h / not already settled 正式三事 bundled（359 item 2 余量） interchangeable / 359 preparefields item 2 interchangeable，也不是已经是本高度刚签的扩展（本页第一件事） interchangeable。**  
   官方写：看见带了扩展，不是已经到了 H 就已经 Prepare 带了扩展。看见上一高的预提交带投票扩展，不是已经 ve-at-h interchangeable——本页钉 not already ve-at-h 单句。看见有扩展挂上，不是已经是本高度刚签的扩展（本页第一件事） interchangeable——三件事分开钉。359 prepare-fields vs same bundled unbundling 在本页 item 2 续。

3. **看见能用上一高 / 看见能用上一高度的预提交 / 看见上一高的票能进请求 is not already 已经交差 interchangeable / 已经 settled interchangeable / 已经交差交差 interchangeable / 359 preparefields bundled interchangeable / 33 fourgates interchangeable，也不是已经 Prepare 请求字段 bundled（359） interchangeable / 831 prepfields-notthissigned interchangeable / 359 preparefields item 1 / 359 preparefields item 3，也不是已经 local_last_commit 是上一高度的预提交带扩展不是已经是本高度刚签的扩展 not already this-signed / not already ve-at-h / not already settled 正式三事 bundled（359 item 2 余量） interchangeable / 359 preparefields item 2 interchangeable，也不是已经是本高度刚签的扩展（本页第一件事） interchangeable / 已经到了 H 就已经 Prepare 带了扩展（本页第二件事） interchangeable。**  
   官方写：看见能用上一高，不是已经交差。看见能用上一高度的预提交，不是已经 settled interchangeable——本页钉 not already settled 单句。看见上一高的票能进请求，不是已经到了 H 就已经 Prepare 带了扩展（本页第二件事） interchangeable——三件事分开钉。359 prepare-fields vs same bundled unbundling 在本页 item 2 续。

怎样填 Prepare 请求字段、怎样读 `local_last_commit`、怎样对头是规范里的做法，本页不抄。Prepare 请求字段 bundled（359）、Prepare 和 Process / Finalize 同一套字段不是已经跑过 Process（359 item 1 余量 / 830）、height / time / proposer_address 对上拟议头不是已经知道本头哈希（359 item 3 余量 / 832）、到了 H 就已经 Prepare 带了扩展（330）、Process 也会在提议者那边叫就已经不用再 Process（351）、候选已经是 ExecuteTxState（311）是另外那套，本页不抄。

## 官方为什么这样拆

- **有上一高的票 not already this-signed ≠ 359 / 330 interchangeable：** 官方把上一高和本高度刚签的扩展分开。
- **带了扩展 not already ve-at-h ≠ 已经到了 H 就已经 Prepare 带了扩展 interchangeable：** 官方把带了扩展和已经到了 H 分开。
- **能用上一高 not already settled ≠ 已经交差 interchangeable：** 官方把能用上一高和已经交差分开；359 prepare-fields vs same bundled unbundling 在本页 item 2 续。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 有上一高的票 | 不是 already this-signed | 不是到了 H 就已经 Prepare 带了扩展 alone（330） |
| 带了扩展 | 不是 already ve-at-h | 不是同一套 already ran-process alone（830） |
| 能用上一高 | 不是 already settled | 不是拟议头 already header-hash alone（832） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 local_last_commit 是上一高度的预提交带扩展不是已经是本高度刚签的扩展 not already this-signed / not already ve-at-h / not already settled 正式三事（359 余量），必须分开有上一高的票 是不是 already this-signed interchangeable / 359 preparefields bundled interchangeable / preparefields-sold-as-same interchangeable、带了扩展 是不是 already ve-at-h interchangeable、能用上一高 是不是 already settled interchangeable。可以跳过「看见有上一高的票就已经是本高度刚签的扩展 interchangeable / 就已经到了 H 就已经 Prepare 带了扩展 interchangeable / 就已经交差 interchangeable」。不要另写怎样填 Prepare 请求字段。359 prepare-fields vs same bundled unbundling 在本页 item 2 续（830 + 831）。

## 本页不抄

- 怎样填 Prepare 请求字段、怎样读 `local_last_commit`、怎样对头。
- Prepare 请求字段 bundled。那是不变量 359。
- Prepare 和 Process / Finalize 同一套字段不是已经跑过 Process。那是不变量 359 item 1 余量 / 830。
- height / time / proposer_address 对上拟议头不是已经知道本头哈希。那是不变量 359 item 3 余量 / 832。
- 到了 H 就已经 Prepare 带了扩展。那是不变量 330。
- Process 也会在提议者那边叫就已经不用再 Process。那是不变量 351。
- 候选已经是 ExecuteTxState。那是不变量 311。
