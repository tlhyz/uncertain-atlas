# 例：看见 ExtendVoteResponse.vote_extension only attached to non-nil Precommit / precommit nil will not call ExtendVote / nil vote does not carry CanonicalVoteExtension 不是已经 ExtendVote Usage bundled interchangeable / 已经会调 ExtendVote interchangeable / 已经签了 nil 票仍带扩展 interchangeable

**层次**：实现 / ExtendVote Usage precommit nil will not call ExtendVote 正式三事。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) ExtendVote Usage / When precommit nil 句。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「only on non-nil Precommit / precommit nil will not call ExtendVote / nil vote no CanonicalVoteExtension 不是 ExtendVote Usage bundled interchangeable / 不是已经会调 ExtendVote interchangeable / 不是已经签了 nil 票仍带扩展 interchangeable」，不是 ExtendVote Usage bundled（437），也不是 ExtendVote only on non-nil Precommit at Req 6（350），也不是应用可以选 0 长扩展（525 余量）。不要另写怎样写 ExtendVote Usage 正式三事、怎样选空扩展、怎样写非确定逻辑。

## 官方三件事

规范把 ExtendVote Usage / When 里 precommit nil 不会叫 ExtendVote 写成三件独立的实现事，不是「看见 precommit nil 就已经会调 ExtendVote interchangeable、已经不会叫 interchangeable、已经签了 nil 票仍带扩展 interchangeable」一件事：

1. **看见 `ExtendVoteResponse.vote_extension` is only attached to non-nil Precommit messages / 看见 vote_extension 只会挂在非 nil Precommit 上 不是已经 ExtendVote Usage bundled（437） interchangeable / 已经会调 ExtendVote interchangeable / 已经签了 nil 票仍带扩展 interchangeable，也不是已经 ExtendVote 只在即将广播非 nil Precommit 时才叫 bundled（350） interchangeable / 已经每一高度一份 interchangeable，也不是已经 ExtendVote When 正式流程 bundled（438） interchangeable / 已经广播 Precommit interchangeable / 已经 construct CanonicalVote interchangeable，也不是已经应用可以选 0 长扩展 bundled（437 第二件事 / 525 余量） interchangeable / 已经不会叫 ExtendVote interchangeable。**  
   官方 ExtendVote Usage 写：ExtendVoteResponse.vote_extension is only attached to non-nil Precommit messages。看见 only on non-nil Precommit，不是已经 ExtendVote Usage bundled（437） interchangeable——437 钉 bundled 三事，本页钉 only on non-nil Precommit 单句。看见 vote_extension 只挂非 nil，不是已经 ExtendVote 只在即将广播非 nil Precommit 时才叫（350） interchangeable——350 钉 Req 6 之前一轮一份，本页钉 Usage 侧 only attached 单句。看见 attached，不是已经 ExtendVote When 正式流程（438） interchangeable——438 钉 construct/broadcast bundled，本页钉 Usage 侧 attachment 单句。
2. **看见 if the consensus algorithm is going to precommit nil, it will not call `ExtendVote` / 看见 precommit nil 不会叫 ExtendVote 不是已经 ExtendVote Usage bundled（437） interchangeable / 已经会调 ExtendVote interchangeable，也不是已经 ExtendVote When 正式流程 bundled（438） interchangeable / 已经 sets lock values interchangeable / 已经 return extension interchangeable，也不是已经 +2/3 prevote nil 才 ExtendVote bundled（361） interchangeable / 已经会调 ExtendVote interchangeable，也不是已经应用可以选 0 长扩展 bundled（437 第二件事 / 525 余量） interchangeable / 已经不会叫 ExtendVote interchangeable。**  
   官方 ExtendVote Usage 写：if the consensus algorithm is going to precommit nil, it will not call ExtendVote。看见 precommit nil，不是已经会调 ExtendVote interchangeable——437 bundled 常被写成「看见 precommit nil 就已经会调」，本页钉 will not call 单句。看见不会叫，不是已经 ExtendVote When 正式流程（438） interchangeable——438 钉正常 When call/return/broadcast，本页钉 nil 路径不调。看见 going to precommit nil，不是已经 +2/3 prevote nil 才 ExtendVote（361） interchangeable——361 钉锁住再调，本页钉 nil 路径不调单句。
3. **看见 when broadcasting precommit nil (+2/3 prevote nil or timeoutPrevote), CometBFT will not call ExtendVote and nil vote does not carry CanonicalVoteExtension / 看见广播 precommit nil 时不叫 ExtendVote、nil 票不带 CanonicalVoteExtension 不是已经 ExtendVote Usage bundled（437） interchangeable / 已经会调 ExtendVote interchangeable / 已经带了扩展 interchangeable，也不是已经 ExtendVote When 正式流程 bundled（438） interchangeable / 已经 fill CanonicalVoteExtension interchangeable / 已经 signs populated CanonicalVoteExtension interchangeable，也不是已经 Process REJECT prevote nil bundled（33） interchangeable / 已经当成块非法 interchangeable，也不是已经应用可以选 0 长扩展 bundled（437 第二件事 / 525 余量） interchangeable / 已经不会叫 ExtendVote interchangeable / 已经跳过 Verify interchangeable。**  
   官方 ExtendVote When 写：when broadcasting precommit nil（+2/3 prevote nil or timeoutPrevote）, CometBFT will not call ExtendVote, and nil vote does not carry CanonicalVoteExtension。看见 When 侧 nil 路径，不是已经 ExtendVote Usage bundled（437） interchangeable——437 钉 bundled 三事，本页钉 When nil 路径单句。看见 nil 票不带 CanonicalVoteExtension，不是已经 fill CanonicalVoteExtension（510） interchangeable——510 钉 When step 4，本页钉 nil 路径无 extension。看见不会 call ExtendVote，不是已经应用可以选 0 长（525 余量） interchangeable——525 钉 0 长仍会 call 非 nil Precommit，本页钉 nil Precommit 不调。

怎样做写 ExtendVote Usage 正式三事、怎样选空扩展、怎样写非确定逻辑 是规范里的做法，本页不抄。ExtendVote Usage bundled（437）、ExtendVote only on non-nil at Req 6（350）、应用可以选 0 长扩展（525 余量）是另外那套，本页不抄。

## 官方为什么这样拆

- **only attached to non-nil Precommit ≠ 已经会调 ExtendVote interchangeable：** 官方把 attachment 条件和已经会 call 分开。
- **precommit nil will not call ExtendVote ≠ ExtendVote Usage bundled interchangeable：** 官方把 nil 路径不调与 0 长仍会 call bundled 分开。
- **nil vote does not carry CanonicalVoteExtension ≠ 已经带了扩展 interchangeable：** 官方把 nil 票无 extension 和 When fill/sign bundled 分开。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| only attached to non-nil Precommit | 不是 already will call | 不是 one extension per round（350） |
| precommit nil will not call ExtendVote | 不是 ExtendVote Usage bundled | 不是 ExtendVote When normal path（438） |
| nil vote no CanonicalVoteExtension | 不是 already has extension | 不是 0-length on non-nil Precommit（525） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 ExtendVote Usage precommit nil will not call ExtendVote 正式三事，必须分开 only on non-nil Precommit 是不是已经会调 ExtendVote interchangeable / 已经签了 nil 票仍带扩展 interchangeable、precommit nil will not call 是不是 ExtendVote Usage bundled interchangeable / 已经不会叫 interchangeable、nil vote no CanonicalVoteExtension 是不是已经 fill CanonicalVoteExtension interchangeable / 已经带了扩展 interchangeable。可以跳过「看见 precommit nil 就已经会调 ExtendVote interchangeable」。不要另写怎样写 ExtendVote Usage 正式三事。

## 本页不抄

- 怎样做写 ExtendVote Usage 正式三事、怎样选空扩展、怎样写非确定逻辑。
- 应用可以选 0 长扩展 / 仍会 call ExtendVote on non-nil。那是不变量 525（437 item 2 余量）。
- ExtendVote When 正式流程 / fill CanonicalVoteExtension。那是不变量 438 / 510。
- ExtendVote 只在即将广播非 nil Precommit 时才叫。那是不变量 350。
