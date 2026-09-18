# 例：看见 Precommit without valid signature extension discarded / 0-length extension valid with valid signature / step 1 before VerifyVoteExtension call 不是已经 Verify When 正式流程 interchangeable / 已经跳过 Verify interchangeable / 已经验过扩展 interchangeable

**层次**：实现 / VerifyVoteExtension When discard invalid extension 正式三事。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) VerifyVoteExtension When step 1。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「discard invalid extension / 0-length with valid sig / step 1 before call 不是 Verify When 正式流程 interchangeable / 不是跳过 Verify interchangeable / 不是已经验过扩展 interchangeable」，不是 Verify When 正式流程（435），也不是空扩展仍会调 Verify（353）。不要另写怎样验伴随签名、怎样调 VerifyVoteExtension、怎样写 ExtendedCommitInfo。

## 官方三件事

规范把 VerifyVoteExtension When step 1 里无有效签扩展就丢掉、0 长扩展有有效签也算有效、在调 Verify 之前写成三件独立的实现事，不是「看见收到 Precommit 就已经跳过 Verify interchangeable、已经验过扩展 interchangeable、已经写进 last_commit interchangeable」一件事：

1. **看见 If the Precommit message does not contain a vote extension with a valid signature, _p_ discards the Precommit message as invalid / 看见 Precommit 没有带有效签的扩展就会当非法丢掉 不是已经 Verify When 正式流程 bundled（435） interchangeable / 已经跳过 Verify interchangeable / 已经验过扩展 interchangeable，也不是已经空扩展仍会调 Verify（353） interchangeable / 已经 0 长就不叫 Verify interchangeable，也不是已经 Precommit 没有带有效签的扩展就会当非法丢掉 bundled（435 第一件事） interchangeable / 已经带有效签就会调 Verify interchangeable。**  
   官方 When step 1 写：If the Precommit message does not contain a vote extension with a valid signature, _p_ discards the Precommit message as invalid。看见 discards as invalid，不是已经 Verify When 正式流程（435） interchangeable——435 钉 steps 1–4 bundled，本页钉 step 1 discard 单句。看见丢掉了，不是已经空扩展仍会调 Verify（353） interchangeable——353 钉 Usage 侧 0 长仍叫 Verify，本页钉 When step 1 无有效签先丢掉。看见没调 Verify，不是已经带有效签就会调 Verify（435 第二件事 bundled） interchangeable——435 钉 step 2 call，本页钉 step 1 在 call 之前。
2. **看见 a 0-length vote extension is valid as long as its accompanying signature is also valid / 看见 0 长扩展只要伴随签名也合法就算有效 不是已经空扩展仍会调 Verify bundled（353） interchangeable / 已经跳过 Verify interchangeable，也不是已经没有扩展就不叫 Verify interchangeable / 已经 0 长就不合法 interchangeable，也不是已经 vote_extension 可以空（437） interchangeable / 已经不会叫 ExtendVote interchangeable，也不是已经 Precommit 没有带有效签的扩展 bundled（435） interchangeable / 已经带有效签就会调 Verify interchangeable。**  
   官方 When step 1 脚注：a 0-length vote extension is valid as long as its accompanying signature is also valid。看见 0 长+有效签合法，不是已经空扩展仍会调 Verify（353） interchangeable——353 钉 Usage 侧仍叫 Verify，本页钉 When step 1 0 长+有效签仍算有效、仍可能进入 step 2。看见 0 长，不是已经没有签就不合法 interchangeable——本页钉 0 长看伴随签。看见有效，不是已经 ExtendVote 侧应用可以选 0 长（437） interchangeable——437 钉 ExtendVote Usage nil 路径，本页钉 Verify When 收到侧 0 长有效性。
3. **看见 step 1 before _p_'s CometBFT calls VerifyVoteExtension (step 2) / 看见 step 1 在调 VerifyVoteExtension 之前 不是已经 Verify When 正式流程 bundled（435） interchangeable / 已经验过扩展 interchangeable，也不是已经 VerifyVoteExtensionResponse.status ACCEPT/REJECT bundled（435 step 3–4） interchangeable / 已经写进 last_commit interchangeable，也不是已经 Verify 不是 called for precommit votes sent by local process（Usage） interchangeable / 已经本地票也 Verify interchangeable，也不是已经 round 0 height h MAY add without calling Verify（352） interchangeable / 已经迟到扩展已经 Verify 过 interchangeable。**  
   官方 When 把 step 1 和 step 2 分开。看见 step 1 在 call 之前，不是已经 Verify When 正式流程（435） interchangeable——435 钉 bundled 四步，本页钉 step 1 discard 单句。看见先丢掉无有效签，不是已经 Application returns ACCEPT/REJECT（435 step 3–4） interchangeable——435 钉 step 3–4 后效，本页钉 step 1 在 return 之前。看见收到他人 Precommit，不是已经 Verify 不对 local process 发出的 Precommit 调用（Usage） interchangeable——Usage 钉本地票不调，本页钉 When step 1 收到侧有效性门槛。

怎样做验伴随签名、怎样调 VerifyVoteExtension、怎样写 ExtendedCommitInfo 是规范里的做法，本页不抄。Verify When 正式流程（435）、空扩展仍会调 Verify（353）、迟到扩展 MAY 不加 Verify（352）是另外那套，本页不抄。

## 官方为什么这样拆

- **discards invalid Precommit ≠ Verify When 正式流程 bundled interchangeable：** 官方把 step 1 discard 单句和 steps 2–4 call/ACCEPT/REJECT bundled 分开。
- **0-length with valid signature ≠ 空扩展仍会调 Verify bundled interchangeable：** 官方把 When step 1 0 长有效性单句和 Usage 侧仍叫 Verify 分开。
- **step 1 before VerifyVoteExtension call ≠ 已经验过扩展 interchangeable：** 官方把 step 1 门槛和 step 2 call 分开。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| discards Precommit without valid signature extension | 不是 Verify When bundled（435） | 不是 skip Verify（353 误解） |
| 0-length extension valid with valid signature | 不是 0 长就不合法 | 不是 ExtendVote 0 长路径（437） |
| step 1 before VerifyVoteExtension call | 不是 already verified | 不是 ACCEPT/REJECT bundled（435） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 VerifyVoteExtension When discard invalid extension 正式三事，必须分开 discards invalid Precommit 是不是 Verify When 正式流程 bundled interchangeable、0-length with valid signature 是不是空扩展仍会调 Verify bundled interchangeable、step 1 before call 是不是已经验过扩展 interchangeable / 已经写进 last_commit interchangeable。可以跳过「看见收到 Precommit 就已经跳过 Verify interchangeable、已经验过扩展 interchangeable」。514 VerifyVoteExtension When discard bundled unbundling 完成（1325 item 1 / 1326 item 2 / 1327 item 3）；精读 [`worked-example-vwdisc-notsig-vs-bundled.md`](worked-example-vwdisc-notsig-vs-bundled.md)（不变量 1325 item 1）、[`worked-example-vwdisc-notzero-vs-bundled.md`](worked-example-vwdisc-notzero-vs-bundled.md)（不变量 1326 item 2）、[`worked-example-vwdisc-notstep-vs-bundled.md`](worked-example-vwdisc-notstep-vs-bundled.md)（不变量 1327 item 3）。不要另写怎样验伴随签名。

## 本页不抄

- 怎样做验伴随签名、怎样调 VerifyVoteExtension、怎样写 ExtendedCommitInfo。
- Verify When 正式流程 / 带有效签就会调 Verify / ACCEPT 留给 h+1 Prepare。那是不变量 435。
- 空扩展仍会调 Verify 就已经跳过 Verify。那是不变量 353。
- 迟到扩展 MAY 不加 Verify 就已经 Verify 过。那是不变量 352。
