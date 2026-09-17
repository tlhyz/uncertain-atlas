# 例：看见 InitChain 请求 chain_id 是链的 ID is not already have ChainID interchangeable / not already full history interchangeable / not already settled interchangeable

**层次**：实现 / InitChain 请求 chain_id not already have ChainID / not already full history / not already settled 正式三事（387 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) InitChain Request。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「InitChain 请求 chain_id not already have ChainID / not already full history / not already settled 正式三事（387 余量）/ not 768 inittime-notchainid interchangeable / not 387 inittime-vs-genesis bundled interchangeable」，不是 InitChain 请求 bundled（387），也不是快照装完就已经有了 ChainID（323）。不要另写怎样写 InitChain 请求。

## 官方三件事

1. **看见 InitChain 请求 `chain_id` 是链的 ID / 看见填了 chain_id / InitChain 这份链 ID is not already 已经有了快照装完后凑齐的 ChainID interchangeable / 323 snapid interchangeable，也不是已经 InitChain 请求 bundled（387） interchangeable / 768 inittime-notchainid interchangeable / 767 inittime-notgenesis interchangeable / 387 inittime item 1 time interchangeable，也不是已经 chain_id not already have ChainID / not already full history / not already settled 正式三事 bundled（387 item 2 余量） interchangeable / 387 inittime item 2 interchangeable。**  
   官方写：`chain_id` 是这条链的 ID。看见填了 chain_id，不是已经有了快照装完后凑齐的 ChainID interchangeable——本页从 387 item 2 侧钉 not already have ChainID 单句。387 inittime vs genesis bundled unbundling 在本页 item 2 续。

2. **看见填了 chain_id / 看见有标识 / InitChain 这份链 ID is not already 已经有从创世的完整历史 interchangeable / 323 snapid interchangeable，也不是已经 InitChain 请求 bundled（387） interchangeable / 768 inittime-notchainid interchangeable / 387 inittime item 3 initial_height interchangeable / 769 inittime-notskip interchangeable。**  
   官方把请求里的链 ID 和已经有完整历史分开——387 bundled 第二件事常与 323 混成「看见填了 chain_id 就已经有了 ChainID 或已经有完整历史 interchangeable」，本页钉 not already full history 单句。

3. **看见填了 chain_id / 看见能回 / InitChain 这份链 ID is not already 已经交差 interchangeable，也不是已经 InitChain 请求 bundled（387） interchangeable / 768 inittime-notchainid interchangeable / 767 inittime-notgenesis interchangeable。**  
   官方把能填 InitChain 请求 chain_id 和已经交差分开。看见能回，不是已经交差 interchangeable。387 inittime vs genesis bundled unbundling 在本页 item 2 续。

怎样写 InitChain 请求、怎样填时间、怎样选起步高是规范里的做法，本页不抄。

## 官方为什么这样拆

- **chain_id not already have ChainID ≠ 323 interchangeable：** 官方把请求里的链 ID 和快照装完后凑齐的 ChainID 分开。
- **chain_id not already full history ≠ 323 interchangeable：** 官方把有标识和已经有从创世的完整历史分开。
- **chain_id not already settled ≠ 已经交差 interchangeable：** 官方把能填 chain_id 和已经交差分开；387 inittime vs genesis bundled unbundling 在本页 item 2 续。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| InitChain 请求 chain_id 是链的 ID | 不是已经有了 ChainID（323） | 不是 InitChain 请求 time（767/387 item 1） |
| 看见填了 chain_id | 不是已经有完整历史（323） | 不是 InitChain 请求 bundled（387） |
| 看见能回 | 不是已经交差 | 不是 InitChain 请求 initial_height（769/387 item 3） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 InitChain 请求 chain_id not already have ChainID / not already full history / not already settled 正式三事（387 余量），必须分开 chain_id 是不是已经有了 ChainID interchangeable / 323、是不是已经有完整历史、是不是已经交差。可以跳过「看见填了 chain_id 就已经有了 ChainID」。不要另写怎样写 InitChain 请求。387 inittime vs genesis bundled unbundling 在本页 item 2 续；完成 [`worked-example-inittime-notskip-vs-bundled.md`](worked-example-inittime-notskip-vs-bundled.md)（不变量 769 item 3）。

## 本页不抄

- 怎样写 InitChain 请求、怎样填时间、怎样选起步高。
- InitChain 请求 bundled。那是不变量 387。
- InitChain 请求 time。那是不变量 387 item 1 余量 / 767。
- InitChain 请求 initial_height。那是不变量 387 item 3 余量 / 769。
- 快照装完就已经有了 ChainID。那是不变量 323。
