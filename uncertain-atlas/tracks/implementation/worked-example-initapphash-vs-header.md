# 例：看见 InitChain 回包 app_hash 是起步应用哈希不是已经是本头 AppHash；看见 Finalize 请求 hash 是这块的哈希不是已经知道本头哈希；看见 CommitInfo.round 是提交轮不是已经按投票权排过

**层次**：实现 / InitChain 回包余栏。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) InitChain Response / FinalizeBlock Request / CommitInfo。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5。本页是「InitChain 回包 app_hash 是起步应用哈希不是已经是本头 AppHash / Finalize 请求 hash 是这块的哈希不是已经知道本头哈希 / CommitInfo.round 是提交轮不是已经按投票权排过」，不是本头 AppHash 就已经是本高度交差，也不是 Prepare 没有头哈希就已经知道本头。不要另写怎样写 InitChain 回包余栏。

## 官方三件事

规范把 InitChain 回包 `app_hash` 是起步应用哈希、Finalize 请求 `hash` 是这块的哈希、CommitInfo `round` 是提交轮写成三件独立的实现事，不是「看见填了 InitChain 回包余栏就已经是本头 AppHash、已经知道本头哈希、已经按投票权排过」一件事：

1. **看见 InitChain 回包 `app_hash` 是起步应用哈希 / 看见回了起步哈希 不是已经是本头 AppHash，也不是已经没有集合。**  
   官方写：`app_hash` 是起步应用哈希。看见回了起步哈希，不是已经是本头那份 AppHash。看见有起步根，不是已经交差。看见能回，不是已经没有集合。
2. **看见 Finalize 请求 `hash` 是这块的哈希 / 看见填了 hash 不是已经知道本头哈希，也不是已经跑过 Process。**  
   官方写：`hash` 是这块的哈希。看见填了 hash，不是已经是 Prepare 那种还没有头哈希就已经知道本头。看见有块哈希，不是已经是 height / time 对上拟议头那种已经知道本头哈希。看见能填，不是已经交差。
3. **看见 CommitInfo `round` 是提交轮 / 看见填了 round 不是已经按投票权排过，也不是已经罚没。**  
   官方写：`round` 是提交轮，反映上一高度块提议者决定时的那一轮。看见填了 round，不是已经按投票权降序排过。看见有轮次，不是已经按到场定奖惩。看见能填，不是已经交差。

怎样写 InitChain 回包余栏、怎样填起步哈希、怎样填提交轮是规范里的做法，本页不抄。本头 AppHash 就已经是本高度交差是不变量 147，本页不抄。

## 官方为什么这样拆

- **InitChain 回包 app_hash 是起步应用哈希 ≠ 已经是本头 AppHash：** 官方把起步应用哈希和本头 AppHash 分开。
- **Finalize 请求 hash 是这块的哈希 ≠ 已经知道本头哈希：** 官方把这块的哈希和已经知道本头哈希分开。
- **CommitInfo.round 是提交轮 ≠ 已经按投票权排过：** 官方把提交轮和票序分开。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| InitChain 回包 app_hash 是起步应用哈希 | 不是已经是本头 AppHash | 不是本头 AppHash 就已经是本高度交差（147） |
| Finalize 请求 hash 是这块的哈希 | 不是已经知道本头哈希 | 不是 Prepare 没有头哈希就已经知道本头（311） |
| CommitInfo.round 是提交轮 | 不是已经按投票权排过 | 不是 VoteInfo 按投票权降序排就已经进了块（365） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看「看见填了 InitChain 回包余栏就已经是本头 AppHash、已经知道本头哈希、已经按投票权排过」，必须分开 InitChain 回包 app_hash 是起步应用哈希是不是已经是本头 AppHash、Finalize 请求 hash 是这块的哈希是不是已经知道本头哈希、CommitInfo.round 是提交轮是不是已经按投票权排过。可以跳过「看见填了 InitChain 回包余栏就已经是本头 AppHash」。不要另写怎样写 InitChain 回包余栏。392 initapphash vs header bundled unbundling 完成（755 item 1 / 756 item 2 / 757 item 3）；精读 [`worked-example-initapphash-notheader-vs-bundled.md`](worked-example-initapphash-notheader-vs-bundled.md)（不变量 755 item 1）。

## 本页不抄

- 怎样写 InitChain 回包余栏、怎样填起步哈希、怎样填提交轮。
- 本头 AppHash 就已经是本高度交差。那是不变量 147。
- Prepare 没有头哈希就已经知道本头。那是不变量 311。
- VoteInfo 按投票权降序排就已经进了块。那是不变量 365。
