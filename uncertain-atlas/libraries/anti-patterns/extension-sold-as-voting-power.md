# 反模式：提议者注入的扩展被写成投票权预言机

> 真值：[ASA-2024-006](../../tracks/failure-museum/asa-2024-006.md)、[不变式 68](../invariants/README.md)、[扩展精读](../../tracks/consensus/worked-example-vote-extension.md)。亲戚：[extension-path-sold-as-checked](extension-path-sold-as-checked.md)、[vote-extension-sold-as-block](vote-extension-sold-as-block.md)。

## 一句话

看见默认 `ValidateVoteExtensions`，就写成投票权已经按状态机核对；或让 ProcessProposal 从提议者注入的扩展推断总值 / 每人值。

## 正确写法

「投票权必须读已提交集合。提议者注入的 VoteExtension 不是预言机。扩展签名为真 ≠ 权重已对齐。」
