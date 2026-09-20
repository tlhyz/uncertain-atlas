# 例：看见两份签都在且没 non_rp 就签空切片不是已经只有一份签不是已经只有一份签；看见two signatures present and empty-slice if no non_rp is not already one signature不是已经没 non_rp 就没有第二份签；看见两份签都在且没 non_rp 就签空切片不是已经只有一份签不是已经 optional 就跳过 Verify

**层次**：实现 / 规范对象。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) Data Types ExtendedVoteInfo Usage 句。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「ExtViUse two sigs when enabled empty-slice if no non_rp not already one-sig / not already no-second / not already 358-replay 正式三事（447 余量）/ not 1367 eviuse-nottwo interchangeable / not 447 extviusage-vs-expose bundled interchangeable」，不是 extviusage vs expose bundled（447），也不是已经 non_rp 按原样签就已经有重放保护（358），也不是已经 ExtendVoteResponse 已是签过的信息（418）。不要另写 怎样让应用再验签、怎样把引擎验过当成应用验完、怎样把空切片当成没有第二份签。

## 官方三件事

1. **看见两份签都在且没 non_rp 就签空切片不是已经只有一份签 / 看见两份签都在且没 non_rp 就签空切片不是已经只有一份签 这份对象 is not already 已经只有一份签 interchangeable，也不是已经 extviusage vs expose bundled（447） interchangeable / 1367 eviuse-nottwo interchangeable / 1365 eviuse-notapp interchangeable，也不是已经 ExtViUse two sigs when enabled empty-slice if no non_rp not already one-sig / not already no-second / not already 358-replay 正式三事 bundled（447 item 3 余量） interchangeable / 447 eviuse item 3 interchangeable。**  
   官方把两份签都在且没 non_rp 就签空切片不是已经只有一份签和已经只有一份签写成两件。看见两份签都在且没 non_rp 就签空切片不是已经只有一份签，不是已经只有一份签。

2. **看见two signatures present and empty-slice if no non_rp is not already one signature / 看见两份签都在且没 non_rp 就签空切片不是已经只有一份签 / 这份对象 is not already 已经没 non_rp 就没有第二份签 interchangeable，也不是已经 extviusage vs expose bundled（447） interchangeable / 1367 eviuse-nottwo interchangeable / 1366 eviuse-notexp interchangeable，也不是已经 non_rp 按原样签就已经有重放保护 interchangeable / 358 non_rp 按原样签就已经有重放保护 interchangeable。**  
   官方把two signatures present and empty-slice if no non_rp is not already one signature和已经没 non_rp 就没有第二份签写成两件。看见two signatures present and empty-slice if no non_rp is not already one signature，不是已经没 non_rp 就没有第二份签。

3. **看见两份签都在且没 non_rp 就签空切片不是已经只有一份签 / 看见two signatures present and empty-slice if no non_rp is not already one signature / 这份对象 is not already 已经 optional 就跳过 Verify interchangeable，也不是已经 extviusage vs expose bundled（447） interchangeable / 1367 eviuse-nottwo interchangeable / 1365 eviuse-notapp interchangeable，也不是已经 ExtendVoteResponse 已是签过的信息 interchangeable / 418 ExtendVoteResponse 已是签过的信息 interchangeable。**  
   官方把两份签都在且没 non_rp 就签空切片不是已经只有一份签和已经 optional 就跳过 Verify写成两件。看见两份签都在且没 non_rp 就签空切片不是已经只有一份签，不是已经 optional 就跳过 Verify。

栈怎么写、分隔符、例串是规范里的取值，本页不抄。不要另写 怎样让应用再验签、怎样把引擎验过当成应用验完、怎样把空切片当成没有第二份签。

## 官方为什么这样拆

- **两份签都在 不是已经只有一份签 interchangeable：官方把启用扩展时两份签都在和 optional 没填分开。**
- **看见签空切片 不是已经没 non_rp 就没有第二份签。**
- **看见 optional can be empty 不是已经跳过 Verify。**

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 已经只有一份签 | 不是已经只有一份签 | 不是已经non_rp 按原样签就已经有重放保护（358） |
| 已经没 non_rp 就没有第二份签 | 不是已经没 non_rp 就没有第二份签 | 不是已经ExtendVoteResponse 已是签过的信息（418） |
| 已经 optional 就跳过 Verify | 不是已经 optional 就跳过 Verify | 不是已经1365 eviuse-notapp |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 ExtViUse two sigs when enabled empty-slice if no non_rp not already one-sig / not already no-second / not already 358-replay 正式三事（447 余量），必须分开是不是已经只有一份签、是不是已经没 non_rp 就没有第二份签、是不是已经 optional 就跳过 Verify。可以跳过「看见 Prepare 里有 ExtendedVoteInfo 就已经应用验完」。不要另写 怎样让应用再验签、怎样把引擎验过当成应用验完、怎样把空切片当成没有第二份签。447 ExtendedVoteInfo Usage expose signature bundled unbundling 在本页 item 3 完成；本页收束本批。

## 本页不抄

- 怎样写 ExtendedVoteInfo Usage 暴露签正式三事、怎样再验签、怎样读空切片。
- 怎样让应用再验签、怎样把引擎验过当成应用验完、怎样把空切片当成没有第二份签。
