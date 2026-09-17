# 反模式：废弃 runtime API 还在被写成返回编码已经兼容

> 真值：[Polkadot 2026-03](../../tracks/failure-museum/polkadot-2026-03-deprecated-runtime-api-scale.md)、[不变式 114](../invariants/README.md)。亲戚：[tx-depth-sold-as-api-depth](tx-depth-sold-as-api-depth.md)、[halt-sold-as-one-kind](halt-sold-as-one-kind.md)。

## 一句话

看见入口标了废弃、或看见中继还在最终，就写成旧整理者仍能把块送进中继，返回多一个字段也不裂。

## 正确写法

「仍可调用的废弃 API，返回编码必须与仍在外的调用方兼容。整理者还能写块不是中继已经收到。」
