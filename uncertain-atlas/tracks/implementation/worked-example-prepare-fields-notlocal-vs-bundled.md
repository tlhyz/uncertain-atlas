# 例：看见 local_last_commit 是上一高度的预提交带扩展 is not already this-height extension interchangeable / not already H Prepare has extensions interchangeable / not already settled interchangeable

**层次**：实现 / local_last_commit 是上一高度的预提交带扩展 not already this-height extension / not already H Prepare has extensions / not already settled 正式三事（359 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) PrepareProposal Usage。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「local_last_commit 是上一高度的预提交带扩展 not already this-height extension / not already H Prepare has extensions / not already settled 正式三事（359 余量）/ not 846 prepare-fields-notlocal interchangeable / not 359 prepare-fields-vs-same bundled interchangeable」，不是 Prepare 请求字段 bundled（359），也不是到了 H 就已经 Prepare 带了扩展（330），也不是 decided_last_commit 就已经是 local_last_commit（422）。不要另写怎样填 Prepare 请求字段。

## 官方三件事

1. **看见 `local_last_commit` 是上一高度的预提交带扩展 / 看见有上一高的票 这份上一高 is not already 已经是本高度刚签的扩展 interchangeable，也不是已经 Prepare 请求字段 bundled（359） interchangeable / 846 prepare-fields-notlocal interchangeable / 845 prepare-fields-notrun interchangeable / 359 prepare-fields item 1 同一套 interchangeable，也不是已经 local_last_commit 是上一高度的预提交带扩展 not already this-height extension / not already H Prepare has extensions / not already settled 正式三事 bundled（359 item 2 余量） interchangeable / 359 prepare-fields item 2 interchangeable。**  
   官方写：`local_last_commit` 是上一高度的预提交，包括促成上一块决定的那些，以及对应的投票扩展。看见有上一高的票，不是已经是本高度刚签的 *e* interchangeable——本页从 359 item 2 侧钉 not already this-height extension 单句。359 prepare-fields vs same bundled unbundling 在本页 item 2 续。

2. **看见有上一高的票 / 看见带了扩展 / 这份上一高 is not already 已经到了 H 就已经 Prepare 带了扩展 interchangeable / 330 veheight interchangeable，也不是已经 Prepare 请求字段 bundled（359） interchangeable / 846 prepare-fields-notlocal interchangeable / 359 prepare-fields item 3 对上拟议头 interchangeable / 847 prepare-fields-nothash interchangeable，也不是已经 decided_last_commit 就已经是 local_last_commit interchangeable / 422 finreq interchangeable。**  
   官方把带了扩展和已经到了 H 就已经 Prepare 带了扩展分开——359 bundled 第二件事常与 330 混成「看见有上一高的票就已经是本高度刚签的扩展或已经到了 H 带了扩展 interchangeable」，本页钉 not already H Prepare has extensions 单句。

3. **看见有上一高的票 / 看见能用上一高 / 这份上一高 is not already 已经交差 interchangeable，也不是已经 Prepare 请求字段 bundled（359） interchangeable / 846 prepare-fields-notlocal interchangeable / 845 prepare-fields-notrun interchangeable，也不是已经 VoteInfo 就已经是本高度刚签的扩展 interchangeable / 365 voteinfo interchangeable。**  
   官方把能用上一高和已经交差分开。看见能用上一高，不是已经交差 interchangeable。359 prepare-fields vs same bundled unbundling 在本页 item 2 续。

怎样填 Prepare 请求字段、怎样读 `local_last_commit`、怎样对头是规范里的做法，本页不抄。

## 官方为什么这样拆

- **local_last_commit 是上一高度的预提交带扩展 not already this-height extension ≠ 已经是本高度刚签的扩展 interchangeable：** 官方把上一高和本高分开。
- **看见带了扩展 not already H Prepare has extensions ≠ 330 interchangeable：** 官方把带了扩展和已经到了 H 就已经 Prepare 带了扩展分开。
- **看见能用上一高 not already settled ≠ 已经交差 interchangeable：** 官方把能用上一高和已经交差分开；359 prepare-fields vs same bundled unbundling 在本页 item 2 续。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| local_last_commit 是上一高度的预提交带扩展 | 不是已经是本高度刚签的扩展 | 不是到了 H 就已经 Prepare 带了扩展（330） |
| 看见带了扩展 | 不是已经到了 H 就已经 Prepare 带了扩展 | 不是 decided_last_commit 就已经是 local_last_commit（422） |
| 看见能用上一高 | 不是已经交差 | 不是 VoteInfo 就已经是本高度刚签的扩展（365） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 local_last_commit 是上一高度的预提交带扩展 not already this-height extension / not already H Prepare has extensions / not already settled 正式三事（359 余量），必须分开是不是已经是本高度刚签的扩展、是不是已经到了 H 就已经 Prepare 带了扩展、是不是已经交差。可以跳过「看见有上一高的票就已经是本高度刚签的扩展」。不要另写怎样填 Prepare 请求字段。359 prepare-fields vs same bundled unbundling 在本页 item 2 续；续 [`worked-example-prepare-fields-nothash-vs-bundled.md`](worked-example-prepare-fields-nothash-vs-bundled.md)（不变量 847 item 3）。

## 本页不抄

- 怎样填 Prepare 请求字段、怎样读 local_last_commit、怎样对头。
- Prepare 请求字段 bundled。那是不变量 359。
- Prepare 和 Process / Finalize 同一套字段。那是不变量 359 item 1 余量 / 845。
- 到了 H 就已经 Prepare 带了扩展。那是不变量 330。
- decided_last_commit 就已经是 local_last_commit。那是不变量 422。
