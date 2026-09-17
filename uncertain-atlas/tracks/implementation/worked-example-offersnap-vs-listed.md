# 例：看见 OfferSnapshot 请求 snapshot 是拿来装回的那份快照不是已经是本地清单；看见 OfferSnapshot 回包 result 是这次 Offer 的结果不是已经装完；看见 OfferSnapshot 在用 state sync 引导节点时叫不是已经必须实现快照连接

**层次**：实现 / OfferSnapshot 请求。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) OfferSnapshot。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5。本页是「OfferSnapshot 请求 snapshot 是拿来装回的那份快照不是已经是本地清单 / OfferSnapshot 回包 result 是这次 Offer 的结果不是已经装完 / OfferSnapshot 在用 state sync 引导节点时叫不是已经必须实现快照连接」，不是 ListSnapshots 回了本地清单就已经是同一份，也不是 Offer 收下就已经装完。不要另写怎样写 OfferSnapshot 请求。

## 官方三件事

规范把 OfferSnapshot 请求 `snapshot` 是拿来装回的那份快照、回包 `result` 是这次 Offer 的结果、Usage 是在用 state sync 引导节点时叫写成三件独立的实现事，不是「看见填了 OfferSnapshot 请求就已经是本地清单、已经装完、已经必须实现快照连接」一件事：

1. **看见 OfferSnapshot 请求 `snapshot` 是拿来装回的那份快照 / 看见填了 snapshot 不是已经是本地清单，也不是已经是同一份。**  
   官方写：`snapshot` 是拿来装回的那份快照。看见填了 snapshot，不是已经是 ListSnapshots 回的那份本地清单。看见有这份，不是已经五个字段都对上、已经是同一份。看见能填，不是已经交差。
2. **看见 OfferSnapshot 回包 `result` 是这次 Offer 的结果 / 看见回了 result 不是已经装完，也不是已经收下。**  
   官方写：`result` 是这次 Offer 的结果。看见回了 result，不是已经 Offer 收下就已经装完。看见有结果，不是已经收下。看见能回，不是已经交差。
3. **看见 OfferSnapshot 在用 state sync 引导节点时叫 / 看见在引导时叫了 不是已经必须实现快照连接，也不是已经切进共识。**  
   官方写：`OfferSnapshot` 在用 state sync 引导节点时叫。看见在引导时叫了，不是已经四门里有 Snapshot Connection 就必须实现。看见能叫，不是已经切进共识。看见能填，不是已经交差。

怎样写 OfferSnapshot 请求、怎样填 snapshot、怎样填 result 是规范里的做法，本页不抄。ListSnapshots 回了本地清单就已经是同一份是不变量 395，本页不抄。

## 官方为什么这样拆

- **OfferSnapshot 请求 snapshot 是拿来装回的那份快照 ≠ 已经是本地清单：** 官方把拿来装回的那份和本地清单分开。
- **OfferSnapshot 回包 result 是这次 Offer 的结果 ≠ 已经装完：** 官方把这次 Offer 的结果和 Offer 收下就已经装完分开。
- **OfferSnapshot 在用 state sync 引导节点时叫 ≠ 已经必须实现快照连接：** 官方把引导时叫和门在就必须实现分开。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| OfferSnapshot 请求 snapshot 是拿来装回的那份快照 | 不是已经是本地清单 | 不是 ListSnapshots 回包 snapshots 是本地状态快照清单就已经是同一份（395） |
| OfferSnapshot 回包 result 是这次 Offer 的结果 | 不是已经装完 | 不是 Offer 收下就已经装完（321） |
| OfferSnapshot 在用 state sync 引导节点时叫 | 不是已经必须实现快照连接 | 不是四门里有 Snapshot Connection 就已经必须实现快照（334） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看「看见填了 OfferSnapshot 请求就已经是本地清单、已经装完、已经必须实现快照连接」，必须分开 OfferSnapshot 请求 snapshot 是拿来装回的那份快照是不是已经是本地清单、OfferSnapshot 回包 result 是这次 Offer 的结果是不是已经装完、OfferSnapshot 在用 state sync 引导节点时叫是不是已经必须实现快照连接。可以跳过「看见填了 OfferSnapshot 请求就已经是本地清单」。不要另写怎样写 OfferSnapshot 请求。396 offersnap vs listed bundled unbundling 完成（737 item 1 / 738 item 2 / 739 item 3）；精读 [`worked-example-offersnapreq-notlisted-vs-bundled.md`](worked-example-offersnapreq-notlisted-vs-bundled.md)（不变量 737 item 1）。

## 本页不抄

- 怎样写 OfferSnapshot 请求、怎样填 snapshot、怎样填 result。
- ListSnapshots 回包 snapshots 是本地状态快照清单就已经是同一份。那是不变量 395。
- Offer 收下就已经装完。那是不变量 321。
- 四门里有 Snapshot Connection 就已经必须实现快照。那是不变量 334。
- 只有轻客户端验过的 AppHash 可信任。那是不变量 38。
