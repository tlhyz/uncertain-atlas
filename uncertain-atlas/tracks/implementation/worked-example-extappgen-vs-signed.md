# 例：看见 ExtendVoteResponse.vote_extension 是应用生成的信息、将由 CometBFT 签名不是已经签过 / 已经包进 CanonicalVoteExtension；看见 ExtendVoteResponse.non_rp_extension 是应用生成的信息、将由 CometBFT 签名并挂到 Precommit、相对 vote_extension 不做重放保护不是已经和 vote_extension 同一份签法 / 已经有重放保护；看见 will be signed 并 attached to Precommit 不是已经广播 Precommit / 已经写进 last_commit

**层次**：实现 / ExtendVote Response Usage application-generated 正式三事。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) ExtendVote Usage。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「ExtendVoteResponse.vote_extension 是应用生成的信息、将由 CometBFT 签名不是已经签过 / 已经包进 CanonicalVoteExtension / ExtendVoteResponse.non_rp_extension 是应用生成的信息、将由 CometBFT 签名并挂到 Precommit、相对 vote_extension 不做重放保护不是已经和 vote_extension 同一份签法 / 已经有重放保护 / will be signed 并 attached to Precommit 不是已经广播 Precommit / 已经写进 last_commit」，不是 ExtendVoteResponse.vote_extension 是 CometBFT 签的信息、可以 0 长、标成非确定就已经会包进 CanonicalVoteExtension，也不是 vote_extension 会包进 CanonicalVoteExtension 就已经按原样签。不要另写怎样写 ExtendVote Response Usage application-generated 正式三事。

## 官方三件事

规范把 ExtendVote Response Usage 里 application-generated、will be signed、attached to Precommit、non_rp 不做重放保护写成三件独立的实现事，不是「看见应用回了扩展就已经签过、已经包进 CanonicalVoteExtension、已经广播 Precommit」一件事：

1. **看见 `ExtendVoteResponse.vote_extension` 是 application-generated information that will be signed / 看见应用生成的信息、将由 CometBFT 签名 不是已经签过，也不是已经包进 `CanonicalVoteExtension`。**  
   官方写：`ExtendVoteResponse.vote_extension` 是 application-generated information that will be signed。看见应用生成的信息，不是已经 CometBFT 签完。看见 will be signed，不是已经填进 `CanonicalVoteExtension` 并签那份包装。看见将由 CometBFT 签名，不是已经 attached to Precommit。
2. **看见 `ExtendVoteResponse.non_rp_extension` 是 application-generated information that will be signed by CometBFT and attached to the Precommit message / 看见第二份也是应用生成的、将签名并挂到 Precommit / 相对 `vote_extension` 不做重放保护 不是已经和 `vote_extension` 同一份签法，也不是已经有重放保护。**  
   官方写：`ExtendVoteResponse.non_rp_extension` 也是 application-generated information that will be signed by CometBFT and attached to the Precommit message。No replay-protection is applied to the data as compared to `ExtendVoteResponse.vote_extension`。Applications can use this if raw vote extension data needs to be signed without any wrapping structure。看见第二份也是应用生成的，不是已经和第一份同一对象。看见 will be signed and attached，不是已经按原样签完。看见不做重放保护，不是已经有 Height / Round / ChainID 包装。
3. **看见 will be signed 并 attached to the Precommit message / 看见规范写「将签名并挂到 Precommit」 不是已经广播 Precommit，也不是已经写进 last_commit。**  
   官方把 will be signed 和 attached to the Precommit message 写在 Usage 里，描述的是 ExtendVote 回包之后 CometBFT 还要做的事，不是 When 里已经完成的广播。看见 attached to Precommit，不是已经构造 Precommit 并广播。看见 will be signed，不是已经 Verify 过他人扩展。看见挂到 Precommit，不是已经写进 last_commit。

怎样写 ExtendVote Response Usage application-generated 正式三事、怎样选 non_rp、怎样挂到 Precommit 是规范里的做法，本页不抄。ExtendVoteResponse.vote_extension 是 CometBFT 签的信息、可以 0 长、标成非确定就已经会包进 CanonicalVoteExtension是不变量 418，本页不抄。

## 官方为什么这样拆

- **application-generated vote_extension will be signed ≠ 已经签过 / 已经包进 CanonicalVoteExtension：** 官方把应用生成和 CometBFT 后续签名、包装分开。
- **application-generated non_rp will be signed and attached、不做重放保护 ≠ 已经和 vote_extension 同一份签法：** 官方把两份应用生成扩展和两种签名路径分开。
- **will be signed and attached to Precommit ≠ 已经广播 / 已经写进 last_commit：** 官方把 Usage 里的将来时和 When 里的已完成步骤分开。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| application-generated vote_extension will be signed | 不是已经包进 CanonicalVoteExtension | 不是 ExtendVoteResponse.vote_extension 是 CometBFT 签的信息、可以 0 长、标成非确定就已经会包进 CanonicalVoteExtension（418） |
| non_rp application-generated、不做重放保护 | 不是已经和 vote_extension 同一份签法 | 不是 vote_extension 会包进 CanonicalVoteExtension、non_rp_extension 按原样签（358） |
| will be signed and attached to Precommit | 不是已经广播 Precommit | 不是应用回 extension 后 CometBFT 会填进 CanonicalVoteExtension 并广播 Precommit（438） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看「看见应用回了扩展就已经签过、已经包进 CanonicalVoteExtension、已经广播 Precommit」，必须分开 ExtendVoteResponse.vote_extension 是应用生成的信息、将由 CometBFT 签名是不是已经签过 / 已经包进 CanonicalVoteExtension、ExtendVoteResponse.non_rp_extension 是应用生成的信息、将由 CometBFT 签名并挂到 Precommit、相对 vote_extension 不做重放保护是不是已经和 vote_extension 同一份签法 / 已经有重放保护、will be signed 并 attached to Precommit 是不是已经广播 Precommit / 已经写进 last_commit。可以跳过「看见应用回了扩展就已经签过」。不要另写怎样写 ExtendVote Response Usage application-generated 正式三事。

## 本页不抄

- 怎样写 ExtendVote Response Usage application-generated 正式三事、怎样选 non_rp、怎样挂到 Precommit。
- ExtendVoteResponse.vote_extension 是 CometBFT 签的信息、可以 0 长、标成非确定就已经会包进 CanonicalVoteExtension。那是不变量 418。
- vote_extension 会包进 CanonicalVoteExtension、non_rp_extension 按原样签。那是不变量 358。
- 应用回 extension 后 CometBFT 会填进 CanonicalVoteExtension 并广播 Precommit。那是不变量 438。
