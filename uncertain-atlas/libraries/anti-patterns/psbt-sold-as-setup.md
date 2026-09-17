# 反模式：看见部分签名包就当成已经是跨厂安全多签开户 / 看见指纹对上就当成已经核过 KEY / 看见 TOKEN 就当成已经是钱包种子

**层次**：应用 / 失败模式。  
**分类**：事实（对象）+ 推断（事故）。  
**来源**：[BIP-129](https://github.com/bitcoin/bips/blob/master/bip-0129.mediawiki)。  
**例**：[部分签名包 ≠ 已经是跨厂安全多签开户](../../tracks/implementation/worked-example-setup-vs-psbt.md)。

## 塌法

1. 看见部分签名包 / 看见签流程，就当成已经是跨厂安全多签开户，或当成成员、脚本类型、派生路径和门限已经核过。
2. 看见指纹对上 / 看见钥记录，就当成已经核过 KEY，或当成各方已经确认同一份。
3. 看见 TOKEN / 看见加密会话，就当成已经是钱包种子，或当成已经防篡改存储，或当成以后已经会用这份配置去长地址。
4. 看见第一地址，就当成对手改不了配置。
5. 看见本页开户，就当成已经批准这一笔花。

## 为什么会出事

官方写：174 理顺了签名，还缺跨厂安全开户。指纹很容易伪造，必须精确比对 KEY。TOKEN 只在开户阶段需要，还可以编成看起来像种子的助记句。存盘防不防篡改、以后会不会用这份配置去长地址，不在本页范围。

## 和相邻反模式

- [psbt-sold-as-broadcast](psbt-sold-as-broadcast.md) 是部分签名包 ≠ 已经能广播，不是本页。
- [policy-sold-as-descriptor](policy-sold-as-descriptor.md) 是登记过 ≠ 已经批准这笔花，不是本页。
- [script-in-path-sold-as-needed](script-in-path-sold-as-needed.md) 是主种子 ≠ 已经够找回，不是本页。
- [entropy-sold-as-seed](entropy-sold-as-seed.md) 是派生熵 ≠ 已经是目标种子，不是本页。
