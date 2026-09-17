# 例：看见 Precommit 没有带有效签的扩展就会当非法丢掉、不调 Verify 不是已经跳过 Verify；看见带有效签就会调 VerifyVoteExtension 不是已经验过扩展；看见 ACCEPT 会把票和扩展留给 h+1 自己提议时的 Prepare 填 ExtendedCommitInfo、REJECT 会把 Precommit 当非法丢掉 不是已经写进 last_commit

**层次**：实现 / Verify When 正式流程。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) VerifyVoteExtension When。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「Precommit 没有带有效签的扩展就会当非法丢掉、不调 Verify 不是已经跳过 Verify / 带有效签就会调 VerifyVoteExtension 不是已经验过扩展 / ACCEPT 会把票和扩展留给 h+1 自己提议时的 Prepare 填 ExtendedCommitInfo、REJECT 会把 Precommit 当非法丢掉 不是已经写进 last_commit」，不是空扩展仍会调 Verify 就已经跳过 Verify，也不是 ExtendVoteRequest 的内容对应共识即将发 Precommit 的那份拟议块就已经会调 ExtendVote。不要另写怎样写 Verify When 正式流程。

## 官方三件事

规范把 Precommit 没有有效签先丢掉、带有效签才调 Verify、ACCEPT 留给下一高 Prepare / REJECT 丢掉整张 Precommit 写成三件独立的实现事，不是「看见收到 Precommit 就已经跳过 Verify、已经验过扩展、已经写进 last_commit」一件事：

1. **看见 Precommit 没有带有效签的扩展就会当非法丢掉、不调 Verify / 看见丢掉了 不是已经跳过 Verify，也不是已经验过扩展。**  
   官方写：若 Precommit 没有带有效签的扩展，*p* 把这张 Precommit 当非法丢掉。0 长度扩展只要伴随签名也合法，就算有效。看见丢掉了，不是已经空扩展仍会调 Verify 那种已经跳过。看见没调 Verify，不是已经验过扩展。看见没签，不是已经 Accept。
2. **看见带有效签就会调 `VerifyVoteExtension` / 看见 CometBFT 会叫 不是已经验过扩展，也不是已经 Accept。**  
   官方写：节点 *p* 在一轮 *r*、高度 *h*，收到验证者 *q*（*q* ≠ *p*）的 Precommit，且扩展带有效签，*p* 的 CometBFT 会调 `VerifyVoteExtension`。应用通过 `VerifyVoteExtensionResponse.status` 回 `ACCEPT` 或 `REJECT`。看见叫了，不是已经验过扩展。看见会调，不是已经 Accept。看见收到他人票，不是已经不对本进程自己发出的 Precommit 调用那种本地票。
3. **看见 `ACCEPT` 会把票和扩展留在内部结构、给 *h+1* 自己提议时的 Prepare 填 `ExtendedCommitInfo` / 看见 `REJECT` 会把 Precommit 当非法丢掉 不是已经写进 last_commit，也不是已经 Verify 过迟到扩展。**  
   官方写：若应用回 `ACCEPT`，*p* 会把收到的票和对应扩展留在内部结构，用来在高度 *h+1*、自己当提议者的那些轮里，给 `PrepareProposal` 填 `ExtendedCommitInfo`。若应用回 `REJECT`，*p* 会把 Precommit 当非法丢掉。看见收下了，不是已经 +2/3 之后才进来的扩展写进了 commit info 那种已经 Verify 过。看见留给下一高，不是已经写进 last_commit。看见丢掉了，不是已经当成块非法。

怎样写 Verify When 正式流程、怎样验伴随签名、怎样攒下一高 Prepare 是规范里的做法，本页不抄。空扩展仍会调 Verify 是不变量 353，本页不抄。

## 官方为什么这样拆

- **Precommit 没有带有效签的扩展就会当非法丢掉、不调 Verify ≠ 已经跳过 Verify：** 官方把签先丢掉和空扩展仍会调 Verify 分开。
- **带有效签就会调 VerifyVoteExtension ≠ 已经验过扩展：** 官方把会叫 Verify 和已经 Accept 分开。
- **ACCEPT 留给 h+1 Prepare / REJECT 丢掉 Precommit ≠ 已经写进 last_commit：** 官方把本高 ACCEPT 留下去和迟到扩展已经 Verify 过分开。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| Precommit 没有带有效签的扩展就会当非法丢掉、不调 Verify | 不是已经跳过 Verify | 不是空扩展仍会调 Verify 就已经跳过 Verify（353） |
| 带有效签就会调 VerifyVoteExtension | 不是已经验过扩展 | 不是 VerifyStatus 的 ACCEPT 就已经验过扩展（434） |
| ACCEPT 留给 h+1 Prepare / REJECT 丢掉 Precommit | 不是已经写进 last_commit | 不是 +2/3 之后才进来的扩展写进了 commit info 就已经 Verify 过（352） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看「看见收到 Precommit 就已经跳过 Verify、已经验过扩展、已经写进 last_commit」，必须分开 Precommit 没有带有效签的扩展就会当非法丢掉、不调 Verify 是不是已经跳过 Verify、带有效签就会调 VerifyVoteExtension 是不是已经验过扩展、ACCEPT 留给 h+1 Prepare / REJECT 丢掉 Precommit 是不是已经写进 last_commit。可以跳过「看见收到 Precommit 就已经验过扩展」。不要另写怎样写 Verify When 正式流程。

## 本页不抄

- 怎样写 Verify When 正式流程、怎样验伴随签名、怎样攒下一高 Prepare。
- 空扩展仍会调 Verify 就已经跳过 Verify。那是不变量 353。
- ExtendVoteRequest 的内容对应共识即将发 Precommit 的那份拟议块就已经会调 ExtendVote。那是不变量 409。
- +2/3 之后才进来的扩展写进了 commit info 就已经 Verify 过。那是不变量 352。
- VerifyVoteExtensionResponse.status 是应用认为这份扩展合法还是非法就已经当成块非法。那是不变量 433。
