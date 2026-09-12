# 反模式：看见签过的节点记录就当成已经是最新一份 / 已经发现 / 已经换了身份方案

**层次**：网络 / 失败模式。  
**分类**：事实（对象）+ 推断（事故）。  
**来源**：[EIP-778](https://eips.ethereum.org/EIPS/eip-778)。  
**例**：[节点记录 ≠ 已经最新](../../tracks/network/worked-example-enr-vs-newest.md)。

## 塌法

1. 看见签过的记录，就当成已经有可连地址，或当成已经从发现里找到。
2. 看见记录有效，就当成已经是最新一份；或看见序号，就当成全网已经换完。
3. 看见多出来的键被收下，就当成这些键已经被解释，或当成身份方案已经换。
4. 看见默认方案名，就当成已经换了发现协议，或当成新身份方案已经被网络接受。
5. 看见文本前缀记录或 DNS / ENS 转发，就当成已经信任这个邻居。

## 为什么会出事

官方写：没有端点仍可有效；加新键不要求共识，换身份方案要。签过不是已经比过序号。转发通道不是发现已经齐，也不是信任已经齐。

## 和相邻反模式

- [forkid-sold-as-same-chain](forkid-sold-as-same-chain.md) 是分叉标识 ≠ 已经同一条链，不是本页。
- [eip8-sold-as-upgraded](eip8-sold-as-upgraded.md) 是忽略版本 ≠ 已经在说新协议，不是本页。
- [window-sold-as-consensus](window-sold-as-consensus.md) 是历史窗 / 7642，不是本页。
- [inbound-cap-sold-as-handshake](inbound-cap-sold-as-handshake.md) 是握手配额，不是本页。
