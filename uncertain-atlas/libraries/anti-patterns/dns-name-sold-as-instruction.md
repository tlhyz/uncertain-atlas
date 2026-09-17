# 反模式：看见可读名字就当成已经该走 DNS / 看见 TXT 就当成已经合法 / 看见复制了名字就当成已经是 URI

**层次**：应用 / 失败模式。  
**分类**：事实（对象）+ 推断（事故）。  
**来源**：[BIP-353](https://github.com/bitcoin/bips/blob/master/bip-0353.mediawiki)。  
**例**：[可读名字 ≠ 已经该走 DNS](../../tracks/lifecycle/worked-example-dns-name-vs-instruction.md)。

## 塌法

1. 看见可读名字，就当成已经该走 DNS，或当成已经比地址更好。
2. 看见一条 TXT，就当成已经是合法付款指示，或当成远端解析器已经核过。
3. 看见同一标签上多条记录，就当成可以挑一条用。
4. 看见复制了可读名字，就当成已经复制了 URI，或当成缓存已经不过期。
5. 看见 DNS 还没过期，就当成里面的报价还有效。

## 为什么会出事

官方写：有地址或 URI 就必须优先用那个。必须以「bitcoin:」开头，多条则整组非法。必须自己验 DNSSEC 到根，不得让远端代验。缓存不得超过 TTL。复制应当复制 URI。

## 和相邻反模式

- [uri-sold-as-authorized](uri-sold-as-authorized.md) 是看见付款 URI ≠ 已经授权，不是本页这条 DNS 名字。
- [silent-payment-sold-as-output](silent-payment-sold-as-output.md) 是看见静默付款地址 ≠ 已经有输出，不是本页。
- [address-sold-as-utxo](address-sold-as-utxo.md) 是看见地址串 ≠ 已经有输出，不是本页。
