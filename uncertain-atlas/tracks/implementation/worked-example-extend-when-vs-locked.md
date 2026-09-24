# 例：看见收到提案和全部块片并且 +2/3 prevote 同一 id(v) 才锁住再调 ExtendVote 不是已经会调 ExtendVote；看见 ExtendVote 调用是同步的不是已经能在返回之后再改扩展；看见应用回了一串字节共识算法不解释不是已经是同一份扩展

**层次**：实现 / ExtendVote 何时调用。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) ExtendVote When。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5。本页是「收到提案和全部块片并且 +2/3 prevote 同一 id(v) 才锁住再调 ExtendVote 不是已经会调 ExtendVote / ExtendVote 调用是同步的不是已经能在返回之后再改扩展 / 应用回了一串字节共识算法不解释不是已经是同一份扩展」，不是一轮只能交出一份扩展，也不是 Process 调用是同步的。不要另写怎样写 ExtendVote 何时调用。361 extend-when vs locked bundled unbundling 启动（833）；精读 [`worked-example-extwhen-notwillcall-vs-bundled.md`](worked-example-extwhen-notwillcall-vs-bundled.md)（不变量 833 item 1）。

## 官方三件事

规范把 +2/3 prevote 同一 `id(v)` 并且收齐块片才锁住再调 ExtendVote、这次调用是同步的、回包字节不被共识算法解释写成三件独立的实现事，不是「看见到了 prevote 步就已经会调 ExtendVote、已经能稍后改扩展、已经是同一份扩展」一件事：

1. **看见收到提案和全部块片、并且 +2/3 prevote 同一 `id(v)` 才锁住再调 ExtendVote / 看见到了 prevote 步 不是已经会调 ExtendVote，也不是已经是一轮只能交出一份扩展。**  
   官方写：验证者 *p* 处在一轮 *r*、高度 *h* 的 prevote 步，收到提议者 *q* 的提案 *v* 和全部块片，并且收到同一 `id(v)` 的 +2/3 prevote，才锁住 *v*，再调 `ExtendVote`。看见到了 prevote 步，不是已经会调。看见有提案，不是已经锁住。看见规范写了 When，不是已经是一轮一份扩展。
2. **看见 ExtendVote 调用是同步的 / 看见引擎在等回包 不是已经能在返回之后再改扩展，也不是已经离开关键路径。**  
   官方写：CometBFT 调 `ExtendVote` 是同步的。看见是同步的，不是已经能稍后改扩展。看见引擎在等，不是已经离开关键路径。看见回了，不是已经交差。
3. **看见应用回了一串字节、共识算法不解释 / 看见回了 extension 不是已经是同一份扩展，也不是已经包进 CanonicalVoteExtension。**  
   官方写：应用回一份字节数组 `ExtendVoteResponse.extension`，共识算法不解释。看见回了，不是已经同一份扩展。看见不解释，不是已经包进 `CanonicalVoteExtension`。看见有字节，不是已经交差。

怎样写 ExtendVote 何时调用、怎样锁住、怎样选空是规范里的做法，本页不抄。一轮只能交出一份扩展是不变量 350，本页不抄。

## 官方为什么这样拆

- **+2/3 prevote 同一 id(v) 才锁住再调 ExtendVote ≠ 已经会调 ExtendVote：** 官方把锁住再调和已经会调分开。
- **ExtendVote 调用是同步的 ≠ 已经能在返回之后再改扩展：** 官方把同步和稍后改分开。
- **回包字节不被共识算法解释 ≠ 已经是同一份扩展：** 官方把不解释和已经同一份分开。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| +2/3 prevote 同一 id(v) 才锁住再调 ExtendVote | 不是已经会调 ExtendVote | 不是一轮只能交出一份扩展就已经是每一高度一份（350） |
| ExtendVote 调用是同步的 | 不是已经能在返回之后再改扩展 | 不是 Process 调用是同步的就已经能稍后改裁决（354） |
| 回包字节不被共识算法解释 | 不是已经是同一份扩展 | 不是 vote_extension 会包进 CanonicalVoteExtension 就已经按原样签（358） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看「看见到了 prevote 步就已经会调 ExtendVote、已经能稍后改扩展、已经是同一份扩展」，必须分开 +2/3 prevote 同一 id(v) 才锁住再调 ExtendVote 是不是已经会调 ExtendVote、ExtendVote 调用是同步的是不是已经能在返回之后再改扩展、回包字节不被共识算法解释是不是已经是同一份扩展。可以跳过「看见到了 prevote 步就已经会调 ExtendVote」。不要另写怎样写 ExtendVote 何时调用。361 extend-when vs locked bundled unbundling 启动（833）。

## 本页不抄

- 怎样写 ExtendVote 何时调用、怎样锁住、怎样选空。
- 一轮只能交出一份扩展就已经是每一高度一份。那是不变量 350。
- Process 调用是同步的就已经能稍后改裁决。那是不变量 354。
- vote_extension 会包进 CanonicalVoteExtension 就已经按原样签。那是不变量 358。
