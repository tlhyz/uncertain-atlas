# 反模式：看见没开布隆服务位就当成已经退役 / 已经改用客户端侧过滤 / 已经私人

**层次**：轻客户端 / 失败模式。  
**分类**：事实（对象）+ 推断（事故）。  
**来源**：[BIP-111](https://github.com/bitcoin/bips/blob/master/bip-0111.mediawiki)。  
**例**：[布隆服务位 ≠ 已经退役](../../tracks/light-clients/worked-example-bloom-bit-vs-retired.md)。

## 塌法

1. 看见没开布隆服务位，就当成全网布隆已经退役，或当成已经改用客户端侧过滤。
2. 看见开了这一位，就当成已经私人，或当成拒绝服务面已经没了。
3. 看见协议版本够了，就当成已经在遵守这一位。
4. 看见因过滤器命令被断开，就当成那些交易已经共识非法。
5. 看见本页，就当成已经写了客户端侧过滤，或当成已经是有限历史服务位。

## 为什么会出事

官方写：旧协议没给布隆单独一位。本页只让这个节点显式宣布或关掉。旧版本仍可能继续服。开了这一位不是已经私人。没开不是全网已经退役。

## 和相邻反模式

- [cfilter-sold-as-have](cfilter-sold-as-have.md) 是过滤器对上 ≠ 已经有块，也不是「支持新协议就已经关掉布隆」。
- [feefilter-sold-as-rejected](feefilter-sold-as-rejected.md) 是费率过滤器 ≠ 已经拒进池，不是本页。
- [limited-service-sold-as-archive](limited-service-sold-as-archive.md) 是有限历史服务位 ≠ 已经是归档，不是本页。
