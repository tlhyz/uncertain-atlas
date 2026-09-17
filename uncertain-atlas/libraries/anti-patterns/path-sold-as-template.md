# 反模式：看见一条派生路径就当成已经是一份路径模板 / 看见写死了熟路径检查就当成已经能互操作 / 看见完整模板就当成已经是半截模板

**层次**：应用 / 失败模式。  
**分类**：事实（对象）+ 推断（事故）。  
**来源**：[BIP-88](https://github.com/bitcoin/bips/blob/master/bip-0088.mediawiki)。  
**例**：[一条派生路径 ≠ 已经是一份路径模板](../../tracks/implementation/worked-example-template-vs-path.md)。

## 塌法

1. 看见一条派生路径 / 看见 43 / 44 / 45 / 49 / 84 那种方案，就当成已经是一份路径模板，或当成已经能被软件无歧义解析。
2. 看见写死了熟路径检查，就当成已经能互操作，或当成已经挡住乱派生。
3. 看见以 `m/` 开头的完整模板，就当成已经是半截模板，或当成已经可以只配后半段。
4. 看见模板长度对上，就当成已经是同一条路径。
5. 看见看起来像路径的模板，就当成已经带了通配或区间约束。

## 为什么会出事

官方写：就算用了现有派生方案，各家用得并不齐。给人看的竖线写法不是给软件解析的。写死熟路径会逼厂家硬塞进熟路径。找零打到不认识的路径上可能丢掉找零。完整模板匹配整条，半截才匹配一段，长度对不上就失败。

## 和相邻反模式

- [purpose-sold-as-compatible](purpose-sold-as-compatible.md) 是自称 compatible ≠ 已经能互操作，不是本页。
- [script-in-path-sold-as-needed](script-in-path-sold-as-needed.md) 是路径里的脚本类型 ≠ 已经必要，不是本页。
- [psbt-sold-as-setup](psbt-sold-as-setup.md) 是部分签名包 ≠ 已经是跨厂开户，不是本页。
- [xpub-sold-as-spendable](xpub-sold-as-spendable.md) 是扩展公钥 ≠ 已经能花，不是本页。
