# 反模式：看见脚本各走各的路径就当成已经是多签该有的树 / 看见路径里的脚本类型就当成已经必要 / 看见主种子就当成已经够找回

**层次**：应用 / 失败模式。  
**分类**：事实（对象）+ 推断（事故）。  
**来源**：[BIP-87](https://github.com/bitcoin/bips/blob/master/bip-0087.mediawiki)。  
**例**：[脚本各走各的路径 ≠ 已经是多签该有的树](../../tracks/implementation/worked-example-multisig-path-vs-script.md)。

## 塌法

1. 看见 44 / 49 / 84 那种脚本各走各的路径 / 看见 45 那种只认一种脚本，就当成已经是多签该有的树，或当成已经不必再带描述符。
2. 看见路径里的脚本类型 / 看见 48 那种多插一层，就当成已经必要，或当成已经是本页。
3. 看见这份不按脚本拆的树 / 看见主种子，就当成已经给单签用，或当成已经够找回。
4. 看见描述符定了脚本，就当成已经是一份钱包策略。
5. 看见本页树，就当成已经知道该看哪种输出脚本。

## 为什么会出事

官方写：有了描述符之后，按脚本拆路径对多签是多余的。不该把钥和脚本混在同一层。这份层次只给多签；共同签名人必须同时备份私钥信息和描述符，以后才能正确找回。

## 和相邻反模式

- [script-type-sold-as-account](script-type-sold-as-account.md) 是脚本类型层 ≠ 已经是账户层，不是本页。
- [purpose-sold-as-compatible](purpose-sold-as-compatible.md) 是 BIP32 compatible ≠ 已经能互操作，不是本页。
- [policy-sold-as-descriptor](policy-sold-as-descriptor.md) 是钱包策略 ≠ 已经是一条描述符，不是本页。
