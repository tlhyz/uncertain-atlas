# 反模式：看见没定义 lane_priorities 就当成已经排了优先 / 看见空表对空默认就当成已经选型 / 看见优先级 0 留给不设道就当成已经进了块

**层次**：实现 / 失败模式。  
**分类**：事实（对象）+ 推断（事故）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) Info Usage。  
**例**：[没定义 lane_priorities ≠ 已经排了优先](../../tracks/implementation/worked-example-lane-vs-priority.md)。

## 塌法

1. 看见应用可以不定义 `lane_priorities`、这时引擎把交易都放进一条道 / 看见没填表，就当成已经排了优先，或当成已经交差。
2. 看见 `lane_priorities` 空当且仅当 `default_lane` 空、默认道必须是表里的一个标识 / 看见对上了，就当成已经选型，或当成已经交差。
3. 看见最低优先级是 1、0 留给应用不设道（`ResponseCheckTx` 里空 `lane_id`） / 看见写了 0，就当成已经进了块，或当成已经从池里删掉。

## 为什么会出事

官方写：应用不必定义 `lane_priorities`。这时 CometBFT 把所有交易分到一条道。`lane_priorities` 空，当且仅当 `default_lane` 空。`default_lane` 必须是表里定义过的一个标识。一条道最低优先级是 `1`。`0` 留给应用不设道的情况，对应空的 `lane_id`。

## 和相邻反模式

- [lane-notpriority-sold-as-bundled](lane-notpriority-sold-as-bundled.md) 是没定义 lane_priorities not already prioritized / not already checktx-priority / not already settled 正式三事（367 item 1），不是本页 bundled 全段 alone。
- [lane-notalgo-sold-as-bundled](lane-notalgo-sold-as-bundled.md) 是空表对空默认 not already algo / not already prioritized / not already in-block 正式三事（367 item 2），不是本页 bundled 全段 alone。
- [lane-notinblock-sold-as-bundled](lane-notinblock-sold-as-bundled.md) 是优先级 0 留给不设道 not already in-block / not already removed / not already consensus-order 正式三事（367 item 3），不是本页 bundled 全段 alone。
- [checktxresponse-sold-as-exec](checktxresponse-sold-as-exec.md) 是 CheckTx 的 Priority 就已经是共识顺序，不是本页这种没定义 lane_priorities 不是已经排了优先。
- [checktxstate-sold-as-execute](checktxstate-sold-as-execute.md) 是 CheckTxState 就已经是 ExecuteTxState，不是本页这种空表对空默认不是已经选型。
- [proposed-sold-as-removed](proposed-sold-as-removed.md) 是提案收了就已经从池里删掉，不是本页这种优先级 0 留给不设道不是已经进了块。
