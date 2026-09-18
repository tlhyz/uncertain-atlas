# 例：看见 FinalizeBlockResponse.app_hash is not already next-header interchangeable / not already this-header interchangeable / not already index-only interchangeable

**层次**：实现 / FinalizeBlockResponse.app_hash not already next-header / not already this-header / not already index-only 正式三事（432 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) FinalizeBlock Response / Usage。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「FinalizeBlockResponse.app_hash not already next-header / not already this-header / not already index-only 正式三事（432 余量）/ not 1074 fend-notapphash interchangeable / not 432 finrespend-vs-params bundled interchangeable」，不是 Finalize 回包末栏 bundled（432），也不是 Finalize 回包 app_hash 可以空或硬编码就已经印进本头（404），也不是 Finalize 回包 events 标成非确定那种只是索引。不要另写怎样写 Finalize 回包末栏。

## 官方三件事

1. **看见 FinalizeBlockResponse.app_hash 是应用状态默克尔根 / 看见回了 app_hash 这份栏 is not already 已经写进下一块头的 AppHash interchangeable，也不是已经 Finalize 回包末栏 bundled（432） interchangeable / 1074 fend-notapphash interchangeable / 1073 fend-notheffect interchangeable / 432 finrespend item 1 cparam interchangeable，也不是已经 FinalizeBlockResponse.app_hash not already next-header / not already this-header / not already index-only 正式三事 bundled（432 item 2 余量） interchangeable / 432 finrespend item 2 interchangeable。**  
   官方写：app_hash 是 The Merkle root hash of the application state。Deterministic 列是 Yes。Usage 也写：FinalizeBlockResponse.app_hash 会作为下一块头的 Header.AppHash。看见回了根，不是已经写进下一块头 interchangeable——这块刚 Commit，下一块还没造。本页从 432 item 2 侧钉 not already next-header 单句。432 finrespend vs params bundled unbundling 在本页 item 2 续。

2. **看见有默克尔根 / 看见回了 app_hash / 这份栏 is not already 已经是本头 AppHash interchangeable，也不是已经 Finalize 回包末栏 bundled（432） interchangeable / 1074 fend-notapphash interchangeable / 432 finrespend item 3 delay interchangeable / 1075 fend-nottimeout interchangeable，也不是已经 Finalize 回包 app_hash 可以空或硬编码就已经印进本头 interchangeable / 404 finharddet interchangeable。**  
   官方把有默克尔根和已经是本头 AppHash 分开。看见有默克尔根，不是已经是本头 AppHash interchangeable。本页钉 not already this-header 单句。

3. **看见必须确定 / 看见回了 app_hash / 这份栏 is not already 已经只是索引 interchangeable，也不是已经 Finalize 回包末栏 bundled（432） interchangeable / 1074 fend-notapphash interchangeable / 1073 fend-notheffect interchangeable，也不是已经 Finalize 回包 events 标成非确定那种只是索引 interchangeable / 431 finrespbar interchangeable。**  
   官方把必须确定和已经只是索引分开。看见必须确定，不是已经只是索引 interchangeable。432 finrespend vs params bundled unbundling 在本页 item 2 续。

怎样写 Finalize 回包末栏、怎样编 ConsensusParams、怎样填 next_block_delay 是规范里的做法，本页不抄。

## 官方为什么这样拆

- **FinalizeBlockResponse.app_hash not already next-header ≠ 已经写进下一块头的 AppHash interchangeable：** 官方把下一块头 AppHash 和本头 AppHash、本高度交差分开。
- **看见有默克尔根 not already this-header ≠ 已经是本头 AppHash interchangeable：** 官方把有默克尔根和已经是本头 AppHash 分开。
- **看见必须确定 not already index-only ≠ 已经只是索引 interchangeable：** 官方把必须确定和已经只是索引分开；432 finrespend vs params bundled unbundling 在本页 item 2 续。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| FinalizeBlockResponse.app_hash 是应用状态默克尔根 | 不是已经写进下一块头的 AppHash | 不是 Finalize 回包 app_hash 可以空或硬编码就已经印进本头（404） |
| 看见有默克尔根 | 不是已经是本头 AppHash | 不是本头 AppHash 就已经是本高度交差 |
| 看见必须确定 | 不是已经只是索引 | 不是 next_block_delay 就已经是本地 timeout_commit（1075） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 FinalizeBlockResponse.app_hash not already next-header / not already this-header / not already index-only 正式三事（432 余量），必须分开是不是已经写进下一块头、是不是已经是本头 AppHash、是不是已经只是索引。可以跳过「看见回了 Finalize 回包末栏就已经在块 H 生效」。不要另写怎样写 Finalize 回包末栏。432 finrespend vs params bundled unbundling 在本页 item 2 续；续 [`worked-example-fend-nottimeout-vs-bundled.md`](worked-example-fend-nottimeout-vs-bundled.md)（不变量 1075 item 3）。

## 本页不抄

- 怎样写 Finalize 回包末栏、怎样编 ConsensusParams、怎样填 next_block_delay。
- Finalize 回包末栏 bundled。那是不变量 432。
- Finalize 回包 app_hash 可以空或硬编码就已经印进本头。那是不变量 404。
- Finalize 回包 events 标成非确定那种只是索引。那是不变量 431。
