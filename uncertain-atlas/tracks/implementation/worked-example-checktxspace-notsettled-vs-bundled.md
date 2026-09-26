# 例：看见回了事件 / 看见能按账户查 / 看见有类型键值 is not already already settled interchangeable / already excluded interchangeable / already ordered interchangeable

**层次**：实现 / CheckTx 回包 events 是给索引用的类型键值不是已经交差 not already settled / not already excluded / not already ordered 正式三事（381 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) CheckTx Response。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「CheckTx 回包 events 是给索引用的类型键值不是已经交差 not already settled / not already excluded / not already ordered 正式三事（381 余量）/ not 891 checktxspace-notsettled interchangeable / not 381 checktxspace bundled interchangeable」，不是 checktxspace bundled（381），也不是 CheckTx 回包 codespace 是码的命名空间不是已经是回包码（381 item 1 余量 / 890）或 CheckTx 的 lane_id 必须在 Info 回包车道范围内不是已经不设道（381 item 3 余量）。不要另写怎样写 CheckTx 回包。

## 官方三件事

规范把 Methods 里 CheckTx 回包 events 是给索引用的类型键值 和「已经是回了事件就已经交差 interchangeable / 已经是能按账户查就已经没进块 interchangeable / 已经是有类型键值就已经是共识顺序 interchangeable / 已经是 checktxspace bundled interchangeable」分开写成三件独立的实现事，不是「看见回了事件就已经交差 interchangeable / 就已经没进块 interchangeable / 就已经是共识顺序 interchangeable」一件事：

1. **看见回了事件 / 看见 CheckTx 回包 events 是给索引用的类型键值 / 看见回了 events is not already 已经交差 interchangeable / 已经 settled interchangeable / 已经交差交差 interchangeable / 381 checktxspace bundled interchangeable / 316 txresults interchangeable / checktxspace-sold-as-code interchangeable，也不是已经 checktxspace bundled（381） interchangeable / 891 checktxspace-notsettled interchangeable / 381 checktxspace item 2 interchangeable，也不是已经 CheckTx 回包 events 是给索引用的类型键值不是已经交差 not already settled / not already excluded / not already ordered 正式三事 bundled（381 item 2 余量） interchangeable / 381 checktxspace item 2 interchangeable，也不是已经写了空间就已经是回包码（890） interchangeable / 填了道就已经不设道（381 item 3） interchangeable / 316 txresults interchangeable，也不是已经结果列表就已经同一顺序（316） interchangeable。**  
   官方写：`events` 是给交易建索引的类型和键值，例如按账户。看见回了事件，不是已经交差。看见回了事件，不是已经 settled interchangeable——381 钉 bundled 三事，本页从 item 2 侧钉 not already settled 单句。看见 CheckTx 回包 events 是给索引用的类型键值，不是已经 checktxspace bundled（381） interchangeable——381 钉 bundled，本页钉 item 2 第一件事。看见回了 events，不是已经结果列表就已经同一顺序（316） interchangeable——316 另钉。381 checktxspace-vs-code bundled unbundling 在本页 item 2 续。

2. **看见能按账户查 / 看见能按账户建索引 / 看见有账户索引 is not already 已经没进块 interchangeable / 已经 excluded interchangeable / 已经没进块交差 interchangeable / 381 checktxspace bundled interchangeable / 373 checktxopt interchangeable，也不是已经 checktxspace bundled（381） interchangeable / 891 checktxspace-notsettled interchangeable / 381 checktxspace item 1 写了空间 interchangeable / 381 checktxspace item 3 填了道 interchangeable，也不是已经 CheckTx 回包 events 是给索引用的类型键值不是已经交差 not already settled / not already excluded / not already ordered 正式三事 bundled（381 item 2 余量） interchangeable / 381 checktxspace item 2 interchangeable，也不是已经交差（本页第一件事） interchangeable。**  
   官方写：看见能按账户查，不是已经没进块。看见能按账户建索引，不是已经 excluded interchangeable——本页钉 not already excluded 单句。看见有账户索引，不是已经交差（本页第一件事） interchangeable——三件事分开钉。381 checktxspace-vs-code bundled unbundling 在本页 item 2 续。

3. **看见有类型键值 / 看见有索引类型键值 / 看见有 events 类型键值 is not already 已经是共识顺序 interchangeable / 已经 ordered interchangeable / 已经是共识顺序交差 interchangeable / 381 checktxspace bundled interchangeable / 890 checktxspace-notcode interchangeable，也不是已经 checktxspace bundled（381） interchangeable / 891 checktxspace-notsettled interchangeable / 381 checktxspace item 1 / 381 checktxspace item 3，也不是已经 CheckTx 回包 events 是给索引用的类型键值不是已经交差 not already settled / not already excluded / not already ordered 正式三事 bundled（381 item 2 余量） interchangeable / 381 checktxspace item 2 interchangeable，也不是已经交差（本页第一件事） interchangeable / 已经没进块（本页第二件事） interchangeable。**  
   官方写：看见有类型键值，不是已经是共识顺序。看见有索引类型键值，不是已经 ordered interchangeable——本页钉 not already ordered 单句。看见有 events 类型键值，不是已经没进块（本页第二件事） interchangeable——三件事分开钉。381 checktxspace-vs-code bundled unbundling 在本页 item 2 续。

怎样写 CheckTx 回包、怎样填码空间、怎样选道是规范里的做法，本页不抄。checktxspace bundled（381）、CheckTx 回包 codespace 是码的命名空间不是已经是回包码（381 item 1 余量 / 890）、CheckTx 的 lane_id 必须在 Info 回包车道范围内不是已经不设道（381 item 3 余量）、引擎对回包码不再赋予别的含义就已经被引擎用了 Data（373）、结果列表就已经同一顺序（316）、没定义 lane_priorities 就已经排了优先（367）是另外那套，本页不抄。

## 官方为什么这样拆

- **回了事件 not already settled ≠ 381 / 316 interchangeable：** 官方把索引事件和 Finalize 回执交差分开。
- **能按账户查 not already excluded ≠ 已经没进块 interchangeable：** 官方把能按账户查和已经没进块分开。
- **有类型键值 not already ordered ≠ 已经是共识顺序 interchangeable：** 官方把有类型键值和已经是共识顺序分开；381 checktxspace-vs-code bundled unbundling 在本页 item 2 续。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 回了事件 | 不是 already settled | 不是结果列表就已经同一顺序 alone（316） |
| 能按账户查 | 不是 already excluded | 不是写了空间 already code alone（890） |
| 有类型键值 | 不是 already ordered | 不是填了道 already unset alone（381 item 3） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 CheckTx 回包 events 是给索引用的类型键值不是已经交差 not already settled / not already excluded / not already ordered 正式三事（381 余量），必须分开回了事件 是不是 already settled interchangeable / 381 checktxspace bundled interchangeable / checktxspace-sold-as-code interchangeable、能按账户查 是不是 already excluded interchangeable、有类型键值 是不是 already ordered interchangeable。可以跳过「看见回了事件就已经交差 interchangeable / 就已经没进块 interchangeable / 就已经是共识顺序 interchangeable」。不要另写怎样写 CheckTx 回包。381 checktxspace-vs-code bundled unbundling 在本页 item 2 续（890 + 891）。

## 本页不抄

- 怎样写 CheckTx 回包、怎样填码空间、怎样选道。
- checktxspace bundled。那是不变量 381。
- CheckTx 回包 codespace 是码的命名空间不是已经是回包码。那是不变量 381 item 1 余量 / 890。
- CheckTx 的 lane_id 必须在 Info 回包车道范围内不是已经不设道。那是不变量 381 item 3 余量。
- 引擎对回包码不再赋予别的含义就已经被引擎用了 Data。那是不变量 373。
- 结果列表就已经同一顺序。那是不变量 316。
- 没定义 lane_priorities 就已经排了优先。那是不变量 367。
