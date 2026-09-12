# 反模式：看见发了 sendheaders 就当成已经有块 / 已经改用头通告 / 重组已经处理完

**层次**：网络 / 失败模式。  
**分类**：事实（对象）+ 推断（事故）。  
**来源**：[BIP-130](https://github.com/bitcoin/bips/blob/master/bip-0130.mediawiki)。  
**例**：[头通告偏好 ≠ 已经有块](../../tracks/network/worked-example-sendheaders-vs-have.md)。

## 塌法

1. 看见发了 sendheaders，就当成已经改用头通告，或当成已经有那块。
2. 看见协议版本够了，就当成已经在发、或已经在遵守。
3. 看见用头通告新尖，就当成块已经在手里，或当成头先同步已经做完。
4. 看见重组时先发了头，就当成中间块已经在手里，或当成重组已经处理完。
5. 看见本页，就当成已经写了宣布≠收到，或当成已经是 compact 拼块，或当成已经是后继地址偏好。

## 为什么会出事

官方写：这条空消息只表示更想用头收通告。改用头通告是许可，不是必须。先发头是为了少一次回头要头、让中间块能立刻要，不是块已经到了。

## 和相邻反模式

- [addrv2-sold-as-reachable](addrv2-sold-as-reachable.md) 是后继地址 ≠ 已经连得上，不是本页。
- [cfilter-sold-as-have](cfilter-sold-as-have.md) 是过滤器对上 ≠ 已经有块，不是本页。
- [header-equals-settlement](header-equals-settlement.md) 是只看头就放货，不是本页。
