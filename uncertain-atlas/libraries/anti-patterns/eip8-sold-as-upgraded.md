# 反模式：看见忽略版本 / 多余字段就当成已经在说新协议 / 已经改了共识 / 已经退役旧握手

**层次**：网络 / 失败模式。  
**分类**：事实（对象）+ 推断（事故）。  
**来源**：[EIP-8](https://eips.ethereum.org/EIPS/eip-8)。  
**例**：[忽略版本 ≠ 已经在说新协议](../../tracks/network/worked-example-eip8-vs-already-new.md)。

## 塌法

1. 看见对方没因版本号断开，就当成两边已经谈成新功能。
2. 看见能吞多余列表元素，就当成发现或握手已经升级完。
3. 看见本页跟 Homestead 一起上，就当成已经改了共识，或当成已经写了交易创建 / 高 `s` / 空合约 / 难度。
4. 看见仍接受旧第 4 版包，就当成旧握手已经退役；或反过来，看见新编码，就当成旧节点已经消失。
5. 看见明文长度前缀，就当成已经抗审查，或当成身份已经暴露。

## 为什么会出事

官方写：更低版本的节点会盲目假定对端向后兼容。能连上不是能力协商已经齐。类别是 Networking，不是 Core。向后兼容写明旧第 4 版包仍合法。

## 和相邻反模式

- [homestead-sold-as-create](homestead-sold-as-create.md) 是共识四件事，不是本页。
- [window-sold-as-consensus](window-sold-as-consensus.md) 是历史窗 / 7642，不是本页。
- [inbound-cap-sold-as-handshake](inbound-cap-sold-as-handshake.md) 是握手配额，不是本页。
