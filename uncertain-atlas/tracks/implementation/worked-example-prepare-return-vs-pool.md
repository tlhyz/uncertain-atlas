# 例：看见整池可见不是已经只能看见装得进一块的子集；看见聚合体积可以超过 max_tx_bytes 不是已经能回超限列表；看见 Req 2 保证回的列表不让块超字节上限不是已经是引擎会帮你裁

**层次**：实现 / PrepareProposal 回包上限。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Formal Requirement 2 [`PrepareProposal`, tx-size]。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5。本页是「整池可见不是已经只能看见装得进一块的子集 / 聚合体积可以超过 max_tx_bytes 不是已经能回超限列表 / Req 2 保证回的列表不让块超字节上限不是已经是引擎会帮你裁」，不是整池都给 Prepare 就已经没有上限，也不是 -1 就按 100 MB 验已经没有上限。不要另写怎样裁回包。345 preparereturn vs pool bundled unbundling 完成（788+789+790）；精读 [`worked-example-prepare-notblocksubset-vs-bundled.md`](worked-example-prepare-notblocksubset-vs-bundled.md)（不变量 788 item 1）、[`worked-example-prepare-notoversize-vs-bundled.md`](worked-example-prepare-notoversize-vs-bundled.md)（不变量 789 item 2）、[`worked-example-prepare-notenginecut-vs-bundled.md`](worked-example-prepare-notenginecut-vs-bundled.md)（不变量 790 item 3）。

## 官方三件事

规范把 Prepare 回包上限写成三件独立的实现事，不是「看见整池都给了就已经能整包交回去、已经超了就能回超限、已经是引擎会帮你裁」一件事：

1. **看见整池可见 / 看见 MaxBytes 写成 -1 把池子都交来 不是已经只能看见装得进一块的子集，也不是已经没有上限。**  
   官方写：忙链可能想**看见内存池里全部交易**，而不是只看见装得进一块的那一子集。应用可以把 `ConsensusParams.Block.MaxBytes` 写成 -1，让引擎按最大可能的 `MaxBytes`（100 MB）验，并把池子里所有交易交给 `PrepareProposal`。看见整池都来了，不是已经只能看见装得进一块的那些。看见能看见全部，不是已经没有上限。
2. **看见聚合体积可以超过 `PrepareProposalRequest.max_tx_bytes` / 看见池子加起来比这次上限大 不是已经能回超限列表，也不是已经交差。**  
   官方写：在这种设置下，**所有交易加起来的体积可以超过**这次请求里的 `max_tx_bytes`。看见池子比上限大，不是已经能整包交回去。看见请求里带了上限，不是池子已经按这个上限裁过。看见能看见超限的池，不是已经能回超限。
3. **看见 Requirement 2 保证回的列表不让块超字节上限 / 看见回包不得超过 `max_tx_bytes` 不是已经是引擎会帮你裁，也不是已经是 MaxBytes 扣掉头集合证据之后的交易上限。**  
   官方写：因此 Requirement 2 保证应用回的交易列表体积**永远不会**让这块超过字节上限。看见有这道要求，不是引擎已经替你裁。看见回包绿了，不是已经扣过开销。看见块不会超，不是已经是 344 那种扣掉头 / 集合 / 证据才是交易上限。

怎样裁回包、怎样设 `MaxBytes = -1`、默认取值是规范里的做法，本页不抄。整池都给 Prepare 不是已经没有上限是不变量 299，本页不抄。

## 官方为什么这样拆

- **整池可见 ≠ 已经只能看见装得进一块的子集：** 官方把看见全部和只看见装得进一块分开。
- **聚合体积可以超过 max_tx_bytes ≠ 已经能回超限列表：** 官方把池子可以超这次上限和回包仍不得超过分开。
- **Req 2 保证回的列表不让块超字节上限 ≠ 已经是引擎会帮你裁：** 官方把应用必须守回包上限和引擎替你裁分开。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 整池可见 | 不是已经只能看见装得进一块的子集 | 不是整池都给 Prepare 就已经没有上限（299） |
| 聚合体积可以超过 max_tx_bytes | 不是已经能回超限列表 | 不是 -1 就按 100 MB 验已经没有上限（337） |
| Req 2 保证回的列表不让块超字节上限 | 不是已经是引擎会帮你裁 | 不是 MaxBytes 减去头集合证据才是交易上限（344）；不是四门已经结算（33） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看「看见整池都给了就已经能整包交回去、已经超了就能回超限、已经是引擎会帮你裁」，必须分开整池可见是不是已经只能看见装得进一块的子集、聚合体积可以超过 max_tx_bytes 是不是已经能回超限列表、Req 2 保证回的列表不让块超字节上限是不是已经是引擎会帮你裁。可以跳过「看见整池都给了就已经能整包交回去」。不要另写怎样裁回包。345 preparereturn vs pool bundled unbundling 完成（788+789+790）。

## 本页不抄

- 怎样裁回包、怎样设 `MaxBytes = -1`、默认取值。
- 整池都给 Prepare 就已经没有上限。那是不变量 299。
- -1 就按 100 MB 验已经没有上限。那是不变量 337。
- MaxBytes 减去头集合证据才是交易上限。那是不变量 344。
- 四门已经结算。那是不变量 33。
