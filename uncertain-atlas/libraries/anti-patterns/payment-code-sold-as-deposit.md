# 反模式：看见付款码就当成已经是存款地址 / 看见通知输出就当成已经能花 / 看见第一次付款就当成已经不必再通知

**层次**：应用 / 失败模式。  
**分类**：事实（对象）+ 推断（事故）。  
**来源**：[BIP-47](https://github.com/bitcoin/bips/blob/master/bip-0047.mediawiki)。  
**例**：[付款码 ≠ 已经是存款地址](../../tracks/lifecycle/worked-example-payment-code-vs-notification.md)。

## 塌法

1. 看见付款码 / 看见公开身份，就当成已经是存款地址，或当成已经付过。
2. 看见通知交易 / 看见通知地址上有输出，就当成已经是付款，或当成已经能花。
3. 看见已经收过，就当成已经可以免通知，或当成往回打也不必再通知。
4. 看见从种子找回，就当成发出去的通知名单还在，或当成已经不必再发通知。
5. 看见 352 不必链上通知，就当成已经是本页。

## 为什么会出事

官方写：第一次付款前必须先发通知交易。通知地址上收到的输出不得显示为可花余额。即使以前收过，第一次往回打仍必须先发通知。从种子找回之后必须当成新钱包再发通知。这和 352 官方写成不必再发链上通知不是同一句。

## 和相邻反模式

- [silent-payment-sold-as-output](silent-payment-sold-as-output.md) 是静默付款地址 ≠ 已经有输出，不是本页这条必须通知。
- [derived-sold-as-output-key](derived-sold-as-output-key.md) 是派生钥 ≠ 已经是输出钥，不是本页。
- [xpub-sold-as-spendable](xpub-sold-as-spendable.md) 是扩展公钥 ≠ 已经能花，不是本页。
