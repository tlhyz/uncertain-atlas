# 例：看见 MaxBytes 写成 -1 is not already unlimited interchangeable / not already app-free interchangeable / not already settled interchangeable

**层次**：共识 / MaxBytes 写成 -1 not already unlimited / not already app-free / not already settled 正式三事（299 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [Creating a proposal](https://github.com/cometbft/cometbft/blob/main/spec/consensus/creating-proposal.md) Consensus Protocol / evidence before txs。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行。本页是「MaxBytes 写成 -1 not already unlimited / not already app-free / not already settled 正式三事（299 余量）/ not 991 evidreap-notunlim interchangeable / not 299 evidence-vs-reap bundled interchangeable」，不是造提案 bundled（299），也不是 -1 就按 100 MB 验就已经没有上限（337），也不是证据窗已经盖住解绑（46）。不要另写怎样算扣减或怎样从池里收割。

## 官方三件事

1. **看见 MaxBytes 写成 -1 / 看见把未处理交易全给了 Prepare 这份交给 is not already 已经没有上限 interchangeable，也不是已经造提案 bundled（299） interchangeable / 991 evidreap-notunlim interchangeable / 989 evidreap-notfull interchangeable / 990 evidreap-notsame interchangeable / 299 evidence item 1 先装证据 interchangeable，也不是已经 MaxBytes 写成 -1 not already unlimited / not already app-free / not already settled 正式三事 bundled（299 item 3 余量） interchangeable / 299 evidence item 3 interchangeable。**  
   官方写：若块上限写成 -1，引擎会把内存池里未处理的交易都交给 PrepareProposal。应用回的列表仍不得超过这次请求里的 MaxTxBytes。看见写成 -1，不是已经没有上限 interchangeable——本页从 299 item 3 侧钉 not already unlimited 单句。299 evidence vs reap bundled unbundling 在本页 item 3 完成。

2. **看见整池都给了应用 / 看见写成 -1 / 这份交给 is not already 已经应用可以随便回 interchangeable，也不是已经造提案 bundled（299） interchangeable / 991 evidreap-notunlim interchangeable / 299 evidence item 2 两条上限 interchangeable / 990 evidreap-notsame interchangeable，也不是已经 -1 就按 100 MB 验就已经没有上限 interchangeable / 337 maxbytes-cap interchangeable。**  
   官方把整池都给了应用和应用已经可以随便回分开。看见整池都给了应用，不是应用已经可以随便回 interchangeable。本页钉 not already app-free 单句。

3. **看见回了列表 / 看见写成 -1 / 这份交给 is not already 已经交差 interchangeable，也不是已经造提案 bundled（299） interchangeable / 991 evidreap-notunlim interchangeable / 989 evidreap-notfull interchangeable，也不是已经证据窗已经盖住解绑 interchangeable / 46 evidence window interchangeable。**  
   官方把回了列表和已经过了 Process 分开。看见回了列表，不是已经交差 interchangeable。299 evidence vs reap bundled unbundling 在本页 item 3 完成。

扣减公式、整块体积取值、怎样收割是规范里的做法，本页不抄。

## 官方为什么这样拆

- **MaxBytes 写成 -1 not already unlimited ≠ 已经没有上限 interchangeable：** 官方把整池都给 Prepare 和应用仍不得超过 MaxTxBytes 写成两件事。
- **看见整池都给了应用 not already app-free ≠ 已经可以随便回 interchangeable：** 官方把整池都给了应用和应用已经可以随便回分开。
- **看见回了列表 not already settled ≠ 已经交差 interchangeable：** 官方把回了列表和已经过了 Process 分开；299 evidence vs reap bundled unbundling 在本页 item 3 完成。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| MaxBytes 写成 -1 | 不是已经没有上限 | 不是 -1 就按 100 MB 验就已经没有上限（337） |
| 看见整池都给了应用 | 不是应用已经可以随便回 | 不是证据窗已经盖住解绑（46） |
| 看见回了列表 | 不是已经交差 | 不是先装证据就已经装满交易（989） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 MaxBytes 写成 -1 not already unlimited / not already app-free / not already settled 正式三事（299 余量），必须分开是不是已经没有上限、是不是应用已经可以随便回、是不是已经交差。可以跳过「看见先装证据就已经装满交易」。不要另写怎样算扣减或怎样从池里收割。299 evidence vs reap bundled unbundling 在本页 item 3 完成。

## 本页不抄

- 扣减公式、整块体积取值、protobuf 开销数字。
- 造提案 bundled。那是不变量 299。
- -1 就按 100 MB 验就已经没有上限。那是不变量 337。
- 证据窗已经盖住解绑。那是不变量 46。
