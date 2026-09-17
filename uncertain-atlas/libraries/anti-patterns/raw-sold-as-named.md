# 反模式：看见 raw 就当成已经具名 / 看见 addr 就当成已经是那份输出脚本 / 看见一份包装就当成已经是 combo

**层次**：应用 / 失败模式。  
**分类**：事实（对象）+ 推断（事故）。  
**来源**：[BIP-385](https://github.com/bitcoin/bips/blob/master/bip-0385.mediawiki)。  
**例**：[raw ≠ 已经具名脚本](../../tracks/implementation/worked-example-raw-vs-named.md)。

## 塌法

1. 看见 raw / 看见一串十六进制脚本，就当成已经能套进 sh / wsh，或当成已经是 pk / sh 那种具名表达式。
2. 看见 addr / 看见一个地址，就当成已经能套进 sh / wsh，或当成已经把那份输出脚本写在描述符里。
3. 看见一份 raw 或 addr 包住一个对象，就当成已经是一份 combo，或当成已经是一份钱包策略。
4. 看见包住了今天在用的地址，就当成已经在链上有这笔输出。
5. 看见本页包装，就当成已经是描述符已经是地址。

## 为什么会出事

官方写：`raw` 和 `addr` 都只能当顶层。raw 的参数就是脚本本身；addr 产出的是这个地址产出的那份输出脚本。本页是包一个对象，不是一把钥上的几份传统脚本。

## 和相邻反模式

- [combo-sold-as-one-script](combo-sold-as-one-script.md) 是 combo ≠ 已经一种脚本，不是本页。
- [address-sold-as-utxo](address-sold-as-utxo.md) 是地址串 ≠ 已经有输出，不是本页。
- [pk-sold-as-toplevel](pk-sold-as-toplevel.md) 是 pk ≠ 已经和 pkh / sh 同一套放置，不是本页。
