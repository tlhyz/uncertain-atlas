# 模式：把邻居过滤三件事说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Peer Filtering、Paths。  
**例**：[发了 addr 过滤查询 ≠ 已经收下这个人](../../tracks/implementation/worked-example-peerfilter-vs-query.md)。

## 三个名字

1. **发了 addr 过滤查询不是已经收下这个人：** 看见 TCP 连上不是已经过了 id。
2. **id 过滤查询绿了不是已经过了 addr：** 看见公钥地址对上不是已经能交互。
3. **有 /store 路径不是已经是引擎在用：** 看见规范写了三条路径不是已经三条都在用。

## 为什么要分开叫

官方把两道无数据 Query、任意一道非零就拒连、眼下只用 `/p2p` 写成三件事。把它们叫成一个「看见连上了就已经收下」，会把自动封禁表、InitPeer 时序和 QueryState 一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看「连上就已经过滤过」，先数清问的是发了 addr 过滤查询不是已经收下这个人、id 过滤查询绿了不是已经过了 addr，还是有 /store 路径不是已经是引擎在用，再决定要不要同一次发布。
