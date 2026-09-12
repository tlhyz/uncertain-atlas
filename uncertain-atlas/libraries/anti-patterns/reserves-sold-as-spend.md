# 反模式：看见储备证明交易就当成已经能花 / 看见其余输入签过就当成已经控制资金 / 看见 POR 栏就当成已经是普通花费

**层次**：应用 / 失败模式。  
**分类**：事实（对象）+ 推断（事故）。  
**来源**：[BIP-127](https://github.com/bitcoin/bips/blob/master/bip-0127.mediawiki)。  
**例**：[储备证明交易 ≠ 已经能花](../../tracks/lifecycle/worked-example-reserves-vs-spend.md)。

## 塌法

1. 看见储备证明交易 / 看见普通交易序列化，就当成已经能花，或当成已经能确认。
2. 看见其余输入签过 / 看见承诺了消息，就当成已经是 258 那种控制资金，或当成已经付过，或当成现在还能花。
3. 看见 POR 栏 / 看见硬件钱包弹出确认，就当成已经是普通花费，或当成已经有前一笔未花输出。
4. 看见没有矿工费，就当成已经是付款。
5. 看见某一块时有过，就当成隐私已经齐，或当成已经是更藏余额的那种证明。

## 为什么会出事

官方写：第一笔输入让这笔永远确认不了。其余输入的签名必须承诺到承诺输入；它核的是某一块时有过，不管那之后。承诺输入并不花掉链上已有的未花输出；设备若不认得，会问是不是要把这些币全部打走。

## 和相邻反模式

- [signed-message-sold-as-control](signed-message-sold-as-control.md) 是签过 ≠ 已经控制资金，不是本页这种不能确认的交易。
- [psbt-sold-as-broadcast](psbt-sold-as-broadcast.md) 是部分签名包 ≠ 已经能广播，不是本页。
- [xpub-sold-as-spendable](xpub-sold-as-spendable.md) 是扩展公钥 ≠ 已经能花，不是本页。
- [address-sold-as-utxo](address-sold-as-utxo.md) 是地址串 ≠ 已经有输出，不是本页。
