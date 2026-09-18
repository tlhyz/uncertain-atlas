# 例：看见non_rp 将签名并挂上且不做重放保护不是已经同一份签法不是已经和 vote_extension 同一份签法；看见non_rp will be signed and attached without replay-protection is not same signing不是已经 non_rp 按原样签 bundled；看见non_rp 将签名并挂上且不做重放保护不是已经同一份签法不是已经有重放保护

**层次**：实现 / 规范对象。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) ExtendVote Usage application-generated information that will be signed 句。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「ExtAppGen appgen non_rp will-be-signed-attached no-replay-prot not already same-sign / not already 358-raw / not already replay-prot 正式三事（439 余量）/ not 1351 eappgen-notnrp interchangeable / not 439 extappgen-vs-signed bundled interchangeable」，不是 extappgen vs signed bundled（439），也不是已经 non_rp 按原样签（358），也不是已经 ExtendVoteResponse 已是签过的信息（418）。不要另写 怎样签 vote_extension、怎样包进 CanonicalVoteExtension、怎样广播 Precommit。

## 官方三件事

1. **看见non_rp 将签名并挂上且不做重放保护不是已经同一份签法 / 看见non_rp 将签名并挂上且不做重放保护不是已经同一份签法 这份对象 is not already 已经和 vote_extension 同一份签法 interchangeable，也不是已经 extappgen vs signed bundled（439） interchangeable / 1351 eappgen-notnrp interchangeable / 1350 eappgen-notsig interchangeable，也不是已经 ExtAppGen appgen non_rp will-be-signed-attached no-replay-prot not already same-sign / not already 358-raw / not already replay-prot 正式三事 bundled（439 item 2 余量） interchangeable / 439 eappgen item 2 interchangeable。**  
   官方把non_rp 将签名并挂上且不做重放保护不是已经同一份签法和已经和 vote_extension 同一份签法写成两件。看见non_rp 将签名并挂上且不做重放保护不是已经同一份签法，不是已经和 vote_extension 同一份签法。

2. **看见non_rp will be signed and attached without replay-protection is not same signing / 看见non_rp 将签名并挂上且不做重放保护不是已经同一份签法 / 这份对象 is not already 已经 non_rp 按原样签 bundled interchangeable，也不是已经 extappgen vs signed bundled（439） interchangeable / 1351 eappgen-notnrp interchangeable / 1352 eappgen-notbcast interchangeable，也不是已经 non_rp 按原样签 interchangeable / 358 non_rp 按原样签 interchangeable。**  
   官方把non_rp will be signed and attached without replay-protection is not same signing和已经 non_rp 按原样签 bundled写成两件。看见non_rp will be signed and attached without replay-protection is not same signing，不是已经 non_rp 按原样签 bundled。

3. **看见non_rp 将签名并挂上且不做重放保护不是已经同一份签法 / 看见non_rp will be signed and attached without replay-protection is not same signing / 这份对象 is not already 已经有重放保护 interchangeable，也不是已经 extappgen vs signed bundled（439） interchangeable / 1351 eappgen-notnrp interchangeable / 1350 eappgen-notsig interchangeable，也不是已经 ExtendVoteResponse 已是签过的信息 interchangeable / 418 ExtendVoteResponse 已是签过的信息 interchangeable。**  
   官方把non_rp 将签名并挂上且不做重放保护不是已经同一份签法和已经有重放保护写成两件。看见non_rp 将签名并挂上且不做重放保护不是已经同一份签法，不是已经有重放保护。

栈怎么写、分隔符、例串是规范里的取值，本页不抄。不要另写 怎样签 vote_extension、怎样包进 CanonicalVoteExtension、怎样广播 Precommit。

## 官方为什么这样拆

- **non_rp 不做重放保护 不是已经和 vote_extension 同一份签法 interchangeable：官方把两份应用生成扩展和两种签名路径分开。**
- **看见 will be signed and attached 不是已经 non_rp 按原样签：358 钉按原样签，本页钉 application-generated 将来时。**
- **看见不做重放保护 不是已经有 Height/Round/ChainID 包装：官方把 raw 路径和包装路径分开。**

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 已经和 vote_extension 同一份签法 | 不是已经和 vote_extension 同一份签法 | 不是已经non_rp 按原样签（358） |
| 已经 non_rp 按原样签 bundled | 不是已经 non_rp 按原样签 bundled | 不是已经ExtendVoteResponse 已是签过的信息（418） |
| 已经有重放保护 | 不是已经有重放保护 | 不是已经1350 eappgen-notsig |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 ExtAppGen appgen non_rp will-be-signed-attached no-replay-prot not already same-sign / not already 358-raw / not already replay-prot 正式三事（439 余量），必须分开是不是已经和 vote_extension 同一份签法、是不是已经 non_rp 按原样签 bundled、是不是已经有重放保护。可以跳过「看见应用回了扩展就已经签过」。不要另写 怎样签 vote_extension、怎样包进 CanonicalVoteExtension、怎样广播 Precommit。439 ExtendVote Response application-generated will-be-signed bundled unbundling 在本页 item 2 续；续 [`worked-example-eappgen-notbcast-vs-bundled.md`](worked-example-eappgen-notbcast-vs-bundled.md)（不变量 1352 item 3）。

## 本页不抄

- 怎样写 ExtendVote Response Usage application-generated 正式三事、怎样选 non_rp、怎样挂到 Precommit。
- 怎样签 vote_extension、怎样包进 CanonicalVoteExtension、怎样广播 Precommit。
