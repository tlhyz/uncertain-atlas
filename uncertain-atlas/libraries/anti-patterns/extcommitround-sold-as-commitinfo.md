# 反模式：看见 ExtendedCommitInfo.round 是提交轮就当成已经是 CommitInfo.round / 看见 Finalize 请求 next_validators_hash 是下一验证者集合默克尔根就当成已经是同一套字段 / 看见 Echo 请求 Message 是要回显的字符串就当成已经是 Flush

**层次**：实现 / 失败模式。  
**分类**：事实（对象）+ 推断（事故）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) ExtendedCommitInfo / FinalizeBlock Request / Echo Request。  
**例**：[ExtendedCommitInfo.round 是提交轮 ≠ 已经是 CommitInfo.round](../../tracks/implementation/worked-example-extcommitround-vs-commitinfo.md)。

## 塌法

1. 看见 ExtendedCommitInfo `round` 是提交轮 / 看见填了 round，就当成已经是 CommitInfo.round，或当成已经按投票权排过。
2. 看见 Finalize 请求 `next_validators_hash` 是下一验证者集合默克尔根 / 看见填了 next_validators_hash，就当成已经是同一套字段，或当成已经换了人。
3. 看见 Echo 请求 `Message` 是要回显的字符串 / 看见填了 Message，就当成已经是 Flush，或当成已经送到。

## 为什么会出事

官方写：ExtendedCommitInfo `round` 是提交轮，反映上一高度块提议者决定时的那一轮。Finalize 请求 `next_validators_hash` 是下一验证者集合的默克尔根。Echo 请求 `Message` 是要回显的字符串。

## 和相邻反模式

- [initapphash-sold-as-header](initapphash-sold-as-header.md) 是 CommitInfo.round 就已经按投票权排过，不是本页这种 ExtendedCommitInfo.round 是提交轮不是已经是 CommitInfo.round。
- [preparefields-sold-as-same](preparefields-sold-as-same.md) 是 Prepare 和 Process / Finalize 同一套字段就已经跑过 Process，不是本页这种 Finalize 请求 next_validators_hash 是下一验证者集合默克尔根不是已经是同一套字段。
- [flush-sold-as-sent](flush-sold-as-sent.md) 是 Flush 要把客户端排队的消息冲到服务端就已经送到，不是本页这种 Echo 请求 Message 是要回显的字符串不是已经是 Flush。
