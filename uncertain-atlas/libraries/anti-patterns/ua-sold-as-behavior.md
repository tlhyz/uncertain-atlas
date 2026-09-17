# 反模式：看见协议版本就当成已经是客户端版本 / 看见 user agent 就当成已经可以按实现改行为

**层次**：网络 / 失败模式。  
**分类**：事实（对象）+ 推断（事故）。  
**来源**：[BIP-14](https://github.com/bitcoin/bips/blob/master/bip-0014.mediawiki)。  
**例**：[协议版本 ≠ 客户端版本](../../tracks/network/worked-example-ua-vs-protocol.md)。

## 塌法

1. 看见协议版本，就当成已经是客户端版本，或当成已经是实现版本。
2. 看见实现发了新版本，就当成已经抬了协议。
3. 看见一条 user agent，就当成已经可以按这家实现换规则。
4. 看见同一协议版本，就当成已经是同一套实现。
5. 看见 user agent 里叠了几层名字，就当成已经多了一项协议能力。

## 为什么会出事

官方写：协议版本要从客户端版本里拆开。user agent 只是信息牌。协议不应当随 user agent 改。按实现换协议会把网络撕开。

## 和相邻反模式

- [feature-sold-as-enabled](feature-sold-as-enabled.md) 是协议版本够了 ≠ 已经支持某项功能，不是本页这条拆版本。
- [pong-sold-as-live](pong-sold-as-live.md) 是回了 pong ≠ 已经还活着，不是本页。
- [eip8-sold-as-upgraded](eip8-sold-as-upgraded.md) 是忽略多余字段 ≠ 已经是新协议，不是本页。
