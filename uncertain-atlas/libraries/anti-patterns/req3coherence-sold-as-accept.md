# 反模式：看见正确提议者的准备提案必须被正确接收者 Accept 就当成已经是任意块都会 Accept / 看见 Prepare 或 Process 里有确定 bug 会让踩中的人算拜占庭就当成已经只是活性问题 / 看见 Req 3 是大量测试和自动验证的目标就当成已经测过

**层次**：实现 / 失败模式。  
**分类**：事实（对象）+ 推断（事故）。  
**来源**：[Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Formal Requirement 3 [`PrepareProposal`, `ProcessProposal`, coherence]。  
**例**：[正确提议者的准备提案必须被正确接收者 Accept ≠ 已经是任意块都会 Accept](../../tracks/implementation/worked-example-req3-coherence-vs-accept.md)。

## 塌法

1. 看见正确提议者交出的准备提案、正确接收者 Process 必须 Accept / 看见正确进程之间永远过，就当成已经是任意块都会 Accept，或当成已经是 Process 默认 Accept。
2. 看见 Prepare 或 Process（或两边）里有确定 bug / 看见踩中的人严格算拜占庭，就当成已经只是活性问题，或当成已经是 Process 非确定 bug。
3. 看见同一份代码库很可能同时踩中、多数 prevote nil / 看见 Req 3 因此是大量测试和自动验证的目标，就当成已经测过，或当成已经是引擎会帮你挡。

## 为什么会出事

官方写：正确进程交出的准备提案，正确接收者的 Process 必须 Accept。若 Prepare 或 Process（或两边）里有确定 bug，踩中的人严格算拜占庭。同一份代码库很可能同时踩中，多数 prevote nil，严重伤活性。因此 Requirement 3 是大量测试和自动验证的目标。

## 和相邻反模式

- [req3-notany-sold-as-bundled](req3-notany-sold-as-bundled.md) 是正确提议者的准备提案必须被正确接收者 Accept not already any-block / not already default-accept / not already settled 正式三事（347 item 1），不是本页 bundled 全段 alone。
- [req3-notbyz-sold-as-bundled](req3-notbyz-sold-as-bundled.md) 是 Prepare 或 Process 里有确定 bug 会让踩中的人算拜占庭 not already only-liveness / not already process-nondet / not already settled 正式三事（347 item 2），不是本页 bundled 全段 alone。
- [req3-nottested-sold-as-bundled](req3-nottested-sold-as-bundled.md) 是 Req 3 是大量测试和自动验证的目标 not already tested / not already engine-blocks / not already settled 正式三事（347 item 3），不是本页 bundled 全段 alone。
- [checktx-sold-as-prepared](checktx-sold-as-prepared.md) 是四门已经结算，不是本页这种正确提议者的准备提案必须被正确接收者 Accept 不是已经是任意块都会 Accept。
- [processdet-sold-as-prepare](processdet-sold-as-prepare.md) 是 Process 必须只依赖请求和上一份状态，不是本页这种 Prepare 或 Process 里有确定 bug 会让踩中的人算拜占庭不是已经只是活性问题。
- [preparenondet-sold-as-deterministic](preparenondet-sold-as-deterministic.md) 是 Prepare 没有确定性要求，不是本页这种 Req 3 是大量测试和自动验证的目标不是已经测过。
