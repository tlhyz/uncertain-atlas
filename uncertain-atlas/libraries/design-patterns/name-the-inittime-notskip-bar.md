# 模式：把 InitChain 请求 initial_height not already can skip / not already past crash steps / not already settled 正式三事（387 余量） 说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) InitChain Request。  
**例**：[InitChain ≠ bundled（387）](../../tracks/implementation/worked-example-inittime-notskip-vs-bundled.md)。

## 三个名字

1. **initial_height 不是已经能跳步：** 看见填了起步高，不是已经 320 interchangeable / 769 inittime-notskip interchangeable。
2. **看见填了起步高 不是已经过了崩溃三步：** 看见写成 1，不是已经 320 interchangeable。
3. **看见有高度 不是已经交差：** 看见 InitChain 请求 initial_height，不是已经交差 interchangeable。

官方把 InitChain 请求 time / chain_id / initial_height 三条核心句拆成三个名字。把它们叫成一个「看见叫了 InitChain 就已经过了 genesis_time」，会把三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 InitChain 请求 initial_height 正式三事（387 余量），先数清问的是是不是已经能跳步 / 320、是不是已经过了崩溃三步、还是看见有高度是不是已经交差，再决定要不要同一次发布。387 inittime vs genesis bundled unbundling 在本页 item 3 完成。
