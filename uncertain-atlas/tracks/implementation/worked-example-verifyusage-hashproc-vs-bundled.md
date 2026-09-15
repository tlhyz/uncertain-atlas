# 例：看见 hash in the request points to a block / does not guarantee exposed via ProcessProposal / not hash means already Process'd 不是已经 Verify Usage bundled interchangeable / 已经对该块跑过 Process interchangeable / 已经是提议者那边也会叫 Process interchangeable

**层次**：实现 / VerifyVoteExtension Usage hash does not guarantee Process 正式三事。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) VerifyVoteExtension Usage hash 句。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「hash points to a block / does not guarantee Process / not already Process'd 不是 Verify Usage bundled interchangeable / 不是已经对该块跑过 Process interchangeable / 不是已经是提议者那边也会叫 Process interchangeable」，不是 Verify Usage bundled（353），也不是 Process 也会在提议者那边叫（351），也不是 VerifyVoteExtensionRequest.hash 表栏（422）。不要另写怎样写 Verify 何时调用、怎样写空扩展、怎样缓存 Process。

## 官方三件事

规范把 VerifyVoteExtension Usage 里请求 hash 不保证已经 Process 写成三件独立的实现事，不是「看见请求里的 hash 就已经对该块跑过 Process interchangeable、已经 Process 过 interchangeable、已经对上这次 Process interchangeable」一件事：

1. **看见 the hash in the request points to a block / 看见请求里的 hash 指向某块 不是已经 Verify Usage bundled（353） interchangeable / 已经对该块跑过 Process interchangeable / 已经 Process 过 interchangeable，也不是已经 VerifyVoteExtensionRequest.hash 是扩展要指的那份拟议块哈希 bundled（422） interchangeable / 已经 ExtendVoteRequest.hash interchangeable / 已经对上拟议块头 interchangeable，也不是已经 VerifyVoteExtensionRequest.hash 不保证跑过 Process bundled（353 第三件事） interchangeable / 已经对该块跑过 Process bundled interchangeable，也不是已经 FinalizeBlockRequest.hash 是已决块哈希 bundled（394） interchangeable / 已经 Process 跑过 interchangeable。**  
   官方 VerifyVoteExtension Usage 写：the hash in the request points to a block。看见 points to a block，不是已经 Verify Usage bundled（353） interchangeable——353 钉 bundled 三事，本页钉 hash 指向某块单句。看见请求里的 hash，不是已经 VerifyVoteExtensionRequest.hash 表栏（422） interchangeable——422 钉表描述「扩展要指的那份拟议块哈希」，本页钉 Usage 侧 points to a block 单句。看见有 hash，不是已经 Finalize 请求栏 hash（394） interchangeable——394 钉已决块哈希，本页钉 Verify 请求 hash 指向拟议块。
2. **看见 does not guarantee the block has been exposed to the Application via `ProcessProposal` / 看见不保证已经通过 ProcessProposal 暴露给应用 不是已经 Verify Usage bundled（353） interchangeable / 已经对该块跑过 Process interchangeable / 已经 Process 过 interchangeable，也不是已经 Process 也会在提议者那边叫 bundled（351） interchangeable / 已经不用再 Process interchangeable / 已经对上这次 Process interchangeable，也不是已经 ProcessProposalRequest.txs 等于 PrepareProposalResponse.txs bundled（351） interchangeable / 已经列表对得上 interchangeable，也不是已经 Verify When step 2 call bundled（515） interchangeable / 已经验过扩展 interchangeable / 已经 Accept interchangeable。**  
   官方 VerifyVoteExtension Usage 写：does not guarantee the block has been exposed to the Application via ProcessProposal。看见 does not guarantee，不是已经 Process 过 interchangeable——353 bundled 常被写成「有 hash 就已经 Process 过」，本页钉不保证单句。看见 exposed via ProcessProposal，不是已经 Process 也会在提议者那边叫（351） interchangeable——351 钉提议者也会叫 Process，本页钉不保证已经暴露。看见 not guarantee，不是已经 Verify When call（515） interchangeable——515 钉收到他人票后 call Verify，本页钉 hash 不保证 Process 前提。
3. **看见 hash does not guarantee Process is not already Process'd / 看见 hash 不保证 Process 不是已经对该块跑过 Process 不是已经 Verify Usage bundled（353） interchangeable / 已经 Process 过 interchangeable / 已经对上这次 Process interchangeable，也不是已经 Process 也会在提议者那边叫 bundled（351） interchangeable / 已经不用再 Process interchangeable，也不是已经 empty extension still calls Verify bundled（521） interchangeable / 已经仍会 call interchangeable，也不是已经 not called for local process bundled（522） interchangeable / 已经本地票也 Verify interchangeable，也不是已经 VerifyVoteExtensionRequest.hash 表栏 bundled（422） interchangeable / 已经不保证跑过 Process interchangeable。**  
   官方 VerifyVoteExtension Usage 把 hash 指向某块和不保证 Process 分开——353 bundled 三事常被写成「看见 hash 就已经 Process 过」，本页钉 not already Process'd 单句。看见不保证，不是已经 Process 也会在提议者那边叫（351） interchangeable——351 钉通常紧跟 Prepare，本页钉不保证已经暴露。看见 hash，不是已经 Verify Usage bundled（353） interchangeable——353 钉 bundled 三事，本页钉 hash does not guarantee Process 单句。

怎样做写 Verify 何时调用、怎样写空扩展、怎样缓存 Process 是规范里的做法，本页不抄。Verify Usage bundled（353）、Process 也会在提议者那边叫（351）、VerifyVoteExtensionRequest.hash 表栏（422）是另外那套，本页不抄。

## 官方为什么这样拆

- **hash points to a block ≠ 已经对该块跑过 Process interchangeable：** 官方把有 hash 和已经 Process 过分开。
- **does not guarantee exposed via ProcessProposal ≠ 已经是提议者那边也会叫 Process interchangeable：** 官方把不保证和提议者也会叫 Process 分开。
- **hash does not guarantee Process ≠ Verify Usage bundled interchangeable：** 官方把 hash 不保证 Process 单句和 empty ext / local process bundled 分开。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| hash in request points to a block | 不是 already Process'd | 不是 Finalize hash（394） |
| does not guarantee exposed via ProcessProposal | 不是 proposer also Process（351） | 不是 txs list matched（351） |
| hash does not guarantee Process | 不是 Verify Usage bundled（353） | 不是 Verify When call（515） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 VerifyVoteExtension Usage hash does not guarantee Process 正式三事，必须分开 hash points to a block 是不是已经对该块跑过 Process interchangeable / 已经 Process 过 interchangeable、does not guarantee exposed via ProcessProposal 是不是已经是提议者那边也会叫 Process interchangeable / 已经对上这次 Process interchangeable、hash does not guarantee Process 是不是 Verify Usage bundled interchangeable / 已经验过扩展 interchangeable。可以跳过「看见请求里的 hash 就已经对该块跑过 Process interchangeable」。不要另写怎样写 Verify 何时调用。

## 本页不抄

- 怎样做写 Verify 何时调用、怎样写空扩展、怎样缓存 Process。
- Verify Usage bundled / empty extension still calls / not called for local process。那是不变量 353 / 521 / 522。
- Process 也会在提议者那边叫 / 通常紧跟 Prepare。那是不变量 351。
- VerifyVoteExtensionRequest.hash 表栏描述。那是不变量 422。
