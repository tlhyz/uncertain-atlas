# 反模式：看见协议版本够了就当成已经会 pong / 看见 pong 就当成已经对上 / 看见回了就当成已经还活着

**层次**：网络 / 失败模式。  
**分类**：事实（对象）+ 推断（事故）。  
**来源**：[BIP-31](https://github.com/bitcoin/bips/blob/master/bip-0031.mediawiki)。  
**例**：[pong ≠ 已经还活着](../../tracks/network/worked-example-pong-vs-live.md)。

## 塌法

1. 看见协议版本够了，就当成已经会带 nonce 的 ping，或当成对端已经会回 pong。
2. 看见一条 pong，就当成已经对上刚发的那一次 ping。
3. 看见 nonce 是零，就当成已经测过往返，或当成已经重叠过。
4. 看见回了 pong，就当成已经还活着，或当成已经不卡，或当成已经是睡前那个人。
5. 看见测到一次往返，就当成已经永远响应。

## 为什么会出事

官方写：必须自己抬版本才能加入；旧客户端不会被送来 pong。nonce 用来在重叠时把答复分开。本页是发现死连接、测负载、测远近的工具，不是一次绿灯。

## 和相邻反模式

- [feature-sold-as-enabled](feature-sold-as-enabled.md) 是协议版本够了 ≠ 已经支持某项功能，不是本页这条探活。
- [enr-seq-sold-as-have](enr-seq-sold-as-have.md) 是发现 ping 里的记录序号 ≠ 已经有当前记录，不是本页。
- [disabletx-sold-as-lifetime](disabletx-sold-as-lifetime.md) 是关掉转发 ≠ 已经终身只传块，不是本页。
