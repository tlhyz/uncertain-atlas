# 例：看见从池子按优先级收未决交易不是已经 preliminary raw proposal bundled；看见造头再调 Prepare不是已经整池可见；看见从池子按优先级收未决交易不是已经 validValue 非 nil 跳过 Prepare

**层次**：实现 / 规范对象。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) PrepareProposal When。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「PrepareWhen collect not already raw-proposal / not already full-pool / not already validValue-skip 正式三事（505 余量）/ not 1310 prepwhen-notprio interchangeable / not 505 preparewhen-collect-vs-bundled bundled interchangeable」，不是 preparewhen collect vs bundled bundled（505），也不是已经 Prepare Usage raw proposal（503），也不是已经 validValue 跳过 Prepare（356）。不要另写 怎样从池子收交易、怎样造头、怎样改 Prepare 列表。

## 官方三件事

1. **看见从池子按优先级收未决交易 / 看见从池子按优先级收未决交易 这份对象 is not already 已经 preliminary raw proposal bundled interchangeable，也不是已经 preparewhen collect vs bundled bundled（505） interchangeable / 1310 prepwhen-notprio interchangeable / 1311 prepwhen-notsync interchangeable，也不是已经 PrepareWhen collect not already raw-proposal / not already full-pool / not already validValue-skip 正式三事 bundled（505 item 1 余量） interchangeable / 505 prepwhen item 1 interchangeable。**  
   官方把从池子按优先级收未决交易和已经 preliminary raw proposal bundled写成两件。看见从池子按优先级收未决交易，不是已经 preliminary raw proposal bundled。

2. **看见造头再调 Prepare / 看见从池子按优先级收未决交易 / 这份对象 is not already 已经整池可见 interchangeable，也不是已经 preparewhen collect vs bundled bundled（505） interchangeable / 1310 prepwhen-notprio interchangeable / 1312 prepwhen-notmanip interchangeable，也不是已经 Prepare Usage raw proposal interchangeable / 503 Prepare Usage raw proposal interchangeable。**  
   官方把造头再调 Prepare和已经整池可见写成两件。看见造头再调 Prepare，不是已经整池可见。

3. **看见从池子按优先级收未决交易 / 看见造头再调 Prepare / 这份对象 is not already 已经 validValue 非 nil 跳过 Prepare interchangeable，也不是已经 preparewhen collect vs bundled bundled（505） interchangeable / 1310 prepwhen-notprio interchangeable / 1311 prepwhen-notsync interchangeable，也不是已经 validValue 跳过 Prepare interchangeable / 356 validValue 跳过 Prepare interchangeable。**  
   官方把从池子按优先级收未决交易和已经 validValue 非 nil 跳过 Prepare写成两件。看见从池子按优先级收未决交易，不是已经 validValue 非 nil 跳过 Prepare。

栈怎么写、分隔符、例串是规范里的取值，本页不抄。不要另写 怎样从池子收交易、怎样造头、怎样改 Prepare 列表。

## 官方为什么这样拆

- **collect priority / create header 不是 raw proposal bundled interchangeable：官方把 When 侧收池造头单句和 Usage raw proposal bundled 分开。**
- **看见造头再调 Prepare 不是已经整池可见：本页钉 When 侧按优先级收未决，不是已经没有上限。**
- **看见从池子收 不是已经 validValue 非 nil 跳过 Prepare：那是不变量 356。**

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 已经 preliminary raw proposal bundled | 不是已经 preliminary raw proposal bundled | 不是已经Prepare Usage raw proposal（503） |
| 已经整池可见 | 不是已经整池可见 | 不是已经validValue 跳过 Prepare（356） |
| 已经 validValue 非 nil 跳过 Prepare | 不是已经 validValue 非 nil 跳过 Prepare | 不是已经1311 prepwhen-notsync |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 PrepareWhen collect not already raw-proposal / not already full-pool / not already validValue-skip 正式三事（505 余量），必须分开是不是已经 preliminary raw proposal bundled、是不是已经整池可见、是不是已经 validValue 非 nil 跳过 Prepare。可以跳过「看见自己是提议者就已经 raw proposal bundled interchangeable、已经能在返回后再改裁决、已经 Prepare 改列表 bundled interchangeable」。不要另写 怎样从池子收交易、怎样造头、怎样改 Prepare 列表。505 PrepareProposal When collect bundled unbundling 在本页 item 1 启动；续 [`worked-example-prepwhen-notsync-vs-bundled.md`](worked-example-prepwhen-notsync-vs-bundled.md)（不变量 1311 item 2）。

## 本页不抄

- 怎样做从池子收交易、怎样造头、怎样改 Prepare 列表、怎样缓存候选。
- 怎样从池子收交易、怎样造头、怎样改 Prepare 列表。
