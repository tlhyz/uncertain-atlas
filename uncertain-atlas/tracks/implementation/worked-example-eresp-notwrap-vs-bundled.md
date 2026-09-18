# 例：看见 ExtendVoteResponse.vote_extension is not already canonical-wrapped interchangeable / not already same-ext interchangeable / not already settled interchangeable

**层次**：实现 / ExtendVoteResponse.vote_extension not already canonical-wrapped / not already same-ext / not already settled 正式三事（418 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) ExtendVote Response / VerifyVoteExtension Request。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「ExtendVoteResponse.vote_extension not already canonical-wrapped / not already same-ext / not already settled 正式三事（418 余量）/ not 1082 eresp-notwrap interchangeable / not 418 extresp-vs-wrap bundled interchangeable」，不是扩展回包栏 bundled（418），也不是 vote_extension 会包进 CanonicalVoteExtension 就已经按原样签（358），也不是 ExtendVote 没有确定性要求就已经是同一份扩展（338）。不要另写怎样写扩展回包栏。

## 官方三件事

1. **看见 ExtendVoteResponse.vote_extension 是 CometBFT 签的信息、可以 0 长、标成非确定 / 看见回了扩展 这份栏 is not already 已经会包进 CanonicalVoteExtension interchangeable，也不是已经扩展回包栏 bundled（418） interchangeable / 1082 eresp-notwrap interchangeable / 1083 eresp-notraw interchangeable / 418 extresp item 2 non_rp interchangeable，也不是已经 ExtendVoteResponse.vote_extension not already canonical-wrapped / not already same-ext / not already settled 正式三事 bundled（418 item 1 余量） interchangeable / 418 extresp item 1 interchangeable。**  
   官方写：vote_extension 是 CometBFT 签的信息，可以 0 长。表上 Deterministic = No。看见回了扩展，不是已经会包进 CanonicalVoteExtension interchangeable——本页从 418 item 1 侧钉 not already canonical-wrapped 单句。418 extresp vs wrap bundled unbundling 在本页 item 1 启动。

2. **看见标成非确定 / 看见回了扩展 / 这份栏 is not already 已经是同一份扩展 interchangeable，也不是已经扩展回包栏 bundled（418） interchangeable / 1082 eresp-notwrap interchangeable / 418 extresp item 3 verify-nonrp interchangeable / 1084 eresp-nottable interchangeable，也不是已经 ExtendVote 没有确定性要求就已经是同一份扩展 interchangeable / 338 prepare-nondet interchangeable。**  
   官方把标成非确定和已经是同一份扩展分开。看见标成非确定，不是已经是同一份扩展 interchangeable。本页钉 not already same-ext 单句。

3. **看见可以 0 长 / 看见回了扩展 / 这份栏 is not already 已经交差 interchangeable，也不是已经扩展回包栏 bundled（418） interchangeable / 1082 eresp-notwrap interchangeable / 1083 eresp-notraw interchangeable，也不是已经 vote_extension 会包进 CanonicalVoteExtension 就已经按原样签 interchangeable / 358 extresp interchangeable。**  
   官方把可以 0 长和已经交差分开。看见可以 0 长，不是已经交差 interchangeable。418 extresp vs wrap bundled unbundling 在本页 item 1 启动。

怎样写扩展回包栏、怎样填 vote_extension、怎样填 non_rp_extension 是规范里的做法，本页不抄。

## 官方为什么这样拆

- **ExtendVoteResponse.vote_extension not already canonical-wrapped ≠ 已经会包进 CanonicalVoteExtension interchangeable：** 官方把回包表描述和 Usage 里那份包装分开。
- **看见标成非确定 not already same-ext ≠ 已经是同一份扩展 interchangeable：** 官方把标成非确定和已经是同一份扩展分开。
- **看见可以 0 长 not already settled ≠ 已经交差 interchangeable：** 官方把可以 0 长和已经交差分开；418 extresp vs wrap bundled unbundling 在本页 item 1 启动。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| ExtendVoteResponse.vote_extension 是 CometBFT 签的信息、可以 0 长、标成非确定 | 不是已经会包进 CanonicalVoteExtension | 不是 vote_extension 会包进 CanonicalVoteExtension 就已经按原样签（358） |
| 看见标成非确定 | 不是已经是同一份扩展 | 不是 ExtendVote 没有确定性要求就已经是同一份扩展（338） |
| 看见可以 0 长 | 不是已经交差 | 不是 non_rp_extension 就已经按原样签（1083） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 ExtendVoteResponse.vote_extension not already canonical-wrapped / not already same-ext / not already settled 正式三事（418 余量），必须分开是不是已经会包进 CanonicalVoteExtension、是不是已经是同一份扩展、是不是已经交差。可以跳过「看见填了扩展回包栏就已经会包进 CanonicalVoteExtension」。不要另写怎样写扩展回包栏。418 extresp vs wrap bundled unbundling 在本页 item 1 启动；续 [`worked-example-eresp-notraw-vs-bundled.md`](worked-example-eresp-notraw-vs-bundled.md)（不变量 1083 item 2）。

## 本页不抄

- 怎样写扩展回包栏、怎样填 vote_extension、怎样填 non_rp_extension。
- 扩展回包栏 bundled。那是不变量 418。
- vote_extension 会包进 CanonicalVoteExtension 就已经按原样签。那是不变量 358。
- ExtendVote 没有确定性要求就已经是同一份扩展。那是不变量 338。
