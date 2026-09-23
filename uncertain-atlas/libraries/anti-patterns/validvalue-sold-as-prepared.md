# 反模式：看见 validValue 非 nil 就当成已经还会调 Prepare / 看见自己是提议者就当成已经每轮都会调 Prepare / 看见没调 Prepare 就当成已经又装了一份 raw 提案

**层次**：实现 / 失败模式。  
**分类**：事实（对象）+ 推断（事故）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) PrepareProposal When。  
**例**：[validValue 非 nil ≠ 已经还会调 Prepare](../../tracks/implementation/worked-example-validvalue-vs-prepare.md)。

## 塌法

1. 看见 validValue 非 nil / 看见本轮直接用它，就当成已经还会调 Prepare，或当成已经能再改列表。
2. 看见只有提议者且 validValue 为 nil 才会调 Prepare / 看见自己是提议者，就当成已经每轮都会调 Prepare，或当成已经交差。
3. 看见 validValue 非 nil 时不会再从池子按优先级收交易、不会再造头 / 看见没调 Prepare，就当成已经又装了一份 raw 提案，或当成已经从提案拿掉 tx。

## 为什么会出事

官方写：若 *p* 有非 `nil` 的 *validValue*，共识算法用它当提案，不再调 `PrepareProposal`。只有提议者且 *validValue* 为 `nil` 才走 Prepare 那条路；那条路上才会从内存池按优先级收未决交易并造头。

## 和相邻反模式

- [vv-notstillprepare-sold-as-bundled](vv-notstillprepare-sold-as-bundled.md) 是 validValue 非 nil not already still-prepare / not already can-revise / not already settled 正式三事（356 item 1），不是本页 bundled 全段 alone。
- [vv-noteveryround-sold-as-bundled](vv-noteveryround-sold-as-bundled.md) 是自己是提议者 not already will-call / not already vv-nil / not already every-round 正式三事（356 item 2），不是本页 bundled 全段 alone。
- [candidate-sold-as-execute](candidate-sold-as-execute.md) 是候选已经是 ExecuteTxState，不是本页这种 validValue 非 nil 不是已经还会调 Prepare。
- [preparenondet-sold-as-deterministic](preparenondet-sold-as-deterministic.md) 是 Prepare 没有确定性要求，不是本页这种自己是提议者不是已经每轮都会调 Prepare。
- [preparedrop-sold-as-evicted](preparedrop-sold-as-evicted.md) 是从提案拿掉 tx 不是已经从内存池删掉，不是本页这种没调 Prepare 不是已经又装了一份 raw 提案。
