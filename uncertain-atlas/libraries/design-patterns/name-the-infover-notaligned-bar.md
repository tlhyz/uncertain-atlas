# 模式：把 block_version / p2p_version not already versions aligned / not already full history / not already settled 正式三事（379 余量） 说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) Info Request。  
**例**：[block_version ≠ bundled（379）](../../tracks/implementation/worked-example-infover-notaligned-vs-bundled.md)。

## 三个名字

1. **两列 不是已经版本也对上：** 看见填了两列，不是已经 323 interchangeable / 792 infover-notaligned interchangeable。
2. **看见填了两列 不是已经有完整历史：** 看见有块版本，不是已经有完整历史 interchangeable。
3. **看见有 P2P 版本 不是已经交差：** 看见 block_version / p2p_version，不是已经交差 interchangeable。

官方把 Info 请求 version / block_version / p2p_version / abci_version 三条核心句拆成三个名字。把它们叫成一个「看见 Info 请求带了版本就已经是 app_version」，会把三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 block_version / p2p_version 正式三事（379 余量），先数清问的是是不是已经版本也对上 / 323、是不是已经有完整历史、还是看见有 P2P 版本是不是已经交差，再决定要不要同一次发布。379 infover vs appversion bundled unbundling 在本页 item 2 续。
