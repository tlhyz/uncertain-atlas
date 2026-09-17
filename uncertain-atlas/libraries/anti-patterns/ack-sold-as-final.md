# 反模式：看见付款请求就当成已经授权 / 看见付款报文就当成已经是回执 / 看见回执就当成已经最终

**层次**：应用 / 失败模式。  
**分类**：事实（对象）+ 推断（事故）。  
**来源**：[BIP-70](https://github.com/bitcoin/bips/blob/master/bip-0070.mediawiki)。  
**例**：[付款请求 ≠ 已经是回执](../../tracks/lifecycle/worked-example-request-vs-ack.md)。

## 塌法

1. 看见付款请求 / 看见商家名字 / 看见证书身份，就当成已经授权，或当成已经是那条地址，或当成已经付过。
2. 看见付款报文 / 看见里面有签过的交易，就当成已经是回执，或当成商家已经收下，或当成已经有确认。
3. 看见回执 / 看见「已收到」那句备忘，就当成已经最终，或当成已经确认。
4. 看见退款输出，就当成已经退过。
5. 看见身份类型写成「没有」，就当成已经核过商家。

## 为什么会出事

官方写：钱包必须先核身份和过期，再问顾客要不要提交。商家收到付款报文，必须自己判断是否满足条件，只有满足才应当再广播。回执备忘可以只是「已收下、正在处理」，后继回执还可以改确认数。

## 和相邻反模式

- [uri-sold-as-authorized](uri-sold-as-authorized.md) 是付款 URI ≠ 已经授权，不是本页这三份消息。
- [original-sold-as-payjoin](original-sold-as-payjoin.md) 是原始包 ≠ 已经是 payjoin，不是本页。
- [legacy-sign-sold-as-322](legacy-sign-sold-as-322.md) 是旧式签消息 ≠ 已经是 322，不是本页。
- [address-sold-as-utxo](address-sold-as-utxo.md) 是地址串 ≠ 已经有输出，不是本页。
