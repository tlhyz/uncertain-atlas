# 反模式：看见 CheckTx 回包 codespace 是码的命名空间就当成已经是回包码 / 看见 CheckTx 回包 events 是给索引用的类型键值就当成已经交差 / 看见 CheckTx 的 lane_id 必须在 Info 回包车道范围内就当成已经不设道

**层次**：实现 / 失败模式。  
**分类**：事实（对象）+ 推断（事故）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) CheckTx Response。  
**例**：[CheckTx 回包 codespace 是码的命名空间 ≠ 已经是回包码](../../tracks/implementation/worked-example-checktxspace-vs-code.md)。

## 塌法

1. 看见 CheckTx 回包 `codespace` 是码的命名空间 / 看见写了空间，就当成已经是回包码，或当成已经没进块。
2. 看见 CheckTx 回包 `events` 是给索引用的类型键值 / 看见回了事件，就当成已经交差，或当成已经没进块。
3. 看见 CheckTx 的 `lane_id` 必须在 Info 回包车道范围内 / 看见填了道，就当成已经不设道，或当成已经排了优先。

## 为什么会出事

官方写：`codespace` 是这个 `code` 的命名空间。`events` 是给交易建索引的类型和键值，例如按账户。`lane_id` 的值必须落在应用在 `ResponseInfo` 里定义过的那些道。

## 和相邻反模式

- [checktxspace-notunset-sold-as-bundled](checktxspace-notunset-sold-as-bundled.md) 是 CheckTx 的 lane_id 必须在 Info 回包车道范围内不是已经不设道 not already unset / not already priority / not already included 正式三事（381 item 3），不是本页 bundled 全段 alone。
- [checktxspace-notsettled-sold-as-bundled](checktxspace-notsettled-sold-as-bundled.md) 是 CheckTx 回包 events 是给索引用的类型键值不是已经交差 not already settled / not already excluded / not already ordered 正式三事（381 item 2），不是本页 bundled 全段 alone。
- [checktxspace-notcode-sold-as-bundled](checktxspace-notcode-sold-as-bundled.md) 是 CheckTx 回包 codespace 是码的命名空间不是已经是回包码 not already code / not already excluded / not already settled 正式三事（381 item 1），不是本页 bundled 全段 alone。
- [checktxopt-sold-as-block](checktxopt-sold-as-block.md) 是引擎对回包码不再赋予别的含义就已经被引擎用了 Data，不是本页这种 CheckTx 回包 codespace 是码的命名空间不是已经是回包码。
- [exectxresult-sold-as-consensus](exectxresult-sold-as-consensus.md) 是结果列表就已经同一顺序，不是本页这种 CheckTx 回包 events 是给索引用的类型键值不是已经交差。
- [lane-sold-as-priority](lane-sold-as-priority.md) 是没定义 lane_priorities 就已经排了优先，不是本页这种 CheckTx 的 lane_id 必须在 Info 回包车道范围内不是已经不设道。
