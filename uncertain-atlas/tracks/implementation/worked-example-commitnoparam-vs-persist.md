# 例：看见 Commit 不带参数不是已经落盘；看见 Echo 回包 Message 是入参那串不是已经是入参字段；看见 Echo 用来测实现不是已经刷完

**层次**：实现 / Commit 空请求。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) Commit Request / Echo Response / Echo Usage。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5。本页是「Commit 不带参数不是已经落盘 / Echo 回包 Message 是入参那串不是已经是入参字段 / Echo 用来测实现不是已经刷完」，不是 Finalize 改了就已经落盘，也不是 Echo 请求 Message 就已经是 Flush。不要另写怎样写 Commit 空请求。

## 官方三件事

规范把 Commit 不带参数、Echo 回包 `Message` 是入参那串、Echo 用来测实现写成三件独立的实现事，不是「看见叫了 Commit 就已经落盘、已经是入参字段、已经刷完」一件事：

1. **看见 Commit Request / 看见 Commit 不带参数不是已经落盘，也不是已经交差。**  
   官方写：Commit 不带参数。看见不带参数，不是已经必须在 Commit 落盘。看见能叫，不是已经交差。看见能回，不是已经是 `retain_height`。
2. **看见 Echo Response `Message` / 看见 Echo 回包 Message 是入参那串不是已经是入参字段，也不是已经回显。**  
   官方写：回包 `Message` 是入参那串。看见回了 Message，不是已经是 Echo 请求那份要回显的字符串。看见能回，不是已经回显。看见能填，不是已经交差。
3. **看见 Echo Usage / 看见 Echo 用来测实现不是已经刷完，也不是已经送到。**  
   官方写：Echo 用来测 ABCI 客户端/服务端实现。看见能测，不是已经是 Flush 那种把排队冲到服务端。看见能回，不是已经送到。看见能叫，不是已经交差。

怎样写 Commit 空请求、怎样填 Echo 回包、怎样测实现是规范里的做法，本页不抄。Finalize 改了就已经落盘是不变量 335，本页不抄。

## 官方为什么这样拆

- **Commit 不带参数 ≠ 已经落盘：** 官方把不带参数和必须在 Commit 落盘分开。
- **Echo 回包 Message 是入参那串 ≠ 已经是入参字段：** 官方把回包那串和请求要回显的字符串分开。
- **Echo 用来测实现 ≠ 已经刷完：** 官方把测实现和 Flush 冲排队分开。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| Commit 不带参数 | 不是已经落盘 | 不是 Finalize 改了就已经落盘（335） |
| Echo 回包 Message 是入参那串 | 不是已经是入参字段 | 不是 Echo 请求 Message 就已经是 Flush（394） |
| Echo 用来测实现 | 不是已经刷完 | 不是 Flush 要把客户端排队的消息冲到服务端就已经送到（374） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看「看见叫了 Commit 就已经落盘、已经是入参字段、已经刷完」，必须分开 Commit 不带参数是不是已经落盘、Echo 回包 Message 是入参那串是不是已经是入参字段、Echo 用来测实现是不是已经刷完。可以跳过「看见叫了 Commit 就已经落盘」。不要另写怎样写 Commit 空请求。

## 本页不抄

- 怎样写 Commit 空请求、怎样填 Echo 回包、怎样测实现。
- Finalize 改了就已经落盘。那是不变量 335。
- Echo 请求 Message 就已经是 Flush。那是不变量 394。
- Flush 要把客户端排队的消息冲到服务端就已经送到。那是不变量 374。
