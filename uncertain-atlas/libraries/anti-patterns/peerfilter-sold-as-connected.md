# 反模式：看见发了 addr 过滤查询就当成已经收下这个人 / 看见 id 过滤查询绿了就当成已经过了 addr / 看见有 /store 路径就当成已经是引擎在用

**层次**：实现 / 失败模式。  
**分类**：事实（对象）+ 推断（事故）。  
**来源**：[Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Peer Filtering、Paths。  
**例**：[发了 addr 过滤查询 ≠ 已经收下这个人](../../tracks/implementation/worked-example-peerfilter-vs-query.md)。

## 塌法

1. 看见发了 `/p2p/filter/addr` / 看见 TCP 已经连上，就当成已经收下这个人，或当成已经过了 id 那一道。
2. 看见发了 `/p2p/filter/id` / 看见公钥地址对上，就当成已经过了 addr 那一道，或当成已经能交互。
3. 看见有 `/store` / `/app` 路径 / 看见 Query 能带路径，就当成已经是引擎在用，或当成已经是过滤。

## 为什么会出事

官方写：连上时发两道没有额外数据的 Query。任意一道回非零码就拒连。高层路径可以有 `/p2p`、`/store`、`/app`，眼下 CometBFT 只用 `/p2p` 过滤邻居。

## 和相邻反模式

- [autoban-sold-as-bound](autoban-sold-as-bound.md) 是自动封禁表 ≠ 已经有界，不是本页这种连上时的两道 Query。
- [initpeer-sold-as-added](initpeer-sold-as-added.md) 是 InitPeer ≠ 已经能交互，不是本页。
- [querystate-sold-as-execute](querystate-sold-as-execute.md) 是 QueryState ≠ 已经是 ExecuteTxState，不是本页。
