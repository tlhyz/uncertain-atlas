# 模式：点名 rvert-notburn 杠

**层次**：实现 / EIP-140 leftover-gas revert not already INVALID-burn / not already OOG-burn / not already 177-bundled 正式三事（177 余量）。  
**分类**：建议（产品）。  
**来源**：Ethereum [EIP-140](https://eips.ethereum.org/EIPS/eip-140)（Final, Core, REVERT instruction）。  
**对应**：[`../tracks/implementation/worked-example-rvert-notburn-vs-bundled.md`](../tracks/implementation/worked-example-rvert-notburn-vs-bundled.md)。

- **带回剩余气的回滚不是已经烧光 不是已经像非法指令那样烧光剩余气：看见带回剩余气的回滚不是已经烧光，不是已经像非法指令那样烧光剩余气 interchangeable / 1380 rvert-notburn interchangeable。**
- **leftover-gas revert is not already burn 不是已经是气耗尽烧光：看见leftover-gas revert is not already burn，不是已经是气耗尽烧光 interchangeable / 1380 rvert-notburn interchangeable。**
- **带回剩余气的回滚不是已经烧光 不是已经 177 bundled：看见带回剩余气的回滚不是已经烧光，不是已经 177 bundled interchangeable / 1380 rvert-notburn interchangeable。**

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 EIP-7 DELEGATECALL 正式三事（177 余量），必须分开 not already CALLCODE、not already CALL、not already 7702 三件事。
