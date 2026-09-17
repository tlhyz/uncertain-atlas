# 例：看见 InitChain 请求 time 是创世时间不是已经过了 genesis_time；看见 InitChain 请求 chain_id 是链的 ID 不是已经有了 ChainID；看见 InitChain 请求 initial_height 是起步块高度不是已经能跳步

**层次**：实现 / InitChain 请求。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) InitChain Request。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5。本页是「InitChain 请求 time 是创世时间不是已经过了 genesis_time / InitChain 请求 chain_id 是链的 ID 不是已经有了 ChainID / InitChain 请求 initial_height 是起步块高度不是已经能跳步」，不是进程起来就已经过了 genesis_time，也不是快照装完就已经有了 ChainID。不要另写怎样写 InitChain 请求。

## 官方三件事

规范把 InitChain 请求 `time` 是创世时间、`chain_id` 是链的 ID、`initial_height` 是起步块高度写成三件独立的实现事，不是「看见叫了 InitChain 就已经过了 genesis_time、已经有了 ChainID、已经能跳步」一件事：

1. **看见 InitChain 请求 `time` 是创世时间 / 看见填了 time 不是已经过了 genesis_time，也不是已经开出块。**  
   官方写：`time` 是创世时间。看见填了 time，不是已经过了创世文件里的 `genesis_time`。看见有时间，不是已经开出块。看见能填，不是已经交差。
2. **看见 InitChain 请求 `chain_id` 是链的 ID / 看见填了 chain_id 不是已经有了 ChainID，也不是已经有完整历史。**  
   官方写：`chain_id` 是这条链的 ID。看见填了 chain_id，不是已经有了快照装完后凑齐的 ChainID。看见有标识，不是已经有从创世的完整历史。看见能回，不是已经交差。
3. **看见 InitChain 请求 `initial_height` 是起步块高度 / 看见填了起步高 不是已经能跳步，也不是已经过了崩溃三步。**  
   官方写：`initial_height` 是起步块的高度，通常是 1。看见填了起步高，不是已经能从半截高度接着走。看见写成 1，不是已经过了崩溃三步。看见有高度，不是已经交差。

怎样写 InitChain 请求、怎样填时间、怎样选起步高是规范里的做法，本页不抄。进程起来就已经过了 genesis_time 是不变量 303，本页不抄。

## 官方为什么这样拆

- **InitChain 请求 time 是创世时间 ≠ 已经过了 genesis_time：** 官方把请求里的创世时间和创世文件里的 genesis_time 分开。
- **InitChain 请求 chain_id 是链的 ID ≠ 已经有了 ChainID：** 官方把请求里的链 ID 和快照装完后凑齐的 ChainID 分开。
- **InitChain 请求 initial_height 是起步块高度 ≠ 已经能跳步：** 官方把起步高度和崩溃恢复已经能跳步分开。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| InitChain 请求 time 是创世时间 | 不是已经过了 genesis_time | 不是进程起来就已经过了 genesis_time（303） |
| InitChain 请求 chain_id 是链的 ID | 不是已经有了 ChainID | 不是快照装完就已经有了 ChainID（323） |
| InitChain 请求 initial_height 是起步块高度 | 不是已经能跳步 | 不是启动 Info 对上就已经能跳步（320） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看「看见叫了 InitChain 就已经过了 genesis_time、已经有了 ChainID、已经能跳步」，必须分开 InitChain 请求 time 是创世时间是不是已经过了 genesis_time、InitChain 请求 chain_id 是链的 ID 是不是已经有了 ChainID、InitChain 请求 initial_height 是起步块高度是不是已经能跳步。可以跳过「看见叫了 InitChain 就已经过了 genesis_time」。不要另写怎样写 InitChain 请求。387 inittime vs genesis bundled unbundling 完成（767 item 1 / 768 item 2 / 769 item 3）；精读 [`worked-example-inittime-notgenesis-vs-bundled.md`](worked-example-inittime-notgenesis-vs-bundled.md)（不变量 767 item 1）。

## 本页不抄

- 怎样写 InitChain 请求、怎样填时间、怎样选起步高。
- 进程起来就已经过了 genesis_time。那是不变量 303。
- 快照装完就已经有了 ChainID。那是不变量 323。
- 启动 Info 对上就已经能跳步。那是不变量 320。
