# 例：看见应用生成 vote_extension 将签名不是已经签过不是已经签过；看见application-generated vote_extension will be signed is not already signed不是已经包进 CanonicalVoteExtension；看见应用生成 vote_extension 将签名不是已经签过不是已经 attached to Precommit

**层次**：实现 / 规范对象。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) ExtendVote Usage application-generated information that will be signed 句。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「ExtAppGen appgen vote_extension will-be-signed not already signed / not already 418-wrap / not already attached 正式三事（439 余量）/ not 1350 eappgen-notsig interchangeable / not 439 extappgen-vs-signed bundled interchangeable」，不是 extappgen vs signed bundled（439），也不是已经 ExtendVoteResponse 是 CometBFT 签的信息、可以 0 长、标成非确定就已经包进包装（418），也不是已经 vote_extension 包进 CanonicalVoteExtension、non_rp 按原样签（358）。不要另写 怎样签 vote_extension、怎样包进 CanonicalVoteExtension、怎样广播 Precommit。

## 官方三件事

1. **看见应用生成 vote_extension 将签名不是已经签过 / 看见应用生成 vote_extension 将签名不是已经签过 这份对象 is not already 已经签过 interchangeable，也不是已经 extappgen vs signed bundled（439） interchangeable / 1350 eappgen-notsig interchangeable / 1351 eappgen-notnrp interchangeable，也不是已经 ExtAppGen appgen vote_extension will-be-signed not already signed / not already 418-wrap / not already attached 正式三事 bundled（439 item 1 余量） interchangeable / 439 eappgen item 1 interchangeable。**  
   官方把应用生成 vote_extension 将签名不是已经签过和已经签过写成两件。看见应用生成 vote_extension 将签名不是已经签过，不是已经签过。

2. **看见application-generated vote_extension will be signed is not already signed / 看见应用生成 vote_extension 将签名不是已经签过 / 这份对象 is not already 已经包进 CanonicalVoteExtension interchangeable，也不是已经 extappgen vs signed bundled（439） interchangeable / 1350 eappgen-notsig interchangeable / 1352 eappgen-notbcast interchangeable，也不是已经 ExtendVoteResponse 是 CometBFT 签的信息、可以 0 长、标成非确定就已经包进包装 interchangeable / 418 ExtendVoteResponse 是 CometBFT 签的信息、可以 0 长、标成非确定就已经包进包装 interchangeable。**  
   官方把application-generated vote_extension will be signed is not already signed和已经包进 CanonicalVoteExtension写成两件。看见application-generated vote_extension will be signed is not already signed，不是已经包进 CanonicalVoteExtension。

3. **看见应用生成 vote_extension 将签名不是已经签过 / 看见application-generated vote_extension will be signed is not already signed / 这份对象 is not already 已经 attached to Precommit interchangeable，也不是已经 extappgen vs signed bundled（439） interchangeable / 1350 eappgen-notsig interchangeable / 1351 eappgen-notnrp interchangeable，也不是已经 vote_extension 包进 CanonicalVoteExtension、non_rp 按原样签 interchangeable / 358 vote_extension 包进 CanonicalVoteExtension、non_rp 按原样签 interchangeable。**  
   官方把应用生成 vote_extension 将签名不是已经签过和已经 attached to Precommit写成两件。看见应用生成 vote_extension 将签名不是已经签过，不是已经 attached to Precommit。

栈怎么写、分隔符、例串是规范里的取值，本页不抄。不要另写 怎样签 vote_extension、怎样包进 CanonicalVoteExtension、怎样广播 Precommit。

## 官方为什么这样拆

- **application-generated will be signed 不是已经签过 interchangeable：官方把应用生成和 CometBFT 后续签名分开。**
- **看见 will be signed 不是已经包进 CanonicalVoteExtension：418 钉「是 CometBFT 签的信息就已经会包进包装」，本页钉将来时还没签。**
- **看见应用回了扩展 不是已经 attached to Precommit：Usage 写 will be signed，不是已经挂上。**

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 已经签过 | 不是已经签过 | 不是已经ExtendVoteResponse 是 CometBFT 签的信息、可以 0 长、标成非确定就已经包进包装（418） |
| 已经包进 CanonicalVoteExtension | 不是已经包进 CanonicalVoteExtension | 不是已经vote_extension 包进 CanonicalVoteExtension、non_rp 按原样签（358） |
| 已经 attached to Precommit | 不是已经 attached to Precommit | 不是已经1351 eappgen-notnrp |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 ExtAppGen appgen vote_extension will-be-signed not already signed / not already 418-wrap / not already attached 正式三事（439 余量），必须分开是不是已经签过、是不是已经包进 CanonicalVoteExtension、是不是已经 attached to Precommit。可以跳过「看见应用回了扩展就已经签过」。不要另写 怎样签 vote_extension、怎样包进 CanonicalVoteExtension、怎样广播 Precommit。439 ExtendVote Response application-generated will-be-signed bundled unbundling 在本页 item 1 启动；续 [`worked-example-eappgen-notnrp-vs-bundled.md`](worked-example-eappgen-notnrp-vs-bundled.md)（不变量 1351 item 2）。

## 本页不抄

- 怎样写 ExtendVote Response Usage application-generated 正式三事、怎样选 non_rp、怎样挂到 Precommit。
- 怎样签 vote_extension、怎样包进 CanonicalVoteExtension、怎样广播 Precommit。
