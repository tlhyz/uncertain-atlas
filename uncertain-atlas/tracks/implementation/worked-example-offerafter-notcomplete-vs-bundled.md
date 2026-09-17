# 例：看见 ApplySnapshotChunk Result ACCEPT 是这块收下了 is not already complete interchangeable / not already this-chunk result interchangeable / not already Offer ACCEPT interchangeable

**层次**：实现 / ApplySnapshotChunk Result ACCEPT not already complete / not this-chunk result / not Offer ACCEPT 正式三事（401 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) OfferSnapshot Usage / ApplySnapshotChunk Result。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「ApplySnapshotChunk Result ACCEPT not already complete / not this-chunk result / not Offer ACCEPT 正式三事（401 余量）/ not 730 offerafter-notcomplete interchangeable / not 401 offeraccept-vs-restored bundled interchangeable」，不是 Offer 收下之后 bundled（401），也不是一块 chunk 收下就已经齐（321）或 Apply 回包 result 就已经是 Offer 的结果（397）或 OfferSnapshot Result ACCEPT（402 / 726）。不要另写怎样写 Offer 收下之后。

## 官方三件事

1. **看见 ApplySnapshotChunk Result `ACCEPT` 是这块收下了 / 看见回了 ACCEPT / Apply ACCEPT 这块收下了 is not already 已经一块 chunk 收下就已经齐 interchangeable / 321 offerrestored interchangeable，也不是已经 Offer 收下之后 bundled（401） interchangeable / 730 offerafter-notcomplete interchangeable / 728 offerafter-notrestored interchangeable / 401 offeraccept item 1 收下之后才去拉装 interchangeable，也不是已经 Apply ACCEPT not already complete / not this-chunk result / not Offer ACCEPT 正式三事 bundled（401 item 3 余量） interchangeable / 401 offeraccept item 3 interchangeable。**  
   官方 Data Types 写：`ACCEPT` 是这块收下了。看见回了 ACCEPT，不是已经一块 chunk 收下就已经齐 interchangeable——本页从 401 item 3 侧钉 not already complete 单句。401 offeraccept vs restored bundled unbundling 在本页 item 3 完成。

2. **看见回了 ACCEPT / 看见能收这块 / Apply ACCEPT 这块收下了 is not already 已经是 ApplySnapshotChunk 回包 result 那份装这块的结果 interchangeable / 397 applyresult interchangeable，也不是已经 Offer 收下之后 bundled（401） interchangeable / 730 offerafter-notcomplete interchangeable / 401 offeraccept item 2 回包拒 interchangeable / 729 offerafter-notabort interchangeable。**  
   官方把这块收下了和回包 result 就已经是 Offer 的结果分开——401 bundled 第三件事常与 397 混成「看见回了 ACCEPT 就已经是装这块的结果 interchangeable」，本页钉 not this-chunk result 单句。

3. **看见回了 ACCEPT / 看见 Usage 这句 / Apply ACCEPT 这块收下了 is not already 已经 OfferSnapshot Result `ACCEPT` 那种收下这份、开始装块 interchangeable / 402 / 726 offerunk-notrestored interchangeable，也不是已经 Offer 收下之后 bundled（401） interchangeable / 730 offerafter-notcomplete interchangeable / 728 offerafter-notrestored interchangeable。**  
   官方把 Apply ACCEPT 这块收下了和 Offer ACCEPT 收下这份、开始装块分开。看见能收这块，不是已经 402 / 726 interchangeable。401 offeraccept vs restored bundled unbundling 在本页 item 3 完成。

怎样写 Offer 收下之后、怎样在装这块时拒、怎样挑 ACCEPT 是规范里的做法，本页不抄。

## 官方为什么这样拆

- **Apply ACCEPT not already complete ≠ 321 interchangeable：** 官方把这块收下了和一块 chunk 收下就已经齐分开。
- **Apply ACCEPT not this-chunk result ≠ 397 interchangeable：** 官方把这块收下了和回包 result 就已经是 Offer 的结果分开。
- **Apply ACCEPT not Offer ACCEPT ≠ 402 / 726 interchangeable：** 官方把 Apply ACCEPT 和 Offer ACCEPT 开始装块分开；401 offeraccept vs restored bundled unbundling 在本页 item 3 完成。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| ApplySnapshotChunk Result ACCEPT 是这块收下了 | 不是已经齐（321） | 不是收下之后才去拉装（728/401 item 1） |
| 看见回了 ACCEPT | 不是已经是装这块的结果（397） | 不是 Offer 收下之后 bundled（401） |
| 看见能收这块 | 不是已经 Offer ACCEPT（402 / 726） | 不是回包拒还要再收 Offer（729/401 item 2） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 ApplySnapshotChunk Result ACCEPT not already complete / not this-chunk result / not Offer ACCEPT 正式三事（401 余量），必须分开 Apply ACCEPT 是不是已经齐 interchangeable / 321、是不是已经是装这块的结果 interchangeable / 397、是不是已经 Offer ACCEPT interchangeable / 402 / 726。可以跳过「看见回了 ACCEPT 就已经齐」。不要另写怎样写 Offer 收下之后。401 offeraccept vs restored bundled unbundling 在本页 item 3 完成。

## 本页不抄

- 怎样写 Offer 收下之后、怎样在装这块时拒、怎样挑 ACCEPT。
- Offer 收下之后 bundled。那是不变量 401。
- Offer 收下之后才去拉块并装。那是不变量 401 item 1 余量 / 728。
- 在装这块的回包里拒掉这份、还要再收 Offer。那是不变量 401 item 2 余量 / 729。
- 一块 chunk 收下就已经齐。那是不变量 321。
- ApplySnapshotChunk 回包 result 就已经是 Offer 的结果。那是不变量 397。
- OfferSnapshot Result ACCEPT。那是不变量 402 / 726。
