# 反模式：看见分叉标识对上就当成已经同一条链 / 已经兼容 / 已经改了共识

**层次**：网络 / 失败模式。  
**分类**：事实（对象）+ 推断（事故）。  
**来源**：[EIP-2124](https://eips.ethereum.org/EIPS/eip-2124)。  
**例**：[分叉标识 ≠ 已经同一条链](../../tracks/network/worked-example-forkid-vs-same-chain.md)。

## 塌法

1. 看见分叉哈希对上，就当成已经同一条链，或当成创世相同就够了。
2. 看见通告了下一分叉，就当成已经兼容；或看见子集 / 超集，就当成已经陈旧 / 已经该升级。
3. 看见硬分叉会拒旧节点，就当成分叉前就已经该踢掉剩下来的节点。
4. 看见握手或发现记录里能嵌这份摘要，就当成已经改了共识，或当成三向分叉已经能分开。
5. 看见四字节摘要，就当成已经是密码学身份。

## 为什么会出事

官方写：必须交叉核对，不能朴素比较。还在同步和软件陈旧不是同一句话。本页类别是 Networking，不定义功能变化。只通告下一次，是因为未来分叉还不确定。

## 和相邻反模式

- [eip8-sold-as-upgraded](eip8-sold-as-upgraded.md) 是忽略版本 ≠ 已经在说新协议，不是本页。
- [window-sold-as-consensus](window-sold-as-consensus.md) 是历史窗 / 7642，不是本页。
- [config-sold-as-aligned](config-sold-as-aligned.md) 是分叉配置 RPC ≠ 已经同根，不是本页。
- [inbound-cap-sold-as-handshake](inbound-cap-sold-as-handshake.md) 是握手配额，不是本页。
