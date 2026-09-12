# 反模式：把 `tr(KEY)` 写成已经有脚本路径

> 状态：已部署。
> 类别：Applications。
> 类型：信息型。
> 状态判定：事实（BIP-386 正文）。
> 来源：<https://github.com/bitcoin/bips/blob/master/bip-0386.mediawiki>
> 相邻：[`derived-sold-as-output-key.md`](derived-sold-as-output-key.md) · [`keypath-sold-as-tree.md`](keypath-sold-as-tree.md) · [`xpub-sold-as-spendable.md`](xpub-sold-as-spendable.md)

## 被折叠的对象

`tr(KEY)` / 没有树参数、树表达式 / 一对花括号、压缩钥 / 未压缩钥 被写成已经有脚本路径 / 已经同一套 tweak、已经是旧脚本嵌套 / 已经随便哪条旧表达式都能进树、已经是 x-only / 已经允许未压缩钥。

## 官方为什么把它拆开

1. `tr` 只能出现在顶层。没有树参数时，只产无脚本路径的 P2TR。有树时，树变成 BIP-341 的脚本树，merkle 根再和内部钥一起算输出钥。
2. 树要么是一条允许进树的脚本表达式，要么是一对树。写本 BIP 时已存在的表达式里，只有 `pk()` 能进树。后来才加 BIP-379 的 Miniscript 片段和 BIP-387 的 `multi_a` / `sortedmulti_a`。
3. `tr()` 下面的钥都必须产出 x-only 公钥。未压缩钥不允许。压缩钥会隐式转成 x-only。扩展钥的子钥也必须按 x-only 序列化。`tr()` 里还多一种 64 位十六进制 x-only 公钥写法。

## 本页不教的东西

不抄树花括号怎么写。不抄 HashTapTweak / merkle 公式。不抄测试向量。不写十六进制宽度。不写例钥。不写怎样把压缩钥抬成 x-only。

## 对不确定的建议

第一版不要把 `tr(KEY)` 写成已经有脚本路径。不要把树表达式写成已经是旧脚本嵌套。不要把压缩钥写成已经是 x-only。
