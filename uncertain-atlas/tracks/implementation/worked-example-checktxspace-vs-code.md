# 例：看见 CheckTx 回包 codespace 是码的命名空间不是已经是回包码；看见 CheckTx 回包 events 是给索引用的类型键值不是已经交差；看见 CheckTx 的 lane_id 必须在 Info 回包车道范围内不是已经不设道

**层次**：实现 / CheckTx 回包。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) CheckTx Response。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「CheckTx 回包 codespace 是码的命名空间不是已经是回包码 / CheckTx 回包 events 是给索引用的类型键值不是已经交差 / CheckTx 的 lane_id 必须在 Info 回包车道范围内不是已经不设道」，不是引擎对回包码不再赋予别的含义就已经被引擎用了 Data，也不是没定义 lane_priorities 就已经排了优先。不要另写怎样写 CheckTx 回包。381 checktxspace-vs-code bundled unbundling 启动（890）；精读 [`worked-example-checktxspace-notcode-vs-bundled.md`](worked-example-checktxspace-notcode-vs-bundled.md)（不变量 890 item 1）。

## 官方三件事

规范把 CheckTx 回包 `codespace` 是码的命名空间、`events` 是给索引用的类型键值、`lane_id` 必须在 Info 回包车道范围内写成三件独立的实现事，不是「看见 CheckTx 回了码空间就已经是回包码、已经交差、已经不设道」一件事：

1. **看见 CheckTx 回包 `codespace` 是码的命名空间 / 看见写了空间 不是已经是回包码，也不是已经没进块。**  
   官方写：`codespace` 是这个 `code` 的命名空间。看见写了空间，不是已经是回包码本身。看见有命名空间，不是已经没进块。看见能回，不是已经交差。
2. **看见 CheckTx 回包 `events` 是给索引用的类型键值 / 看见回了事件 不是已经交差，也不是已经没进块。**  
   官方写：`events` 是给交易建索引的类型和键值，例如按账户。看见回了事件，不是已经交差。看见能按账户查，不是已经没进块。看见有类型键值，不是已经是共识顺序。
3. **看见 CheckTx 的 `lane_id` 必须在 Info 回包车道范围内 / 看见填了道 不是已经不设道，也不是已经排了优先。**  
   官方写：`lane_id` 的值必须落在应用在 `ResponseInfo` 里定义过的那些道。看见填了道，不是已经空 `lane_id` 那种不设道。看见在范围内，不是已经排了优先。看见能指道，不是已经进了块。

怎样写 CheckTx 回包、怎样填码空间、怎样选道是规范里的做法，本页不抄。引擎对回包码不再赋予别的含义就已经被引擎用了 Data 是不变量 373，本页不抄。

## 官方为什么这样拆

- **CheckTx 回包 codespace 是码的命名空间 ≠ 已经是回包码：** 官方把码的命名空间和回包码本身分开。
- **CheckTx 回包 events 是给索引用的类型键值 ≠ 已经交差：** 官方把索引事件和 Finalize 回执交差分开。
- **CheckTx 的 lane_id 必须在 Info 回包车道范围内 ≠ 已经不设道：** 官方把必须落在 Info 车道里和空 lane_id 留给不设道分开。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| CheckTx 回包 codespace 是码的命名空间 | 不是已经是回包码 | 不是引擎对回包码不再赋予别的含义就已经被引擎用了 Data（373） |
| CheckTx 回包 events 是给索引用的类型键值 | 不是已经交差 | 不是结果列表就已经同一顺序（316） |
| CheckTx 的 lane_id 必须在 Info 回包车道范围内 | 不是已经不设道 | 不是没定义 lane_priorities 就已经排了优先（367） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看「看见 CheckTx 回了码空间就已经是回包码、已经交差、已经不设道」，必须分开 CheckTx 回包 codespace 是码的命名空间是不是已经是回包码、CheckTx 回包 events 是给索引用的类型键值是不是已经交差、CheckTx 的 lane_id 必须在 Info 回包车道范围内是不是已经不设道。可以跳过「看见 CheckTx 回了码空间就已经是回包码」。不要另写怎样写 CheckTx 回包。381 checktxspace-vs-code bundled unbundling 启动（890）。

## 本页不抄

- 怎样写 CheckTx 回包、怎样填码空间、怎样选道。
- 引擎对回包码不再赋予别的含义就已经被引擎用了 Data。那是不变量 373。
- 结果列表就已经同一顺序。那是不变量 316。
- 没定义 lane_priorities 就已经排了优先。那是不变量 367。
