# 例：看见提案收了交易 is not already deleted interchangeable / not already in-block interchangeable / not already processed interchangeable

**层次**：共识 / 提案收了 not already deleted / not already in-block / not already processed 正式三事（301 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [Mempool](https://github.com/cometbft/cometbft/blob/main/spec/mempool/mempool.md) mempool / proposed vs removed。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)、[L9.2](../../courses/level-09-systems/L09-M02-mempool.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行。本页是「提案收了 not already deleted / not already in-block / not already processed 正式三事（301 余量）/ not 992 proposed-notdel interchangeable / not 301 proposed-vs-removed bundled interchangeable」，不是内存池交接 bundled（301），也不是四门已经结算（33），也不是先装证据就已经装满交易（299/989）。不要另写怎样加锁、怎样 flush、怎样再验。

## 官方三件事

1. **看见共识从池里收了一串交易 / 看见这些交易进了提案 这份交接 is not already 已经从池里删掉 interchangeable，也不是已经内存池交接 bundled（301） interchangeable / 992 proposed-notdel interchangeable / 993 proposed-notrecheck interchangeable / 301 proposed item 2 commit 后再验 interchangeable，也不是已经提案收了 not already deleted / not already in-block / not already processed 正式三事 bundled（301 item 1 余量） interchangeable / 301 proposed item 1 interchangeable。**  
   官方写：共识向内存池要一串交易来造提案。这时这些交易还不从池里删。因为这块只是提案，还没决定。看见提案带了这些交易，不是池里已经没有它们 interchangeable——本页从 301 item 1 侧钉 not already deleted 单句。301 proposed vs removed bundled unbundling 在本页 item 1 启动。

2. **看见引擎按上限收了前缀 / 看见提案收了 / 这份交接 is not already 已经进块 interchangeable，也不是已经内存池交接 bundled（301） interchangeable / 992 proposed-notdel interchangeable / 301 proposed item 3 CheckTx 绿 interchangeable / 994 proposed-notforever interchangeable，也不是已经四门已经结算 interchangeable / 33 four-gates interchangeable。**  
   官方把按上限收了前缀和这些交易已经进块分开。看见收了前缀，不是已经进块 interchangeable。本页钉 not already in-block 单句。

3. **看见收了 / 看见提案带了这些交易 / 这份交接 is not already 已经过了 Process interchangeable，也不是已经内存池交接 bundled（301） interchangeable / 992 proposed-notdel interchangeable / 993 proposed-notrecheck interchangeable，也不是已经先装证据就已经装满交易 interchangeable / 299/989 evidreap-notfull interchangeable。**  
   官方把收了和已经过了 Process 分开。看见收了，不是已经过了 Process interchangeable。301 proposed vs removed bundled unbundling 在本页 item 1 启动。

实现名单、加锁、flush、再验次数是规范里的做法或取值，本页不抄。

## 官方为什么这样拆

- **提案收了 not already deleted ≠ 已经从池里删掉 interchangeable：** 官方把还没决定写成还不能从池里拿走。
- **看见收了前缀 not already in-block ≠ 已经进块 interchangeable：** 官方把按上限收了前缀和这些交易已经进块分开。
- **看见收了 not already processed ≠ 已经过了 Process interchangeable：** 官方把收了和已经过了 Process 分开；301 proposed vs removed bundled unbundling 在本页 item 1 启动。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 提案收了交易 | 不是已经从池里删掉 | 不是四门已经结算（33） |
| 看见收了前缀 | 不是已经进块 | 不是先装证据就已经装满交易（299/989） |
| 看见收了 | 不是已经过了 Process | 不是 commit 后就已经不用再验（993） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看提案收了 not already deleted / not already in-block / not already processed 正式三事（301 余量），必须分开是不是已经从池里删掉、是不是已经进块、是不是已经过了 Process。可以跳过「看见提案收了就已经从池里拿走」。不要另写怎样加锁、怎样 flush、怎样再验。301 proposed vs removed bundled unbundling 在本页 item 1 启动；续 [`worked-example-proposed-notrecheck-vs-bundled.md`](worked-example-proposed-notrecheck-vs-bundled.md)（不变量 993 item 2）。

## 本页不抄

- 实现名单、加锁、flush、再验次数。
- 内存池交接 bundled。那是不变量 301。
- 四门已经结算。那是不变量 33。
- 先装证据就已经装满交易。那是不变量 299/989。
