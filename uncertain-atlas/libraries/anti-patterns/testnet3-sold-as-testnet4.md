# 反模式：看见 Testnet 4 就当成已经是 Testnet 3 / 看见 20 分钟例外就当成已经没有块风暴 / 看见会 Testnet 3 就当成已经能安全跟 Testnet 4

**层次**：应用 / 失败模式。  
**分类**：事实（对象）+ 推断（事故）。  
**来源**：[BIP-94](https://github.com/bitcoin/bips/blob/master/bip-0094.mediawiki)。  
**例**：[Testnet 4 ≠ 已经是 Testnet 3](../../tracks/implementation/worked-example-testnet4-vs-testnet3.md)。

## 塌法

1. 看见 Testnet 4 / 看见测试币，就当成已经是 Testnet 3，或当成已经是主网，或当成测试币已经没价值。
2. 看见 20 分钟例外 / 看见最低难度，就当成已经没有块风暴，或当成已经拿掉了例外。
3. 看见会 Testnet 3 / 只加了网络参数，就当成已经能安全跟 Testnet 4，或当成已经在验新规则。
4. 看见和主网同一套软分叉，就当成已经是同一条网。
5. 看见 signet，就当成已经是本页。

## 为什么会出事

官方写：本页目标是替换 Testnet 3；测试币被买卖，说明「没价值」这条底已经被破。20 分钟例外还留着；块风暴的修法是调难度改取上一周期第一块。只实现 Testnet 3 规则的节点会收下违反 Testnet 4 的链，因而会被分叉甩开。

## 和相邻反模式

- [signet-sold-as-testnet](signet-sold-as-testnet.md) 是 signet ≠ 已经是 testnet / 工作量 ≠ 已经签过，不是本页这条换网。
- [duplicate-txid-sold-as-unique](duplicate-txid-sold-as-unique.md) 是同一标识 ≠ 已经唯一，不是本页。
- [policy-sold-as-consensus](policy-sold-as-consensus.md) 是策略 ≠ 已经是共识，不是本页这条测试网自己的规则。
