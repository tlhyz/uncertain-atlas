# 例：看见 +2/3 prevote 才锁住再调 ExtendVote is not already will call interchangeable / not already one-per-round interchangeable / not already locked interchangeable

**层次**：实现 / +2/3 prevote 才锁住再调 ExtendVote not already will call / not already one-per-round / not already locked 正式三事（361 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) ExtendVote When。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「+2/3 prevote 才锁住再调 ExtendVote not already will call / not already one-per-round / not already locked 正式三事（361 余量）/ not 842 extend-when-notcall interchangeable / not 361 extend-when-vs-locked bundled interchangeable」，不是 ExtendVote 何时调用 bundled（361），也不是一轮只能交出一份扩展（350），也不是 extwhen-not* 那条别前缀（507–512），也不是 +2/3 precommit 才决定再调 Finalize（362/839）。不要另写怎样写 ExtendVote 何时调用。

## 官方三件事

1. **看见收到提案和全部块片、并且 +2/3 prevote 同一 `id(v)` 才锁住再调 ExtendVote / 看见到了 prevote 步 这份到步 is not already 已经会调 ExtendVote interchangeable，也不是已经 ExtendVote 何时调用 bundled（361） interchangeable / 842 extend-when-notcall interchangeable / 843 extend-when-notlater interchangeable / 361 extend-when item 2 同步 interchangeable，也不是已经 +2/3 prevote 才锁住再调 ExtendVote not already will call / not already one-per-round / not already locked 正式三事 bundled（361 item 1 余量） interchangeable / 361 extend-when item 1 interchangeable。**  
   官方写：验证者 *p* 处在一轮 *r*、高度 *h* 的 prevote 步，收到提议者 *q* 的提案 *v* 和全部块片，并且收到同一 `id(v)` 的 +2/3 prevote，才锁住 *v*，再调 `ExtendVote`。看见到了 prevote 步，不是已经会调 interchangeable——本页从 361 item 1 侧钉 not already will call 单句。361 extend-when vs locked bundled unbundling 在本页 item 1 启动。不是 extwhen-* 那条别前缀（507–512）。

2. **看见到了 prevote 步 / 看见规范写了 When / 这份到步 is not already 已经是一轮只能交出一份扩展 interchangeable / 350 oneext interchangeable，也不是已经 ExtendVote 何时调用 bundled（361） interchangeable / 842 extend-when-notcall interchangeable / 361 extend-when item 3 不解释 interchangeable / 844 extend-when-notsame interchangeable，也不是已经 extwhen-* 那条别前缀 interchangeable / 507–512 extwhen interchangeable。**  
   官方把 When 写了和已经是一轮一份扩展分开——361 bundled 第一件事常与 350 / 362 混成「看见到了 prevote 步就已经会调 ExtendVote 或已经是一轮一份 interchangeable」，本页钉 not already one-per-round 单句。

3. **看见到了 prevote 步 / 看见有提案 / 这份到步 is not already 已经锁住 interchangeable，也不是已经 ExtendVote 何时调用 bundled（361） interchangeable / 842 extend-when-notcall interchangeable / 843 extend-when-notlater interchangeable，也不是已经 +2/3 precommit 才决定再调 Finalize interchangeable / 362 finalize-when / 839 finalize-when-notcall interchangeable。**  
   官方把有提案和已经锁住分开。看见有提案，不是已经锁住 interchangeable。361 extend-when vs locked bundled unbundling 在本页 item 1 启动。

怎样写 ExtendVote 何时调用、怎样锁住、怎样选空是规范里的做法，本页不抄。

## 官方为什么这样拆

- **+2/3 prevote 才锁住再调 ExtendVote not already will call ≠ 已经会调 interchangeable：** 官方把锁住再调和已经会调分开。
- **看见规范写了 When not already one-per-round ≠ 350 interchangeable：** 官方把 When 写了和已经是一轮一份扩展分开。
- **看见有提案 not already locked ≠ 已经锁住 interchangeable：** 官方把有提案和已经锁住分开；361 extend-when vs locked bundled unbundling 在本页 item 1 启动。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| +2/3 prevote 才锁住再调 ExtendVote | 不是已经会调 ExtendVote | 不是一轮只能交出一份扩展（350） |
| 看见规范写了 When | 不是已经是一轮一份扩展 | 不是 extwhen-* 别前缀（507–512） |
| 看见有提案 | 不是已经锁住 | 不是 +2/3 precommit 才决定再调 Finalize（362/839） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 +2/3 prevote 才锁住再调 ExtendVote not already will call / not already one-per-round / not already locked 正式三事（361 余量），必须分开是不是已经会调 ExtendVote、是不是已经是一轮一份扩展、是不是已经锁住。可以跳过「看见到了 prevote 步就已经会调 ExtendVote」。不要另写怎样写 ExtendVote 何时调用。361 extend-when vs locked bundled unbundling 在本页 item 1 启动；续 [`worked-example-extend-when-notlater-vs-bundled.md`](worked-example-extend-when-notlater-vs-bundled.md)（不变量 843 item 2）。

## 本页不抄

- 怎样写 ExtendVote 何时调用、怎样锁住、怎样选空。
- ExtendVote 何时调用 bundled。那是不变量 361。
- ExtendVote 调用是同步的。那是不变量 361 item 2 余量 / 843。
- 一轮只能交出一份扩展。那是不变量 350。
- extwhen-* 别前缀。那是不变量 507–512。
- +2/3 precommit 才决定再调 Finalize。那是不变量 362 / 839。
