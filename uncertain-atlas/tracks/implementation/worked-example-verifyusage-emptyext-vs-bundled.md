# 例：看见 CometBFT will call VerifyVoteExtension even for 0-length extensions / empty extension means sender chose not to extend / still calls Verify is not skip Verify 不是已经 Verify Usage bundled interchangeable / 已经跳过 Verify interchangeable / 已经 0 长就不叫 Verify interchangeable

**层次**：实现 / VerifyVoteExtension Usage empty extension still calls Verify 正式三事。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) VerifyVoteExtension Usage 空扩展句。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「even for 0-length / sender chose not to extend / still calls Verify 不是 Verify Usage bundled interchangeable / 不是已经跳过 Verify interchangeable / 不是已经 0 长就不叫 Verify interchangeable」，不是 Verify Usage bundled（353），也不是 Verify When step 1 discard（514），也不是不对 local process 调用（522 余量）。不要另写怎样写 Verify 何时调用、怎样写空扩展、怎样缓存 Process。

## 官方三件事

规范把 VerifyVoteExtension Usage 里空扩展仍会调 Verify 写成三件独立的实现事，不是「看见空扩展就已经跳过 Verify interchangeable、已经 0 长就不叫 Verify interchangeable、已经不用调 interchangeable」一件事：

1. **看见 CometBFT will call `VerifyVoteExtension` even for 0-length extensions / 看见即使 0 长度也会调 VerifyVoteExtension 不是已经 Verify Usage bundled（353） interchangeable / 已经跳过 Verify interchangeable / 已经 0 长就不叫 Verify interchangeable，也不是已经 Precommit 没有带有效签的扩展就会当非法丢掉 bundled（435 / 514） interchangeable / 已经不带签就不合法 interchangeable，也不是已经 vote_extension 可以空（437） interchangeable / 已经 precommit nil 不会叫 ExtendVote interchangeable，也不是已经 Verify When step 1 discard bundled（514） interchangeable / 已经无有效签先丢掉 interchangeable。**  
   官方 VerifyVoteExtension Usage 写：CometBFT will call VerifyVoteExtension even for 0-length extensions。看见 even for 0-length，不是已经跳过 Verify interchangeable——353 bundled 常被写成「空扩展就已经跳过 Verify」，本页钉 0 长仍会 call 单句。看见仍会调，不是已经 0 长就不叫 Verify interchangeable——514 钉 When step 1 无有效签先丢掉，本页钉 Usage 侧有有效签的 0 长仍会 call。看见 will call，不是已经 Precommit 没有带有效签的扩展 bundled（435） interchangeable——435 第一件事 bundled 常被写成「没扩展就不 call」，本页钉 0 长仍会 call。
2. **看见 an empty extension means the sender chose not to extend / 看见空扩展表示发送方选择不扩 不是已经 Verify Usage bundled（353） interchangeable / 已经跳过 Verify interchangeable，也不是已经空扩展仍会调 Verify bundled interchangeable / 已经 0 长就不合法 interchangeable，也不是已经 vote_extension 可以空（437） interchangeable / 已经不会叫 ExtendVote interchangeable / 已经必须填内容 interchangeable，也不是已经 ExtendVoteResponse.vote_extension 只会挂在非 nil Precommit bundled（437 第一件事） interchangeable / 已经 precommit nil 不会叫 ExtendVote interchangeable，也不是已经 VerifyVoteExtensionRequest.vote_extension 可以 0 长 bundled（422） interchangeable / 已经跳过 Verify interchangeable。**  
   官方 VerifyVoteExtension Usage 写：an empty extension means the sender chose not to extend。看见 sender chose not to extend，不是已经跳过 Verify interchangeable——选择不扩不等于不调 Verify，本页钉语义单句。看见空扩展，不是已经 0 长就不合法 interchangeable——514 钉 0 长+有效签合法，本页钉 Usage 侧 0 长语义。看见 chose not to extend，不是已经 vote_extension 可以空（437） interchangeable——437 钉 ExtendVote 侧可选 0 长，本页钉 Verify Usage 侧 0 长语义。
3. **看见 still calls Verify is not skip Verify / 看见仍会调不是已经跳过 Verify 不是已经 Verify Usage bundled（353） interchangeable / 已经跳过 Verify interchangeable / 已经 0 长就不叫 Verify interchangeable，也不是已经 Verify When 正式流程 step 1 discard bundled（514） interchangeable / 已经无有效签先丢掉 interchangeable，也不是已经 Precommit 没有带有效签的扩展 bundled（435 第一件事） interchangeable / 已经带有效签就会调 Verify bundled interchangeable，也不是已经 Verify 不对 local process 调用 bundled（353 第二件事） interchangeable / 已经本地票也 Verify interchangeable，也不是已经 request hash 不保证 Process bundled（353 第三件事） interchangeable / 已经对该块跑过 Process interchangeable。**  
   官方 VerifyVoteExtension Usage 把仍会 call 和 skip Verify 分开——353 bundled 三事常被写成「空扩展就已经跳过 Verify」，本页钉 still calls Verify 单句。看见仍会调，不是已经 Verify When step 1 discard（514） interchangeable——514 钉无有效签先丢掉，本页钉有有效签 0 长仍会 call。看见 not skip Verify，不是已经 Verify Usage bundled（353） interchangeable——353 钉 bundled 三事，本页钉 empty extension still calls 单句。

怎样做写 Verify 何时调用、怎样写空扩展、怎样缓存 Process 是规范里的做法，本页不抄。Verify Usage bundled（353）、Verify When step 1 discard（514）、不对 local process 调用（522 余量）是另外那套，本页不抄。

## 官方为什么这样拆

- **even for 0-length extensions still calls Verify ≠ 已经跳过 Verify interchangeable：** 官方把 0 长仍会 call 和 skip Verify 分开。
- **empty extension means sender chose not to extend ≠ 已经 0 长就不叫 Verify interchangeable：** 官方把语义和 skip call 分开。
- **still calls Verify ≠ Verify Usage bundled interchangeable：** 官方把 empty extension still calls 单句和 local process / hash bundled 分开。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| even for 0-length still calls Verify | 不是 skip Verify | 不是 no valid sig discard（514） |
| empty extension means sender chose not to extend | 不是 0 长就不合法 | 不是 ExtendVote 0 长路径（437） |
| still calls Verify | 不是 Verify Usage bundled（353） | 不是 local process also Verify（522） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 VerifyVoteExtension Usage empty extension still calls Verify 正式三事，必须分开 even for 0-length 是不是已经跳过 Verify interchangeable / 已经 0 长就不叫 Verify interchangeable、empty extension means sender chose not to extend 是不是已经 0 长就不合法 interchangeable / 已经必须填内容 interchangeable、still calls Verify 是不是 Verify Usage bundled interchangeable / 已经本地票也 Verify interchangeable。可以跳过「看见空扩展就已经跳过 Verify interchangeable」。不要另写怎样写 Verify 何时调用。

## 本页不抄

- 怎样做写 Verify 何时调用、怎样写空扩展、怎样缓存 Process。
- Verify Usage bundled / 不对 local process 调用 / hash 不保证 Process。那是不变量 353。
- Verify When step 1 discard / 0 长+有效签合法。那是不变量 514。
- ExtendVote 0 长 / precommit nil 不会叫 ExtendVote。那是不变量 437。
