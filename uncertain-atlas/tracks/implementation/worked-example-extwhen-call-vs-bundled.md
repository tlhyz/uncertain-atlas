# 例：看见 calls ExtendVote with v in ExtendVoteRequest / The call is synchronous / step 2 after lock values before return extension 不是已经 lock values bundled interchangeable / 已经 ExtendVote 何时调用 bundled interchangeable / 已经 ExtendVote When 正式流程 interchangeable

**层次**：实现 / ExtendVote When call / synchronous 正式三事。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) ExtendVote When step 2。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「calls ExtendVote with v / synchronous call / step 2 before return extension 不是 lock values bundled interchangeable / 不是 ExtendVote 何时调用 bundled interchangeable / 不是 ExtendVote When 正式流程 interchangeable」，不是 ExtendVote When lock values（507），也不是 ExtendVote 何时调用（361）。不要另写怎样填 ExtendVoteRequest、怎样等回包、怎样写扩展。

## 官方三件事

规范把 ExtendVote When step 2 里用 _v_ 调 ExtendVote、同步调用、在 step 1 之后 step 3 之前写成三件独立的实现事，不是「看见设了 lock values 就已经会调 ExtendVote interchangeable、已经能在返回之后再改扩展 interchangeable、已经 ExtendVote 回了 extension 就已经广播 Precommit interchangeable」一件事：

1. **看见 _p_'s CometBFT calls `ExtendVote` with _v_ (in `ExtendVoteRequest`) / 看见用 _v_ 调 ExtendVote、_v_ 在 ExtendVoteRequest 里 不是已经 sets lock values bundled（507） interchangeable / 已经 step 1 before call interchangeable，也不是已经 +2/3 prevote 才锁住再调 ExtendVote bundled（361） interchangeable / 已经会调 ExtendVote interchangeable，也不是已经 ExtendVoteRequest 的内容对应即将发 Precommit 的那份拟议块 bundled（409） interchangeable / 已经填了请求 interchangeable。**  
   官方 When step 2 写：_p_'s CometBFT calls `ExtendVote` with _v_ (in `ExtendVoteRequest`)。看见 calls ExtendVote with v，不是已经 sets lockedValue/validValue（507） interchangeable——507 钉 step 1 lock values，本页钉 step 2 call with v 单句。看见 with v in ExtendVoteRequest，不是已经 +2/3 prevote 才锁住再调（361） interchangeable——361 钉 When 侧门槛 bundled，本页钉 step 2 call with v 单句。看见调 ExtendVote，不是已经 ExtendVoteRequest 对应拟议块（409） interchangeable——409 钉 Usage 侧请求对应，本页钉 When step 2 call 单句。
2. **看见 The call is synchronous / 看见 ExtendVote 调用是同步的、引擎会等到应用返回 不是已经能在返回之后再改扩展 interchangeable / 已经离开关键路径 interchangeable，也不是已经 Process 调用是同步的（354） interchangeable / 已经 async 了还能 Reject interchangeable，也不是已经 PrepareProposal call is synchronous（505） interchangeable / 已经能在返回后再改 PrepareProposalResponse interchangeable，也不是已经 ExtendVote When 正式流程 bundled（438） interchangeable / 已经广播 Precommit interchangeable。**  
   官方 When step 2 续：The call is synchronous。看见 blocks until returns，不是已经能在返回之后再改 ExtendVoteResponse interchangeable——361 第二件事钉 When 侧同步 bundled，本页钉 step 2 synchronous 单句。看见 synchronous ExtendVote call，不是已经 Process 调用是同步的（354） interchangeable——354 钉 Process When 同步，本页钉 ExtendVote When step 2 同步单句。看见引擎在等回包，不是已经离开关键路径（327） interchangeable——327 钉 immediate execution 快路径，本页钉 When step 2 synchronous 语义。
3. **看见 step 2 after sets lock values (step 1) and before Application returns extension bytes (step 3) / 看见 step 2 在设 lock values 之后、在应用回 extension 之前 不是已经 ExtendVote When 正式流程 bundled（438） interchangeable / 已经填进 CanonicalVoteExtension interchangeable / 已经广播 Precommit interchangeable，也不是已经回了一串字节共识算法不解释 bundled（361） interchangeable / 已经包进 CanonicalVoteExtension interchangeable，也不是已经 precommit nil 也会 ExtendVote（437） interchangeable / 已经不会叫 ExtendVote interchangeable。**  
   官方 When 把 step 2 夹在 step 1 和 step 3 之间：step 1 sets lock values；step 2 calls ExtendVote synchronously；step 3 Application returns extension bytes。看见 step 2 在中间，不是已经 ExtendVote When 正式流程（438） interchangeable——438 钉 steps 4–7 包装/签名/广播，本页钉 step 2 call 在 return 之前。看见调了 ExtendVote，不是已经回包字节不被解释（361 第三件事） interchangeable——361 钉 return bytes bundled，本页钉 step 2 在 return 之前单句。看见 synchronous call，不是已经 precommit nil 不会叫 ExtendVote（437） interchangeable——437 钉 nil 票路径，本页钉非 nil Precommit 路径 step 2 顺序。

怎样做填 ExtendVoteRequest、怎样等回包、怎样写扩展是规范里的做法，本页不抄。ExtendVote When lock values（507）、ExtendVote 何时调用（361）、ExtendVote When 正式流程（438）、ExtendVote 请求对应（409）是另外那套，本页不抄。

## 官方为什么这样拆

- **calls ExtendVote with v ≠ lock values bundled interchangeable：** 官方把 step 2 call with v 单句和 step 1 lock values bundled 分开。
- **synchronous ExtendVote call ≠ ExtendVote 何时调用 bundled interchangeable：** 官方把 step 2 synchronous 单句和 361 侧门槛+同步+回包 bundled 分开。
- **step 2 before return extension ≠ ExtendVote When 正式流程 bundled interchangeable：** 官方把 step 2 在 return 之前和 steps 4–7 正式流程 bundled 分开。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| calls ExtendVote with v in ExtendVoteRequest | 不是 lock values bundled（507） | 不是 ExtendVoteRequest 对应 bundled（409） |
| synchronous ExtendVote call | 不是能在返回后再改扩展 | 不是 Process 同步（354） |
| step 2 before return extension | 不是 ExtendVote When 正式流程 bundled（438） | 不是回包字节不被解释 bundled（361） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 ExtendVote When call / synchronous 正式三事，必须分开 calls ExtendVote with v 是不是 lock values bundled interchangeable、The call is synchronous 是不是 ExtendVote 何时调用 bundled interchangeable / 已经能在返回后再改扩展 interchangeable、step 2 before return extension 是不是 ExtendVote When 正式流程 bundled interchangeable / 已经广播 Precommit interchangeable。可以跳过「看见设了 lock values 就已经会调 ExtendVote interchangeable、已经能在返回之后再改扩展 interchangeable、已经 ExtendVote 回了 extension 就已经广播 Precommit interchangeable」。不要另写怎样填 ExtendVoteRequest、怎样等回包。

## 本页不抄

- 怎样做填 ExtendVoteRequest、怎样等回包、怎样写扩展。
- ExtendVote When lock values / step 1 before call。那是不变量 507。
- ExtendVote 何时调用 / +2/3 prevote 才锁住再调 / 回包字节不被解释。那是不变量 361。
- ExtendVote When 正式流程 / 填 CanonicalVoteExtension 并广播。那是不变量 438。
- ExtendVoteRequest 的内容对应即将发 Precommit 的拟议块。那是不变量 409。
