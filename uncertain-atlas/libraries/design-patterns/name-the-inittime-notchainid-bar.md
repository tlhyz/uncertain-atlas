# 模式：把 InitChain 请求 chain_id not already have ChainID / not already full history / not already settled 正式三事（387 余量） 说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) InitChain Request。  
**例**：[InitChain ≠ bundled（387）](../../tracks/implementation/worked-example-inittime-notchainid-vs-bundled.md)。

## 三个名字

1. **chain_id 不是已经有了 ChainID：** 看见填了 chain_id，不是已经 323 interchangeable / 768 inittime-notchainid interchangeable。
2. **看见填了 chain_id 不是已经有完整历史：** 看见有标识，不是已经 323 interchangeable。
3. **看见能回 不是已经交差：** 看见 InitChain 请求 chain_id，不是已经交差 interchangeable。

官方把 InitChain 请求 time / chain_id / initial_height 三条核心句拆成三个名字。把它们叫成一个「看见叫了 InitChain 就已经过了 genesis_time」，会把三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 InitChain 请求 chain_id 正式三事（387 余量），先数清问的是是不是已经有了 ChainID / 323、是不是已经有完整历史、还是看见能回是不是已经交差，再决定要不要同一次发布。387 inittime vs genesis bundled unbundling 在本页 item 2 续。
