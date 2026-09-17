# 反模式：付款 URI 远程取单被写成已验证

> 真值：[BIP72 URI](../../tracks/failure-museum/cve-2024-52918.md)、[不变式 55](../invariants/README.md)、[CVE-2024-52918](https://bitcoincore.org/en/2024/07/03/disclose-bip70-crash/)。亲戚：[rpc-as-verification](rpc-as-verification.md)。

## 一句话

看见钱包能打开付款链接，就写成全节点已验收款；或把远程取单的 OOM 写成共识拒绝。

## 正确写法

「付款 URI 的远程取单是钱包辅助。打开链接不是 `Apply`。下载必须自带界；删掉该协议可以是正确修法。」
