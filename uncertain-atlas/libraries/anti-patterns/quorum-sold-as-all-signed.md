# 反模式：+2/3 被写成其余槽位已签

> 真值：[CVE-2020-15091 / Syringa](../../tracks/failure-museum/cve-2020-15091.md)、[不变式 65](../invariants/README.md)。亲戚：[majority-vote-is-enough](majority-vote-is-enough.md)、[inflight-sold-as-evidence-id](inflight-sold-as-evidence-id.md)。

## 一句话

看见 Commit 已经凑齐 +2/3，就写成其余槽位也签过、或可以塞进错误块的签名；或让应用按未验完的 LastCommitInfo 发奖。

## 正确写法

「每个槽位要么是对本块本 ChainID 的有效签，要么是显式缺席。+2/3 是安全门槛，不是其余槽位的许可证。应用信任引擎验完整个 LastCommit。」
