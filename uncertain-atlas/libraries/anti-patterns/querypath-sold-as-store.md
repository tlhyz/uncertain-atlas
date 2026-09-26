# 反模式：看见 data 按 URI 查询分量解释、可以和 path 一起或代替 path 用就当成已经是 Query 高度 / 看见 path 按 URI 路径解释、/store 必须按键查就当成已经是引擎在用 / 看见规范建议允许 /accounts / /votes 这类查询就当成已经是正常运转必须有

**层次**：实现 / 失败模式。  
**分类**：事实（对象）+ 推断（事故）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) Query Request。  
**例**：[data 按 URI 查询分量解释、可以和 path 一起或代替 path 用 ≠ 已经是 Query 高度](../../tracks/implementation/worked-example-querypath-vs-store.md)。

## 塌法

1. 看见 `data` 按 URI 查询分量解释、可以和 `path` 一起或代替 `path` 用 / 看见填了 `data`，就当成已经是 Query 高度，或当成已经新鲜。
2. 看见 `path` 按 URI 路径解释、`/store` 必须按键查 / 看见写了 `/store`，就当成已经是引擎在用，或当成已经是过滤。
3. 看见规范建议允许 `/accounts/` / `/votes/` 这类查询 / 看见写了类型路径，就当成已经是正常运转必须有，或当成已经复制到各节点。

## 为什么会出事

官方写：`data` 按 URI 查询分量解释，可以和 `path` 一起用，也可以代替 `path`。`path` 按 URI 路径分量解释。应用必须把 `/store` 或任何以 `/store/` 开头的路径当成底层店上的按键查询；这时键应当写在 `data` 里。应用应当允许按具体类型查，例如 `/accounts/...` 或 `/votes/...`。

## 和相邻反模式

- [querypath-notheight-sold-as-bundled](querypath-notheight-sold-as-bundled.md) 是 data 按 URI 查询分量解释、可以和 path 一起或代替 path 用不是已经是 Query 高度 not already height / not already fresh / not already settled 正式三事（377 item 1），不是本页 bundled 全段 alone。
- [queryheight-sold-as-committed](queryheight-sold-as-committed.md) 是 Query 可以对当前或过去高度查就已经是 QueryState，不是本页这种 data 按 URI 查询分量解释、可以和 path 一起或代替 path 用不是已经是 Query 高度。
- [peerfilter-sold-as-connected](peerfilter-sold-as-connected.md) 是有 /store 路径就已经是引擎在用，不是本页这种 path 按 URI 路径解释、/store 必须按键查不是已经是引擎在用。
- [query-sold-as-replicated](query-sold-as-replicated.md) 是实现了 Query 就已经是正常运转必须有，不是本页这种规范建议允许 /accounts / /votes 这类查询不是已经是正常运转必须有。
