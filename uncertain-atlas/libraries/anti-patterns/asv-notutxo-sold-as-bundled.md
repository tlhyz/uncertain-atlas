# 反模式：把 assumevalid assumevalid not already assumeutxo / not already 38 / not already 207 正式三事（25 余量） 写成已经 已经是assumeutxo / 已经是不变量 38 / 已经是不变量 207

**层次**：实现 / assumevalid assumevalid not already assumeutxo / not already 38 / not already 207 正式三事（25 余量）。  
**分类**：建议（产品）。  
**来源**：Bitcoin Core [assumevalid](https://bitcoincore.org/en/2017/03/08/release-0.14.0/)（0.14.0 skip ancestor scripts without forcing the chain）。  
**对应**：[`../tracks/implementation/worked-example-asv-notutxo-vs-bundled.md`](../tracks/implementation/worked-example-asv-notutxo-vs-bundled.md)。

把 assumevalid assumevalid not already assumeutxo / not already 38 / not already 207 正式三事（25 余量） 写成已经 已经是assumeutxo / 已经是不变量 38 / 已经是不变量 207，就是本页。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 assumevalid assumevalid 正式三事（25 余量），必须分开 not already checkpoint-forced、not already assumeutxo、not already weak-subjectivity 三件事，不要和 25 / 38 / 207 / 1518 / 1520 糊成一句。

也不是：

- [asv-notchk-sold-as-bundled](asv-notchk-sold-as-bundled.md) 是 notchk 单句边界（1518），不是本页边界。
- [asv-notws-sold-as-bundled](asv-notws-sold-as-bundled.md) 是 notws 单句边界（1520），不是本页边界。
- [kdas-notpeer-sold-as-bundled](kdas-notpeer-sold-as-bundled.md) 是 EIP-4844 KZG≠DAS 边界（23/1515），不是本页 assumevalid 边界。
