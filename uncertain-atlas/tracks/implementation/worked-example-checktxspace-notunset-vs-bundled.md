# 例：看见填了道 / 看见在范围内 / 看见能指道 is not already already unset interchangeable / already priority interchangeable / already included interchangeable

**层次**：实现 / CheckTx 的 lane_id 必须在 Info 回包车道范围内不是已经不设道 not already unset / not already priority / not already included 正式三事（381 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) CheckTx Response。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「CheckTx 的 lane_id 必须在 Info 回包车道范围内不是已经不设道 not already unset / not already priority / not already included 正式三事（381 余量）/ not 892 checktxspace-notunset interchangeable / not 381 checktxspace bundled interchangeable」，不是 checktxspace bundled（381），也不是 CheckTx 回包 codespace 是码的命名空间不是已经是回包码（381 item 1 余量 / 890）或 CheckTx 回包 events 是给索引用的类型键值不是已经交差（381 item 2 余量 / 891）。不要另写怎样写 CheckTx 回包。

## 官方三件事

规范把 Methods 里 CheckTx 的 lane_id 必须在 Info 回包车道范围内 和「已经是填了道就已经不设道 interchangeable / 已经是在范围内就已经排了优先 interchangeable / 已经是能指道就已经进了块 interchangeable / 已经是 checktxspace bundled interchangeable」分开写成三件独立的实现事，不是「看见填了道就已经不设道 interchangeable / 就已经排了优先 interchangeable / 就已经进了块 interchangeable」一件事：

1. **看见填了道 / 看见 CheckTx 的 lane_id 必须在 Info 回包车道范围内 / 看见填了 lane_id is not already 已经不设道 interchangeable / 已经 unset interchangeable / 已经不设道交差 interchangeable / 381 checktxspace bundled interchangeable / 367 lane-priority interchangeable / checktxspace-sold-as-code interchangeable，也不是已经 checktxspace bundled（381） interchangeable / 892 checktxspace-notunset interchangeable / 381 checktxspace item 3 interchangeable，也不是已经 CheckTx 的 lane_id 必须在 Info 回包车道范围内不是已经不设道 not already unset / not already priority / not already included 正式三事 bundled（381 item 3 余量） interchangeable / 381 checktxspace item 3 interchangeable，也不是已经写了空间就已经是回包码（890） interchangeable / 回了事件就已经交差（891） interchangeable / 367 lane-priority interchangeable，也不是已经没定义 lane_priorities 就已经排了优先（367） interchangeable。**  
   官方写：`lane_id` 的值必须落在应用在 `ResponseInfo` 里定义过的那些道。看见填了道，不是已经空 `lane_id` 那种不设道。看见填了道，不是已经 unset interchangeable——381 钉 bundled 三事，本页从 item 3 侧钉 not already unset 单句。看见 CheckTx 的 lane_id 必须在 Info 回包车道范围内，不是已经 checktxspace bundled（381） interchangeable——381 钉 bundled，本页钉 item 3 第一件事。看见填了 lane_id，不是已经没定义 lane_priorities 就已经排了优先（367） interchangeable——367 另钉。381 checktxspace-vs-code bundled unbundling 在本页 item 3 完成。

2. **看见在范围内 / 看见落在 Info 车道范围内 / 看见道在范围内 is not already 已经排了优先 interchangeable / 已经 priority interchangeable / 已经排了优先交差 interchangeable / 381 checktxspace bundled interchangeable / 367 lane-priority interchangeable，也不是已经 checktxspace bundled（381） interchangeable / 892 checktxspace-notunset interchangeable / 381 checktxspace item 1 写了空间 interchangeable / 381 checktxspace item 2 回了事件 interchangeable，也不是已经 CheckTx 的 lane_id 必须在 Info 回包车道范围内不是已经不设道 not already unset / not already priority / not already included 正式三事 bundled（381 item 3 余量） interchangeable / 381 checktxspace item 3 interchangeable，也不是已经不设道（本页第一件事） interchangeable。**  
   官方写：看见在范围内，不是已经排了优先。看见落在 Info 车道范围内，不是已经 priority interchangeable——本页钉 not already priority 单句。看见道在范围内，不是已经不设道（本页第一件事） interchangeable——三件事分开钉。381 checktxspace-vs-code bundled unbundling 在本页 item 3 完成。

3. **看见能指道 / 看见能指 lane_id / 看见有车道指派 is not already 已经进了块 interchangeable / 已经 included interchangeable / 已经进了块交差 interchangeable / 381 checktxspace bundled interchangeable / 891 checktxspace-notsettled interchangeable，也不是已经 checktxspace bundled（381） interchangeable / 892 checktxspace-notunset interchangeable / 381 checktxspace item 1 / 381 checktxspace item 2，也不是已经 CheckTx 的 lane_id 必须在 Info 回包车道范围内不是已经不设道 not already unset / not already priority / not already included 正式三事 bundled（381 item 3 余量） interchangeable / 381 checktxspace item 3 interchangeable，也不是已经不设道（本页第一件事） interchangeable / 已经排了优先（本页第二件事） interchangeable。**  
   官方写：看见能指道，不是已经进了块。看见能指 lane_id，不是已经 included interchangeable——本页钉 not already included 单句。看见有车道指派，不是已经排了优先（本页第二件事） interchangeable——三件事分开钉。381 checktxspace-vs-code bundled unbundling 在本页 item 3 完成。

怎样写 CheckTx 回包、怎样填码空间、怎样选道是规范里的做法，本页不抄。checktxspace bundled（381）、CheckTx 回包 codespace 是码的命名空间不是已经是回包码（381 item 1 余量 / 890）、CheckTx 回包 events 是给索引用的类型键值不是已经交差（381 item 2 余量 / 891）、引擎对回包码不再赋予别的含义就已经被引擎用了 Data（373）、结果列表就已经同一顺序（316）、没定义 lane_priorities 就已经排了优先（367）是另外那套，本页不抄。

## 官方为什么这样拆

- **填了道 not already unset ≠ 381 / 367 interchangeable：** 官方把必须落在 Info 车道里和空 lane_id 留给不设道分开。
- **在范围内 not already priority ≠ 已经排了优先 interchangeable：** 官方把在范围内和已经排了优先分开。
- **能指道 not already included ≠ 已经进了块 interchangeable：** 官方把能指道和已经进了块分开；381 checktxspace-vs-code bundled unbundling 在本页 item 3 完成。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 填了道 | 不是 already unset | 不是没定义 lane_priorities 就已经排了优先 alone（367） |
| 在范围内 | 不是 already priority | 不是写了空间 already code alone（890） |
| 能指道 | 不是 already included | 不是回了事件 already settled alone（891） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 CheckTx 的 lane_id 必须在 Info 回包车道范围内不是已经不设道 not already unset / not already priority / not already included 正式三事（381 余量），必须分开填了道 是不是 already unset interchangeable / 381 checktxspace bundled interchangeable / checktxspace-sold-as-code interchangeable、在范围内 是不是 already priority interchangeable、能指道 是不是 already included interchangeable。可以跳过「看见填了道就已经不设道 interchangeable / 就已经排了优先 interchangeable / 就已经进了块 interchangeable」。不要另写怎样写 CheckTx 回包。381 checktxspace-vs-code bundled unbundling 在本页 item 3 完成（890 + 891 + 892）。

## 本页不抄

- 怎样写 CheckTx 回包、怎样填码空间、怎样选道。
- checktxspace bundled。那是不变量 381。
- CheckTx 回包 codespace 是码的命名空间不是已经是回包码。那是不变量 381 item 1 余量 / 890。
- CheckTx 回包 events 是给索引用的类型键值不是已经交差。那是不变量 381 item 2 余量 / 891。
- 引擎对回包码不再赋予别的含义就已经被引擎用了 Data。那是不变量 373。
- 结果列表就已经同一顺序。那是不变量 316。
- 没定义 lane_priorities 就已经排了优先。那是不变量 367。
