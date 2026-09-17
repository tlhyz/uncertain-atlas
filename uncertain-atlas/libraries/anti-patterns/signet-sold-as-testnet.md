# 反模式：看见 signet 就当成已经是 testnet / 看见 signet 就当成已经是 regtest / 看见工作量过了就当成已经签过

**层次**：应用 / 失败模式。  
**分类**：事实（对象）+ 推断（事故）。  
**来源**：[BIP-325](https://github.com/bitcoin/bips/blob/master/bip-0325.mediawiki)。  
**例**：[signet ≠ 已经是 testnet](../../tracks/implementation/worked-example-signet-vs-testnet.md)。

## 塌法

1. 看见 signet，就当成已经是 testnet，或当成已经和 testnet 一样不可靠。
2. 看见它比 testnet 稳，就当成已经和主网同一套结算。
3. 看见 signet，就当成已经是 regtest，或当成任何一方都能完全控制。
4. 看见头上有合法工作量 / 只加了网络参数就能连上，就当成已经签过，或当成已经全验证通过。
5. 看见同一份创世，就当成已经是同一条 signet。

## 为什么会出事

官方写：testnet 出了名不可靠；regtest 造块没有代价，任何一方都能完全控制。signet 要的是可预期的不可靠。头上有工作量只是「大概」合法；全验证必须验 coinbase 里的块签名，或只连受信任的人。创世相同，消息起始字节由挑战决定。

## 和相邻反模式

- [duplicate-txid-sold-as-unique](duplicate-txid-sold-as-unique.md) 是主网同一标识 ≠ 已经唯一，不是本页这条测试网。
- [dummy-sold-as-unused](dummy-sold-as-unused.md) 是 dummy ≠ 已经随便填，不是本页。
- [txid-sold-as-wtxid](txid-sold-as-wtxid.md) 是两个哈希不是一回事，不是本页。
