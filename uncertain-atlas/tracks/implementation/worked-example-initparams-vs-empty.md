# 例：看见 InitChain 请求 consensus_params 是起步共识参数不是已经没有参数；看见 InitChain 请求 validators 是起步验证者名单不是已经没有集合；看见 InitChain 请求 app_state_bytes 是序列化起步应用状态不是已经验过应用状态

**层次**：实现 / InitChain 请求余栏。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) InitChain Request。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5。本页是「InitChain 请求 consensus_params 是起步共识参数不是已经没有参数 / InitChain 请求 validators 是起步验证者名单不是已经没有集合 / InitChain 请求 app_state_bytes 是序列化起步应用状态不是已经验过应用状态」，不是 InitChain 回了空 ConsensusParams 就已经没有参数，也不是 InitChain 回了空名单就已经没有集合。不要另写怎样写 InitChain 请求余栏。

## 官方三件事

规范把 InitChain 请求 `consensus_params` 是起步共识参数、`validators` 是起步验证者名单、`app_state_bytes` 是序列化起步应用状态写成三件独立的实现事，不是「看见填了 InitChain 请求余栏就已经没有参数、已经没有集合、已经验过应用状态」一件事：

1. **看见 InitChain 请求 `consensus_params` 是起步共识参数 / 看见填了起步参数 不是已经没有参数，也不是已经用了回包空参数。**  
   官方写：`consensus_params` 是起步时共识关键参数。看见填了起步参数，不是已经没有参数。看见有这份请求栏，不是已经是 InitChain 回了空就改用创世参数。看见能填，不是已经交差。
2. **看见 InitChain 请求 `validators` 是起步验证者名单 / 看见填了起步名单 不是已经没有集合，也不是已经用了回包空名单。**  
   官方写：`validators` 是起步创世验证者，按投票权排序。看见填了起步名单，不是已经没有集合。看见有这份请求栏，不是已经是 InitChain 回了空就改用创世名单。看见能回，不是已经交差。
3. **看见 InitChain 请求 `app_state_bytes` 是序列化起步应用状态 / 看见填了 JSON 字节 不是已经验过应用状态，也不是已经懂余额。**  
   官方写：`app_state_bytes` 是序列化起步应用状态，JSON 字节。看见填了 JSON 字节，不是已经验过创世文件里的应用段。看见有字节，不是已经懂余额。看见能填，不是已经交差。

怎样写 InitChain 请求余栏、怎样选起步参数、怎样排起步名单是规范里的做法，本页不抄。InitChain 回了空 ConsensusParams 就已经没有参数是不变量 319，本页不抄。

## 官方为什么这样拆

- **InitChain 请求 consensus_params 是起步共识参数 ≠ 已经没有参数：** 官方把请求里的起步参数和回包空着就已经没有参数分开。
- **InitChain 请求 validators 是起步验证者名单 ≠ 已经没有集合：** 官方把请求里的起步名单和回包空着就已经没有集合分开。
- **InitChain 请求 app_state_bytes 是序列化起步应用状态 ≠ 已经验过应用状态：** 官方把请求里的序列化应用状态和创世文件里的应用段已经验过分开。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| InitChain 请求 consensus_params 是起步共识参数 | 不是已经没有参数 | 不是 InitChain 回了空 ConsensusParams 就已经没有参数（319） |
| InitChain 请求 validators 是起步验证者名单 | 不是已经没有集合 | 不是 InitChain 回了空名单就已经没有集合（318） |
| InitChain 请求 app_state_bytes 是序列化起步应用状态 | 不是已经验过应用状态 | 不是创世 app_state 就已经验过应用状态（303） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看「看见填了 InitChain 请求余栏就已经没有参数、已经没有集合、已经验过应用状态」，必须分开 InitChain 请求 consensus_params 是起步共识参数是不是已经没有参数、InitChain 请求 validators 是起步验证者名单是不是已经没有集合、InitChain 请求 app_state_bytes 是序列化起步应用状态是不是已经验过应用状态。可以跳过「看见填了 InitChain 请求余栏就已经没有参数」。不要另写怎样写 InitChain 请求余栏。

## 本页不抄

- 怎样写 InitChain 请求余栏、怎样选起步参数、怎样排起步名单。
- InitChain 回了空 ConsensusParams 就已经没有参数。那是不变量 319。
- InitChain 回了空名单就已经没有集合。那是不变量 318。
- 创世 app_state 就已经验过应用状态。那是不变量 303。
