# 反模式：看见 CheckTx 技术上可选、不参与处理块就当成已经是四门已经结算 / 看见 Code ≠ 0 会被拒、不会广播也不会进提案就当成已经没进块 / 看见引擎对回包码不再赋予别的含义就当成已经被引擎用了 Data

**层次**：实现 / 失败模式。  
**分类**：事实（对象）+ 推断（事故）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) CheckTx Usage。  
**例**：[CheckTx 技术上可选、不参与处理块 ≠ 已经是四门已经结算](../../tracks/implementation/worked-example-checktxopt-vs-block.md)。

## 塌法

1. 看见 CheckTx 技术上可选、不参与处理块 / 看见能回，就当成已经是四门已经结算，或当成已经交差。
2. 看见 `Code ≠ 0` 会被拒、不会广播也不会进提案 / 看见拒了，就当成已经没进块，或当成已经被池子挡住拜占庭。
3. 看见引擎对回包码不再赋予别的含义 / 看见有码，就当成已经被引擎用了 Data，或当成已经是共识顺序。

## 为什么会出事

官方写：CheckTx 技术上可选，不参与处理块。`CheckTxResponse.Code ≠ 0` 的交易会被拒，不会广播给别的节点，也不会装进提案。CometBFT 对这个回包码不再赋予别的含义。

## 和相邻反模式

- [checktxopt-notexcluded-sold-as-bundled](checktxopt-notexcluded-sold-as-bundled.md) 是 Code ≠ 0 会被拒、不会广播也不会进提案不是已经没进块 not already excluded / not already blocked / not already settled 正式三事（373 item 2），不是本页 bundled 全段 alone。
- [checktxopt-notfourgates-sold-as-bundled](checktxopt-notfourgates-sold-as-bundled.md) 是 CheckTx 技术上可选、不参与处理块不是已经是四门已经结算 not already fourgates / not already settled / not already removed 正式三事（373 item 1），不是本页 bundled 全段 alone。
- [checktx-sold-as-prepared](checktx-sold-as-prepared.md) 是四门已经结算，不是本页这种 CheckTx 技术上可选、不参与处理块不是已经是四门已经结算。
- [exectxresult-sold-as-consensus](exectxresult-sold-as-consensus.md) 是 Finalize 的 Code 非零就已经没进块，不是本页这种 Code ≠ 0 会被拒、不会广播也不会进提案不是已经没进块。
- [checktxresponse-sold-as-exec](checktxresponse-sold-as-exec.md) 是 CheckTx 的 Data 就已经被引擎用了，不是本页这种引擎对回包码不再赋予别的含义不是已经被引擎用了 Data。
