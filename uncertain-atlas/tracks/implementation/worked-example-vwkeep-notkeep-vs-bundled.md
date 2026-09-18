# 例：看见ACCEPT 会把票和扩展留在内部结构不是已经 Verify When 正式流程 bundled；看见keep vote and extension不是已经写进 last_commit；看见ACCEPT 会把票和扩展留在内部结构不是已经 +2/3 之后才进来的扩展写进了 commit info

**层次**：实现 / 规范对象。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) VerifyVoteExtension When step 4。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「VerifyKeep ACCEPT-keep not already Verify-When / not already last_commit / not already late-verified 正式三事（517 余量）/ not 1334 vwkeep-notkeep interchangeable / not 517 verifywhen-keepdiscard-vs-bundled bundled interchangeable」，不是 verifywhen keepdiscard vs bundled bundled（517），也不是已经 Verify When 正式流程（435），也不是已经 迟到扩展（352）。不要另写 怎样写 ExtendedCommitInfo、怎样在 Prepare 填 ExtendedCommitInfo、怎样写 last_commit。

## 官方三件事

1. **看见ACCEPT 会把票和扩展留在内部结构 / 看见ACCEPT 会把票和扩展留在内部结构 这份对象 is not already 已经 Verify When 正式流程 bundled interchangeable，也不是已经 verifywhen keepdiscard vs bundled bundled（517） interchangeable / 1334 vwkeep-notkeep interchangeable / 1335 vwkeep-notpop interchangeable，也不是已经 VerifyKeep ACCEPT-keep not already Verify-When / not already last_commit / not already late-verified 正式三事 bundled（517 item 1 余量） interchangeable / 517 vwkeep item 1 interchangeable。**  
   官方把ACCEPT 会把票和扩展留在内部结构和已经 Verify When 正式流程 bundled写成两件。看见ACCEPT 会把票和扩展留在内部结构，不是已经 Verify When 正式流程 bundled。

2. **看见keep vote and extension / 看见ACCEPT 会把票和扩展留在内部结构 / 这份对象 is not already 已经写进 last_commit interchangeable，也不是已经 verifywhen keepdiscard vs bundled bundled（517） interchangeable / 1334 vwkeep-notkeep interchangeable / 1336 vwkeep-notrej interchangeable，也不是已经 Verify When 正式流程 interchangeable / 435 Verify When 正式流程 interchangeable。**  
   官方把keep vote and extension和已经写进 last_commit写成两件。看见keep vote and extension，不是已经写进 last_commit。

3. **看见ACCEPT 会把票和扩展留在内部结构 / 看见keep vote and extension / 这份对象 is not already 已经 +2/3 之后才进来的扩展写进了 commit info interchangeable，也不是已经 verifywhen keepdiscard vs bundled bundled（517） interchangeable / 1334 vwkeep-notkeep interchangeable / 1335 vwkeep-notpop interchangeable，也不是已经 迟到扩展 interchangeable / 352 迟到扩展 interchangeable。**  
   官方把ACCEPT 会把票和扩展留在内部结构和已经 +2/3 之后才进来的扩展写进了 commit info写成两件。看见ACCEPT 会把票和扩展留在内部结构，不是已经 +2/3 之后才进来的扩展写进了 commit info。

栈怎么写、分隔符、例串是规范里的取值，本页不抄。不要另写 怎样写 ExtendedCommitInfo、怎样在 Prepare 填 ExtendedCommitInfo、怎样写 last_commit。

## 官方为什么这样拆

- **ACCEPT keep for h+1 Prepare 不是 Verify When 正式流程 bundled interchangeable：官方把 step 4 ACCEPT keep 单句和 steps 1–3 bundled 分开。**
- **看见留在内部结构 不是已经写进 last_commit：435 第三件事 bundled 常被写成 ACCEPT 就已经写进 last_commit，本页钉 keep 在内部结构、给 h+1 Prepare 用。**
- **看见收下了 不是已经迟到扩展写进了 commit info：352 钉迟到扩展 MAY 路径，本页钉正常 When step 4 ACCEPT keep。**

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 已经 Verify When 正式流程 bundled | 不是已经 Verify When 正式流程 bundled | 不是已经Verify When 正式流程（435） |
| 已经写进 last_commit | 不是已经写进 last_commit | 不是已经迟到扩展（352） |
| 已经 +2/3 之后才进来的扩展写进了 commit info | 不是已经 +2/3 之后才进来的扩展写进了 commit info | 不是已经1335 vwkeep-notpop |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 VerifyKeep ACCEPT-keep not already Verify-When / not already last_commit / not already late-verified 正式三事（517 余量），必须分开是不是已经 Verify When 正式流程 bundled、是不是已经写进 last_commit、是不是已经 +2/3 之后才进来的扩展写进了 commit info。可以跳过「看见 ACCEPT 就已经写进 last_commit interchangeable、已经 Verify 过迟到扩展 interchangeable」。不要另写 怎样写 ExtendedCommitInfo、怎样在 Prepare 填 ExtendedCommitInfo、怎样写 last_commit。517 VerifyVoteExtension When keepdiscard bundled unbundling 在本页 item 1 启动；续 [`worked-example-vwkeep-notpop-vs-bundled.md`](worked-example-vwkeep-notpop-vs-bundled.md)（不变量 1335 item 2）。

## 本页不抄

- 怎样做写 ExtendedCommitInfo、怎样在 Prepare 填 ExtendedCommitInfo、怎样写 last_commit。
- 怎样写 ExtendedCommitInfo、怎样在 Prepare 填 ExtendedCommitInfo、怎样写 last_commit。
