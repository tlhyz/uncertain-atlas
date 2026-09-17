# 例：看见 Echo 回包 Message 是入参那串 is not already request field interchangeable / not already echoed interchangeable / not already Echo Usage response interchangeable

**层次**：实现 / Echo 回包 Message not request field / not already echoed / not Echo Usage response 正式三事（399 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) Commit Request / Echo Response / Echo Usage。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「Echo 回包 Message not request field / not already echoed / not Echo Usage response 正式三事（399 余量）/ not 732 commitnoparam-notreqfield interchangeable / not 399 commitnoparam-vs-persist bundled interchangeable」，不是 Commit 空请求 bundled（399），也不是 Echo 请求 Message 就已经是 Flush（394）或 Echo Usage Response（492 / 675）。不要另写怎样写 Commit 空请求。

## 官方三件事

1. **看见 Echo Response `Message` / 看见 Echo 回包 Message 是入参那串 / Echo 回包 Message is not already 已经 Echo 请求那份要回显的字符串 interchangeable / 394 extcommitround interchangeable，也不是已经 Commit 空请求 bundled（399） interchangeable / 732 commitnoparam-notreqfield interchangeable / 731 commitnoparam-notpersist interchangeable / 399 commitnoparam item 1 Commit 不带参数 interchangeable，也不是已经 Echo 回包 Message not request field / not already echoed / not Echo Usage response 正式三事 bundled（399 item 2 余量） interchangeable / 399 commitnoparam item 2 interchangeable。**  
   官方写：回包 `Message` 是入参那串。看见回了 Message，不是已经是 Echo 请求那份要回显的字符串 interchangeable——本页从 399 item 2 侧钉 not request field 单句。399 commitnoparam vs persist bundled unbundling 在本页 item 2 续。

2. **看见回了 Message / 看见能回 / Echo 回包 Message is not already 已经回显 interchangeable，也不是已经 Commit 空请求 bundled（399） interchangeable / 732 commitnoparam-notreqfield interchangeable / 399 commitnoparam item 3 Echo 测实现 interchangeable / 733 commitnoparam-notflush interchangeable。**  
   官方把回包那串和已经回显分开——399 bundled 第二件事常与「看见回了 Message 就已经回显 interchangeable」糊成一句，本页钉 not already echoed 单句。

3. **看见回了 Message / 看见能填 / Echo 回包 Message is not already 已经 Echo Usage Response Message interchangeable / 492 / 675 echousage-notreqresp interchangeable，也不是已经 Commit 空请求 bundled（399） interchangeable / 732 commitnoparam-notreqfield interchangeable / 731 commitnoparam-notpersist interchangeable。**  
   官方把 399 侧回包那串和 492 Echo Usage Response 分开。看见能填，不是已经 675 interchangeable。399 commitnoparam vs persist bundled unbundling 在本页 item 2 续。

怎样写 Commit 空请求、怎样填 Echo 回包、怎样测实现是规范里的做法，本页不抄。

## 官方为什么这样拆

- **Echo 回包 Message not request field ≠ 394 interchangeable：** 官方把回包那串和请求要回显的字符串分开。
- **Echo 回包 Message not already echoed ≠ 已经回显 interchangeable：** 官方把能回 Message 和已经回显分开。
- **Echo 回包 Message not Echo Usage response ≠ 492 / 675 interchangeable：** 官方把 399 侧回包和 492 Echo Usage Response 分开；399 commitnoparam vs persist bundled unbundling 在本页 item 2 续。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| Echo 回包 Message 是入参那串 | 不是已经是入参字段（394） | 不是 Commit 不带参数（731/399 item 1） |
| 看见回了 Message | 不是已经回显 | 不是 Commit 空请求 bundled（399） |
| 看见能填 | 不是已经 Echo Usage Response（492 / 675） | 不是 Echo 用来测实现（733/399 item 3） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Echo 回包 Message not request field / not already echoed / not Echo Usage response 正式三事（399 余量），必须分开回包 Message 是不是已经是入参字段 interchangeable / 394、是不是已经回显、是不是已经 Echo Usage Response interchangeable / 492 / 675。可以跳过「看见回了 Message 就已经是入参字段」。不要另写怎样写 Commit 空请求。399 commitnoparam vs persist bundled unbundling 在本页 item 2 续；完成 [`worked-example-commitnoparam-notflush-vs-bundled.md`](worked-example-commitnoparam-notflush-vs-bundled.md)（不变量 733 item 3）。

## 本页不抄

- 怎样写 Commit 空请求、怎样填 Echo 回包、怎样测实现。
- Commit 空请求 bundled。那是不变量 399。
- Commit 不带参数。那是不变量 399 item 1 余量 / 731。
- Echo 用来测实现。那是不变量 399 item 3 余量 / 733。
- Echo 请求 Message 就已经是 Flush。那是不变量 394。
- Echo Usage Response Message。那是不变量 492 / 675。
