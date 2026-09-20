# 例：看见将签名并挂到 Precommit 不是已经广播不是已经广播 Precommit；看见will be signed and attached to Precommit is not already broadcast不是已经写进 last_commit；看见将签名并挂到 Precommit 不是已经广播不是已经 ExtendVote When 正式流程 bundled

**层次**：实现 / 规范对象。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) ExtendVote Usage application-generated information that will be signed 句。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「ExtAppGen will-be-signed attached-to-Precommit not already broadcast / not already last_commit / not already 438-bundled 正式三事（439 余量）/ not 1352 eappgen-notbcast interchangeable / not 439 extappgen-vs-signed bundled interchangeable」，不是 extappgen vs signed bundled（439），也不是已经 ExtendVote When 构造并广播 Precommit（438），也不是已经 ExtendVote When step 7 广播（513）。不要另写 怎样签 vote_extension、怎样包进 CanonicalVoteExtension、怎样广播 Precommit。

## 官方三件事

1. **看见将签名并挂到 Precommit 不是已经广播 / 看见将签名并挂到 Precommit 不是已经广播 这份对象 is not already 已经广播 Precommit interchangeable，也不是已经 extappgen vs signed bundled（439） interchangeable / 1352 eappgen-notbcast interchangeable / 1350 eappgen-notsig interchangeable，也不是已经 ExtAppGen will-be-signed attached-to-Precommit not already broadcast / not already last_commit / not already 438-bundled 正式三事 bundled（439 item 3 余量） interchangeable / 439 eappgen item 3 interchangeable。**  
   官方把将签名并挂到 Precommit 不是已经广播和已经广播 Precommit写成两件。看见将签名并挂到 Precommit 不是已经广播，不是已经广播 Precommit。

2. **看见will be signed and attached to Precommit is not already broadcast / 看见将签名并挂到 Precommit 不是已经广播 / 这份对象 is not already 已经写进 last_commit interchangeable，也不是已经 extappgen vs signed bundled（439） interchangeable / 1352 eappgen-notbcast interchangeable / 1351 eappgen-notnrp interchangeable，也不是已经 ExtendVote When 构造并广播 Precommit interchangeable / 438 ExtendVote When 构造并广播 Precommit interchangeable。**  
   官方把will be signed and attached to Precommit is not already broadcast和已经写进 last_commit写成两件。看见will be signed and attached to Precommit is not already broadcast，不是已经写进 last_commit。

3. **看见将签名并挂到 Precommit 不是已经广播 / 看见will be signed and attached to Precommit is not already broadcast / 这份对象 is not already 已经 ExtendVote When 正式流程 bundled interchangeable，也不是已经 extappgen vs signed bundled（439） interchangeable / 1352 eappgen-notbcast interchangeable / 1350 eappgen-notsig interchangeable，也不是已经 ExtendVote When step 7 广播 interchangeable / 513 ExtendVote When step 7 广播 interchangeable。**  
   官方把将签名并挂到 Precommit 不是已经广播和已经 ExtendVote When 正式流程 bundled写成两件。看见将签名并挂到 Precommit 不是已经广播，不是已经 ExtendVote When 正式流程 bundled。

栈怎么写、分隔符、例串是规范里的取值，本页不抄。不要另写 怎样签 vote_extension、怎样包进 CanonicalVoteExtension、怎样广播 Precommit。

## 官方为什么这样拆

- **will be signed and attached 不是已经广播 interchangeable：官方把 Usage 将来时和 When 已完成广播分开。**
- **看见挂到 Precommit 不是已经写进 last_commit：438 / 513 钉广播或 last_commit，本页钉 Usage 描述。**
- **看见 Usage 写 attached 不是已经 ExtendVote When 正式流程：438 钉 steps 6–7 bundled，本页钉 Response 栏将来时。**

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 已经广播 Precommit | 不是已经广播 Precommit | 不是已经ExtendVote When 构造并广播 Precommit（438） |
| 已经写进 last_commit | 不是已经写进 last_commit | 不是已经ExtendVote When step 7 广播（513） |
| 已经 ExtendVote When 正式流程 bundled | 不是已经 ExtendVote When 正式流程 bundled | 不是已经1350 eappgen-notsig |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 ExtAppGen will-be-signed attached-to-Precommit not already broadcast / not already last_commit / not already 438-bundled 正式三事（439 余量），必须分开是不是已经广播 Precommit、是不是已经写进 last_commit、是不是已经 ExtendVote When 正式流程 bundled。可以跳过「看见应用回了扩展就已经签过」。不要另写 怎样签 vote_extension、怎样包进 CanonicalVoteExtension、怎样广播 Precommit。439 ExtendVote Response application-generated will-be-signed bundled unbundling 在本页 item 3 完成；本页收束本批。

## 本页不抄

- 怎样写 ExtendVote Response Usage application-generated 正式三事、怎样选 non_rp、怎样挂到 Precommit。
- 怎样签 vote_extension、怎样包进 CanonicalVoteExtension、怎样广播 Precommit。
