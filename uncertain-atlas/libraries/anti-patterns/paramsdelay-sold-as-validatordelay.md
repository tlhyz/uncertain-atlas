# 反模式：看见本高 Finalize 回了 ConsensusParams 就当成已经在本高生效 / 看见 H+1 立刻用了新参数就当成已经是验证人集合那种 H+2 才计票 / 看见参数更新写了 H+1 就当成已经是扩展启用高度那种切换

**层次**：实现 / 失败模式。  
**分类**：事实（对象）+ 推断（事故）。  
**来源**：[Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Updating Consensus Parameters / `FinalizeBlock`, `PrepareProposal`/`ProcessProposal`。  
**例**：[本高回了 ConsensusParams ≠ 已经在本高生效](../../tracks/implementation/worked-example-params-delay-vs-set.md)。

## 塌法

1. 看见本高 `FinalizeBlock` 回了 `ConsensusParams` / 看见本高已经交差，就当成已经在本高生效，或当成本高提议已经按新参数。
2. 看见 H+1 立刻用了新参数 / 看见参数走 H→H+1，就当成已经是验证人集合那种 H+2 才计票，或当成已经是 H+3 才带 last_commit。
3. 看见参数更新写了 H+1 / 看见 H+1 已经按新参数，就当成已经是扩展启用高度那种 H / H+1 Prepare 切换，或当成已经只改填的那一项。

## 为什么会出事

官方写：块 H 回的更新，立刻对块 H+1 生效。集合更新是处理 H 之后只在 H+2 生效。扩展启用高度是到了 H 才开始叫 ExtendVote、到 H+1 才 Prepare 带扩展。空 / 没回 / 只填一项是另一套回包规则，不是哪一高度生效。

## 和相邻反模式

- [paramsdelay-noth-sold-as-bundled](paramsdelay-noth-sold-as-bundled.md) 是本高回了 ConsensusParams 不是已经在本高生效 item 1 单句边界，不是本页 ConsensusParams 生效延迟 bundled 全段。
- [paramsdelay-notvalidatorh2-sold-as-bundled](paramsdelay-notvalidatorh2-sold-as-bundled.md) 是 H+1 立刻用了新参数不是已经是验证人集合那种 H+2 才计票 item 2 单句边界，不是本页 ConsensusParams 生效延迟 bundled 全段。
- [validator-update-sold-as-immediate](validator-update-sold-as-immediate.md) 是 H 的 `validator_updates` ≠ 已经 H+1 立刻计票，不是本页这种参数 H→H+1。
- [consensusparams-sold-as-updated](consensusparams-sold-as-updated.md) 是 InitChain 空 / Finalize 没回 / 只填一项，不是本页这种生效高度。
- [veheight-sold-as-prepared](veheight-sold-as-prepared.md) 是到了 H ≠ 已经 Prepare 带了扩展，不是本页这种参数立刻对 H+1 生效。
