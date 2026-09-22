# 例：看见整池可见 / 看见 MaxBytes 写成 -1 把池子都交来 / 看见能看见全部 is not already already block-subset interchangeable / already no-cap interchangeable / already all-visible-is-uncapped interchangeable

**层次**：实现 / 整池可见不是已经只能看见装得进一块的子集 not already block-subset / not already no-cap / not already all-visible-is-uncapped 正式三事（345 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Formal Requirement 2 [`PrepareProposal`, tx-size]。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「整池可见不是已经只能看见装得进一块的子集 not already block-subset / not already no-cap / not already all-visible-is-uncapped 正式三事（345 余量）/ not 788 prepare-notblocksubset interchangeable / not 345 preparereturn bundled interchangeable」，不是 PrepareProposal 回包上限 bundled（345），也不是聚合体积可以超过 max_tx_bytes 不是已经能回超限列表（789 item 2 余量）或 Req 2 保证回的列表不让块超字节上限不是已经是引擎会帮你裁（790 item 3 余量）。不要另写怎样裁回包。

## 官方三件事

规范把 Requirements 里忙链可能想看见内存池里全部交易、而不是只看见装得进一块的那一子集 和「已经是整池都来了就已经只能看见装得进一块的子集 interchangeable / 已经是能看见全部就已经没有上限 interchangeable / 已经是整池可见就已经无上限交差 interchangeable / 已经是 preparereturn bundled interchangeable」分开写成三件独立的实现事，不是「看见整池可见就已经只能看见装得进一块的子集 interchangeable / 就已经没有上限 interchangeable / 就已经整包能回 interchangeable」一件事：

1. **看见整池可见 / 看见 MaxBytes 写成 -1 把池子都交来 / 看见池子里所有交易交给 PrepareProposal is not already 已经只能看见装得进一块的子集 interchangeable / 已经 block-subset interchangeable / 已经只看见一块子集交差 interchangeable / 345 preparereturn bundled interchangeable / 299 evidence-tx interchangeable / preparereturn-sold-as-trimmed interchangeable，也不是已经 PrepareProposal 回包上限 bundled（345） interchangeable / 788 prepare-notblocksubset interchangeable / 345 preparereturn item 1 interchangeable，也不是已经整池可见不是已经只能看见装得进一块的子集 not already block-subset / not already no-cap / not already all-visible-is-uncapped 正式三事 bundled（345 item 1 余量） interchangeable / 345 preparereturn item 1 interchangeable，也不是已经聚合体积可以超过 max_tx_bytes（789） interchangeable / 790 prepare-notenginecut interchangeable / 337 maxbytescap interchangeable，也不是已经整池都给 Prepare 就已经没有上限（299） interchangeable。**  
   官方写：忙链可能想**看见内存池里全部交易**，而不是只看见装得进一块的那一子集。应用可以把 `ConsensusParams.Block.MaxBytes` 写成 -1，让引擎按最大可能的 `MaxBytes`（100 MB）验，并把池子里所有交易交给 `PrepareProposal`。看见整池都来了，不是已经只能看见装得进一块的那些。看见整池可见，不是已经 block-subset interchangeable——345 钉 bundled 三事，本页从 item 1 侧钉 not already block-subset 单句。看见 MaxBytes 写成 -1 把池子都交来，不是已经 PrepareProposal 回包上限 bundled（345） interchangeable——345 钉 bundled，本页钉 item 1 第一件事。看见整池可见，不是已经整池都给 Prepare 就已经没有上限（299） interchangeable——299 另钉。345 preparereturn vs pool bundled unbundling 在本页 item 1 启动。

2. **看见能看见全部 / 看见池子都交来 / 看见不是只交一块子集 is not already 已经没有上限 interchangeable / 已经 no-cap interchangeable / 已经无上限交差 interchangeable / 345 preparereturn bundled interchangeable / 337 maxbytescap interchangeable / maxbytescap-sold-as-unlimited interchangeable，也不是已经 PrepareProposal 回包上限 bundled（345） interchangeable / 788 prepare-notblocksubset interchangeable / 345 preparereturn item 2 超限列表 interchangeable / 345 preparereturn item 3 引擎裁 interchangeable，也不是已经整池可见不是已经只能看见装得进一块的子集 not already block-subset / not already no-cap / not already all-visible-is-uncapped 正式三事 bundled（345 item 1 余量） interchangeable / 345 preparereturn item 1 interchangeable，也不是已经只能看见装得进一块的子集（本页第一件事） interchangeable。**  
   官方写：看见能看见全部，不是已经没有上限。看见池子都交来，不是已经 no-cap interchangeable——本页钉 not already no-cap 单句。看见不是只交一块子集，不是已经只能看见装得进一块的子集（本页第一件事） interchangeable——三件事分开钉。345 preparereturn vs pool bundled unbundling 在本页 item 1 启动。

3. **看见整池都来了 / 看见全部交易在请求里 / 看见 -1 把池子交齐 is not already 已经整包能回 interchangeable / 已经 all-visible-is-uncapped interchangeable / 已经整包交差 interchangeable / 345 preparereturn bundled interchangeable / 789 prepare-notoversize interchangeable，也不是已经 PrepareProposal 回包上限 bundled（345） interchangeable / 788 prepare-notblocksubset interchangeable / 345 preparereturn item 2 / 345 preparereturn item 3，也不是已经整池可见不是已经只能看见装得进一块的子集 not already block-subset / not already no-cap / not already all-visible-is-uncapped 正式三事 bundled（345 item 1 余量） interchangeable / 345 preparereturn item 1 interchangeable，也不是已经只能看见装得进一块的子集（本页第一件事） interchangeable / 已经没有上限（本页第二件事） interchangeable。**  
   官方写：看见整池都来了，不是已经能整包交回去。看见全部交易在请求里，不是已经 all-visible-is-uncapped interchangeable——本页钉 not already all-visible-is-uncapped 单句。看见 -1 把池子交齐，不是已经没有上限（本页第二件事） interchangeable——三件事分开钉。345 preparereturn vs pool bundled unbundling 在本页 item 1 启动。

怎样裁回包、怎样设 `MaxBytes = -1`、默认取值是规范里的做法，本页不抄。PrepareProposal 回包上限 bundled（345）、聚合体积可以超过 max_tx_bytes 不是已经能回超限列表（345 item 2 余量 / 789）、Req 2 保证回的列表不让块超字节上限不是已经是引擎会帮你裁（345 item 3 余量 / 790）、整池都给 Prepare 就已经没有上限（299）、-1 就按 100 MB 验已经没有上限（337）、MaxBytes 减去头集合证据才是交易上限（344）是另外那套，本页不抄。

## 官方为什么这样拆

- **整池可见 not already block-subset ≠ 345 / 299 interchangeable：** 官方把看见全部和只看见装得进一块分开。
- **能看见全部 not already no-cap ≠ 已经没有上限 interchangeable：** 官方把能看见全部和已经没有上限分开。
- **整池都来了 not already all-visible-is-uncapped ≠ 已经整包能回 interchangeable：** 官方把整池可见和已经能整包交回去分开；345 preparereturn vs pool bundled unbundling 在本页 item 1 启动。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 整池可见 | 不是 already block-subset | 不是整池都给 Prepare 就已经没有上限 alone（299） |
| 能看见全部 | 不是 already no-cap | 不是聚合体积可以超过 max_tx_bytes alone（789） |
| 整池都来了 | 不是 already all-visible-is-uncapped | 不是 Req 2 引擎会帮你裁 alone（790） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看整池可见不是已经只能看见装得进一块的子集 not already block-subset / not already no-cap / not already all-visible-is-uncapped 正式三事（345 余量），必须分开整池可见 是不是 already block-subset interchangeable / 345 preparereturn bundled interchangeable / preparereturn-sold-as-trimmed interchangeable、能看见全部 是不是 already no-cap interchangeable、整池都来了 是不是 already all-visible-is-uncapped interchangeable。可以跳过「看见整池都给了就已经能整包交回去 interchangeable / 就已经没有上限 interchangeable / 就已经只能看见一块子集 interchangeable」。不要另写怎样裁回包。345 preparereturn vs pool bundled unbundling 在本页 item 1 启动；续 [`worked-example-prepare-notoversize-vs-bundled.md`](worked-example-prepare-notoversize-vs-bundled.md)（不变量 789 item 2）；完成见 790。

## 本页不抄

- 怎样裁回包、怎样设 `MaxBytes = -1`、默认取值。
- PrepareProposal 回包上限 bundled。那是不变量 345。
- 聚合体积可以超过 max_tx_bytes 不是已经能回超限列表。那是不变量 345 item 2 余量 / 789。
- Req 2 保证回的列表不让块超字节上限不是已经是引擎会帮你裁。那是不变量 345 item 3 余量 / 790。
- 整池都给 Prepare 就已经没有上限。那是不变量 299。
- -1 就按 100 MB 验已经没有上限。那是不变量 337。
- MaxBytes 减去头集合证据才是交易上限。那是不变量 344。
