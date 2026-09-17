# 反模式：看见提案收了交易就当成已经从池里删掉 / 看见本块已 commit 就当成已经不用再验剩下的 / 看见 CheckTx 过了就当成已经永远有效

**层次**：共识 / 失败模式。  
**分类**：事实（对象）+ 推断（事故）。  
**来源**：[Mempool](https://github.com/cometbft/cometbft/blob/main/spec/mempool/mempool.md)。  
**例**：[提案收了 ≠ 已经从池里删掉](../../tracks/mempool/worked-example-proposed-vs-removed.md)。

## 塌法

1. 看见共识从池里收了一串交易 / 看见这些交易进了提案，就当成已经从池里删掉。
2. 看见块已经 commit / 看见本块交易从池里去掉，就当成已经不用再验剩下的。
3. 看见 CheckTx 过了 / 看见进了池，就当成已经进块，或当成已经永远有效。
4. 看见提案带了这些交易，就当成已经过了 Process。
5. 看见曾经绿过，就当成先装证据已经装满交易。

## 为什么会出事

官方写：提案还没决定，所以还不从池里删。块决定之后才去掉本块交易，还留着的要按新状态再验。有效性可以随应用状态变。

## 和相邻反模式

- [evidence-sold-as-full-block](evidence-sold-as-full-block.md) 是先装证据 ≠ 已经装满交易，不是本页这种还在池里。
- [state-sold-as-block](state-sold-as-block.md) 是本地 State ≠ 已经进了块，不是本页。
