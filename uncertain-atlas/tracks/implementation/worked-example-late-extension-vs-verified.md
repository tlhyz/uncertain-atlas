# 例：看见 +2/3 之后才进来的扩展写进了 commit info 不是已经 Verify 过；看见建议按 Verify 同款逻辑再看一遍不是已经是引擎会再 Verify；看见下一高度 round 0 把上一高度 Precommit 写进 ExtendedCommitInfo 不是已经又叫了 Verify

**层次**：实现 / +2/3 之后才进来的扩展。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) PrepareProposal When / VerifyVoteExtension When。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5。本页是「+2/3 之后才进来的扩展写进了 commit info 不是已经 Verify 过 / 建议按 Verify 同款逻辑再看一遍不是已经是引擎会再 Verify / 下一高度 round 0 写进 ExtendedCommitInfo 不是已经又叫了 Verify」，不是验签拒收整张预提交就已经是块非法，也不是正确进程交出的扩展必须被正确接收者 Verify Accept。不要另写怎样再验迟到扩展。352 lateext vs verified bundled unbundling 启动（809）；精读 [`worked-example-lateext-notverified-vs-bundled.md`](worked-example-lateext-notverified-vs-bundled.md)（不变量 809 item 1）。

## 官方三件事

规范把 +2/3 之后才进来的扩展、Prepare 要用时建议再看、下一高度可以不叫 Verify 写成三件独立的实现事，不是「看见 last_commit 里有扩展就已经 Verify 过、已经是引擎会再 Verify、已经又叫了 Verify」一件事：

1. **看见 +2/3 之后才进来的扩展写进了 commit info / 看见 last_commit 里有扩展 不是已经 Verify 过，也不是已经 Accept。**  
   官方写：commit info 里，过了最低 +2/3 之后才加进来的那些票上的扩展，**没有**被 Verify。看见写进了 last_commit，不是已经 Verify 过。看见有扩展，不是已经 Accept。看见凑齐了 +2/3，不是后来的也已经验过。
2. **看见建议按 `VerifyVoteExtension` 同款逻辑再看一遍 / 看见 Prepare 要用这些扩展改提案 不是已经是引擎会再 Verify，也不是已经是正确进程交出的扩展必须被正确接收者 Verify Accept。**  
   官方写：应用 MAY 用 commit info 里的扩展改提案；这时建议按 Verify 同款逻辑再看一遍。看见建议再看，不是引擎已经再叫了 Verify。看见 Prepare 在用扩展，不是已经过了 Req 6。看见能改提案，不是已经交差。
3. **看见下一高度 round 0 收到上一高度 `CommitRound` 的 Precommit / 看见写进 `ExtendedCommitInfo` 不是已经又叫了 Verify，也不是已经必须再 Verify。**  
   官方写：节点在高度 *h*、round 0，收到验证者 *q*（*q* ≠ *p*）上一高度 *h-1*、`CommitRound` *r* 的 Precommit 时，MAY 把这张票和扩展写进 `ExtendedCommitInfo`，**不**再叫 `VerifyVoteExtension`。看见写进去了，不是已经又 Verify。看见规范允许，不是已经必须再叫。看见是上一高度，不是已经是本轮那次 Verify。

怎样再验迟到扩展、怎样写 Prepare、怎样攒 ExtendedCommitInfo 是规范里的做法，本页不抄。验签拒收整张预提交是不变量 34，本页不抄。

## 官方为什么这样拆

- **+2/3 之后才进来的扩展写进了 commit info ≠ 已经 Verify 过：** 官方把写进 commit info 和已经 Verify 分开。
- **建议按 Verify 同款逻辑再看一遍 ≠ 已经是引擎会再 Verify：** 官方把建议再看和引擎会再叫 Verify 分开。
- **下一高度 round 0 写进 ExtendedCommitInfo ≠ 已经又叫了 Verify：** 官方把可以写入和必须再 Verify 分开。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| +2/3 之后才进来的扩展写进了 commit info | 不是已经 Verify 过 | 不是验签拒收整张预提交就已经是块非法（34） |
| 建议按 Verify 同款逻辑再看一遍 | 不是已经是引擎会再 Verify | 不是正确进程交出的扩展必须被正确接收者 Verify Accept（348） |
| 下一高度 round 0 写进 ExtendedCommitInfo | 不是已经又叫了 Verify | 不是到了 H 已经 Prepare 带了扩展（330） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看「看见 last_commit 里有扩展就已经 Verify 过、已经是引擎会再 Verify、已经又叫了 Verify」，必须分开 +2/3 之后才进来的扩展写进了 commit info 是不是已经 Verify 过、建议按 Verify 同款逻辑再看一遍是不是已经是引擎会再 Verify、下一高度 round 0 写进 ExtendedCommitInfo 是不是已经又叫了 Verify。可以跳过「看见 last_commit 里有扩展就已经 Verify 过」。不要另写怎样再验迟到扩展。352 lateext vs verified bundled unbundling 启动（809）。

## 本页不抄

- 怎样再验迟到扩展、怎样写 Prepare、怎样攒 ExtendedCommitInfo。
- 验签拒收整张预提交就已经是块非法。那是不变量 34。
- 正确进程交出的扩展必须被正确接收者 Verify Accept。那是不变量 348。
- 到了 H 已经 Prepare 带了扩展。那是不变量 330。
