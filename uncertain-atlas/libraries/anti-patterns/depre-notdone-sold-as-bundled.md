# 反模式：把 EIP-6049 later-may-change not already changed / not already 160 / not already 223 正式三事（224 余量） 写成已经 已经变了 / 已经是不变量 160 / 已经是不变量 223

**层次**：实现 / EIP-6049 later-may-change not already changed / not already 160 / not already 223 正式三事（224 余量）。  
**分类**：建议（产品）。  
**来源**：Ethereum [EIP-6049](https://eips.ethereum.org/EIPS/eip-6049)（Final, Meta, Deprecate SELFDESTRUCT）。  
**对应**：[`../tracks/implementation/worked-example-depre-notdone-vs-bundled.md`](../tracks/implementation/worked-example-depre-notdone-vs-bundled.md)。

把 EIP-6049 later-may-change not already changed / not already 160 / not already 223 正式三事（224 余量） 写成已经 已经变了 / 已经是不变量 160 / 已经是不变量 223，就是本页。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 EIP-6049 deprecate 正式三事（224 余量），必须分开 not already consensus-changed、not already client-changed、not already later-changed 三件事，不要和 224 / 160 / 223 / 1416 / 1417 糊成一句。

也不是：

- [depre-notcons-sold-as-bundled](depre-notcons-sold-as-bundled.md) 是 notcons 单句边界（1416），不是本页边界。
- [depre-notcli-sold-as-bundled](depre-notcli-sold-as-bundled.md) 是 notcli 单句边界（1417），不是本页边界。
- [rfnd-notgone-sold-as-bundled](rfnd-notgone-sold-as-bundled.md) 是 EIP-3529 退款削减边界（223/1413），不是本页弃用边界。
