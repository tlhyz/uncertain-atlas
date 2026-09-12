# 反模式：看见共享了扩展公钥就当成已经是链码委托 / 看见委托方那把非扩展钥就当成已经能推出整棵钱包 / 看见这一输入的微调就当成已经是盲签

**层次**：应用 / 失败模式。  
**分类**：事实（对象）+ 推断（事故）。  
**来源**：[BIP-89](https://github.com/bitcoin/bips/blob/master/bip-0089.mediawiki)。  
**例**：[共享了扩展公钥 ≠ 已经是链码委托](../../tracks/implementation/worked-example-delegation-vs-xpub.md)。

## 塌法

1. 看见共享了扩展公钥 / 看见共享了描述符，就当成已经是链码委托，或当成已经对共同签名人藏住余额。
2. 看见委托方那把非扩展钥对，就当成已经是扩展公钥，或当成已经能推出整棵钱包。
3. 看见这一输入的微调 / 看见一次签名会话，就当成已经看见整棵派生，或当成已经是盲签，或当成已经核过找零金额。
4. 看见能共签，就当成已经交出了签名权。
5. 看见盲签，就当成已经并发安全。

## 为什么会出事

官方写：分扩展公钥或描述符，所有人都能扫链。本页委托的是链码，不是签名权。委托方不得持有链码，受托方的扩展公钥不得回传。这一输入的微调只覆盖本笔；找零微调另算。明文盲签协议并不是并发安全的。

## 和相邻反模式

- [xpub-sold-as-spendable](xpub-sold-as-spendable.md) 是扩展公钥 ≠ 已经能花，不是本页。
- [musig-xpub-sold-as-xpub](musig-xpub-sold-as-xpub.md) 是聚合钥 ≠ 已经是扩展公钥，不是本页。
- [policy-sold-as-descriptor](policy-sold-as-descriptor.md) 是登记过 ≠ 已经批准这笔花，不是本页。
- [psbt-sold-as-setup](psbt-sold-as-setup.md) 是部分签名包 ≠ 已经是跨厂开户，不是本页。
