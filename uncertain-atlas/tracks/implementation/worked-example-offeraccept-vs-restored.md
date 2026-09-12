# 例：看见 Offer 收下之后才去拉块并装不是已经装完；看见在装这块的回包里拒掉这份、还要再收 Offer 不是已经中止；看见 ApplySnapshotChunk Result ACCEPT 是这块收下了不是已经齐

**层次**：实现 / Offer 收下之后。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) OfferSnapshot Usage / ApplySnapshotChunk Result。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5。本页是「Offer 收下之后才去拉块并装不是已经装完 / 在装这块的回包里拒掉这份、还要再收 Offer 不是已经中止 / ApplySnapshotChunk Result ACCEPT 是这块收下了不是已经齐」，不是 Offer 收下就已经装完，也不是 OfferSnapshot Result ABORT 就已经中止。不要另写怎样写 Offer 收下之后。

## 官方三件事

规范把 Offer 收下之后才去拉块并装、在装这块的回包里也能拒掉这份、还要准备再收 Offer、ApplySnapshotChunk Result `ACCEPT` 是这块收下了写成三件独立的实现事，不是「看见收下了就已经装完、已经中止、已经齐」一件事：

1. **看见 Offer 收下之后引擎才去拉块并经 ApplySnapshotChunk 装 / 看见收下了 不是已经装完，也不是已经齐。**  
   官方写：收下之后，CometBFT 才去拉块，并经 `ApplySnapshotChunk` 装。看见收下了，不是已经 Offer 收下就已经装完。看见在拉，不是已经齐。看见能收，不是已经交差。
2. **看见在装这块的回包里也能拒掉这份、还要准备再收 Offer / 看见在装这块时拒了 不是已经中止，也不是已经是拒掉这份。**  
   官方写：应用也可以在装这块的回包里拒掉这份；这时还要准备再收 `OfferSnapshot`。看见在装这块时拒了，不是已经 OfferSnapshot Result `ABORT` 那种中止装回、不再试别份。看见还能再收 Offer，不是已经是 ApplySnapshotChunk Result `REJECT_SNAPSHOT` 那种拒掉这份。看见能回，不是已经交差。
3. **看见 ApplySnapshotChunk Result `ACCEPT` 是这块收下了 / 看见回了 ACCEPT 不是已经齐，也不是已经是装这块的结果。**  
   官方写：`ACCEPT` 是这块收下了。看见回了 ACCEPT，不是已经一块 chunk 收下就已经齐。看见能回，不是已经是 ApplySnapshotChunk 回包 result 那份装这块的结果。看见能收这块，不是已经交差。

怎样写 Offer 收下之后、怎样在装这块时拒、怎样挑 ACCEPT 是规范里的做法，本页不抄。Offer 收下就已经装完是不变量 321，本页不抄。

## 官方为什么这样拆

- **Offer 收下之后才去拉块并装 ≠ 已经装完：** 官方把收下之后才去拉块和已经装完分开。
- **在装这块的回包里拒掉这份、还要再收 Offer ≠ 已经中止：** 官方把还能再收 Offer 和中止装回、不再试别份分开。
- **ApplySnapshotChunk Result ACCEPT 是这块收下了 ≠ 已经齐：** 官方把这块收下了和一块 chunk 收下就已经齐分开。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| Offer 收下之后才去拉块并装 | 不是已经装完 | 不是 Offer 收下就已经装完（321） |
| 在装这块的回包里拒掉这份、还要再收 Offer | 不是已经中止 | 不是 OfferSnapshot Result ABORT 就已经中止（400） |
| ApplySnapshotChunk Result ACCEPT 是这块收下了 | 不是已经齐 | 不是 ApplySnapshotChunk 回包 result 就已经是 Offer 的结果（397） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看「看见收下了就已经装完、已经中止、已经齐」，必须分开 Offer 收下之后才去拉块并装是不是已经装完、在装这块的回包里拒掉这份、还要再收 Offer 是不是已经中止、ApplySnapshotChunk Result ACCEPT 是这块收下了是不是已经齐。可以跳过「看见收下了就已经装完」。不要另写怎样写 Offer 收下之后。

## 本页不抄

- 怎样写 Offer 收下之后、怎样在装这块时拒、怎样挑 ACCEPT。
- Offer 收下就已经装完。那是不变量 321。
- OfferSnapshot Result ABORT 就已经中止。那是不变量 400。
- ApplySnapshotChunk 回包 result 就已经是 Offer 的结果。那是不变量 397。
