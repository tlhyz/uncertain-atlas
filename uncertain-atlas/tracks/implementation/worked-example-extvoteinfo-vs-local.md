# 例：看见 ExtendedVoteInfo 从本进程抽出不是已经从块里抽出；看见把验过的签交给应用不是已经按原样签；看见扩展关掉则字段全空不是已经到了启用高度

**层次**：实现 / ExtendedVoteInfo。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) Data Types ExtendedVoteInfo。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5。本页是「ExtendedVoteInfo 从本进程抽出不是已经从块里抽出 / 把验过的签交给应用不是已经按原样签 / 扩展关掉则字段全空不是已经到了启用高度」，不是 VoteInfo 从拟议块或已决块抽出就已经带了公钥，也不是 vote_extension 会包进 CanonicalVoteExtension 就已经按原样签。不要另写怎样写 ExtendedVoteInfo。

## 官方三件事

规范把 `ExtendedVoteInfo` 从本进程抽出、把验过的签交给应用、扩展关掉则字段全空写成三件独立的实现事，不是「看见 Prepare 里有扩展就已经从块里抽出、已经按原样签、已经到了启用高度」一件事：

1. **看见 ExtendedVoteInfo 从本进程的 CometBFT 数据结构抽出 / 看见 Prepare 里有这份 不是已经从拟议块或已决块抽出，也不是已经带了公钥。**  
   官方写：这份信息从本进程里 CometBFT 的数据结构抽出。看见 Prepare 里有 `ExtendedCommitInfo`，不是已经从拟议块或已决块抽出。看见有 `ExtendedVoteInfo.validator`，不是已经带了公钥。看见能抽，不是已经交差。
2. **看见 `extension_signature` 已由引擎验过、交给应用再处理；扩展启用时两份签都在；没给 `non_rp` 就签空切片 / 看见有签 不是已经按原样签，也不是已经有重放保护。**  
   官方写：`extension_signature` 是这份扩展的签，已经由 CometBFT 验过，这样才把签交给应用再处理或再验。扩展启用时两份签都会在。若没给 `non_rp_vote_extension`，这份签签的是空切片。看见有签，不是已经按原样签。看见交给应用，不是已经有重放保护。看见签了空切片，不是已经必须填。
3. **看见扩展关掉则 `vote_extension` / `non_rp_vote_extension` 和对应的签都空 / 看见空着 不是已经到了启用高度，也不是已经交差。**  
   官方写：若投票扩展关掉，`vote_extension`、`non_rp_vote_extension` 和对应的签都空。看见空着，不是已经到了启用高度。看见关掉了，不是已经交差。看见字段在，不是已经从块里抽出。

怎样编 `ExtendedVoteInfo`、怎样验签、怎样开关扩展是规范里的做法，本页不抄。从拟议块或已决块抽出就已经带了公钥是不变量 365，本页不抄。

## 官方为什么这样拆

- **从本进程抽出 ≠ 已经从块里抽出：** 官方把本进程抽出和从块里抽出分开。
- **把验过的签交给应用 ≠ 已经按原样签：** 官方把交给应用和包装方式分开。
- **扩展关掉则字段全空 ≠ 已经到了启用高度：** 官方把关掉全空和启用高度分开。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 从本进程抽出 | 不是已经从块里抽出 | 不是从拟议块或已决块抽出就已经带了公钥（365） |
| 把验过的签交给应用 | 不是已经按原样签 | 不是 vote_extension 会包进 CanonicalVoteExtension 就已经按原样签（358） |
| 扩展关掉则字段全空 | 不是已经到了启用高度 | 不是到了 H 就已经 Prepare 带了扩展（330） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看「看见 Prepare 里有扩展就已经从块里抽出、已经按原样签、已经到了启用高度」，必须分开从本进程抽出是不是已经从块里抽出、把验过的签交给应用是不是已经按原样签、扩展关掉则字段全空是不是已经到了启用高度。可以跳过「看见 Prepare 里有扩展就已经从块里抽出」。不要另写怎样写 ExtendedVoteInfo。369 extvoteinfo vs local bundled unbundling 完成（818 item 1 / 819 item 2 / 820 item 3）；精读 [`worked-example-extvoteinfo-notblock-vs-bundled.md`](worked-example-extvoteinfo-notblock-vs-bundled.md)（不变量 818 item 1）。

## 本页不抄

- 怎样编 `ExtendedVoteInfo`、怎样验签、怎样开关扩展。
- 从拟议块或已决块抽出就已经带了公钥。那是不变量 365。
- vote_extension 会包进 CanonicalVoteExtension 就已经按原样签。那是不变量 358。
- 到了 H 就已经 Prepare 带了扩展。那是不变量 330。
