# 反模式：看见整池可见就当成已经只能看见装得进一块的子集 / 看见聚合体积可以超过 max_tx_bytes 就当成已经能回超限列表 / 看见 Req 2 保证回的列表不让块超字节上限就当成已经是引擎会帮你裁

**层次**：实现 / 失败模式。  
**分类**：事实（对象）+ 推断（事故）。  
**来源**：[Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Formal Requirement 2 [`PrepareProposal`, tx-size]。  
**例**：[整池可见 ≠ 已经只能看见装得进一块的子集](../../tracks/implementation/worked-example-prepare-return-vs-pool.md)。

## 塌法

1. 看见整池可见 / 看见 MaxBytes 写成 -1 把池子都交来，就当成已经只能看见装得进一块的子集，或当成已经没有上限。
2. 看见聚合体积可以超过 `max_tx_bytes` / 看见池子加起来比这次上限大，就当成已经能回超限列表，或当成已经交差。
3. 看见 Requirement 2 保证回的列表不让块超字节上限 / 看见回包不得超过 `max_tx_bytes`，就当成已经是引擎会帮你裁，或当成已经是 MaxBytes 扣掉头集合证据之后的交易上限。

## 为什么会出事

官方写：忙链可以把 MaxBytes 写成 -1，好看见内存池里全部交易，而不是只看见装得进一块的子集。这时所有交易加起来可以超过这次的 `max_tx_bytes`。Requirement 2 保证应用回的列表永远不会让这块超过字节上限。

## 和相邻反模式

- [prepare-notenginecut-sold-as-bundled](prepare-notenginecut-sold-as-bundled.md) 是 Req 2 保证回的列表不让块超 not already engine-cuts / not already overhead-deducted / not already four-gates-settled 正式三事（345 item 3），不是本页 bundled 全段 alone。
- [prepare-notoversize-sold-as-bundled](prepare-notoversize-sold-as-bundled.md) 是聚合体积可以超过 max_tx_bytes not already can-return-oversize / not already request-trimmed / not already settled 正式三事（345 item 2），不是本页 bundled 全段 alone。
- [prepare-notblocksubset-sold-as-bundled](prepare-notblocksubset-sold-as-bundled.md) 是整池可见 not already block-subset / not already no-cap / not already all-visible-is-uncapped 正式三事（345 item 1），不是本页 bundled 全段 alone。
- [evidence-sold-as-full-block](evidence-sold-as-full-block.md) 是整池都给 Prepare 不是已经没有上限，不是本页这种整池可见不是已经只能看见装得进一块的子集。
- [maxbytescap-sold-as-unlimited](maxbytescap-sold-as-unlimited.md) 是 -1 就按 100 MB 验不是已经没有上限，不是本页这种聚合体积可以超过 max_tx_bytes 不是已经能回超限列表。
- [maxbytesoverhead-sold-as-full](maxbytesoverhead-sold-as-full.md) 是 MaxBytes 减去头集合证据才是交易上限，不是本页这种 Req 2 保证回的列表不让块超字节上限不是已经是引擎会帮你裁。
