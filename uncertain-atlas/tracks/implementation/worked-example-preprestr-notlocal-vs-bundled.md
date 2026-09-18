# 例：看见 PrepareProposalRequest.local_last_commit is not already proposed interchangeable / not already last-ext interchangeable / not already settled interchangeable

**层次**：实现 / PrepareProposalRequest.local_last_commit not already proposed / not already last-ext / not already settled 正式三事（424 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) PrepareProposal Request。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「PrepareProposalRequest.local_last_commit not already proposed / not already last-ext / not already settled 正式三事（424 余量）/ not 1049 preprestr-notlocal interchangeable / not 424 prepreqrest-vs-procreq bundled interchangeable」，不是 Prepare 请求余栏 bundled（424），也不是 ProcessProposalRequest.proposed_last_commit 就已经交差 local_last_commit（420），也不是 local_last_commit 是上一高度的预提交带扩展就已经是本高度刚签的扩展（359）。不要另写怎样写 Prepare 请求余栏。

## 官方三件事

1. **看见 PrepareProposalRequest.local_last_commit 是从本进程 CometBFT 数据结构拿到的上一份提交信息 / 看见填了 local_last_commit 这份栏 is not already 已经交差 proposed_last_commit interchangeable，也不是已经 Prepare 请求余栏 bundled（424） interchangeable / 1049 preprestr-notlocal interchangeable / 1050 preprestr-notts interchangeable / 424 prepreqrest item 2 time interchangeable，也不是已经 PrepareProposalRequest.local_last_commit not already proposed / not already last-ext / not already settled 正式三事 bundled（424 item 1 余量） interchangeable / 424 prepreqrest item 1 interchangeable。**  
   官方写：local_last_commit 是上一份提交信息，从本进程 CometBFT 数据结构拿到。看见填了 local_last_commit，不是已经 ProcessProposalRequest.proposed_last_commit 那种已经交差 local_last_commit interchangeable——本页从 424 item 1 侧钉 not already proposed 单句。424 prepreqrest vs procreq bundled unbundling 在本页 item 1 启动。

2. **看见从本进程拿到 / 看见填了 local_last_commit / 这份栏 is not already 已经是本高度刚签的扩展 interchangeable，也不是已经 Prepare 请求余栏 bundled（424） interchangeable / 1049 preprestr-notlocal interchangeable / 424 prepreqrest item 3 misbehavior interchangeable / 1051 preprestr-notpunish interchangeable，也不是已经 local_last_commit 是上一高度的预提交带扩展就已经是本高度刚签的扩展 interchangeable / 359 samefields interchangeable。**  
   官方把从本进程拿到和已经是本高度刚签的扩展分开。看见从本进程拿到，不是已经是本高度刚签的扩展 interchangeable。本页钉 not already last-ext 单句。

3. **看见能指上一份提交 / 看见填了 local_last_commit / 这份栏 is not already 已经交差 interchangeable，也不是已经 Prepare 请求余栏 bundled（424） interchangeable / 1049 preprestr-notlocal interchangeable / 1050 preprestr-notts interchangeable，也不是已经 ProcessProposalRequest.proposed_last_commit 就已经交差 local_last_commit interchangeable / 420 procrestr interchangeable。**  
   官方把能指上一份提交和已经交差分开。看见能指上一份提交，不是已经交差 interchangeable。424 prepreqrest vs procreq bundled unbundling 在本页 item 1 启动。

怎样写 Prepare 请求余栏、怎样填 local_last_commit、怎样填 time 是规范里的做法，本页不抄。

## 官方为什么这样拆

- **PrepareProposalRequest.local_last_commit not already proposed ≠ 已经交差 proposed_last_commit interchangeable：** 官方把从本进程拿到的上一份提交和已经交差 proposed_last_commit 分开。
- **看见从本进程拿到 not already last-ext ≠ 已经是本高度刚签的扩展 interchangeable：** 官方把从本进程拿到和已经是本高度刚签的扩展分开。
- **看见能指上一份提交 not already settled ≠ 已经交差 interchangeable：** 官方把能指上一份提交和已经交差分开；424 prepreqrest vs procreq bundled unbundling 在本页 item 1 启动。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| PrepareProposalRequest.local_last_commit 是从本进程 CometBFT 数据结构拿到的上一份提交信息 | 不是已经交差 proposed_last_commit | 不是 ProcessProposalRequest.proposed_last_commit 就已经交差 local_last_commit（420） |
| 看见从本进程拿到 | 不是已经是本高度刚签的扩展 | 不是 local_last_commit 是上一高度的预提交带扩展就已经是本高度刚签的扩展（359） |
| 看见能指上一份提交 | 不是已经交差 | 不是 time 就已经对上了拟议块头（1050） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 PrepareProposalRequest.local_last_commit not already proposed / not already last-ext / not already settled 正式三事（424 余量），必须分开是不是已经交差 proposed_last_commit、是不是已经是本高度刚签的扩展、是不是已经交差。可以跳过「看见填了 Prepare 请求余栏就已经交差 proposed_last_commit」。不要另写怎样写 Prepare 请求余栏。424 prepreqrest vs procreq bundled unbundling 在本页 item 1 启动；续 [`worked-example-preprestr-notts-vs-bundled.md`](worked-example-preprestr-notts-vs-bundled.md)（不变量 1050 item 2）。

## 本页不抄

- 怎样写 Prepare 请求余栏、怎样填 local_last_commit、怎样填 time。
- Prepare 请求余栏 bundled。那是不变量 424。
- ProcessProposalRequest.proposed_last_commit 就已经交差 local_last_commit。那是不变量 420。
- local_last_commit 是上一高度的预提交带扩展就已经是本高度刚签的扩展。那是不变量 359。
