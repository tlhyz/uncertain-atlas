# 例：看见 sets lockedValue and validValue to v / sets lockedRound and validRound to r / before calling ExtendVote with v 不是已经 +2/3 prevote 锁住 bundled interchangeable / 已经 validValue 跳过 Prepare interchangeable / 已经 ExtendVote When 正式流程 interchangeable

**层次**：实现 / ExtendVote When lock values 正式三事。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) ExtendVote When step 1。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)、[L4.3 锁](../../courses/level-04-bft/L04-M03-locks.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「sets lockedValue/validValue / sets lockedRound/validRound / before ExtendVote call 不是 +2/3 prevote 锁住 bundled interchangeable / 不是 validValue 跳过 Prepare interchangeable / 不是 ExtendVote When 正式流程 interchangeable」，不是 ExtendVote 何时调用（361），也不是 ExtendVote When 正式流程（438）。不要另写怎样写锁、怎样调 ExtendVote、怎样广播 Precommit。

## 官方三件事

规范把 ExtendVote When step 1 里设 lockedValue/validValue、设 lockedRound/validRound、在调 ExtendVote 之前写成三件独立的实现事，不是「看见 +2/3 prevote 就已经 lockedValue/validValue interchangeable、已经 validValue 跳过 Prepare interchangeable、已经 ExtendVote 回了 extension 就已经广播 Precommit interchangeable」一件事：

1. **看见 _p_ sets _lockedValue_ and _validValue_ to _v_ / 看见把 lockedValue 和 validValue 都设成 _v_ 不是已经 +2/3 prevote 同一 `id(v)` 才锁住再调 ExtendVote bundled（361） interchangeable / 已经会调 ExtendVote interchangeable，也不是已经 validValue 非 nil 跳过 Prepare（356） interchangeable / 已经直接用它当提案 interchangeable，也不是已经 ExtendVote When 正式流程 bundled（438） interchangeable / 已经广播 Precommit interchangeable。**  
   官方 When step 1 写：_p_ sets _lockedValue_ and _validValue_ to _v_。看见 sets lockedValue and validValue to v，不是已经 +2/3 prevote 才锁住 *v* 再调 ExtendVote（361） interchangeable——361 钉 When 侧收齐 prevote 才锁住再调，本页钉 step 1 侧 lockedValue/validValue 赋值单句。看见两个值都设成 *v*，不是已经 validValue 非 nil 直接当提案（356） interchangeable——356 钉提议者 Prepare 侧 validValue 跳过，本页钉验证者 Precommit 前 lock values 单句。看见 lockedValue 和 validValue 一起设，不是已经填进 CanonicalVoteExtension 并签名（438） interchangeable——438 钉 When 正式流程 steps 4–7，本页钉 step 1 lock values 单句。
2. **看见 sets _lockedRound_ and _validRound_ to _r_ / 看见把 lockedRound 和 validRound 都设成 _r_ 不是已经 +2/3 prevote 锁住 bundled（361） interchangeable / 已经 locked interchangeable，也不是已经 validValue 非 nil 跳过 Prepare（356） interchangeable / 已经又从池子收了一遍 interchangeable，也不是已经到了 prevote 步就已经 locked interchangeable / 已经 validRound 来自更早一轮 interchangeable。**  
   官方 When step 1 续：and sets _lockedRound_ and _validRound_ to _r_。看见 sets lockedRound and validRound to r，不是已经 +2/3 prevote 才锁住（361） interchangeable——361 钉锁住 *v* 门槛，本页钉 lockedRound/validRound 赋值单句。看见 round 都设成 *r*，不是已经 validValue 跳过 Prepare 那种提议者侧 validValue（356） interchangeable——356 钉 Prepare When validValue，本页钉 ExtendVote When step 1 validRound。看见 lockedRound 和 validRound 一起设，不是已经到了 prevote 步就已经 locked interchangeable——361 第一件事钉门槛，本页钉 step 1 round 赋值单句。
3. **看见 sets lock values as step 1 before _p_'s CometBFT calls `ExtendVote` with _v_ (step 2) / 看见先设 lock values、再调 ExtendVote 不是已经会调 ExtendVote bundled（361） interchangeable / 已经 ExtendVote 调用是同步的 interchangeable，也不是已经 ExtendVote When 正式流程 bundled（438） interchangeable / 已经填进 CanonicalVoteExtension interchangeable / 已经广播 Precommit interchangeable，也不是已经 precommit nil 也会 ExtendVote（437） interchangeable / 已经不会叫 ExtendVote interchangeable。**  
   官方 When 把 step 1 和 step 2 分开：step 1 sets lock values；step 2 _p_'s CometBFT calls `ExtendVote` with _v_。看见 step 1 before step 2，不是已经 +2/3 prevote 才锁住再调 ExtendVote bundled（361） interchangeable——361 钉门槛+同步+回包三事 bundled，本页钉 step 1 在 ExtendVote call 之前单句。看见先设 lock values，不是已经 ExtendVote When 正式流程（438） interchangeable——438 钉 extension 回包后的包装/签名/广播，本页钉 step 1 在 call 之前。看见再调 ExtendVote，不是已经 precommit nil 不会叫 ExtendVote（437） interchangeable——437 钉 Usage/When nil 票不调，本页钉非 nil Precommit 路径 step 1 顺序。

怎样做写锁、怎样调 ExtendVote、怎样构造 Precommit 是规范里的做法，本页不抄。ExtendVote 何时调用（361）、ExtendVote When 正式流程（438）、precommit nil 不会叫 ExtendVote（437）、validValue 跳过 Prepare（356）是另外那套，本页不抄。

## 官方为什么这样拆

- **sets lockedValue/validValue to v ≠ +2/3 prevote 锁住 bundled interchangeable：** 官方把 step 1 lockedValue/validValue 赋值单句和 361 侧门槛 bundled 分开。
- **sets lockedRound/validRound to r ≠ validValue 跳过 Prepare interchangeable：** 官方把 ExtendVote When step 1 round 赋值和 Prepare When validValue 跳过分开。
- **before ExtendVote call ≠ ExtendVote When 正式流程 bundled interchangeable：** 官方把 step 1 在 call 之前和 steps 4–7 正式流程 bundled 分开。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| sets lockedValue and validValue to v | 不是 +2/3 prevote 锁住 bundled（361） | 不是 validValue 跳过 Prepare（356） |
| sets lockedRound and validRound to r | 不是到了 prevote 步就已经 locked | 不是 validValue 跳过 Prepare round（356） |
| step 1 before ExtendVote call | 不是 ExtendVote When 正式流程 bundled（438） | 不是 precommit nil 也会 ExtendVote（437） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 ExtendVote When lock values 正式三事，必须分开 sets lockedValue/validValue 是不是 +2/3 prevote 锁住 bundled interchangeable、sets lockedRound/validRound 是不是 validValue 跳过 Prepare interchangeable、step 1 before ExtendVote call 是不是 ExtendVote When 正式流程 bundled interchangeable / 已经广播 Precommit interchangeable。可以跳过「看见 +2/3 prevote 就已经 lockedValue/validValue interchangeable、已经 validValue 跳过 Prepare interchangeable、已经 ExtendVote 回了 extension 就已经广播 Precommit interchangeable」。不要另写怎样写锁、怎样调 ExtendVote。

## 本页不抄

- 怎样做写锁、怎样调 ExtendVote、怎样构造 Precommit。
- ExtendVote 何时调用 / +2/3 prevote 才锁住再调。那是不变量 361。
- ExtendVote When 正式流程 / 填 CanonicalVoteExtension 并广播。那是不变量 438。
- precommit nil 不会叫 ExtendVote。那是不变量 437。
- validValue 跳过 Prepare。那是不变量 356。
