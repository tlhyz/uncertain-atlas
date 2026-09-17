# 模式：把 Query 证明回包三件事说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) Query Request / Query Response。  
**例**：[Query 请求 prove 是能回就回默克尔证明 ≠ 已经对上 AppHash](../../tracks/implementation/worked-example-queryprove-vs-proof.md)。

## 三个名字

1. **Query 请求 prove 是能回就回默克尔证明不是已经对上 AppHash：** 看见勾了 prove 不是已经是一层树。
2. **Query 回包 proof_ops 是按请求回的、要对这一高 AppHash 验的序列化证明不是已经是按键查：** 看见回了证明不是已经对上 AppHash。
3. **Query 回包 height 是数据来自哪一高不是已经是请求高度：** 看见回了高度不是已经新鲜。

## 为什么要分开叫

官方把 Query 请求 `prove` 是能回就回默克尔证明、Query 回包 `proof_ops` 是按请求回的、要对这一高 AppHash 验的序列化证明、Query 回包 `height` 是数据来自哪一高写成三件事。把它们叫成一个「看见勾了 prove 就已经对上 AppHash」，会把查询证明、回包键值和请求高度一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看「看见勾了 prove 就已经对上 AppHash」，先数清问的是 Query 请求 prove 是能回就回默克尔证明不是已经对上 AppHash、Query 回包 proof_ops 是按请求回的、要对这一高 AppHash 验的序列化证明不是已经是按键查，还是 Query 回包 height 是数据来自哪一高不是已经是请求高度，再决定要不要同一次发布。
