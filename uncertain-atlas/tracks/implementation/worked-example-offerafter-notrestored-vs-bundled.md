# 例：看见 Offer 收下之后才去拉块并装 is not already Offer 收下就已经装完 interchangeable / not already complete interchangeable / not already settled interchangeable

**层次**：实现 / Offer 收下之后才去拉块并装 not already restored / not already complete / not already settled 正式三事（401 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) OfferSnapshot Usage / ApplySnapshotChunk Result。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「Offer 收下之后才去拉块并装 not already restored / not already complete / not already settled 正式三事（401 余量）/ not 728 offerafter-notrestored interchangeable / not 401 offeraccept-vs-restored bundled interchangeable」，不是 Offer 收下之后 bundled（401），也不是 Offer 收下就已经装完（321）或 OfferSnapshot Usage upon accepting retrieve and apply（499 / 648）。不要另写怎样写 Offer 收下之后。

## 官方三件事

1. **看见 Offer 收下之后引擎才去拉块并经 ApplySnapshotChunk 装 / 看见收下了 / 收下之后才去拉装 is not already 已经 Offer 收下就已经装完 interchangeable / 321 offerrestored interchangeable，也不是已经 Offer 收下之后 bundled（401） interchangeable / 728 offerafter-notrestored interchangeable / 729 offerafter-notabort interchangeable / 401 offeraccept item 2 回包拒 interchangeable，也不是已经 Offer 收下之后才去拉块并装 not already restored / not already complete / not already settled 正式三事 bundled（401 item 1 余量） interchangeable / 401 offeraccept item 1 interchangeable。**  
   官方 Usage 写：收下之后，CometBFT 才去拉块，并经 `ApplySnapshotChunk` 装。看见收下了，不是已经 Offer 收下就已经装完 interchangeable——本页从 401 item 1 侧钉 not already restored 单句。401 offeraccept vs restored bundled unbundling 在本页 item 1 启动。

2. **看见收下了 / 看见在拉 / 收下之后才去拉装 is not already 已经一块 chunk 收下就已经齐 interchangeable / 321 offerrestored interchangeable，也不是已经 Offer 收下之后 bundled（401） interchangeable / 728 offerafter-notrestored interchangeable / 401 offeraccept item 3 Apply ACCEPT interchangeable / 730 offerafter-notcomplete interchangeable。**  
   官方把收下之后才去拉块和已经齐分开——401 bundled 第一件事常与「看见收下了就已经齐 interchangeable」糊成一句，本页钉 not already complete 单句。

3. **看见收下了 / 看见 Usage 这句 / 收下之后才去拉装 is not already 已经交差 interchangeable，也不是已经 Offer 收下之后 bundled（401） interchangeable / 728 offerafter-notrestored interchangeable / 648 offersnapusage-notrestored interchangeable / 499 Usage upon accepting interchangeable。**  
   官方把收下之后才去拉块并装和已经交差分开。看见能收，不是已经交差 interchangeable，也不是已经 499 / 648 Usage upon accepting retrieve and apply interchangeable。401 offeraccept vs restored bundled unbundling 在本页 item 1 启动。

怎样写 Offer 收下之后、怎样在装这块时拒、怎样挑 ACCEPT 是规范里的做法，本页不抄。

## 官方为什么这样拆

- **收下之后才去拉装 not already restored ≠ 321 interchangeable：** 官方把收下之后才去拉块和已经装完分开。
- **收下之后才去拉装 not already complete ≠ 321 interchangeable：** 官方把收下之后才去拉块和一块 chunk 收下就已经齐分开。
- **收下之后才去拉装 not already settled ≠ 已经交差 / 499 / 648 interchangeable：** 官方把能收和已经交差、499 Usage upon accepting 分开；401 offeraccept vs restored bundled unbundling 在本页 item 1 启动。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| Offer 收下之后才去拉块并装 | 不是已经装完（321） | 不是回包拒还要再收 Offer（729/401 item 2） |
| 看见收下了 | 不是已经一块 chunk 齐了（321） | 不是 Offer 收下之后 bundled（401） |
| 看见在拉 | 不是已经交差 / 499 / 648 | 不是 Apply ACCEPT 这块收下了（730/401 item 3） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Offer 收下之后才去拉块并装 not already restored / not already complete / not already settled 正式三事（401 余量），必须分开收下之后才去拉装是不是已经装完 interchangeable / 321、是不是已经齐 interchangeable / 321、是不是已经交差 / 499 / 648。可以跳过「看见收下了就已经装完」。不要另写怎样写 Offer 收下之后。401 offeraccept vs restored bundled unbundling 在本页 item 1 启动；续 [`worked-example-offerafter-notabort-vs-bundled.md`](worked-example-offerafter-notabort-vs-bundled.md)（不变量 729 item 2）。

## 本页不抄

- 怎样写 Offer 收下之后、怎样在装这块时拒、怎样挑 ACCEPT。
- Offer 收下之后 bundled。那是不变量 401。
- 在装这块的回包里拒掉这份、还要再收 Offer。那是不变量 401 item 2 余量 / 729。
- ApplySnapshotChunk Result ACCEPT 是这块收下了。那是不变量 401 item 3 余量 / 730。
- Offer 收下就已经装完。那是不变量 321。
- OfferSnapshot Usage upon accepting retrieve and apply。那是不变量 499 / 648。
