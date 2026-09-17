# 反模式：看见正确进程交出的扩展必须被正确接收者 Verify Accept 就当成已经是任意扩展都会 Accept / 看见 Extend 或 Verify 里有确定 bug 会让带无效扩展的 Precommit 被丢掉就当成已经只是活性问题 / 看见会面对和 Req 5 同一类活性问题就当成已经丢了安全性

**层次**：实现 / 失败模式。  
**分类**：事实（对象）+ 推断（事故）。  
**来源**：[Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Formal Requirement 6 [`ExtendVote`, `VerifyVoteExtension`, coherence]。  
**例**：[正确进程交出的扩展必须被正确接收者 Verify Accept ≠ 已经是任意扩展都会 Accept](../../tracks/implementation/worked-example-req6-coherence-vs-accept.md)。

## 塌法

1. 看见正确进程交出的扩展、正确接收者 Verify 必须 Accept / 看见正确进程之间永远过，就当成已经是任意扩展都会 Accept，或当成已经是 Verify 默认 Accept。
2. 看见 Extend 或 Verify（或两边）里有确定 bug / 看见带无效扩展的 Precommit 会被丢掉，就当成已经只是活性问题，或当成已经是块非法，或当成已经是 Verify 非确定 bug。
3. 看见会面对和 Requirement 5 同一类活性问题 / 看见和 Process 确定性那条同一路，就当成已经丢了安全性，或当成已经是 347 那种提案一致性。

## 为什么会出事

官方写：正确进程交出的扩展，正确接收者的 Verify 必须 Accept。若 Extend 或 Verify（或两边）里有确定 bug，带无效扩展的 Precommit 会被丢掉，这时会面对和 Requirement 5 写过的同一类活性问题。

## 和相邻反模式

- [vote-extension-sold-as-block](vote-extension-sold-as-block.md) 是验签拒收整张预提交不是已经是块非法，不是本页这种正确进程交出的扩展必须被正确接收者 Verify Accept 不是已经是任意扩展都会 Accept。
- [verifydet-sold-as-extend](verifydet-sold-as-extend.md) 是 Verify 必须只依赖扩展、这块和上一份状态，不是本页这种 Extend 或 Verify 里有确定 bug 会让带无效扩展的 Precommit 被丢掉不是已经只是活性问题。
- [req3coherence-sold-as-accept](req3coherence-sold-as-accept.md) 是正确提议者的准备提案必须被正确接收者 Accept，不是本页这种会面对和 Req 5 同一类活性问题不是已经丢了安全性。
