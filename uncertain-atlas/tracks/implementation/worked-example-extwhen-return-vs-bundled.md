# 例：看见 Application returns ExtendVoteResponse.extension / not interpreted by the consensus algorithm / step 3 after synchronous call before CanonicalVoteExtension flow 不是已经 ExtendVote 何时调用 bundled interchangeable / 已经 ExtendVote When 正式流程 interchangeable / 已经按原样签 interchangeable

**层次**：实现 / ExtendVote When return extension 正式三事。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) ExtendVote When step 3。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「returns extension / not interpreted / step 3 before CanonicalVoteExtension 不是 ExtendVote 何时调用 bundled interchangeable / 不是 ExtendVote When 正式流程 interchangeable / 不是按原样签 interchangeable」，不是 ExtendVote When call / synchronous（508），也不是 ExtendVote 何时调用（361）。不要另写怎样写扩展、怎样填 CanonicalVoteExtension、怎样验扩展。

## 官方三件事

规范把 ExtendVote When step 3 里应用回 extension 字节、共识算法不解释、在 step 2 之后 step 4 之前写成三件独立的实现事，不是「看见调了 ExtendVote 就已经是同一份扩展 interchangeable、已经包进 CanonicalVoteExtension interchangeable、已经 ExtendVote 回了 extension 就已经广播 Precommit interchangeable」一件事：

1. **看见 The Application returns an array of bytes, `ExtendVoteResponse.extension` / 看见应用回一份字节数组 ExtendVoteResponse.extension 不是已经 ExtendVote When 正式流程 bundled（438） interchangeable / 已经填进 CanonicalVoteExtension interchangeable / 已经广播 Precommit interchangeable，也不是已经 vote_extension 会包进 CanonicalVoteExtension（358） interchangeable / 已经按原样签 interchangeable，也不是已经 application-generated will be signed bundled（439） interchangeable / 已经签过 interchangeable，也不是已经应用可以选 0 长扩展就不会叫 ExtendVote（437） interchangeable / 已经跳过 Verify interchangeable。**  
   官方 When step 3 写：The Application returns an array of bytes, `ExtendVoteResponse.extension`。看见 returns extension bytes，不是已经填进 CanonicalVoteExtension 并签名（438） interchangeable——438 钉 When 正式流程 steps 4–7，本页钉 step 3 return extension 单句。看见 ExtendVoteResponse.extension，不是已经 vote_extension 会包进 CanonicalVoteExtension（358） interchangeable——358 钉 Usage 侧会包进包装，本页钉 When step 3 return 单句。看见回了字节数组，不是已经 application-generated will be signed（439） interchangeable——439 钉 Response Usage 侧 will be signed，本页钉 When step 3 return 单句。
2. **看见 which is not interpreted by the consensus algorithm / 看见共识算法不解释这份 extension 不是已经是同一份扩展 interchangeable / 已经 Verify 过 interchangeable，也不是已经 ExtendVote 何时调用 bundled（361） interchangeable / 已经包进 CanonicalVoteExtension interchangeable，也不是已经 VerifyVoteExtension MUST be deterministic（430） interchangeable / 已经必须同一份扩展 interchangeable，也不是已经造扩展的应用逻辑可以非确定（437） interchangeable / 已经必须确定 interchangeable。**  
   官方 When step 3 续：which is not interpreted by the consensus algorithm。看见 not interpreted，不是已经同一份扩展（361 第三件事） interchangeable——361 钉 When 侧 return+不解释 bundled，本页钉 step 3 not interpreted 单句。看见共识算法不解释，不是已经 Verify 过他人扩展（438） interchangeable——438 钉构造 CanonicalVote 不是已经验过，本页钉 When step 3 不解释单句。看见不解释，不是已经 Verify MUST deterministic（430） interchangeable——430 钉 Verify 回包栏，本页钉 When step 3 共识不解释语义。
3. **看见 step 3 after synchronous ExtendVote call (step 2) and before _p_ sets extension into CanonicalVoteExtension (step 4) / 看见 step 3 在同步 ExtendVote 调用之后、在填 CanonicalVoteExtension 之前 不是已经 ExtendVote When call / synchronous bundled（508） interchangeable / 已经能在返回后再改扩展 interchangeable，也不是已经 ExtendVote When 正式流程 bundled（438） interchangeable / 已经广播 Precommit interchangeable，也不是已经 ExtendVote 何时调用 bundled（361） interchangeable / 已经会调 ExtendVote interchangeable，也不是已经一轮只能交出一份扩展（350） interchangeable / 已经每一高度一份 interchangeable。**  
   官方 When 把 step 3 夹在 step 2 和 step 4 之间。看见 step 3 在中间，不是已经 synchronous ExtendVote call（508） interchangeable——508 钉 step 2 call/sync，本页钉 step 3 return 单句。看见回了 extension，不是已经 ExtendVote When 正式流程（438） interchangeable——438 钉填包装/签名/广播，本页钉 step 3 在填包装之前。看见 Application returns，不是已经 +2/3 prevote 才锁住再调 ExtendVote bundled（361） interchangeable——361 钉门槛 bundled，本页钉 step 3 return 单句。

怎样做写扩展、怎样填 CanonicalVoteExtension、怎样验扩展是规范里的做法，本页不抄。ExtendVote When call / synchronous（508）、ExtendVote 何时调用（361）、ExtendVote When 正式流程（438）、vote_extension 会包进 CanonicalVoteExtension（358）是另外那套，本页不抄。

## 官方为什么这样拆

- **returns ExtendVoteResponse.extension ≠ ExtendVote When 正式流程 bundled interchangeable：** 官方把 step 3 return extension 单句和 steps 4–7 填包装/广播 bundled 分开。
- **not interpreted by consensus ≠ 已经是同一份扩展 interchangeable：** 官方把 When step 3 不解释单句和 361 侧 return+不解释 bundled 分开。
- **step 3 before CanonicalVoteExtension ≠ ExtendVote 何时调用 bundled interchangeable：** 官方把 step 3 在填包装之前和 361 侧门槛 bundled 分开。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| returns ExtendVoteResponse.extension | 不是 ExtendVote When 正式流程 bundled（438） | 不是 vote_extension 会包进包装（358） |
| not interpreted by consensus algorithm | 不是已经是同一份扩展 | 不是 Verify MUST deterministic（430） |
| step 3 before CanonicalVoteExtension | 不是 call / synchronous bundled（508） | 不是 ExtendVote 何时调用 bundled（361） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 ExtendVote When return extension 正式三事，必须分开 returns ExtendVoteResponse.extension 是不是 ExtendVote When 正式流程 bundled interchangeable、not interpreted by consensus 是不是已经是同一份扩展 interchangeable、step 3 before CanonicalVoteExtension 是不是 ExtendVote 何时调用 bundled interchangeable / 已经按原样签 interchangeable。可以跳过「看见调了 ExtendVote 就已经是同一份扩展 interchangeable、已经包进 CanonicalVoteExtension interchangeable、已经 ExtendVote 回了 extension 就已经广播 Precommit interchangeable」。不要另写怎样写扩展、怎样填 CanonicalVoteExtension。

## 本页不抄

- 怎样做写扩展、怎样填 CanonicalVoteExtension、怎样验扩展。
- ExtendVote When call / synchronous。那是不变量 508。
- ExtendVote 何时调用 / +2/3 prevote 才锁住再调 / 回包字节不被解释 bundled。那是不变量 361。
- ExtendVote When 正式流程 / 填 CanonicalVoteExtension 并广播。那是不变量 438。
- vote_extension 会包进 CanonicalVoteExtension 就已经按原样签。那是不变量 358。
