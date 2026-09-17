# 协议档案轨

一条链（或一个通过过滤器的品类）一份档案，**固定 19 节**。

课程讲原理。这里讲「这个项目具体怎么选、付了什么代价」。

模板：[`_template.md`](_template.md)

## 进度

| 对象 | 目录 | 状态 |
|---|---|---|
| Bitcoin | [bitcoin/](bitcoin/README.md) | 第一版 |
| Cosmos / CometBFT | [cometbft/](cometbft/README.md) | 第一版 |
| Ethereum | [ethereum/](ethereum/README.md) | 第一版 |
| Avalanche | [avalanche/](avalanche/README.md) | 第一版（对照） |
| Solana | [solana/](solana/README.md) | 第一版 |
| Sui | [sui/](sui/README.md) | 第一版 |
| Aptos | [aptos/](aptos/README.md) | 第一版 |
| Celestia | [celestia/](celestia/README.md) | 第一版 |
| Polkadot | [polkadot/](polkadot/README.md) | 第一版 |
| Zcash | [zcash/](zcash/README.md) | 第一版 |
| Monero | [monero/](monero/README.md) | 第一版 |
| Mina | [mina/](mina/README.md) | 第一版 |
| 乐观 Rollup（Arbitrum / Optimism 对照） | [optimistic-rollup/](optimistic-rollup/README.md) | 第一版（品类）；`unsafe` ≠ 已推导（不变量 141）；DACert ≠ 已贴文（不变量 142） |
| Algorand | [algorand/](algorand/README.md) | 第一版（抽签对照） |
| Kaspa | [kaspa/](kaspa/README.md) | 第一版（块 DAG 对照） |
| Fuel | [fuel/](fuel/README.md) | 第一版（思想级 UTXO 调度）；谓词 ≠ 脚本（不变量 143） |
| Nervos CKB | [nervos/](nervos/README.md) | 第一版（思想级：占用 / 生成验证分离） |
| NEAR Nightshade | [near/](near/README.md) | 第一版（思想级：一条链 + chunk） |
| Babylon | [babylon/](babylon/README.md) | 仅过滤器页（UTXO 仍在 Bitcoin；k-deep ≠ commit） |
| QRL | [qrl/](qrl/README.md) | 仅过滤器页（XMSS + OTS index） |
| Monad | [monad/](monad/README.md) | 仅过滤器页（共识先定序，再 Apply） |
| EigenLayer | [eigenlayer/](eigenlayer/README.md) | 仅过滤器页（AVS 罚没 ≠ Casper） |
| Starknet | [starknet/](starknet/README.md) | 仅过滤器页（SNOS 程序哈希 + 四档最终性） |

其余第 8 波：有状态 HBS 思想已入 `tracks/post-quantum/stateful-hbs.md`。其它「PQ 品牌链」仍先过过滤器。

## 永久过滤器（2026-09-17 声明）

下列对象**故意不写 19 节**，直到 L10.1 记录要求升级。过滤器页 + 对应不变量即完成标准。禁止为凑数而扩档。

| 对象 | 为何停在过滤器 | 升级条件 |
|---|---|---|
| Cardano | 仅 eUTXO 思想；见 L2.5 / 不变量 150 | 第一版要附件 datum 再开 19 节 |
| Babylon | k-deep ≠ commit（139） | 不确定要锁 BTC 再开 |
| EigenLayer | AVS ≠ Casper（140） | 不确定要 restake 再开 |
| QRL | 只对照 XMSS/OTS | PQ 账本测完再决定是否扩 |
| Monad | 先定序再 Apply | 吞吐专题需要对照实现时再开 |
| Starknet | 四档最终性过滤器（138） | 有效性证明进 v1 再开（默认不要） |
