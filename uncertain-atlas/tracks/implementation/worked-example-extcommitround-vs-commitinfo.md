# 例：看见 ExtendedCommitInfo.round 是提交轮不是已经是 CommitInfo.round；看见 Finalize 请求 next_validators_hash 是下一验证者集合默克尔根不是已经是同一套字段；看见 Echo 请求 Message 是要回显的字符串不是已经是 Flush

**层次**：实现 / ExtendedCommitInfo 轮。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) ExtendedCommitInfo / FinalizeBlock Request / Echo Request。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5。本页是「ExtendedCommitInfo.round 是提交轮不是已经是 CommitInfo.round / Finalize 请求 next_validators_hash 是下一验证者集合默克尔根不是已经是同一套字段 / Echo 请求 Message 是要回显的字符串不是已经是 Flush」，不是 CommitInfo.round 就已经按投票权排过，也不是 Prepare 和 Process / Finalize 同一套字段就已经跑过 Process。不要另写怎样写 ExtendedCommitInfo 轮。

## 官方三件事

规范把 ExtendedCommitInfo `round` 是提交轮、Finalize 请求 `next_validators_hash` 是下一验证者集合默克尔根、Echo 请求 `Message` 是要回显的字符串写成三件独立的实现事，不是「看见填了 ExtendedCommitInfo 轮就已经是 CommitInfo.round、已经是同一套字段、已经是 Flush」一件事：

1. **看见 ExtendedCommitInfo `round` 是提交轮 / 看见填了 round 不是已经是 CommitInfo.round，也不是已经按投票权排过。**  
   官方写：`round` 是提交轮，反映上一高度块提议者决定时的那一轮。看见填了 round，不是已经是 CommitInfo 那份提交轮。看见有轮次，不是已经按投票权降序排过。看见能填，不是已经交差。
2. **看见 Finalize 请求 `next_validators_hash` 是下一验证者集合默克尔根 / 看见填了 next_validators_hash 不是已经是同一套字段，也不是已经换了人。**  
   官方写：`next_validators_hash` 是下一验证者集合的默克尔根。看见填了 next_validators_hash，不是已经是 Prepare 那种字段名对上就已经跑过 Process。看见有下一集合根，不是已经是 H+1 那种已经换了人。看见能填，不是已经交差。
3. **看见 Echo 请求 `Message` 是要回显的字符串 / 看见填了 Message 不是已经是 Flush，也不是已经送到。**  
   官方写：`Message` 是要回显的字符串。看见填了 Message，不是已经是 Flush 那种把排队冲到服务端。看见能回显，不是已经送到。看见能填，不是已经交差。

怎样写 ExtendedCommitInfo 轮、怎样填提交轮、怎样填下一集合根是规范里的做法，本页不抄。CommitInfo.round 就已经按投票权排过是不变量 392，本页不抄。

## 官方为什么这样拆

- **ExtendedCommitInfo.round 是提交轮 ≠ 已经是 CommitInfo.round：** 官方把带扩展的提交轮和不带扩展的提交轮分开。
- **Finalize 请求 next_validators_hash 是下一验证者集合默克尔根 ≠ 已经是同一套字段：** 官方把下一集合根和字段名对上就已经跑过 Process 分开。
- **Echo 请求 Message 是要回显的字符串 ≠ 已经是 Flush：** 官方把回显字符串和冲队列分开。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| ExtendedCommitInfo.round 是提交轮 | 不是已经是 CommitInfo.round | 不是 CommitInfo.round 就已经按投票权排过（392） |
| Finalize 请求 next_validators_hash 是下一验证者集合默克尔根 | 不是已经是同一套字段 | 不是 Prepare 和 Process / Finalize 同一套字段就已经跑过 Process（359） |
| Echo 请求 Message 是要回显的字符串 | 不是已经是 Flush | 不是 Flush 要把客户端排队的消息冲到服务端就已经送到（374） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看「看见填了 ExtendedCommitInfo 轮就已经是 CommitInfo.round、已经是同一套字段、已经是 Flush」，必须分开 ExtendedCommitInfo.round 是提交轮是不是已经是 CommitInfo.round、Finalize 请求 next_validators_hash 是下一验证者集合默克尔根是不是已经是同一套字段、Echo 请求 Message 是要回显的字符串是不是已经是 Flush。可以跳过「看见填了 ExtendedCommitInfo 轮就已经是 CommitInfo.round」。不要另写怎样写 ExtendedCommitInfo 轮。394 extcommitround vs commitinfo bundled unbundling 完成（749 item 1 / 750 item 2 / 751 item 3）；精读 [`worked-example-extcommitround-notcommitinfo-vs-bundled.md`](worked-example-extcommitround-notcommitinfo-vs-bundled.md)（不变量 749 item 1）。

## 本页不抄

- 怎样写 ExtendedCommitInfo 轮、怎样填提交轮、怎样填下一集合根。
- CommitInfo.round 就已经按投票权排过。那是不变量 392。
- Prepare 和 Process / Finalize 同一套字段就已经跑过 Process。那是不变量 359。
- Flush 要把客户端排队的消息冲到服务端就已经送到。那是不变量 374。
