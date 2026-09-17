# 模式：点名 genesis-nottime 杠

**层次**：实现 / 进程起来 not already past-genesis-time / not already handshake-ready / not already settled 正式三事（303 余量）。  
**分类**：建议（产品）。  
**来源**：CometBFT 官方 [Genesis](https://github.com/cometbft/cometbft/blob/main/spec/core/genesis.md) genesis file / app_state。  
**对应**：[`../tracks/implementation/worked-example-genesis-nottime-vs-bundled.md`](../tracks/implementation/worked-example-genesis-nottime-vs-bundled.md)。

- **进程起来 不是已经开出块：** 看见进程起来了，不是已经开出块 interchangeable / 987 genesis-nottime interchangeable。
- **看见握手过了 不是已经过了创世时间：** 看见握手过了，不是已经过了创世时间 interchangeable。
- **看见本机钟到了 不是已经交差：** 看见本机钟到了，不是邻居已经一起动 interchangeable。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看进程起来 正式三事（303 余量），先数清问的是是不是已经开出块、是不是已经过了创世时间、还是看见本机钟到了是不是已经交差，再决定要不要同一次发布。303 genesis vs app bundled unbundling 在本页 item 2 续。
