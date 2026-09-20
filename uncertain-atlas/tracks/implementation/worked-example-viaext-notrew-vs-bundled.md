# 例：看见availability 同句不是已经奖罚完不是已经奖罚完；看见availability same sentence is not already rewarded不是已经交差；看见availability 同句不是已经奖罚完不是已经 Finalize 算完奖惩

**层次**：实现 / 规范对象。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) Data Types VoteInfo Usage / ExtendedVoteInfo Usage 句。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「ViAvail availability same-sentence not already rewarded / not already settled / not already Finalize-computed 正式三事（442 余量）/ not 1374 viaext-notrew interchangeable / not 442 viusageavail-vs-extractpath bundled interchangeable」，不是 viusageavail vs extractpath bundled（442），也不是已经 VoteInfo 能按到场定奖惩就已经罚没（365），也不是已经 ExtendedVoteInfo.block_id_flag 表栏就已经罚没（425）。不要另写 怎样把同一句 availability 写成已经奖罚完、怎样把两条抽出路径写成同一路、怎样按 block_id_flag 直接罚没。

## 官方三件事

1. **看见availability 同句不是已经奖罚完 / 看见availability 同句不是已经奖罚完 这份对象 is not already 已经奖罚完 interchangeable，也不是已经 viusageavail vs extractpath bundled（442） interchangeable / 1374 viaext-notrew interchangeable / 1375 viaext-notblk interchangeable，也不是已经 ViAvail availability same-sentence not already rewarded / not already settled / not already Finalize-computed 正式三事 bundled（442 item 1 余量） interchangeable / 442 viaext item 1 interchangeable。**  
   官方把availability 同句不是已经奖罚完和已经奖罚完写成两件。看见availability 同句不是已经奖罚完，不是已经奖罚完。

2. **看见availability same sentence is not already rewarded / 看见availability 同句不是已经奖罚完 / 这份对象 is not already 已经交差 interchangeable，也不是已经 viusageavail vs extractpath bundled（442） interchangeable / 1374 viaext-notrew interchangeable / 1376 viaext-notloc interchangeable，也不是已经 VoteInfo 能按到场定奖惩就已经罚没 interchangeable / 365 VoteInfo 能按到场定奖惩就已经罚没 interchangeable。**  
   官方把availability same sentence is not already rewarded和已经交差写成两件。看见availability same sentence is not already rewarded，不是已经交差。

3. **看见availability 同句不是已经奖罚完 / 看见availability same sentence is not already rewarded / 这份对象 is not already 已经 Finalize 算完奖惩 interchangeable，也不是已经 viusageavail vs extractpath bundled（442） interchangeable / 1374 viaext-notrew interchangeable / 1375 viaext-notblk interchangeable，也不是已经 ExtendedVoteInfo.block_id_flag 表栏就已经罚没 interchangeable / 425 ExtendedVoteInfo.block_id_flag 表栏就已经罚没 interchangeable。**  
   官方把availability 同句不是已经奖罚完和已经 Finalize 算完奖惩写成两件。看见availability 同句不是已经奖罚完，不是已经 Finalize 算完奖惩。

栈怎么写、分隔符、例串是规范里的取值，本页不抄。不要另写 怎样把同一句 availability 写成已经奖罚完、怎样把两条抽出路径写成同一路、怎样按 block_id_flag 直接罚没。

## 官方为什么这样拆

- **同一句 availability 不是已经奖罚完 interchangeable：官方把能定奖惩和已经算完分开。**
- **看见有 block_id_flag 不是已经交差。**
- **看见 Prepare 里也有 availability 不是已经 Finalize 算完。**

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 已经奖罚完 | 不是已经奖罚完 | 不是已经VoteInfo 能按到场定奖惩就已经罚没（365） |
| 已经交差 | 不是已经交差 | 不是已经ExtendedVoteInfo.block_id_flag 表栏就已经罚没（425） |
| 已经 Finalize 算完奖惩 | 不是已经 Finalize 算完奖惩 | 不是已经1375 viaext-notblk |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 ViAvail availability same-sentence not already rewarded / not already settled / not already Finalize-computed 正式三事（442 余量），必须分开是不是已经奖罚完、是不是已经交差、是不是已经 Finalize 算完奖惩。可以跳过「看见 block_id_flag 就已经奖罚完」。不要另写 怎样把同一句 availability 写成已经奖罚完、怎样把两条抽出路径写成同一路、怎样按 block_id_flag 直接罚没。442 VoteInfo ExtendedVoteInfo availability same-sentence extract-paths bundled unbundling 在本页 item 1 启动；续 [`worked-example-viaext-notblk-vs-bundled.md`](worked-example-viaext-notblk-vs-bundled.md)（不变量 1375 item 2）。

## 本页不抄

- 怎样写 VoteInfo ExtendedVoteInfo Usage 到场定奖惩同句、抽取异路正式三事。
- 怎样把同一句 availability 写成已经奖罚完、怎样把两条抽出路径写成同一路、怎样按 block_id_flag 直接罚没。
