# 模式：把 CheckTx Usage Code≠0 rejected not in-pool gossip / not CheckTx guard bundled / not broadcast_tx received 正式三事（489 余量）说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) CheckTx Usage。  
**例**：[Code≠0 rejected not in-pool gossip ≠ bundled（489）](../../tracks/implementation/worked-example-chktxcodereject-notgossip-vs-bundled.md)。

## 三个名字

1. **Code≠0 will be rejected 不是已经进池就开始流言：** 看见 Methods Usage 会拒，不是已经 P2P 流言出去 interchangeable，不是 686 chktxcodereject-notgossip interchangeable。
2. **看见会拒 不是守卫 bundled 就代表 Code 验完：** 看见 rejected，不是已经 Guardian 第一句 interchangeable，不是 405 checktxguard interchangeable。
3. **看见 rejected 不是 broadcast_tx 别人也会收：** 看见 Usage Code 拒，不是已经 RPC 回了别人也会收 interchangeable，不是 301 bundled interchangeable。

官方把 CheckTx Usage Code≠0 拒、进池流言、守卫 bundled、broadcast_tx received 写成三个名字。把它们叫成一个「看见 CheckTx 回了非零码就已经流言出去」，会把 not gossip、not guard bundled、not broadcast_tx received 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 CheckTx Usage Code≠0 rejected 正式三事（489 余量），先数清问的是会拒 是不是已经流言、是不是守卫 bundled / 405、还是看见 rejected 是不是别人也会收 / 301，再决定要不要同一次发布。489 chktxcodereject vs proposal bundled unbundling 在本页 item 1 启动。
