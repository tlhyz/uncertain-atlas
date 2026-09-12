# 反模式：看见版本里关掉交易转发就当成已经终身只传块 / 已经没有紧凑块 / 已经禁止传地址

**层次**：网络 / 失败模式。  
**分类**：事实（对象）+ 推断（事故）。  
**来源**：[BIP-338](https://github.com/bitcoin/bips/blob/master/bip-0338.mediawiki)。  
**例**：[停交易转发 ≠ 已经终身只传块](../../tracks/network/worked-example-disabletx-vs-lifetime.md)。

## 塌法

1. 看见版本里关掉了交易转发，就当成已经发了本页，或当成已经终身只传块。
2. 看见发了本页，就当成费率过滤器 / 内存池查询 / 布隆已经退役，或当成已经没有块。
3. 看见发了本页，就当成已经禁止传地址，或当成已经断开。
4. 看见协议版本够了，就当成已经实现本页。
5. 看见本页状态是关闭，就当成网上已经默认这样谈。

## 为什么会出事

官方写：版本里的交易转发字段不是终身设定。本页才是这条连接的终身信号。发过或收过本页，不得再发交易类消息，但紧凑块仍允许。地址建议关掉，不是必须。节点可以决定不跟发了本页的人继续连。关闭状态不是已经在主网默认打开。

## 和相邻反模式

- [feefilter-sold-as-rejected](feefilter-sold-as-rejected.md) 是费率过滤器 ≠ 已经拒进池，不是本页这条终身信号。
- [mempool-dump-sold-as-have](mempool-dump-sold-as-have.md) 是内存池查询 ≠ 已经有那些交易，不是本页。
- [bloom-bit-sold-as-retired](bloom-bit-sold-as-retired.md) 是没开布隆位 ≠ 已经退役，不是本页。
- [addrv2-sold-as-reachable](addrv2-sold-as-reachable.md) 是后继地址 ≠ 已经连得上，不是本页。
