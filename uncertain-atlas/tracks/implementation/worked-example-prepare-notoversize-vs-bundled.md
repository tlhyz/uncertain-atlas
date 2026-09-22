# 例：看见聚合体积可以超过 max_tx_bytes / 看见池子加起来比这次上限大 / 看见能看见超限的池 is not already already can-return-oversize interchangeable / already request-trimmed interchangeable / already settled interchangeable

**层次**：实现 / 聚合体积可以超过 max_tx_bytes 不是已经能回超限列表 not already can-return-oversize / not already request-trimmed / not already settled 正式三事（345 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Formal Requirement 2 [`PrepareProposal`, tx-size]。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「聚合体积可以超过 max_tx_bytes 不是已经能回超限列表 not already can-return-oversize / not already request-trimmed / not already settled 正式三事（345 余量）/ not 789 prepare-notoversize interchangeable / not 345 preparereturn bundled interchangeable」，不是 PrepareProposal 回包上限 bundled（345），也不是整池可见不是已经只能看见装得进一块的子集（788 item 1 余量）或 Req 2 保证回的列表不让块超字节上限不是已经是引擎会帮你裁（790 item 3 余量）。不要另写怎样裁回包。

## 官方三件事

规范把 Requirements 里所有交易加起来的体积可以超过这次请求里的 `max_tx_bytes` 和「已经是池子超了就已经能回超限列表 interchangeable / 已经是请求里带了上限就已经按上限裁过 interchangeable / 已经是能看见超限的池就已经交差 interchangeable / 已经是 preparereturn bundled interchangeable」分开写成三件独立的实现事，不是「看见聚合体积可以超过 max_tx_bytes 就已经能回超限列表 interchangeable / 就已经按请求裁过 interchangeable / 就已经交差 interchangeable」一件事：

1. **看见聚合体积可以超过 `PrepareProposalRequest.max_tx_bytes` / 看见池子加起来比这次上限大 / 看见所有交易加起来可以超 is not already 已经能回超限列表 interchangeable / 已经 can-return-oversize interchangeable / 已经回超限交差 interchangeable / 345 preparereturn bundled interchangeable / 299 evidence-tx interchangeable / preparereturn-sold-as-trimmed interchangeable，也不是已经 PrepareProposal 回包上限 bundled（345） interchangeable / 789 prepare-notoversize interchangeable / 345 preparereturn item 2 interchangeable，也不是已经聚合体积可以超过 max_tx_bytes 不是已经能回超限列表 not already can-return-oversize / not already request-trimmed / not already settled 正式三事 bundled（345 item 2 余量） interchangeable / 345 preparereturn item 2 interchangeable，也不是已经整池可见不是已经只能看见一块子集（788） interchangeable / 790 prepare-notenginecut interchangeable / 337 maxbytescap interchangeable，也不是已经整池都给 Prepare 就已经没有上限（299） interchangeable。**  
   官方写：在这种设置下，**所有交易加起来的体积可以超过**这次请求里的 `max_tx_bytes`。看见池子比上限大，不是已经能整包交回去。看见聚合体积可以超过 max_tx_bytes，不是已经 can-return-oversize interchangeable——345 钉 bundled 三事，本页从 item 2 侧钉 not already can-return-oversize 单句。看见池子加起来比这次上限大，不是已经 PrepareProposal 回包上限 bundled（345） interchangeable——345 钉 bundled，本页钉 item 2 第一件事。看见所有交易加起来可以超，不是已经整池都给 Prepare 就已经没有上限（299） interchangeable——299 另钉。345 preparereturn vs pool bundled unbundling 在本页 item 2 续。

2. **看见请求里带了上限 / 看见 `max_tx_bytes` 在请求里 / 看见这次上限写在请求上 is not already 已经按这个上限裁过 interchangeable / 已经 request-trimmed interchangeable / 已经裁过交差 interchangeable / 345 preparereturn bundled interchangeable / 337 maxbytescap interchangeable / maxbytescap-sold-as-unlimited interchangeable，也不是已经 PrepareProposal 回包上限 bundled（345） interchangeable / 789 prepare-notoversize interchangeable / 345 preparereturn item 1 整池可见 interchangeable / 345 preparereturn item 3 引擎裁 interchangeable，也不是已经聚合体积可以超过 max_tx_bytes 不是已经能回超限列表 not already can-return-oversize / not already request-trimmed / not already settled 正式三事 bundled（345 item 2 余量） interchangeable / 345 preparereturn item 2 interchangeable，也不是已经能回超限列表（本页第一件事） interchangeable。**  
   官方写：看见请求里带了上限，不是池子已经按这个上限裁过。看见 `max_tx_bytes` 在请求里，不是已经 request-trimmed interchangeable——本页钉 not already request-trimmed 单句。看见这次上限写在请求上，不是已经能回超限列表（本页第一件事） interchangeable——三件事分开钉。345 preparereturn vs pool bundled unbundling 在本页 item 2 续。

3. **看见能看见超限的池 / 看见池子比上限大还交来 / 看见超限池仍可见 is not already 已经交差 interchangeable / 已经 settled interchangeable / 已经回包交差 interchangeable / 345 preparereturn bundled interchangeable / 790 prepare-notenginecut interchangeable，也不是已经 PrepareProposal 回包上限 bundled（345） interchangeable / 789 prepare-notoversize interchangeable / 345 preparereturn item 1 / 345 preparereturn item 3，也不是已经聚合体积可以超过 max_tx_bytes 不是已经能回超限列表 not already can-return-oversize / not already request-trimmed / not already settled 正式三事 bundled（345 item 2 余量） interchangeable / 345 preparereturn item 2 interchangeable，也不是已经能回超限列表（本页第一件事） interchangeable / 已经按请求裁过（本页第二件事） interchangeable。**  
   官方写：看见能看见超限的池，不是已经能回超限。看见池子比上限大还交来，不是已经 settled interchangeable——本页钉 not already settled 单句。看见超限池仍可见，不是已经按请求裁过（本页第二件事） interchangeable——三件事分开钉。345 preparereturn vs pool bundled unbundling 在本页 item 2 续。

怎样裁回包、怎样设 `MaxBytes = -1`、默认取值是规范里的做法，本页不抄。PrepareProposal 回包上限 bundled（345）、整池可见不是已经只能看见装得进一块的子集（345 item 1 余量 / 788）、Req 2 保证回的列表不让块超字节上限不是已经是引擎会帮你裁（345 item 3 余量 / 790）、整池都给 Prepare 就已经没有上限（299）、-1 就按 100 MB 验已经没有上限（337）、MaxBytes 减去头集合证据才是交易上限（344）是另外那套，本页不抄。

## 官方为什么这样拆

- **聚合体积可以超过 max_tx_bytes not already can-return-oversize ≠ 345 / 299 interchangeable：** 官方把池子可以超这次上限和已经能回超限列表分开。
- **请求里带了上限 not already request-trimmed ≠ 已经按上限裁过 interchangeable：** 官方把请求里写了上限和池子已经裁过分开。
- **能看见超限的池 not already settled ≠ 已经交差 interchangeable：** 官方把能看见超限的池和已经交差分开；345 preparereturn vs pool bundled unbundling 在本页 item 2 续。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 聚合体积可以超过 max_tx_bytes | 不是 already can-return-oversize | 不是整池都给 Prepare 就已经没有上限 alone（299） |
| 请求里带了上限 | 不是 already request-trimmed | 不是整池可见不是已经只能看见一块子集 alone（788） |
| 能看见超限的池 | 不是 already settled | 不是 Req 2 引擎会帮你裁 alone（790） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看聚合体积可以超过 max_tx_bytes 不是已经能回超限列表 not already can-return-oversize / not already request-trimmed / not already settled 正式三事（345 余量），必须分开聚合体积可以超过 max_tx_bytes 是不是 already can-return-oversize interchangeable / 345 preparereturn bundled interchangeable / preparereturn-sold-as-trimmed interchangeable、请求里带了上限 是不是 already request-trimmed interchangeable、能看见超限的池 是不是 already settled interchangeable。可以跳过「看见聚合体积可以超过 max_tx_bytes 就已经能回超限列表 interchangeable / 就已经按请求裁过 interchangeable / 就已经交差 interchangeable」。不要另写怎样裁回包。345 preparereturn vs pool bundled unbundling 在本页 item 2 续（788 + 789）；续 [`worked-example-prepare-notenginecut-vs-bundled.md`](worked-example-prepare-notenginecut-vs-bundled.md)（不变量 790 item 3）；完成见 790。

## 本页不抄

- 怎样裁回包、怎样设 `MaxBytes = -1`、默认取值。
- PrepareProposal 回包上限 bundled。那是不变量 345。
- 整池可见不是已经只能看见装得进一块的子集。那是不变量 345 item 1 余量 / 788。
- Req 2 保证回的列表不让块超字节上限不是已经是引擎会帮你裁。那是不变量 345 item 3 余量 / 790。
- 整池都给 Prepare 就已经没有上限。那是不变量 299。
- -1 就按 100 MB 验已经没有上限。那是不变量 337。
- MaxBytes 减去头集合证据才是交易上限。那是不变量 344。
