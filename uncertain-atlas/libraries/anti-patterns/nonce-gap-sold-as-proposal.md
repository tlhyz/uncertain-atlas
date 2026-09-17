# 反模式：序号有洞仍被写成整包可提案

> 真值：[ASA-2024-002](../../tracks/failure-museum/asa-2024-002.md)、[不变式 69](../invariants/README.md)、[四门精读](../../tracks/consensus/worked-example-prepare-process.md)。亲戚：[checktx-sold-as-prepared](checktx-sold-as-prepared.md)。

## 一句话

看见每笔都过了 CheckTx，或看见默认 `PrepareProposalHandler` + `SenderNonceMempool`，就写成整包一定能被 Process 收下。

## 正确写法

「Prepare 产出的列表必须是诚实 Process 会 Accept 的。按发送者序号装箱时，不连续序号不得变成非法块。单笔进池 ≠ 整包可提案。」
