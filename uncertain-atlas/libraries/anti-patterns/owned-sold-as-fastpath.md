# 反模式：单地址所有被写成已经走快路径

> 真值：[owned ≠ fastpath 工作实例](../../tracks/parallelism/worked-example-owned-vs-fastpath.md)、[不变式 128](../invariants/README.md)。亲戚：[stm-done-sold-as-final](stm-done-sold-as-final.md)、[justified-sold-as-finalized](justified-sold-as-finalized.md)、[header-equals-settlement](header-equals-settlement.md)、[zero-cost-sold-as-safe](zero-cost-sold-as-safe.md)。

## 一句话

看见对象属于一个地址、交易进了某验证者的共识块、或交易引用了 shared 对象，就写成已经绕过共识、已经生效、或调用者已经有权。

## 正确写法

「所有权同时决定谁能用和版本走哪条。Party 仍是单地址所有，版本走共识。引用 shared 不是已经授权。进块不是已被接受。现行客户端不自己拼证书。」
