# 例：看见 +2/3 precommit 才决定再调 Finalize is not already will call interchangeable / not already ExtendVote when interchangeable / not already decided interchangeable

**层次**：实现 / +2/3 precommit 才决定再调 Finalize not already will call / not already ExtendVote when / not already decided 正式三事（362 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) FinalizeBlock When。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「+2/3 precommit 才决定再调 Finalize not already will call / not already ExtendVote when / not already decided 正式三事（362 余量）/ not 839 finalize-when-notcall interchangeable / not 362 finalize-when-vs-decided bundled interchangeable」，不是 Finalize 何时调用 bundled（362），也不是 +2/3 prevote 才锁住再调 ExtendVote（361），也不是 finwhen-not* 那条别前缀（472），也不是 Finalize 回包义务就已经会调（363/836）。不要另写怎样写 Finalize 何时调用。

## 官方三件事

1. **看见收到提案和全部块片、并且 +2/3 precommit 同一 `id(v)` 才决定再调 Finalize / 看见到了这一高 这份到高 is not already 已经会调 Finalize interchangeable，也不是已经 Finalize 何时调用 bundled（362） interchangeable / 839 finalize-when-notcall interchangeable / 840 finalize-when-notpersist interchangeable / 362 finalize-when item 2 先落决定 interchangeable，也不是已经 +2/3 precommit 才决定再调 Finalize not already will call / not already ExtendVote when / not already decided 正式三事 bundled（362 item 1 余量） interchangeable / 362 finalize-when item 1 interchangeable。**  
   官方写：节点 *p* 处在高度 *h*，收到提议者 *q* 的提案 *v* 和全部块片，并且收到同一 `id(v)` 的 +2/3 precommit，才决定 *v*，再调 `FinalizeBlock`。看见到了这一高，不是已经会调 interchangeable——本页从 362 item 1 侧钉 not already will call 单句。362 finalize-when vs decided bundled unbundling 在本页 item 1 启动。不是 finwhen-not* 那条别前缀（472）。

2. **看见到了这一高 / 看见规范写了 When / 这份到高 is not already 已经是 +2/3 prevote 才锁住再调 ExtendVote interchangeable / 361 extwhen interchangeable，也不是已经 Finalize 何时调用 bundled（362） interchangeable / 839 finalize-when-notcall interchangeable / 362 finalize-when item 3 回 AppHash interchangeable / 841 finalize-when-notheader interchangeable，也不是已经 finwhen-not* 那条别前缀 interchangeable / 472 finwhen interchangeable。**  
   官方把 When 写了和已经是 prevote 那条路分开——362 bundled 第一件事常与 361 混成「看见到了这一高就已经会调 Finalize 或已经是 ExtendVote when interchangeable」，本页钉 not already ExtendVote when 单句。

3. **看见到了这一高 / 看见有提案 / 这份到高 is not already 已经决定 interchangeable，也不是已经 Finalize 何时调用 bundled（362） interchangeable / 839 finalize-when-notcall interchangeable / 840 finalize-when-notpersist interchangeable，也不是已经 Finalize 回包义务就已经会调 interchangeable / 363 finalize-equiv / 836 finalize-equiv-notgates interchangeable。**  
   官方把有提案和已经决定分开。看见有提案，不是已经决定 interchangeable。362 finalize-when vs decided bundled unbundling 在本页 item 1 启动。

怎样写 Finalize 何时调用、怎样落决定、怎样算 ResultHash 是规范里的做法，本页不抄。

## 官方为什么这样拆

- **+2/3 precommit 才决定再调 Finalize not already will call ≠ 已经会调 interchangeable：** 官方把决定再调和已经会调分开。
- **看见规范写了 When not already ExtendVote when ≠ 361 interchangeable：** 官方把 Finalize When 和 ExtendVote When 分开。
- **看见有提案 not already decided ≠ 已经决定 interchangeable：** 官方把有提案和已经决定分开；362 finalize-when vs decided bundled unbundling 在本页 item 1 启动。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| +2/3 precommit 才决定再调 Finalize | 不是已经会调 Finalize | 不是 +2/3 prevote 才锁住再调 ExtendVote（361） |
| 看见规范写了 When | 不是已经是 ExtendVote when | 不是 finwhen-not* 别前缀（472） |
| 看见有提案 | 不是已经决定 | 不是 Finalize 回包义务就已经会调（363/836） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 +2/3 precommit 才决定再调 Finalize not already will call / not already ExtendVote when / not already decided 正式三事（362 余量），必须分开是不是已经会调 Finalize、是不是已经是 ExtendVote when、是不是已经决定。可以跳过「看见到了这一高就已经会调 Finalize」。不要另写怎样写 Finalize 何时调用。362 finalize-when vs decided bundled unbundling 在本页 item 1 启动；续 [`worked-example-finalize-when-notpersist-vs-bundled.md`](worked-example-finalize-when-notpersist-vs-bundled.md)（不变量 840 item 2）。

## 本页不抄

- 怎样写 Finalize 何时调用、怎样落决定、怎样算 ResultHash。
- Finalize 何时调用 bundled。那是不变量 362。
- 先落决定再同步调 Finalize。那是不变量 362 item 2 余量 / 840。
- +2/3 prevote 才锁住再调 ExtendVote。那是不变量 361。
- finwhen-not* 别前缀。那是不变量 472。
- Finalize 回包义务就已经会调。那是不变量 363 / 836。
