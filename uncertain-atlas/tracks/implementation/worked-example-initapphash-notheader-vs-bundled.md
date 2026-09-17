# 例：看见 InitChain 回包 app_hash 是起步应用哈希 is not already header AppHash interchangeable / not already no set interchangeable / not already settled interchangeable

**层次**：实现 / InitChain 回包 app_hash not already header AppHash / not already no set / not already settled 正式三事（392 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) InitChain Response / FinalizeBlock Request / CommitInfo。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「InitChain 回包 app_hash not already header AppHash / not already no set / not already settled 正式三事（392 余量）/ not 755 initapphash-notheader interchangeable / not 392 initapphash-vs-header bundled interchangeable」，不是 InitChain 回包余栏 bundled（392），也不是本头 AppHash 就已经是本高度交差（147），也不是 InitChain Usage 空集合 / 决定参数（495/496/695–700）。不要另写怎样写 InitChain 回包余栏。

## 官方三件事

1. **看见 InitChain 回包 `app_hash` 是起步应用哈希 / 看见回了起步哈希 / InitChain 这份起步根 is not already 已经是本头那份 AppHash interchangeable，也不是已经 InitChain 回包余栏 bundled（392） interchangeable / 755 initapphash-notheader interchangeable / 756 initapphash-notknownhash interchangeable / 392 initapphash item 2 Finalize hash interchangeable，也不是已经 app_hash not already header AppHash / not already no set / not already settled 正式三事 bundled（392 item 1 余量） interchangeable / 392 initapphash item 1 interchangeable。**  
   官方写：`app_hash` 是起步应用哈希。看见回了起步哈希，不是已经是本头那份 AppHash interchangeable——本页从 392 item 1 侧钉 not already header AppHash 单句。392 initapphash vs header bundled unbundling 在本页 item 1 启动。

2. **看见回了起步哈希 / 看见有起步根 / InitChain 这份起步根 is not already 已经没有集合 interchangeable，也不是已经 InitChain 回包余栏 bundled（392） interchangeable / 755 initapphash-notheader interchangeable / 392 initapphash item 3 CommitInfo.round interchangeable / 757 initapphash-notranked interchangeable，也不是已经 InitChain Usage 空集合 / 决定参数 interchangeable / 495 initchainusage / 695–700 interchangeable。**  
   官方把起步应用哈希和已经没有集合分开——392 bundled 第一件事常与 147 / 495 混成「看见回了起步哈希就已经没有集合或已经交差 interchangeable」，本页钉 not already no set 单句。

3. **看见回了起步哈希 / 看见能回 / InitChain 这份起步根 is not already 已经交差 interchangeable / 147 apphash interchangeable，也不是已经 InitChain 回包余栏 bundled（392） interchangeable / 755 initapphash-notheader interchangeable / 756 initapphash-notknownhash interchangeable。**  
   官方把能回起步哈希和已经交差分开。看见能回，不是已经交差 interchangeable。392 initapphash vs header bundled unbundling 在本页 item 1 启动。

怎样写 InitChain 回包余栏、怎样填起步哈希、怎样填提交轮是规范里的做法，本页不抄。

## 官方为什么这样拆

- **app_hash not already header AppHash ≠ 本头 AppHash interchangeable：** 官方把起步应用哈希和本头 AppHash 分开。
- **app_hash not already no set ≠ 已经没有集合 interchangeable：** 官方把有起步根和已经没有集合 / InitChain Usage 分开。
- **app_hash not already settled ≠ 147 interchangeable：** 官方把能回起步哈希和本头 AppHash 就已经是本高度交差分开；392 initapphash vs header bundled unbundling 在本页 item 1 启动。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| InitChain 回包 app_hash 是起步应用哈希 | 不是已经是本头 AppHash | 不是 Finalize 请求 hash（756/392 item 2） |
| 看见回了起步哈希 | 不是已经没有集合（495） | 不是 InitChain 回包余栏 bundled（392） |
| 看见能回 | 不是已经交差（147） | 不是 CommitInfo.round（757/392 item 3） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 InitChain 回包 app_hash not already header AppHash / not already no set / not already settled 正式三事（392 余量），必须分开 app_hash 是不是已经是本头 AppHash、是不是已经没有集合、是不是已经交差 interchangeable / 147。可以跳过「看见回了起步哈希就已经是本头 AppHash」。不要另写怎样写 InitChain 回包余栏。392 initapphash vs header bundled unbundling 在本页 item 1 启动；续 [`worked-example-initapphash-notknownhash-vs-bundled.md`](worked-example-initapphash-notknownhash-vs-bundled.md)（不变量 756 item 2）。

## 本页不抄

- 怎样写 InitChain 回包余栏、怎样填起步哈希、怎样填提交轮。
- InitChain 回包余栏 bundled。那是不变量 392。
- Finalize 请求 hash。那是不变量 392 item 2 余量 / 756。
- CommitInfo.round。那是不变量 392 item 3 余量 / 757。
- 本头 AppHash 就已经是本高度交差。那是不变量 147。
- InitChain Usage 空集合 / 决定参数。那是不变量 495 / 496 / 695–700。
