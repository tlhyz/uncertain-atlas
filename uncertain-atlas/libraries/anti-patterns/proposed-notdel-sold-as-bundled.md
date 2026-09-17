# 反模式：把 提案收了 not already deleted / not already in-block / not already processed 正式三事（301 余量） 写成已经 已经从池里删掉 / 已经进块 / 已经过了 Process

**层次**：共识 / 提案收了 not already deleted / not already in-block / not already processed 正式三事（301 余量）。  
**分类**：建议（产品）。  
**来源**：CometBFT 官方 [Mempool](https://github.com/cometbft/cometbft/blob/main/spec/mempool/mempool.md) mempool / proposed vs removed。  
**对应**：[`../tracks/mempool/worked-example-proposed-notdel-vs-bundled.md`](../tracks/mempool/worked-example-proposed-notdel-vs-bundled.md)。

把 提案收了 not already deleted / not already in-block / not already processed 正式三事（301 余量） 写成已经 已经从池里删掉 / 已经进块 / 已经过了 Process，就是本页。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看提案收了 正式三事（301 余量），必须分开 not already deleted、not already in-block、not already processed 三件事，不要和 301 / 33 / 299 / 993 / 994 糊成一句。

也不是：

- [evidreap-notunlim-sold-as-bundled](evidreap-notunlim-sold-as-bundled.md) 是 -1 仍未没有上限边界（299/991），不是本页提案收了仍未从池里删掉边界。
- 四门已经结算是不变量 33，不是本页收了前缀仍未进块边界。
