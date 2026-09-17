# 反模式：看见协议版本够了就当成已经支持某项功能 / 看见 feature 就当成已经启用

**层次**：网络 / 失败模式。  
**分类**：事实（对象）+ 推断（事故）。  
**来源**：[BIP-434](https://github.com/bitcoin/bips/blob/master/bip-0434.md)。  
**例**：[协议版本 ≠ 已经启用功能](../../tracks/network/worked-example-feature-vs-enabled.md)。

## 塌法

1. 看见协议版本够了，就当成已经支持某项功能，或当成已经实现本页。
2. 看见一条 `feature` 通告，就当成已经启用，或当成已经理解。
3. 看见不认识的 `featureid`，就当成已经非法，或当成已经必须断开。
4. 看见 `verack` 之后才来的 `feature`，就当成已经是本页协商，或当成已经启用。
5. 看见忽略了不认识的消息，就当成已经实现本页。

## 为什么会出事

官方写：本页是为了以后不必再协调改协议版本。必须忽略不支持的标识。必须把发送窗钉在 `verack` 之前。没通过本页表示支持，就不得在 `verack` 之后发该功能引入的消息。

## 和相邻反模式

- [disabletx-sold-as-lifetime](disabletx-sold-as-lifetime.md) 是版本里关掉转发 ≠ 已经终身只传块，不是本页这条功能协商。
- [sendheaders-sold-as-have](sendheaders-sold-as-have.md) 是发了 sendheaders ≠ 已经有块，不是本页。
- [wtxidrelay-sold-as-have](wtxidrelay-sold-as-have.md) 是按 wtxid 通告 ≠ 已经有交易，不是本页。
