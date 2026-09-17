# 例：看见 Echo 请求 Message 是要回显的字符串 is not already Flush interchangeable / not already delivered interchangeable / not already settled interchangeable

**层次**：实现 / Echo 请求 Message not already Flush / not already delivered / not already settled 正式三事（394 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) ExtendedCommitInfo / FinalizeBlock Request / Echo Request。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「Echo 请求 Message not already Flush / not already delivered / not already settled 正式三事（394 余量）/ not 751 extcommitround-notflush interchangeable / not 394 extcommitround-vs-commitinfo bundled interchangeable」，不是 ExtendedCommitInfo 轮 bundled（394），也不是 Flush 要把客户端排队的消息冲到服务端就已经送到（374），也不是 Commit 空请求 Echo 回包 Message 就已经是入参字段（399/732）。不要另写怎样写 ExtendedCommitInfo 轮。

## 官方三件事

1. **看见 Echo 请求 `Message` 是要回显的字符串 / 看见填了 Message / Echo 这份要回显的串 is not already 已经是 Flush 那种把排队冲到服务端 interchangeable / 374 flush interchangeable，也不是已经 ExtendedCommitInfo 轮 bundled（394） interchangeable / 751 extcommitround-notflush interchangeable / 749 extcommitround-notcommitinfo interchangeable / 394 extcommitround item 1 round interchangeable，也不是已经 Message not already Flush / not already delivered / not already settled 正式三事 bundled（394 item 3 余量） interchangeable / 394 extcommitround item 3 interchangeable。**  
   官方写：`Message` 是要回显的字符串。看见填了 Message，不是已经是 Flush 那种把排队冲到服务端 interchangeable——本页从 394 item 3 侧钉 not already Flush 单句。394 extcommitround vs commitinfo bundled unbundling 在本页 item 3 完成。

2. **看见填了 Message / 看见能回显 / Echo 这份要回显的串 is not already 已经送到 interchangeable / 374 flush interchangeable，也不是已经 ExtendedCommitInfo 轮 bundled（394） interchangeable / 751 extcommitround-notflush interchangeable / 394 extcommitround item 2 next_validators_hash interchangeable / 750 extcommitround-notsamefields interchangeable，也不是已经 Commit 空请求 Echo 回包 Message 就已经是入参字段 interchangeable / 399 commitnoparam / 732 commitnoparam-notreqfield interchangeable。**  
   官方把回显字符串和已经送到分开——394 bundled 第三件事常与 374 混成「看见填了 Echo 请求 Message 就已经送到 interchangeable」，本页钉 not already delivered 单句。

3. **看见填了 Message / 看见能填 / Echo 这份要回显的串 is not already 已经交差 interchangeable，也不是已经 ExtendedCommitInfo 轮 bundled（394） interchangeable / 751 extcommitround-notflush interchangeable / 749 extcommitround-notcommitinfo interchangeable。**  
   官方把能填 Echo 请求 Message 和已经交差分开。看见能填，不是已经交差 interchangeable。394 extcommitround vs commitinfo bundled unbundling 在本页 item 3 完成。

怎样写 ExtendedCommitInfo 轮、怎样填提交轮、怎样填下一集合根是规范里的做法，本页不抄。

## 官方为什么这样拆

- **Message not already Flush ≠ 374 interchangeable：** 官方把回显字符串和冲队列分开。
- **Message not already delivered ≠ 374 interchangeable：** 官方把能回显和已经送到分开。
- **Message not already settled ≠ 已经交差 interchangeable：** 官方把能填 Echo 请求 Message 和已经交差分开；394 extcommitround vs commitinfo bundled unbundling 在本页 item 3 完成。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| Echo 请求 Message 是要回显的字符串 | 不是已经是 Flush（374） | 不是 ExtendedCommitInfo.round（749/394 item 1） |
| 看见填了 Message | 不是已经送到（374） | 不是 ExtendedCommitInfo 轮 bundled（394） |
| 看见能填 | 不是已经交差 | 不是 Commit 空请求 Echo 回包 Message（399/732） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Echo 请求 Message not already Flush / not already delivered / not already settled 正式三事（394 余量），必须分开 Message 是不是已经是 Flush interchangeable / 374、是不是已经送到 interchangeable / 374、是不是已经交差。可以跳过「看见填了 Echo 请求 Message 就已经是 Flush」。不要另写怎样写 ExtendedCommitInfo 轮。394 extcommitround vs commitinfo bundled unbundling 在本页 item 3 完成。

## 本页不抄

- 怎样写 ExtendedCommitInfo 轮、怎样填提交轮、怎样填下一集合根。
- ExtendedCommitInfo 轮 bundled。那是不变量 394。
- ExtendedCommitInfo.round。那是不变量 394 item 1 余量 / 749。
- Finalize 请求 next_validators_hash。那是不变量 394 item 2 余量 / 750。
- Flush 要把客户端排队的消息冲到服务端就已经送到。那是不变量 374。
- Commit 空请求 Echo 回包 Message 就已经是入参字段。那是不变量 399 / 732。
