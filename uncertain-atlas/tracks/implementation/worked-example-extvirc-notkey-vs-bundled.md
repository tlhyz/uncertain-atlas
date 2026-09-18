# 例：看见 ExtendedVoteInfo.validator is not already has-key interchangeable / not already extracted interchangeable / not already settled interchangeable

**层次**：实现 / ExtendedVoteInfo.validator not already has-key / not already extracted / not already settled 正式三事（425 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) Data Types ExtendedVoteInfo。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「ExtendedVoteInfo.validator not already has-key / not already extracted / not already settled 正式三事（425 余量）/ not 1052 extvirc-notkey interchangeable / not 425 extvirest-vs-voteinfo bundled interchangeable」，不是 ExtendedVoteInfo 表余栏 bundled（425），也不是 ExtendedVoteInfo 从本进程抽出就已经从块里抽出（369），也不是 Validator 用 address 认人就已经带了公钥（364）。不要另写怎样写 ExtendedVoteInfo 表余栏。

## 官方三件事

1. **看见 ExtendedVoteInfo.validator 是发了这张票的验证者 / 看见填了 validator 这份栏 is not already 已经带了公钥 interchangeable，也不是已经 ExtendedVoteInfo 表余栏 bundled（425） interchangeable / 1052 extvirc-notkey interchangeable / 1053 extvirc-notflag interchangeable / 425 extvirest item 2 block_id_flag interchangeable，也不是已经 ExtendedVoteInfo.validator not already has-key / not already extracted / not already settled 正式三事 bundled（425 item 1 余量） interchangeable / 425 extvirest item 1 interchangeable。**  
   官方写：validator 是发了这张票的验证者。看见填了 validator，不是已经 ExtendedVoteInfo 从本进程抽出那种看见有 ExtendedVoteInfo.validator 就已经带了公钥 interchangeable——本页从 425 item 1 侧钉 not already has-key 单句。425 extvirest vs voteinfo bundled unbundling 在本页 item 1 启动。

2. **看见能指发票的人 / 看见填了 validator / 这份栏 is not already 已经从本进程抽出 interchangeable，也不是已经 ExtendedVoteInfo 表余栏 bundled（425） interchangeable / 1052 extvirc-notkey interchangeable / 425 extvirest item 3 non_rp_sig interchangeable / 1054 extvirc-notgive interchangeable，也不是已经 ExtendedVoteInfo 从本进程抽出就已经从块里抽出 interchangeable / 369 extviout interchangeable。**  
   官方把能指发票的人和已经从本进程抽出分开。看见能指发票的人，不是已经从本进程抽出 interchangeable。本页钉 not already extracted 单句。

3. **看见能指人 / 看见填了 validator / 这份栏 is not already 已经交差 interchangeable，也不是已经 ExtendedVoteInfo 表余栏 bundled（425） interchangeable / 1052 extvirc-notkey interchangeable / 1053 extvirc-notflag interchangeable，也不是已经 Validator 用 address 认人就已经带了公钥 interchangeable / 364 validator interchangeable。**  
   官方把能指人和已经交差分开。看见能指人，不是已经交差 interchangeable。425 extvirest vs voteinfo bundled unbundling 在本页 item 1 启动。

怎样写 ExtendedVoteInfo 表余栏、怎样填 validator、怎样填 block_id_flag 是规范里的做法，本页不抄。

## 官方为什么这样拆

- **ExtendedVoteInfo.validator not already has-key ≠ 已经带了公钥 interchangeable：** 官方把发了这张票的验证者和已经带了公钥分开。
- **看见能指发票的人 not already extracted ≠ 已经从本进程抽出 interchangeable：** 官方把能指发票的人和已经从本进程抽出分开。
- **看见能指人 not already settled ≠ 已经交差 interchangeable：** 官方把能指人和已经交差分开；425 extvirest vs voteinfo bundled unbundling 在本页 item 1 启动。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| ExtendedVoteInfo.validator 是发了这张票的验证者 | 不是已经带了公钥 | 不是 ExtendedVoteInfo 从本进程抽出就已经从块里抽出（369） |
| 看见能指发票的人 | 不是已经从本进程抽出 | 不是 Validator 用 address 认人就已经带了公钥（364） |
| 看见能指人 | 不是已经交差 | 不是 block_id_flag 就已经罚没（1053） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 ExtendedVoteInfo.validator not already has-key / not already extracted / not already settled 正式三事（425 余量），必须分开是不是已经带了公钥、是不是已经从本进程抽出、是不是已经交差。可以跳过「看见填了 ExtendedVoteInfo 表余栏就已经带了公钥」。不要另写怎样写 ExtendedVoteInfo 表余栏。425 extvirest vs voteinfo bundled unbundling 在本页 item 1 启动；续 [`worked-example-extvirc-notflag-vs-bundled.md`](worked-example-extvirc-notflag-vs-bundled.md)（不变量 1053 item 2）。

## 本页不抄

- 怎样写 ExtendedVoteInfo 表余栏、怎样填 validator、怎样填 block_id_flag。
- ExtendedVoteInfo 表余栏 bundled。那是不变量 425。
- ExtendedVoteInfo 从本进程抽出就已经从块里抽出。那是不变量 369。
- Validator 用 address 认人就已经带了公钥。那是不变量 364。
