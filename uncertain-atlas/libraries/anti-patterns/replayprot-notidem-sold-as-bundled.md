# 反模式：把 通常不受欢迎 not already no-exception / not already pool-guaranteed / not already settled 正式三事（313 余量） 写成已经 已经没有幂等例外 / 已经由内存池保证 / 已经交差

**层次**：实现 / 通常不受欢迎 not already no-exception / not already pool-guaranteed / not already settled 正式三事（313 余量）。  
**分类**：建议（产品）。  
**来源**：CometBFT 官方 [Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Replay Protection。  
**对应**：[`../tracks/implementation/worked-example-replayprot-notidem-vs-bundled.md`](../tracks/implementation/worked-example-replayprot-notidem-vs-bundled.md)。

把 通常不受欢迎 not already no-exception / not already pool-guaranteed / not already settled 正式三事（313 余量） 写成已经 已经没有幂等例外 / 已经由内存池保证 / 已经交差，就是本页。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看通常不受欢迎 正式三事（313 余量），必须分开 not already no-exception、not already pool-guaranteed、not already settled 三件事，不要和 313 / 161 / 314 / 965 / 966 糊成一句。

也不是：

- [replayprot-notapp-sold-as-bundled](replayprot-notapp-sold-as-bundled.md) 是过了 CheckTx 仍无应用级保护单句边界（966 item 2），不是本页通常不受欢迎仍有幂等例外边界。
- JSON chainId 已经编进签名哈希是不变量 161，不是本页幂等仍不是内存池保证边界。
