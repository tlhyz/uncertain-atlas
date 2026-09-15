# 例：看见 VerifyVoteExtension is not called for precommit votes sent by the local process / not called for local process is not already self-verified / not called for local process is not Verify When received from q≠p 不是已经 Verify Usage bundled interchangeable / 已经本地票也 Verify interchangeable / 已经 Accept interchangeable

**层次**：实现 / VerifyVoteExtension Usage not called for local process 正式三事。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) VerifyVoteExtension Usage 本地票句。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「not called for local process / not already self-verified / not received from q≠p When call 不是 Verify Usage bundled interchangeable / 不是已经本地票也 Verify interchangeable / 不是已经 Accept interchangeable」，不是 Verify Usage bundled（353），也不是 Verify When step 2 call received from q≠p（515），也不是 ExtendVote When 正式流程（438）。不要另写怎样写 Verify 何时调用、怎样写空扩展、怎样缓存 Process。

## 官方三件事

规范把 VerifyVoteExtension Usage 里不对本地 Precommit 调用写成三件独立的实现事，不是「看见是本地票就已经自己验过 interchangeable、已经 Accept interchangeable、已经本地票也 Verify interchangeable」一件事：

1. **看见 `VerifyVoteExtension` is not called for precommit votes sent by the local process / 看见不对本进程自己发出的 Precommit 调用 不是已经 Verify Usage bundled（353） interchangeable / 已经本地票也 Verify interchangeable / 已经自己验过 interchangeable，也不是已经 Verify When 正式流程 step 2 call bundled（515） interchangeable / 已经 received from q≠p interchangeable / 已经 CometBFT 会叫 interchangeable，也不是已经 ExtendVote When 正式流程 bundled（438） interchangeable / 已经广播 Precommit interchangeable / 已经 construct CanonicalVote interchangeable，也不是已经 empty extension still calls Verify bundled（521） interchangeable / 已经 0 长仍会 call interchangeable，也不是已经 Verify 不是 called for precommit votes sent by local process bundled（353 第二件事） interchangeable / 已经本地票也 Verify bundled interchangeable。**  
   官方 VerifyVoteExtension Usage 写：VerifyVoteExtension is not called for precommit votes sent by the local process。看见 not called for local process，不是已经 Verify Usage bundled（353） interchangeable——353 钉 bundled 三事，本页钉不对本地票 call 单句。看见不调本地票，不是已经 Verify When step 2 call（515） interchangeable——515 钉收到他人 Precommit from q≠p 后 call，本页钉 Usage 侧本地票不调。看见 is not called，不是已经 ExtendVote When 正式流程（438） interchangeable——438 钉本地 ExtendVote 路径，本页钉 Verify Usage 侧本地票不调。
2. **看见 not called for local process is not already self-verified / 看见不调本地票不是已经自己验过 不是已经 Verify Usage bundled（353） interchangeable / 已经自己验过 interchangeable / 已经 Accept interchangeable，也不是已经正确进程交出的扩展必须被正确接收者 Verify Accept（348） interchangeable / 已经 Req 6 已经测过 interchangeable，也不是已经 Verify When step 3 return status bundled（516） interchangeable / 已经 Application returns ACCEPT interchangeable，也不是已经 ExtendVote When return extension bundled（509） interchangeable / 已经签过 extension interchangeable，也不是已经 empty extension still calls Verify bundled（521） interchangeable / 已经仍会 call interchangeable。**  
   官方 VerifyVoteExtension Usage 把不调本地票和已经自己验过分开——353 bundled 常被写成「是自己签的就已经自己验过」，本页钉 not self-verified 单句。看见不调，不是已经 Accept（348 / 516） interchangeable——348 钉 Req 6 必须 Accept 是接收侧，本页钉本地票不调不等于已经 Accept。看见 not called，不是已经 ExtendVote 回了 extension（509） interchangeable——509 钉本地 ExtendVote return，本页钉 Verify 不调本地票。
3. **看见 not called for local process is not Verify When received from q≠p / 看见不调本地票不是 When 侧收到他人票后 call 不是已经 Verify Usage bundled（353） interchangeable / 已经本地票也 Verify interchangeable，也不是已经 Verify When 正式流程 step 2 call bundled（515） interchangeable / 已经 received from q≠p interchangeable / 已经带有效签就会调 Verify interchangeable，也不是已经 Verify When step 1 discard bundled（514） interchangeable / 已经收到他人 Precommit interchangeable，也不是已经 request hash 不保证 Process bundled（353 第三件事 / 523 余量） interchangeable / 已经对该块跑过 Process interchangeable，也不是已经 empty extension still calls Verify bundled（521） interchangeable / 已经 0 长仍会 call interchangeable。**  
   官方 VerifyVoteExtension Usage 把本地票不调与 When 侧收到他人票后 call 分开——515 钉 When step 2 received from q≠p，本页钉 Usage 侧 local process not called 单句。看见不调本地票，不是已经 received from q≠p（515） interchangeable——515 前提 _q_ ≠ _p_，本页钉 local process 不调。看见 not called，不是已经 Verify Usage bundled（353） interchangeable——353 钉 bundled 三事，本页钉 local process not called 单句。

怎样做写 Verify 何时调用、怎样写空扩展、怎样缓存 Process 是规范里的做法，本页不抄。Verify Usage bundled（353）、Verify When step 2 call（515）、ExtendVote When 正式流程（438）是另外那套，本页不抄。

## 官方为什么这样拆

- **not called for local process ≠ 已经本地票也 Verify interchangeable：** 官方把 Usage 侧本地票不调与 When 侧收到侧 call 分开。
- **not called for local process ≠ 已经自己验过 interchangeable：** 官方把不调本地票和已经 Accept / 自己验过分开。
- **not called for local process ≠ received from q≠p When call interchangeable：** 官方把 Usage 侧 local process 与 When step 2 收到他人票分开。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| not called for local process | 不是 local process also Verify | 不是 When received from q≠p（515） |
| not already self-verified | 不是 already Accept | 不是 Req 6 must Accept（348） |
| not Verify When received from q≠p | 不是 Verify Usage bundled（353） | 不是 ExtendVote local path（438） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 VerifyVoteExtension Usage not called for local process 正式三事，必须分开 not called for local process 是不是已经本地票也 Verify interchangeable / 已经 received from q≠p interchangeable、not already self-verified 是不是已经 Accept interchangeable / 已经 Req 6 已经测过 interchangeable、not Verify When received from q≠p 是不是 Verify Usage bundled interchangeable / 已经带有效签就会调 Verify interchangeable。可以跳过「看见是本地票就已经自己验过 interchangeable、已经 Accept interchangeable」。不要另写怎样写 Verify 何时调用。

## 本页不抄

- 怎样做写 Verify 何时调用、怎样写空扩展、怎样缓存 Process。
- Verify Usage bundled / empty extension still calls Verify / hash 不保证 Process。那是不变量 353 / 521 / 523。
- Verify When step 2 call received from q≠p。那是不变量 515。
- ExtendVote When 正式流程 / return extension。那是不变量 438 / 509。
