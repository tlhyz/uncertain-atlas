# 例：看见 application can choose 0-length vote extension / still calls ExtendVote on non-nil Precommit / choosing empty is not skip Verify 不是已经 ExtendVote Usage bundled interchangeable / 已经不会叫 ExtendVote interchangeable / 已经跳过 Verify interchangeable

**层次**：实现 / ExtendVote Usage application can choose 0-length extension 正式三事。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) ExtendVote Usage 0-length 句。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「can choose 0-length / still calls ExtendVote on non-nil / choosing empty not skip Verify 不是 ExtendVote Usage bundled interchangeable / 不是已经不会叫 ExtendVote interchangeable / 不是已经跳过 Verify interchangeable」，不是 ExtendVote Usage bundled（437），也不是 precommit nil will not call ExtendVote（524），也不是 empty extension still calls Verify（521）。不要另写怎样写 ExtendVote Usage 正式三事、怎样选空扩展、怎样写非确定逻辑。

## 官方三件事

规范把 ExtendVote Usage 里应用可以选 0 长扩展写成三件独立的实现事，不是「看见能空 就已经不会叫 ExtendVote interchangeable、已经跳过 Verify interchangeable、已经必须填内容 interchangeable」一件事：

1. **看见 the Application can choose a 0-length vote extension / 看见应用可以选 0 长 vote extension 不是已经 ExtendVote Usage bundled（437） interchangeable / 已经不会叫 ExtendVote interchangeable / 已经必须填内容 interchangeable，也不是已经 precommit nil will not call ExtendVote bundled（437 第一件事 / 524） interchangeable / 已经 precommit nil 不会叫 ExtendVote interchangeable，也不是已经 ExtendVote When return extension bundled（509） interchangeable / 已经必须回非空 interchangeable，也不是已经 empty extension still calls Verify bundled（521） interchangeable / 已经 Verify 侧 0 长仍会 call interchangeable。**  
   官方 ExtendVote Usage 写：the Application can choose a 0-length vote extension。看见 can choose 0-length，不是已经 ExtendVote Usage bundled（437） interchangeable——437 钉 bundled 三事，本页钉 can choose 0-length 单句。看见应用可以选空，不是已经 precommit nil will not call ExtendVote（524） interchangeable——524 钉 nil Precommit 不调，本页钉非 nil 路径可选 0 长。看见能空，不是已经 ExtendVote When return extension（509） interchangeable——509 钉 When step 3 return bytes，本页钉 Usage 侧可选 0 长单句。
2. **看见 CometBFT will still call `ExtendVote` on non-nil Precommit even when the Application returns 0-length extension / 看见非 nil Precommit 仍会 call ExtendVote 不是已经 ExtendVote Usage bundled（437） interchangeable / 已经不会叫 ExtendVote interchangeable，也不是已经 precommit nil will not call ExtendVote bundled（524） interchangeable / 已经 precommit nil 不会叫 ExtendVote interchangeable，也不是已经 ExtendVote When 正式流程 bundled（438） interchangeable / 已经 sets lock values interchangeable / 已经 broadcast Precommit interchangeable，也不是已经 +2/3 prevote nil 才 ExtendVote bundled（361） interchangeable / 已经 nil 路径也会 call interchangeable。**  
   官方 ExtendVote Usage 写：看见选了空，不是已经不会叫 ExtendVote——437 bundled 常被写成「选了 0 长就已经不会叫」，本页钉仍会 call 单句。看见仍会叫 ExtendVote，不是已经 precommit nil will not call（524） interchangeable——524 钉 nil 路径不调，本页钉非 nil + 0 长仍会 call。看见 still calls on non-nil Precommit，不是已经 ExtendVote When 正式流程（438） interchangeable——438 钉 When call/return/broadcast bundled，本页钉 Usage 侧仍会 call 单句。
3. **看见 choosing a 0-length extension is not skip Verify / 看见选了空不是已经跳过 Verify 不是已经 ExtendVote Usage bundled（437） interchangeable / 已经跳过 Verify interchangeable / 已经 0 长就不叫 Verify interchangeable，也不是已经 empty extension still calls Verify bundled（521） interchangeable / 已经 Verify 侧 0 长仍会 call interchangeable，也不是已经 Precommit 没有带有效签的扩展 bundled（514 / 435） interchangeable / 已经 0 长就不合法 interchangeable，也不是已经 precommit nil will not call ExtendVote bundled（524） interchangeable / 已经 nil 路径不调 interchangeable。**  
   官方 ExtendVote Usage 写：看见选了空，不是已经跳过 Verify 那种已经不用验。看见 choosing empty，不是已经 skip Verify interchangeable——437 bundled 常与 Verify Usage bundled 混成「能空就已经跳过 Verify」，本页钉 ExtendVote 侧选了空不是 skip Verify 单句。看见 not skip Verify，不是已经 empty extension still calls Verify（521） interchangeable——521 钉 Verify 侧 0 长仍会 call，本页钉 ExtendVote 侧选了空不等于接收侧不调 Verify。看见 0-length on non-nil，不是已经 0 长就不合法（514） interchangeable——514 钉 0 长+有效签合法，本页钉 ExtendVote 侧可选 0 长。

怎样做写 ExtendVote Usage 正式三事、怎样选空扩展、怎样写非确定逻辑 是规范里的做法，本页不抄。ExtendVote Usage bundled（437）、precommit nil will not call ExtendVote（524）、empty extension still calls Verify（521）是另外那套，本页不抄。

## 官方为什么这样拆

- **can choose 0-length ≠ 已经不会叫 ExtendVote interchangeable：** 官方把可选 0 长与 nil 路径不调分开。
- **still calls ExtendVote on non-nil ≠ precommit nil will not call interchangeable：** 官方把非 nil + 0 长仍会 call 与 524 nil 路径不调分开。
- **choosing empty not skip Verify ≠ 已经跳过 Verify interchangeable：** 官方把 ExtendVote 侧选空与 Verify 侧仍会 call bundled 分开。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| can choose 0-length extension | 不是 won't call ExtendVote | 不是 precommit nil won't call（524） |
| still calls ExtendVote on non-nil | 不是 ExtendVote Usage bundled | 不是 ExtendVote When normal path（438） |
| choosing empty not skip Verify | 不是 skip Verify | 不是 Verify empty still calls（521） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 ExtendVote Usage application can choose 0-length extension 正式三事，必须分开 can choose 0-length 是不是已经不会叫 ExtendVote interchangeable / 已经必须填内容 interchangeable、still calls ExtendVote on non-nil 是不是 precommit nil will not call interchangeable / 已经 nil 路径也会 call interchangeable、choosing empty not skip Verify 是不是已经跳过 Verify interchangeable / 已经 0 长就不叫 Verify interchangeable。可以跳过「看见能空 就已经不会叫 ExtendVote interchangeable」。不要另写怎样写 ExtendVote Usage 正式三事。

## 本页不抄

- 怎样做写 ExtendVote Usage 正式三事、怎样选空扩展、怎样写非确定逻辑。
- precommit nil will not call ExtendVote / nil vote no CanonicalVoteExtension。那是不变量 524（437 item 1）。
- CometBFT will call VerifyVoteExtension even for 0-length extensions。那是不变量 521（353 item 1）。
- 造扩展的应用逻辑可以非确定。那是不变量 526（437 item 3 余量）。
