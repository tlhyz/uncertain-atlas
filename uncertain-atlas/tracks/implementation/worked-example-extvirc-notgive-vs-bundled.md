# 例：看见 ExtendedVoteInfo.non_rp_extension_signature is not already given-to-app interchangeable / not already same-as-extsig interchangeable / not already settled interchangeable

**层次**：实现 / ExtendedVoteInfo.non_rp_extension_signature not already given-to-app / not already same-as-extsig / not already settled 正式三事（425 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) Data Types ExtendedVoteInfo。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「ExtendedVoteInfo.non_rp_extension_signature not already given-to-app / not already same-as-extsig / not already settled 正式三事（425 余量）/ not 1054 extvirc-notgive interchangeable / not 425 extvirest-vs-voteinfo bundled interchangeable」，不是 ExtendedVoteInfo 表余栏 bundled（425），也不是 ExtendedVoteInfo.extension_signature 就已经把验过的签交给应用（421），也不是 ExtendedVoteInfo.non_rp_vote_extension 就已经按原样签（421）。不要另写怎样写 ExtendedVoteInfo 表余栏。

## 官方三件事

1. **看见 ExtendedVoteInfo.non_rp_extension_signature 是发送验证者造、CometBFT 验过的非重放保护扩展签 / 看见填了 non_rp_extension_signature 这份栏 is not already 已经把验过的签交给应用 interchangeable，也不是已经 ExtendedVoteInfo 表余栏 bundled（425） interchangeable / 1054 extvirc-notgive interchangeable / 1052 extvirc-notkey interchangeable / 425 extvirest item 1 validator interchangeable，也不是已经 ExtendedVoteInfo.non_rp_extension_signature not already given-to-app / not already same-as-extsig / not already settled 正式三事 bundled（425 item 3 余量） interchangeable / 425 extvirest item 3 interchangeable。**  
   官方写：non_rp_extension_signature 是发送验证者造、CometBFT 验过的非重放保护扩展签。看见填了 non_rp_extension_signature，不是已经 ExtendedVoteInfo.extension_signature 那种已经把验过的签交给应用 interchangeable——本页从 425 item 3 侧钉 not already given-to-app 单句。425 extvirest vs voteinfo bundled unbundling 在本页 item 3 完成。

2. **看见验过了 / 看见填了 non_rp_extension_signature / 这份栏 is not already 已经是 extension_signature interchangeable，也不是已经 ExtendedVoteInfo 表余栏 bundled（425） interchangeable / 1054 extvirc-notgive interchangeable / 425 extvirest item 2 block_id_flag interchangeable / 1053 extvirc-notflag interchangeable，也不是已经 ExtendedVoteInfo.extension_signature 就已经把验过的签交给应用 interchangeable / 421 extvicol interchangeable。**  
   官方把验过了和已经是 extension_signature 分开。看见验过了，不是已经是 extension_signature interchangeable。本页钉 not already same-as-extsig 单句。

3. **看见能指第二份签 / 看见填了 non_rp_extension_signature / 这份栏 is not already 已经交差 interchangeable，也不是已经 ExtendedVoteInfo 表余栏 bundled（425） interchangeable / 1054 extvirc-notgive interchangeable / 1052 extvirc-notkey interchangeable，也不是已经 ExtendedVoteInfo.non_rp_vote_extension 就已经按原样签 interchangeable / 421 extvicol interchangeable。**  
   官方把能指第二份签和已经交差分开。看见能指第二份签，不是已经交差 interchangeable。425 extvirest vs voteinfo bundled unbundling 在本页 item 3 完成。

怎样写 ExtendedVoteInfo 表余栏、怎样填 validator、怎样填 block_id_flag 是规范里的做法，本页不抄。

## 官方为什么这样拆

- **ExtendedVoteInfo.non_rp_extension_signature not already given-to-app ≠ 已经把验过的签交给应用 interchangeable：** 官方把发送验证者造、CometBFT 验过的非重放保护扩展签和已经把验过的签交给应用分开。
- **看见验过了 not already same-as-extsig ≠ 已经是 extension_signature interchangeable：** 官方把验过了和已经是 extension_signature 分开。
- **看见能指第二份签 not already settled ≠ 已经交差 interchangeable：** 官方把能指第二份签和已经交差分开；425 extvirest vs voteinfo bundled unbundling 在本页 item 3 完成。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| ExtendedVoteInfo.non_rp_extension_signature 是发送验证者造、CometBFT 验过的非重放保护扩展签 | 不是已经把验过的签交给应用 | 不是 ExtendedVoteInfo.extension_signature 就已经把验过的签交给应用（421） |
| 看见验过了 | 不是已经是 extension_signature | 不是 ExtendedVoteInfo.non_rp_vote_extension 就已经按原样签（421） |
| 看见能指第二份签 | 不是已经交差 | 不是 validator 就已经带了公钥（1052） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 ExtendedVoteInfo.non_rp_extension_signature not already given-to-app / not already same-as-extsig / not already settled 正式三事（425 余量），必须分开是不是已经把验过的签交给应用、是不是已经是 extension_signature、是不是已经交差。可以跳过「看见填了 ExtendedVoteInfo 表余栏就已经带了公钥」。不要另写怎样写 ExtendedVoteInfo 表余栏。425 extvirest vs voteinfo bundled unbundling 在本页 item 3 完成。

## 本页不抄

- 怎样写 ExtendedVoteInfo 表余栏、怎样填 validator、怎样填 block_id_flag。
- ExtendedVoteInfo 表余栏 bundled。那是不变量 425。
- ExtendedVoteInfo.extension_signature 就已经把验过的签交给应用。那是不变量 421。
- ExtendedVoteInfo.non_rp_vote_extension 就已经按原样签。那是不变量 421。
