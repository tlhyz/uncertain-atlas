# 例：看见 Proposal message with block _v_ + all block parts from proposer _q_ 不是已经只有 hash / 已经 Process 跑过；看见 Precommit from 2f+1 voting power same id(_v_) 不是已经 +2/3 prevote ExtendVote；看见 then decides block _v_ 不是已经到了这一高就会调 Finalize

**层次**：实现 / FinalizeBlock When trigger Proposal block parts 2f+1 precommit 正式三事。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) FinalizeBlock When preamble。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「Proposal + all block parts 不是已经只有 hash / 已经 Process 跑过、2f+1 precommit same id(v) 不是已经 +2/3 prevote ExtendVote、decides block v 不是已经到了这一高就会调 Finalize」，不是 Finalize 何时调用 bundled 三事里 AppHash/ResultHash 那套，不是 persist decision / synchronous call 三事，也不是 +2/3 prevote 才锁住再调 ExtendVote 三事。不要另写怎样收块片、怎样数 2f+1。

## 官方三件事

规范把 FinalizeBlock When 触发条件写成三件独立的实现事，不是「看见到了这一高、有提案、有 +2/3 precommit 就已经会调 Finalize interchangeable」一件事：

1. **看见 the Proposal message with block _v_ for a round _r_, along with all its block parts, from _q_ / 看见提议者 _q_ 的提案 _v_ 和全部块片 不是已经只有 `FinalizeBlockRequest.hash` / 已经 Process 跑过，也不是已经收到部分块片就可以决定。**  
   官方 When 写：_p_ receives the Proposal message with block _v_ for a round _r_, along with all its block parts, from _q_, which is the proposer of round _r_, height _h_。看见 all its block parts，不是已经只有 hash 栏对上。看见 from proposer _q_，不是已经任意节点流言 partial block interchangeable。看见 Proposal + parts，不是已经 ProcessProposal 跑过就代表已经收齐 interchangeable——Process guarantee（472）另钉 at least one non-byzantine has run Process。
2. **看见 Precommit messages from 2f + 1 validators' voting power for round _r_, height _h_, precommitting the same block id(_v_) / 看见 2f+1 投票权对同一 id(_v_) precommit 不是已经 +2/3 prevote 同一 id(_v_) 才 ExtendVote（361），也不是已经 +2/3 precommit 就可以没有 all block parts interchangeable。**  
   官方 When 写：Precommit messages from 2f + 1 validators' voting power … precommitting the same block id(_v_)。看见 2f+1 投票权，不是已经 +2/3 prevote 锁住 ExtendVote（361）那种已经 interchangeable。看见 precommitting the same block id(_v_)，不是已经 +2/3 precommit 对 nil 或不同 BlockID interchangeable。看见 Precommit 门槛，不是已经 When calling FinalizeBlock Process guarantee（472）就已经是同一句 interchangeable。
3. **看见 then _p_ decides block _v_ and finalizes consensus for height _h_ / 看见然后决定 _v_ 不是已经处在高度 _h_ 就会调 Finalize，也不是已经 decides 就已经 persist outputs / 已经交差。**  
   官方写：then _p_ decides block _v_ and finalizes consensus for height _h_ in the following way。看见 decides block _v_，不是已经 +2/3 precommit 决定触发（362 bundled 第一句）就已经是同一句 interchangeable——362 bundled 另钉 AppHash/ResultHash 第三件事，本页只钉 When preamble 触发三事。看见 finalizes consensus for height _h_，不是已经 persist decision（478 第 1 步）就已经是同一句 interchangeable。看见 then，不是已经到了这一高就会调 Finalize。

怎样收块片、怎样数 2f+1、怎样落决定是规范里的做法，本页不抄。Finalize 何时调用 bundled（362）是 +2/3 precommit 决定再调 Finalize / 先落决定 / AppHash ResultHash 那套另一切片，persist decision / synchronous call（478）是 When 第 1–2 步那套另一切片，+2/3 prevote ExtendVote（361）是 prevote 锁住再 Extend 那套另一切片，Process guarantee（472）是 at least one non-byzantine Process 那套另一切片，本页不抄。

## 官方为什么这样拆

- **Proposal + all block parts ≠ 已经只有 hash / 已经 Process 跑过：** 官方把收齐 Proposal 和全部块片与只有 hash、Process 跑过分开。
- **2f+1 precommit same id(v) ≠ 已经 +2/3 prevote ExtendVote：** 官方把 Precommit 门槛和 Prevote/ExtendVote 锁住分开。
- **decides block v ≠ 已经到了这一高就会调 Finalize / 已经交差：** 官方把决定 _v_ 和 persist outputs / 已经交差分开。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| Proposal + all block parts | 不是已经只有 hash | 不是 Finalize 请求 hash 栏（428） |
| 2f+1 precommit same id(v) | 不是已经 +2/3 prevote ExtendVote | 不是 +2/3 prevote ExtendVote（361） |
| decides block v | 不是已经到了这一高就会调 Finalize | 不是 persist decision（478） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看「看见到了这一高、有 +2/3 precommit 就已经会调 Finalize」，必须分开 Proposal + all block parts 是不是已经只有 hash、2f+1 precommit same id(v) 是不是已经 +2/3 prevote ExtendVote、decides block v 是不是已经 persist outputs / 已经交差。可以跳过「看见有 +2/3 precommit 就已经会调 Finalize」。不要另写怎样收块片。

## 本页不抄

- 怎样收块片、怎样数 2f+1、怎样落决定。
- Finalize 何时调用 bundled 三事。那是不变量 362。
- persist decision / synchronous call 三事。那是不变量 478。
- +2/3 prevote ExtendVote 三事。那是不变量 361。
- Process guarantee 三事。那是不变量 472。
