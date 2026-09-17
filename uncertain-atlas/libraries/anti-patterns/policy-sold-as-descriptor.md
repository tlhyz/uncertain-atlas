# 反模式：看见钱包策略就当成已经是一条描述符 / 看见钥占位就当成已经是精确公钥 / 看见登记过就当成已经批准这笔花

**层次**：应用 / 失败模式。  
**分类**：事实（对象）+ 推断（事故）。  
**来源**：[BIP-388](https://github.com/bitcoin/bips/blob/master/bip-0388.mediawiki)。  
**例**：[钱包策略 ≠ 已经是一条描述符](../../tracks/implementation/worked-example-policy-vs-descriptor.md)。

## 塌法

1. 看见钱包策略 / 看见一个账户，就当成已经是一条描述符，或当成已经把账户收成一句描述符。
2. 看见钥占位 / 看见账户根，就当成已经是那把精确公钥，或当成已经带齐派生。
3. 看见登记过 / 看见登记证明，就当成已经批准这笔花，或当成已经不必再核验。
4. 看见写了 policy，就当成已经是 Miniscript 那种 policy 语言。
5. 看见本页策略，就当成已经是描述符已经是地址。

## 为什么会出事

官方写：钱包策略由模板加一列钥信息组成。KEY 永远对应最终脚本里那一把精确公钥；占位里不许再写派生。第一次用之前要登记；登记证明不是已经批准这一笔。本页和能编译成 Miniscript 的 policy 语言不是一回事。

## 和相邻反模式

- [keys-sold-as-scripts](keys-sold-as-scripts.md) 是备份 ≠ 已经知道脚本，不是本页。
- [miniscript-sold-as-script](miniscript-sold-as-script.md) 是 Miniscript ≠ 已经是链上脚本，不是本页。
- [tap-psbt-sold-as-old](tap-psbt-sold-as-old.md) 是旧 PSBT 栏 ≠ 已经能装 Taproot，不是本页。
