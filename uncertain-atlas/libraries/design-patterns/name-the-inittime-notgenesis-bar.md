# 模式：把 InitChain 请求 time not already past genesis_time / not already producing blocks / not already settled 正式三事（387 余量） 说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) InitChain Request。  
**例**：[InitChain ≠ bundled（387）](../../tracks/implementation/worked-example-inittime-notgenesis-vs-bundled.md)。

## 三个名字

1. **time 不是已经过了 genesis_time：** 看见填了 time，不是已经 303 interchangeable / 767 inittime-notgenesis interchangeable。
2. **看见填了 time 不是已经开出块：** 看见有时间，不是已经 303 interchangeable。
3. **看见能填 不是已经交差：** 看见 InitChain 请求 time，不是已经交差 interchangeable。

官方把 InitChain 请求 time / chain_id / initial_height 三条核心句拆成三个名字。把它们叫成一个「看见叫了 InitChain 就已经过了 genesis_time」，会把三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 InitChain 请求 time 正式三事（387 余量），先数清问的是是不是已经过了 genesis_time / 303、是不是已经开出块、还是看见能填是不是已经交差，再决定要不要同一次发布。387 inittime vs genesis bundled unbundling 在本页 item 1 启动。
