# 反模式：blob gas 被写成普通执行 gas

> 真值：[blob 费 ≠ 执行气工作实例](../../tracks/light-clients/worked-example-blob-fee-vs-gas.md)、[不变式 145](../invariants/README.md)、[不变式 23](../invariants/README.md)。亲戚：[kzg-sold-as-das](kzg-sold-as-das.md)、[policy-sold-as-consensus](policy-sold-as-consensus.md)。

## 一句话

看见「也付了 gas」或看见合约调用了 `BLOBHASH`，就把 blob gas 写成普通执行 gas，或把承诺引用写成已经读到 sidecar 字节，或把付了 blob fee 写成数据已经永存。

## 正确写法

「blob gas 是独立于普通 gas 的新气种。EVM 能读 versioned hash，不是已经读到袋里的字节。blob fee 执行前烧掉、失败不退。执行层不负责持久化 blob。」
