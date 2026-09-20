# 反模式：看见 Query 回了就当成已经复制到各节点 / 看见查到了就当成已经新鲜 / 看见实现了 Query 就当成已经是正常运转必须有

**层次**：实现 / 失败模式。  
**分类**：事实（对象）+ 推断（事故）。  
**来源**：[Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Query。  
**例**：[Query 回了 ≠ 已经复制到各节点](../../tracks/implementation/worked-example-query-vs-replicated.md)。

## 塌法

1. 看见 Query 回了 / 看见 RPC 能查，就当成已经复制到各节点，或当成已经过了共识。
2. 看见查到了 / 看见本地有这份，就当成已经新鲜，或当成已经是当前尖。
3. 看见实现了 Query / 看见规范写了 Query，就当成已经是正常运转必须有，或当成已经是过滤或证明。

## 为什么会出事

官方写：对 Query 的调用不会在各节点之间复制，查的是本节点本地状态，可能读到旧的。需要共识的读必须走交易。正常运转技术上不要求实现 Query。

## 和相邻反模式

- [query-notreplicated-sold-as-bundled](query-notreplicated-sold-as-bundled.md) 是 Query 回了不是已经复制到各节点 item 1 单句边界，不是本页 Query bundled 全段。
- [query-notfresh-sold-as-bundled](query-notfresh-sold-as-bundled.md) 是查到了不是已经新鲜 item 2 单句边界，不是本页 Query bundled 全段。
- [querystate-sold-as-execute](querystate-sold-as-execute.md) 是 QueryState ≠ 已经是 ExecuteTxState，不是本页这种本地查询。
- [queryproof-sold-as-apphash](queryproof-sold-as-apphash.md) 是 Query 回了 Proof ≠ 已经对上 AppHash，不是本页。
- [peerfilter-sold-as-connected](peerfilter-sold-as-connected.md) 是发了 addr 过滤查询 ≠ 已经收下这个人，不是本页。
