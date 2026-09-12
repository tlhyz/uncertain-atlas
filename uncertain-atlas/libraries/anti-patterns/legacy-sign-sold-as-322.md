# 反模式：看见本页这种签消息就当成已经是 322 / 看见头字节标了种类就当成已经有地址 / 看见旧习惯就当成已经互操作

**层次**：应用 / 失败模式。  
**分类**：事实（对象）+ 推断（事故）。  
**来源**：[BIP-137](https://github.com/bitcoin/bips/blob/master/bip-0137.mediawiki)。  
**例**：[本页这种签消息 ≠ 已经是 322](../../tracks/lifecycle/worked-example-legacy-sign-vs-322.md)。

## 塌法

1. 看见本页这种签消息 / 看见用私钥签过一条消息，就当成已经是 322，或当成已经控制资金。
2. 看见头字节标了地址种类，就当成已经有那条地址，或当成已经有一笔能花的输出。
3. 看见旧的 P2PKH 签消息习惯 / 看见本页这种格式，就当成已经互操作，或当成所有旧校验器已经肯收。
4. 看见为了兼容还在用本页，就当成 322 已经没必要。
5. 看见覆盖了旧地址，就当成隔离见证那种头已经到处能过。

## 为什么会出事

官方写：后来另有一套签消息格式，好处比本页多；本页留下来是为了兼容。若不另定标准，就分不清面前这份签对应哪一种地址。有的软件会检查头字节落在哪一段，会把较新的隔离见证头当成错误。

## 和相邻反模式

- [signed-message-sold-as-control](signed-message-sold-as-control.md) 是签过 ≠ 已经控制资金，不是本页这种旧格式不是已经是 322。
- [reserves-sold-as-spend](reserves-sold-as-spend.md) 是储备证明交易 ≠ 已经能花，不是本页。
- [address-sold-as-utxo](address-sold-as-utxo.md) 是地址串 ≠ 已经有输出，不是本页这种头字节。
- [psbt-sold-as-broadcast](psbt-sold-as-broadcast.md) 是部分签名包 ≠ 已经能广播，不是本页。
