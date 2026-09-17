# 反模式：看见静默付款地址就当成已经有输出 / 看见扫过就当成已经收到 / 看见再用就当成已经同一笔

**层次**：应用 / 失败模式。  
**分类**：事实（对象）+ 推断（事故）。  
**来源**：[BIP-352](https://github.com/bitcoin/bips/blob/master/bip-0352.mediawiki)。  
**例**：[静默付款地址 ≠ 已经有输出](../../tracks/lifecycle/worked-example-silent-payment-vs-output.md)。

## 塌法

1. 看见一条静默付款地址，就当成已经有一笔链上输出，或当成已经付过。
2. 看见扫过一遍，就当成已经收到，或当成已经能从冷存花。
3. 看见同一条码再用，就当成已经同一笔脚本，或当成已经把各次付款连上。
4. 看见没有链上通知，就当成已经没有付款。
5. 看见专用编码过了校验，就当成已经是旧的见证地址方案。

## 为什么会出事

官方写：静态码不是链上输出。每一次静默付款都走到一个新地址。必须扫链才能发现。扫描和花费分开。链下通知只是把风险挪走。轻客户端怎么扫仍在研究。

## 和相邻反模式

- [address-sold-as-utxo](address-sold-as-utxo.md) 是看见地址串 ≠ 已经有输出，不是本页这条静态码。
- [uri-sold-as-authorized](uri-sold-as-authorized.md) 是看见付款 URI ≠ 已经授权，不是本页。
- [xpub-sold-as-spendable](xpub-sold-as-spendable.md) 是看见扩展公钥 ≠ 已经能花，不是本页。
- [signed-message-sold-as-control](signed-message-sold-as-control.md) 是看见签过 ≠ 已经控制资金，不是本页。
