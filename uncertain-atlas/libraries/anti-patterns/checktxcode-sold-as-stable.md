# 反模式：看见同一高度回了不同码就当成已经有了 CheckTxCode / 看见还在振荡就当成已经过了 h_stable / 看见本地不再振荡就当成已经各节点同一份 b

**层次**：实现 / 失败模式。  
**分类**：事实（对象）+ 推断（事故）。  
**来源**：[Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Formal Requirement 13 [`CheckTx`, eventual non-oscillation]。  
**例**：[同一高度回了不同码 ≠ 已经有了 CheckTxCode](../../tracks/implementation/worked-example-checktx-oscillate-vs-stable.md)。

## 塌法

1. 看见同一高度 CheckTx 回了不同码 / 看见 CheckTxCodes 是集合，就当成已经有了 CheckTxCode，或当成已经能说 OK。
2. 看见还在振荡 / 看见还在池里，就当成已经过了 h_stable，或当成已经离池。
3. 看见本地 h_p,stable / 看见本节点不再振荡，就当成已经是全局同一高度，或当成已经各节点同一份 b。

## 为什么会出事

官方写：同一高度的码是集合，不是单元素就没有 CheckTxCode。最终存在 *h_stable* 之后不再振荡，此刻来回不是已经齐。稳定高度可以看成本地，*b* 必须各正确进程相同。

## 和相邻反模式

- [checktxoscillate-nothstable-sold-as-bundled](checktxoscillate-nothstable-sold-as-bundled.md) 是还在振荡不是已经过了 h_stable item 2 单句边界，不是本页 CheckTx 最终不再振荡 bundled 全段。
- [checktxoscillate-notcode-sold-as-bundled](checktxoscillate-notcode-sold-as-bundled.md) 是同一高度回了不同码不是已经有了 CheckTxCode item 1 单句边界，不是本页 CheckTx 最终不再振荡 bundled 全段。
- [checktxstate-sold-as-execute](checktxstate-sold-as-execute.md) 是 CheckTxState ≠ 已经是 ExecuteTxState，不是本页这种最终不再振荡。
- [proposed-sold-as-removed](proposed-sold-as-removed.md) 是提案收了 ≠ 已经从池里删掉，不是本页。
- [indexer-sold-as-replay](indexer-sold-as-replay.md) 是索引器 ≠ 已经保证不重放，不是本页。
