# 模式：把 Query 回了不是已经复制到各节点 not already replicated / not already consensus-passed / not already network-same 正式三事（329 余量）说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Query。  
**例**：[Query 回了 not already replicated ≠ bundled（329）](../../tracks/implementation/worked-example-query-notreplicated-vs-bundled.md)。

## 三个名字

1. **Query 回了 不是 already replicated：** 看见 Query 回了 / 查有回包 / 通用查询回了，不是已经复制到各节点 interchangeable / 已经复制交差 interchangeable，不是 329 query bundled interchangeable / 33 four gates interchangeable / query-sold-as-replicated interchangeable。

2. **RPC 能查 不是 already consensus-passed：** 看见 RPC 能查 / RPC 绿了 / 经 RPC 暴露给用户，不是已经过了共识 interchangeable / 已经共识读交差 interchangeable，不是 325 queryproof interchangeable / 329 query item 2 interchangeable。

3. **查的是本节点本地 不是 already network-same：** 看见查的是本节点本地 / 本地状态 / 本机查询，不是已经全网同一份 interchangeable / 已经全网同一份交差 interchangeable，不是 314 querystate interchangeable / 329 query item 3 interchangeable。

官方把 Query 回了单句、already replicated、already consensus-passed、already network-same 写成三个名字。把它们叫成一个「看见 Query 回了就已经复制到各节点 interchangeable / 就已经过了共识 interchangeable / 就已经全网同一份 interchangeable」，会把 not already replicated、not already consensus-passed、not already network-same 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Query 回了不是已经复制到各节点 not already replicated / not already consensus-passed / not already network-same 正式三事（329 余量），先数清问的是 Query 回了 是不是 already replicated / 329 / query-sold-as-replicated，是不是 RPC 能查 是不是 already consensus-passed，还是查的是本节点本地 是不是 already network-same，再决定要不要同一次发布。329 query vs replicated bundled unbundling 在本页 item 1 启动。
