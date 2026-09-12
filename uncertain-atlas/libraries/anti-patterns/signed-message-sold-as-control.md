# 反模式：看见签过的消息就当成已经控制资金 / 已经付过 / 清单已经齐

**层次**：应用 / 失败模式。  
**分类**：事实（对象）+ 推断（事故）。  
**来源**：[BIP-322](https://github.com/bitcoin/bips/blob/master/bip-0322.mediawiki)。  
**例**：[签过的消息 ≠ 已经控制资金](../../tracks/lifecycle/worked-example-signed-message-vs-control.md)。

## 塌法

1. 看见验过一条签消息，就当成已经能花，或当成已经肯签真正的交易。
2. 看见签过，就当成已经证明发过上一笔，或当成已经付过款。
3. 看见资金证明清单，就当成已经齐，或当成已经没花。
4. 看见长得像交易的签，就当成已经能广播。
5. 看见离线验过，就当成链上状态已经核过。

## 为什么会出事

官方写：没有任何签消息协议真能证明控制资金。签名一做出来就已经过时。握着密钥的人可以愿意替别人签消息，却不肯签真正的交易。本页证明发过上一笔做不到。清单不齐，未花必须问链。

## 和相邻反模式

- [uri-sold-as-authorized](uri-sold-as-authorized.md) 是看见付款 URI ≠ 已经授权，不是本页这条签消息。
- [address-sold-as-utxo](address-sold-as-utxo.md) 是看见地址串 ≠ 已经有输出，不是本页。
- [psbt-sold-as-broadcast](psbt-sold-as-broadcast.md) 是看见部分签名包 ≠ 已经能广播，不是本页。
