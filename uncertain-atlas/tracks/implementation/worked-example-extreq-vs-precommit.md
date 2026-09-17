# 例：看见 ExtendVoteRequest 的内容对应共识即将发 Precommit 的那份拟议块不是已经会调 ExtendVote；看见 Precommit 没有带有效签的扩展就会当非法丢掉、不调 Verify 不是已经跳过 Verify；看见 Verify ACCEPT 会把这张票和扩展留在内部结构、给 h+1 自己提议时的 Prepare 填 ExtendedCommitInfo 不是已经 Verify 过迟到扩展

**层次**：实现 / ExtendVote 请求对应。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) ExtendVote Usage / VerifyVoteExtension When。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「ExtendVoteRequest 的内容对应共识即将发 Precommit 的那份拟议块不是已经会调 ExtendVote / Precommit 没有带有效签的扩展就会当非法丢掉、不调 Verify 不是已经跳过 Verify / Verify ACCEPT 会把这张票和扩展留在内部结构、给 h+1 自己提议时的 Prepare 填 ExtendedCommitInfo 不是已经 Verify 过迟到扩展」，不是一轮只能交出一份扩展就已经是每一高度一份，也不是空扩展仍会调 Verify 就已经跳过 Verify。不要另写怎样写 ExtendVote 请求对应。

## 官方三件事

规范把 `ExtendVoteRequest` 的内容对应即将发 Precommit 的那份拟议块、没有有效签的扩展先丢掉整张 Precommit、ACCEPT 才把票和扩展留给下一高 Prepare 写成三件独立的实现事，不是「看见填了 ExtendVote 请求对应就已经会调 ExtendVote、已经跳过 Verify、已经 Verify 过迟到扩展」一件事：

1. **看见 `ExtendVoteRequest` 的内容对应共识即将发 Precommit 的那份拟议块 / 看见填了请求 不是已经会调 ExtendVote，也不是已经签了 nil 票。**  
   官方写：`ExtendVoteRequest` 的内容对应共识算法即将发 Precommit 的那份拟议块。看见填了请求，不是已经到了 prevote 步就已经会调。看见对上了拟议块，不是已经只在即将广播非 nil Precommit 时才叫。看见有内容，不是已经交差。
2. **看见 Precommit 没有带有效签的扩展就会当非法丢掉、不调 Verify / 看见空扩展 不是已经跳过 Verify，也不是已经自己验过。**  
   官方写：若 Precommit 没有带有效签的扩展，*p* 把这张 Precommit 当非法丢掉。0 长度扩展只要伴随签名也合法，就算有效。看见丢掉了，不是已经空扩展仍会调 Verify 那种已经跳过。看见空扩展，不是已经没有签。看见没调 Verify，不是已经自己验过。
3. **看见 Verify `ACCEPT` 会把这张票和扩展留在内部结构、给 *h+1* 自己提议时的 Prepare 填 `ExtendedCommitInfo` / 看见收下了 不是已经 Verify 过迟到扩展，也不是已经交差。**  
   官方写：应用回 `ACCEPT` 后，*p* 把收到的票和对应扩展留在内部结构，用来在高度 *h+1*、自己当提议者的那些轮里，给 `PrepareProposal` 填 `ExtendedCommitInfo`。看见收下了，不是已经 +2/3 之后才进来的扩展写进了 commit info 那种已经 Verify 过。看见留给下一高，不是已经交差。看见能填，不是已经必须再 Verify。

怎样写 ExtendVote 请求对应、怎样验伴随签名、怎样攒下一高 Prepare 是规范里的做法，本页不抄。一轮只能交出一份扩展就已经是每一高度一份是不变量 350，本页不抄。

## 官方为什么这样拆

- **ExtendVoteRequest 的内容对应共识即将发 Precommit 的那份拟议块 ≠ 已经会调 ExtendVote：** 官方把请求内容和已经会调分开。
- **Precommit 没有带有效签的扩展就会当非法丢掉、不调 Verify ≠ 已经跳过 Verify：** 官方把签先丢掉和空扩展仍会调分开。
- **Verify ACCEPT 会把这张票和扩展留在内部结构、给 h+1 自己提议时的 Prepare 填 ExtendedCommitInfo ≠ 已经 Verify 过迟到扩展：** 官方把本高 ACCEPT 留下去和迟到扩展已经 Verify 过分开。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| ExtendVoteRequest 的内容对应共识即将发 Precommit 的那份拟议块 | 不是已经会调 ExtendVote | 不是一轮只能交出一份扩展就已经是每一高度一份（350） |
| Precommit 没有带有效签的扩展就会当非法丢掉、不调 Verify | 不是已经跳过 Verify | 不是空扩展仍会调 Verify 就已经跳过 Verify（353） |
| Verify ACCEPT 会把这张票和扩展留在内部结构、给 h+1 自己提议时的 Prepare 填 ExtendedCommitInfo | 不是已经 Verify 过迟到扩展 | 不是 +2/3 之后才进来的扩展写进了 commit info 就已经 Verify 过（352） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看「看见填了 ExtendVote 请求对应就已经会调 ExtendVote、已经跳过 Verify、已经 Verify 过迟到扩展」，必须分开 ExtendVoteRequest 的内容对应共识即将发 Precommit 的那份拟议块是不是已经会调 ExtendVote、Precommit 没有带有效签的扩展就会当非法丢掉、不调 Verify 是不是已经跳过 Verify、Verify ACCEPT 会把这张票和扩展留在内部结构、给 h+1 自己提议时的 Prepare 填 ExtendedCommitInfo 是不是已经 Verify 过迟到扩展。可以跳过「看见填了 ExtendVote 请求对应就已经会调 ExtendVote」。不要另写怎样写 ExtendVote 请求对应。409 extreq vs precommit bundled unbundling 完成（1031 item 1 / 1032 item 2 / 1033 item 3）；精读 [`worked-example-extpre-notcall-vs-bundled.md`](worked-example-extpre-notcall-vs-bundled.md)（不变量 1031 item 1）。

## 本页不抄

- 怎样写 ExtendVote 请求对应、怎样验伴随签名、怎样攒下一高 Prepare。
- 一轮只能交出一份扩展就已经是每一高度一份。那是不变量 350。
- 空扩展仍会调 Verify 就已经跳过 Verify。那是不变量 353。
- +2/3 之后才进来的扩展写进了 commit info 就已经 Verify 过。那是不变量 352。
