# 例：看见 vote_extension 会包进 CanonicalVoteExtension 不是已经按原样签；看见 non_rp_extension 按应用给的字节原样签不是已经有重放保护；看见应用要签原样数据可以用 non_rp 不是已经和 vote_extension 同一份

**层次**：实现 / 两份扩展两份签。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) ExtendVote Usage / VerifyVoteExtension Usage。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5。本页是「vote_extension 会包进 CanonicalVoteExtension 不是已经按原样签 / non_rp_extension 按原样签不是已经有重放保护 / 要签原样数据可以用 non_rp 不是已经和 vote_extension 同一份」，不是 CanonicalVoteExtension 就已经是 CanonicalVote，也不是空扩展仍验签。不要另写怎样编两份扩展。358 nonrp vs wrapped bundled unbundling 完成（827+828+829）；精读 [`worked-example-nonrp-notraw-vs-bundled.md`](worked-example-nonrp-notraw-vs-bundled.md)（不变量 827 item 1）；精读 [`worked-example-nonrp-notprotected-vs-bundled.md`](worked-example-nonrp-notprotected-vs-bundled.md)（不变量 828 item 2）；精读 [`worked-example-nonrp-notsame-vs-bundled.md`](worked-example-nonrp-notsame-vs-bundled.md)（不变量 829 item 3）。

## 官方三件事

规范把 `vote_extension` 包进 `CanonicalVoteExtension` 再签、`non_rp_extension` 按原样签且没有重放保护、应用要签原样数据才用第二份字段写成三件独立的实现事，不是「看见有扩展就已经按原样签、已经有重放保护、已经和 vote_extension 同一份」一件事：

1. **看见 `vote_extension` 会包进 `CanonicalVoteExtension` / 看见绑了 Height Round ChainID 不是已经按原样签，也不是已经是 `CanonicalVote`。**  
   官方写：`ExtendVoteResponse.vote_extension` 会进 `CanonicalVoteExtension`，再填 Height、Round、ChainID 后签名。看见绑了这些字段，不是已经按应用给的字节原样签。看见有包装，不是已经是票上那份 `CanonicalVote`。看见签了，不是已经交差。
2. **看见 `non_rp_extension` 按应用给的字节原样签 / 看见没有包装 不是已经有重放保护，也不是已经必须填。**  
   官方写：`non_rp_extension` 由 CometBFT 签名并挂上 Precommit，**不**再套一层重放保护，和 `vote_extension` 不同。看见按原样签了，不是已经有 Height / Round / ChainID。看见字段在，不是已经必须填。看见没有包装，不是已经交差。
3. **看见应用要签原样数据可以用 `non_rp` / 看见有第二份字段 不是已经和 `vote_extension` 同一份，也不是已经是空扩展仍验签。**  
   官方写：应用若要把原样扩展数据签出去、不要包装，可以用这份字段。`non_rp_vote_extension` 可选，也可以空。看见有第二份，不是已经和第一份同一对象。看见能空，不是已经是 34 那种空扩展仍验签。看见能用，不是已经交差。

怎样编两份扩展、怎样自防重放、怎样选空是规范里的做法，本页不抄。`CanonicalVoteExtension` 就已经是 `CanonicalVote` 是不变量 34，本页不抄。

## 官方为什么这样拆

- **vote_extension 会包进 CanonicalVoteExtension ≠ 已经按原样签：** 官方把包装和原样签分开。
- **non_rp_extension 按原样签 ≠ 已经有重放保护：** 官方把没有包装和已经有保护分开。
- **要签原样数据可以用 non_rp ≠ 已经和 vote_extension 同一份：** 官方把第二份字段和第一份分开。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| vote_extension 会包进 CanonicalVoteExtension | 不是已经按原样签 | 不是 CanonicalVoteExtension 就已经是 CanonicalVote（34） |
| non_rp_extension 按原样签 | 不是已经有重放保护 | 不是一轮只能交出一份扩展就已经是每一高度一份（350） |
| 要签原样数据可以用 non_rp | 不是已经和 vote_extension 同一份 | 不是空扩展仍会调 Verify 就已经跳过 Verify（353） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看「看见有扩展就已经按原样签、已经有重放保护、已经和 vote_extension 同一份」，必须分开 vote_extension 会包进 CanonicalVoteExtension 是不是已经按原样签、non_rp_extension 按原样签是不是已经有重放保护、要签原样数据可以用 non_rp 是不是已经和 vote_extension 同一份。可以跳过「看见有扩展就已经按原样签」。不要另写怎样编两份扩展。358 nonrp vs wrapped bundled unbundling 完成（827+828+829）。

## 本页不抄

- 怎样编两份扩展、怎样自防重放、怎样选空。
- CanonicalVoteExtension 就已经是 CanonicalVote。那是不变量 34。
- 一轮只能交出一份扩展就已经是每一高度一份。那是不变量 350。
- 空扩展仍会调 Verify 就已经跳过 Verify。那是不变量 353。
