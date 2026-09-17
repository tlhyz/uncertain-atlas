# 例：看见 ExtendVote 调用是同步的 is not already can change later interchangeable / not already left critical path interchangeable / not already settled interchangeable

**层次**：实现 / ExtendVote 调用是同步的 not already can change later / not already left critical path / not already settled 正式三事（361 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) ExtendVote When。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「ExtendVote 调用是同步的 not already can change later / not already left critical path / not already settled 正式三事（361 余量）/ not 843 extend-when-notlater interchangeable / not 361 extend-when-vs-locked bundled interchangeable」，不是 ExtendVote 何时调用 bundled（361），也不是 Process 调用是同步的就已经能稍后改裁决（354），也不是先落决定再同步调 Finalize（362/840）。不要另写怎样写 ExtendVote 何时调用。

## 官方三件事

1. **看见 ExtendVote 调用是同步的 / 看见引擎在等回包 这份同步 is not already 已经能在返回之后再改扩展 interchangeable，也不是已经 ExtendVote 何时调用 bundled（361） interchangeable / 843 extend-when-notlater interchangeable / 842 extend-when-notcall interchangeable / 361 extend-when item 1 +2/3 interchangeable，也不是已经 ExtendVote 调用是同步的 not already can change later / not already left critical path / not already settled 正式三事 bundled（361 item 2 余量） interchangeable / 361 extend-when item 2 interchangeable。**  
   官方写：CometBFT 调 `ExtendVote` 是同步的。看见是同步的，不是已经能稍后改扩展 interchangeable——本页从 361 item 2 侧钉 not already can change later 单句。361 extend-when vs locked bundled unbundling 在本页 item 2 续。

2. **看见引擎在等回包 / 看见引擎在等 / 这份同步 is not already 已经离开关键路径 interchangeable，也不是已经 ExtendVote 何时调用 bundled（361） interchangeable / 843 extend-when-notlater interchangeable / 361 extend-when item 3 不解释 interchangeable / 844 extend-when-notsame interchangeable，也不是已经 Process 调用是同步的就已经能稍后改裁决 interchangeable / 354 procsync interchangeable。**  
   官方把引擎在等和已经离开关键路径分开——361 bundled 第二件事常与 354 混成「看见是同步的就已经能稍后改扩展或已经离开关键路径 interchangeable」，本页钉 not already left critical path 单句。

3. **看见引擎在等回包 / 看见回了 / 这份同步 is not already 已经交差 interchangeable，也不是已经 ExtendVote 何时调用 bundled（361） interchangeable / 843 extend-when-notlater interchangeable / 842 extend-when-notcall interchangeable，也不是已经先落决定再同步调 Finalize interchangeable / 362 finalize-when / 840 finalize-when-notpersist interchangeable。**  
   官方把回了和已经交差分开。看见回了，不是已经交差 interchangeable。361 extend-when vs locked bundled unbundling 在本页 item 2 续。

怎样写 ExtendVote 何时调用、怎样锁住、怎样选空是规范里的做法，本页不抄。

## 官方为什么这样拆

- **ExtendVote 调用是同步的 not already can change later ≠ 已经能稍后改扩展 interchangeable：** 官方把同步和稍后改分开。
- **看见引擎在等 not already left critical path ≠ 已经离开关键路径 interchangeable：** 官方把引擎在等和已经离开关键路径分开。
- **看见回了 not already settled ≠ 已经交差 interchangeable：** 官方把回了和已经交差分开；361 extend-when vs locked bundled unbundling 在本页 item 2 续。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| ExtendVote 调用是同步的 | 不是已经能在返回之后再改扩展 | 不是 Process 调用是同步的就已经能稍后改裁决（354） |
| 看见引擎在等 | 不是已经离开关键路径 | 不是先落决定再同步调 Finalize（362/840） |
| 看见回了 | 不是已经交差 | 不是 Finalize 何时调用就已经交差（362/840） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 ExtendVote 调用是同步的 not already can change later / not already left critical path / not already settled 正式三事（361 余量），必须分开是不是已经能稍后改扩展、是不是已经离开关键路径、是不是已经交差。可以跳过「看见是同步的就已经能稍后改扩展」。不要另写怎样写 ExtendVote 何时调用。361 extend-when vs locked bundled unbundling 在本页 item 2 续；续 [`worked-example-extend-when-notsame-vs-bundled.md`](worked-example-extend-when-notsame-vs-bundled.md)（不变量 844 item 3）。

## 本页不抄

- 怎样写 ExtendVote 何时调用、怎样锁住、怎样选空。
- ExtendVote 何时调用 bundled。那是不变量 361。
- +2/3 prevote 才锁住再调 ExtendVote。那是不变量 361 item 1 余量 / 842。
- Process 调用是同步的就已经能稍后改裁决。那是不变量 354。
- 先落决定再同步调 Finalize。那是不变量 362 / 840。
