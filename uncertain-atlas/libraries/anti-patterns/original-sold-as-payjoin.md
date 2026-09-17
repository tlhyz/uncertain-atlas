# 反模式：看见带 pj= 的付款 URI 就当成已经是 payjoin 付款 / 看见原始包就当成已经是提案 / 看见收款方加了输入就当成已经另开一笔

**层次**：应用 / 失败模式。  
**分类**：事实（对象）+ 推断（事故）。  
**来源**：[BIP-78](https://github.com/bitcoin/bips/blob/master/bip-0078.mediawiki)。  
**例**：[带 pj= 的付款 URI ≠ 已经是 payjoin 付款](../../tracks/lifecycle/worked-example-payjoin-vs-original.md)。

## 塌法

1. 看见带 `pj=` 的付款 URI / 看见 payjoin 端点，就当成已经是原始包，或当成已经是提案，或当成已经是 payjoin 付款。
2. 看见原始包，就当成已经是 Payjoin 提案，或当成已经是 Payjoin 交易。
3. 看见收款方加了输入 / 看见合并整理，就当成已经另开一笔，或当成已经对全网私人，或当成已经能把 payjoin 交易再当原始包。
4. 看见 `pjos=0`，就当成已经做完 payjoin。
5. 看见不是大家熟知的错误句，就当成已经该给用户看。

## 为什么会出事

官方写：`pj=` 只描述端点；原始包必须能广播，却还不是提案；提案必须用上原始包的全部输入，却还不是已经广播的交易。收款方加输入是为了不另开一笔。原始包里的输入以前见过，就是探测或再入。不是大家熟知的错误句不得上发送方界面。

## 和相邻反模式

- [uri-sold-as-authorized](uri-sold-as-authorized.md) 是付款 URI ≠ 已经授权，不是本页。
- [psbt-sold-as-broadcast](psbt-sold-as-broadcast.md) 是部分签名包 ≠ 已经能广播，不是本页。
- [rbf-sold-as-replaced](rbf-sold-as-replaced.md) 是替换信号 ≠ 已经换掉，不是本页。
- [policy-sold-as-consensus](policy-sold-as-consensus.md) 是策略 ≠ 已经是共识，不是本页。
