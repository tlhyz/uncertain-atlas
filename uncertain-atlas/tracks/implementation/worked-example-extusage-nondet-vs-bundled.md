# 例：看见 application logic that creates extensions can be non-deterministic / logic can vary / no MUST deterministic for ExtendVote 不是已经 ExtendVote Usage bundled interchangeable / 已经必须同一份扩展 interchangeable / 已经 Verify 必须确定 interchangeable

**层次**：实现 / ExtendVote Usage extension creation logic can be non-deterministic 正式三事。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) ExtendVote Usage non-deterministic 句。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「logic can be non-deterministic / logic can vary / no MUST deterministic for ExtendVote 不是 ExtendVote Usage bundled interchangeable / 不是已经必须同一份扩展 interchangeable / 不是已经 Verify 必须确定 interchangeable」，不是 ExtendVote Usage bundled（437），也不是 VerifyVoteExtension MUST be deterministic（430），也不是 ExtendVote 没有确定性要求 at Req（338）。不要另写怎样写 ExtendVote Usage 正式三事、怎样选空扩展、怎样写非确定逻辑。

## 官方三件事

规范把 ExtendVote Usage 里造扩展的应用逻辑可以非确定写成三件独立的实现事，不是「看见可以非确定 就已经必须同一份扩展 interchangeable、已经是同一块就同一份 interchangeable、已经 Verify 必须确定 interchangeable」一件事：

1. **看见 the Application logic that creates the extension can be non-deterministic / 看见造扩展的应用逻辑可以非确定 不是已经 ExtendVote Usage bundled（437） interchangeable / 已经必须同一份扩展 interchangeable / 已经 Verify 必须确定 interchangeable，也不是已经 VerifyVoteExtension MUST be deterministic bundled（430） interchangeable / 已经 status 必须只依赖请求和上一份状态 interchangeable，也不是已经 ExtendVote When return extension bundled（509） interchangeable / 已经 not interpreted by consensus interchangeable / 已经必须是同一份扩展 interchangeable，也不是已经 precommit nil will not call ExtendVote bundled（524） interchangeable / 已经 precommit nil 不会叫 interchangeable。**  
   官方 ExtendVote Usage 写：the Application logic that creates the extension can be non-deterministic。看见 can be non-deterministic，不是已经 ExtendVote Usage bundled（437） interchangeable——437 钉 bundled 三事，本页钉 logic can be non-deterministic 单句。看见造扩展逻辑可以非确定，不是已经 VerifyVoteExtension MUST be deterministic（430） interchangeable——430 钉 Verify 侧 MUST deterministic，本页钉 ExtendVote 侧 can be non-deterministic。看见 logic that creates the extension，不是已经 ExtendVote When return extension（509） interchangeable——509 钉 When step 3 return bytes，本页钉 Usage 侧 creation logic 单句。
2. **看见 logic can vary / same block does not imply same extension / 看见逻辑可以变、同一块不蕴涵同一份扩展 不是已经 ExtendVote Usage bundled（437） interchangeable / 已经必须同一份扩展 interchangeable，也不是已经 which is not interpreted by the consensus algorithm bundled（509） interchangeable / 已经 not interpreted 就是已经是同一份 interchangeable，也不是已经 ExtendVote 没有确定性要求 at Req bundled（338） interchangeable / 已经 ExtendVote 没有确定性要求就是已经是同一块 interchangeable，也不是已经 application can choose 0-length bundled（525） interchangeable / 已经能空就是必须填内容 interchangeable。**  
   官方 ExtendVote Usage 写：看见逻辑可以变，不是已经是同一块就一定是同一份。看见 logic can vary，不是已经 must same extension interchangeable——437 bundled 常被写成「同一块就同一份」，本页钉 same block does not imply same extension 单句。看见不蕴涵同一份，不是已经 not interpreted by consensus（509） interchangeable——509 钉共识不解释 bytes，本页钉 creation logic 可以变单句。看见 logic can vary，不是已经 ExtendVote 没有确定性要求 at Req（338） interchangeable——338 钉 Req 侧没有 MUST deterministic，本页钉 Usage 侧 logic can vary 单句。
3. **看见 no MUST deterministic requirement for ExtendVote unlike Verify / 看见 ExtendVote 没有这道必须确定、不像 Verify 那样 MUST deterministic 不是已经 ExtendVote Usage bundled（437） interchangeable / 已经 Verify 必须确定 interchangeable，也不是已经 VerifyVoteExtension MUST be deterministic bundled（430） interchangeable / 已经 status 必须只依赖请求和上一份状态 interchangeable，也不是已经 ProcessProposal MUST be deterministic bundled（340） interchangeable / 已经 Process 必须确定 interchangeable，也不是已经 Prepare MAY be non-deterministic bundled（504） interchangeable / 已经 Prepare 可以非确定 interchangeable / 已经 ExtendVote 也 MUST deterministic interchangeable。**  
   官方 ExtendVote Usage 写：看见没有这道必须确定，不是已经 Verify 必须确定。看见 no MUST deterministic for ExtendVote，不是已经 VerifyVoteExtension MUST be deterministic（430） interchangeable——430 钉 Verify 侧 MUST，本页钉 ExtendVote 侧没有这道 MUST 单句。看见 unlike Verify，不是已经 Process MUST be deterministic（340） interchangeable——340 钉 Process 侧 MUST，本页钉 ExtendVote 侧没有这道 MUST。看见没有这道必须确定，不是已经 ExtendVote Usage bundled（437） interchangeable——437 bundled 常与 Verify MUST 混成「扩展路径都必须确定」，本页钉 ExtendVote 没有这道 MUST 单句。

怎样做写 ExtendVote Usage 正式三事、怎样选空扩展、怎样写非确定逻辑 是规范里的做法，本页不抄。ExtendVote Usage bundled（437）、VerifyVoteExtension MUST be deterministic（430）、ExtendVote 没有确定性要求 at Req（338）是另外那套，本页不抄。

## 官方为什么这样拆

- **logic can be non-deterministic ≠ 已经必须同一份扩展 interchangeable：** 官方把可以非确定和 must same extension 分开。
- **logic can vary / same block ≠ same extension ≠ ExtendVote Usage bundled interchangeable：** 官方把 logic can vary 与 not interpreted bundled 分开。
- **no MUST deterministic for ExtendVote ≠ Verify MUST deterministic interchangeable：** 官方把 ExtendVote 没有这道 MUST 与 Verify MUST deterministic 分开。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| logic can be non-deterministic | 不是 must same extension | 不是 Verify MUST deterministic（430） |
| logic can vary / same block | 不是 same extension | 不是 not interpreted by consensus（509） |
| no MUST deterministic for ExtendVote | 不是 Verify MUST | 不是 ExtendVote no det req at Req（338） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 ExtendVote Usage extension creation logic can be non-deterministic 正式三事，必须分开 logic can be non-deterministic 是不是已经必须同一份扩展 interchangeable / 已经 Verify 必须确定 interchangeable、logic can vary 是不是 same block implies same extension interchangeable / 已经 not interpreted interchangeable、no MUST deterministic for ExtendVote 是不是 Verify MUST deterministic interchangeable / 已经 Process MUST deterministic interchangeable。可以跳过「看见可以非确定 就已经必须同一份扩展 interchangeable」。不要另写怎样写 ExtendVote Usage 正式三事。

## 本页不抄

- 怎样做写 ExtendVote Usage 正式三事、怎样选空扩展、怎样写非确定逻辑。
- precommit nil will not call ExtendVote。那是不变量 524（437 item 1）。
- application can choose 0-length extension。那是不变量 525（437 item 2）。
- ExtendVote When return extension / not interpreted by consensus。那是不变量 509。
