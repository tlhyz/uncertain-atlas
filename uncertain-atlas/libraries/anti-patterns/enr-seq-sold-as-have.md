# 反模式：看见 ping 带了记录序号就当成已经有当前记录 / 已经解析 / 已经没有放大

**层次**：网络 / 失败模式。  
**分类**：事实（对象）+ 推断（事故）。  
**来源**：[EIP-868](https://eips.ethereum.org/EIPS/eip-868)。  
**例**：[发现要记录 ≠ 已经有](../../tracks/network/worked-example-enr-request-vs-have.md)。

## 塌法

1. 看见 ping / pong 带了序号，就当成已经拿到当前记录，或当成两边序号对上就已经取回记录。
2. 看见能发请求，就当成已经解析完；或看见回了记录，就当成已经核过是答复者签的。
3. 看见协议里有请求，就当成放大面已经消失。
4. 看见 FindNode 找到人，就当成已经有记录，或当成已经信任。
5. 看见本页，就当成已经写了记录格式，或当成 DNS 转发已经齐。

## 为什么会出事

官方写：ping 只通告序号；当前记录要另发请求。答复必须核签。请求和 FindNode 同一条放大防护。查找找到人不是记录已经在手里。

## 和相邻反模式

- [enr-sold-as-newest](enr-sold-as-newest.md) 是记录格式 ≠ 已经最新，不是本页。
- [forkid-sold-as-same-chain](forkid-sold-as-same-chain.md) 是分叉标识 ≠ 已经同一条链，不是本页。
- [eip8-sold-as-upgraded](eip8-sold-as-upgraded.md) 是忽略版本 ≠ 已经在说新协议，不是本页。
- [inbound-cap-sold-as-handshake](inbound-cap-sold-as-handshake.md) 是握手配额，不是本页。
