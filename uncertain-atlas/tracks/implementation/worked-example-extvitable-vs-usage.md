# 例：看见 ExtendedVoteInfo.vote_extension 是发送验证者的应用给的非确定扩展不是已经从本进程抽出；看见 ExtendedVoteInfo.non_rp_vote_extension 是发送验证者的应用给的非重放保护扩展不是已经按原样签；看见 ExtendedVoteInfo.extension_signature 是发送验证者造、CometBFT 验过的扩展签不是已经把验过的签交给应用

**层次**：实现 / ExtendedVoteInfo 表栏。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) Data Types ExtendedVoteInfo。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「ExtendedVoteInfo.vote_extension 是发送验证者的应用给的非确定扩展不是已经从本进程抽出 / ExtendedVoteInfo.non_rp_vote_extension 是发送验证者的应用给的非重放保护扩展不是已经按原样签 / ExtendedVoteInfo.extension_signature 是发送验证者造、CometBFT 验过的扩展签不是已经把验过的签交给应用」，不是 ExtendedVoteInfo 从本进程抽出就已经从块里抽出，也不是 ExtendVoteResponse.vote_extension 是 CometBFT 签的信息、可以 0 长、标成非确定就已经会包进 CanonicalVoteExtension。不要另写怎样写 ExtendedVoteInfo 表栏。

## 官方三件事

规范把 ExtendedVoteInfo 表上 `vote_extension` 是发送验证者的应用给的非确定扩展、`non_rp_vote_extension` 是发送验证者的应用给的非重放保护扩展、`extension_signature` 是发送验证者造、CometBFT 验过的扩展签写成三件独立的实现事，不是「看见填了 ExtendedVoteInfo 表栏就已经从本进程抽出、已经按原样签、已经把验过的签交给应用」一件事：

1. **看见 `ExtendedVoteInfo.vote_extension` 是发送验证者的应用给的非确定扩展 / 看见填了 vote_extension 不是已经从本进程抽出，也不是已经是 ExtendVoteResponse.vote_extension。**  
   官方写：`vote_extension` 是发送验证者的应用给的非确定扩展。看见填了 vote_extension，不是已经 ExtendedVoteInfo 从本进程的 CometBFT 数据结构抽出那种已经从块里抽出。看见是应用给的，不是已经 `ExtendVoteResponse.vote_extension` 是 CometBFT 签的信息、可以 0 长、标成非确定那种已经会包进 CanonicalVoteExtension。看见能指扩展，不是已经交差。
2. **看见 `ExtendedVoteInfo.non_rp_vote_extension` 是发送验证者的应用给的非重放保护扩展 / 看见填了 non_rp_vote_extension 不是已经按原样签，也不是已经是 ExtendVoteResponse.non_rp_extension。**  
   官方写：`non_rp_vote_extension` 是发送验证者的应用给的非重放保护扩展。看见填了 non_rp_vote_extension，不是已经 `non_rp_extension` 按应用给的字节原样签那种已经有重放保护。看见是应用给的，不是已经 `ExtendVoteResponse.non_rp_extension` 是 CometBFT 签的信息、可以 0 长、标成非确定那种已经按原样签。看见能指第二份，不是已经交差。
3. **看见 `ExtendedVoteInfo.extension_signature` 是发送验证者造、CometBFT 验过的扩展签 / 看见填了 extension_signature 不是已经把验过的签交给应用，也不是已经有重放保护。**  
   官方写：`extension_signature` 是发送验证者造、CometBFT 验过的扩展签。看见填了 extension_signature，不是已经 `extension_signature` 已由引擎验过、交给应用再处理那种已经按原样签。看见验过了，不是已经有重放保护。看见能指签，不是已经交差。

怎样写 ExtendedVoteInfo 表栏、怎样填 vote_extension、怎样填 extension_signature 是规范里的做法，本页不抄。ExtendedVoteInfo 从本进程抽出就已经从块里抽出是不变量 369，本页不抄。

## 官方为什么这样拆

- **ExtendedVoteInfo.vote_extension 是发送验证者的应用给的非确定扩展 ≠ 已经从本进程抽出：** 官方把表上这份发送验证者的应用给的非确定扩展和 Usage 里那份从本进程抽出分开。
- **ExtendedVoteInfo.non_rp_vote_extension 是发送验证者的应用给的非重放保护扩展 ≠ 已经按原样签：** 官方把表上这份发送验证者的应用给的非重放保护扩展和回包栏那份 CometBFT 签的非重放保护扩展分开。
- **ExtendedVoteInfo.extension_signature 是发送验证者造、CometBFT 验过的扩展签 ≠ 已经把验过的签交给应用：** 官方把表上这份发送验证者造、CometBFT 验过的扩展签和 Usage 里那份交给应用再处理分开。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| ExtendedVoteInfo.vote_extension 是发送验证者的应用给的非确定扩展 | 不是已经从本进程抽出 | 不是 ExtendedVoteInfo 从本进程抽出就已经从块里抽出（369） |
| ExtendedVoteInfo.non_rp_vote_extension 是发送验证者的应用给的非重放保护扩展 | 不是已经按原样签 | 不是 ExtendVoteResponse.non_rp_extension 是 CometBFT 签的信息、可以 0 长、标成非确定就已经按原样签（418） |
| ExtendedVoteInfo.extension_signature 是发送验证者造、CometBFT 验过的扩展签 | 不是已经把验过的签交给应用 | 不是 vote_extension 会包进 CanonicalVoteExtension 就已经按原样签（358） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看「看见填了 ExtendedVoteInfo 表栏就已经从本进程抽出、已经按原样签、已经把验过的签交给应用」，必须分开 ExtendedVoteInfo.vote_extension 是发送验证者的应用给的非确定扩展是不是已经从本进程抽出、ExtendedVoteInfo.non_rp_vote_extension 是发送验证者的应用给的非重放保护扩展是不是已经按原样签、ExtendedVoteInfo.extension_signature 是发送验证者造、CometBFT 验过的扩展签是不是已经把验过的签交给应用。可以跳过「看见填了 ExtendedVoteInfo 表栏就已经从本进程抽出」。不要另写怎样写 ExtendedVoteInfo 表栏。421 extvitable vs usage bundled unbundling 完成（1043 item 1 / 1044 item 2 / 1045 item 3）；精读 [`worked-example-extvicol-notextract-vs-bundled.md`](worked-example-extvicol-notextract-vs-bundled.md)（不变量 1043 item 1）。

## 本页不抄

- 怎样写 ExtendedVoteInfo 表栏、怎样填 vote_extension、怎样填 extension_signature。
- ExtendedVoteInfo 从本进程抽出就已经从块里抽出。那是不变量 369。
- ExtendVoteResponse.vote_extension 是 CometBFT 签的信息、可以 0 长、标成非确定就已经会包进 CanonicalVoteExtension。那是不变量 418。
- vote_extension 会包进 CanonicalVoteExtension 就已经按原样签。那是不变量 358。
