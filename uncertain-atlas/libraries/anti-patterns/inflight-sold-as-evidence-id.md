# 反模式：飞行中的 last commit 被写成证据身份

> 真值：[CVE-2021-21271 / Mulberry](../../tracks/failure-museum/cve-2021-21271.md)、[不变式 64](../invariants/README.md)、[证据精读](../../tracks/economic/worked-example-evidence.md)。亲戚：[evidence-equals-slash](evidence-equals-slash.md)、[recompute-sold-as-bft-time](recompute-sold-as-bft-time.md)。

## 一句话

看见双签，就用「我此刻这块还没最终的 last commit」给证据盖时间戳；或把出块算法直接当成证据身份算法。

## 正确写法

「证据身份字段必须取自全网一致的已提交信息。飞行中的 last commit 不是证据时间戳。双签不得因此变成断开诚实者的 DoS。」
