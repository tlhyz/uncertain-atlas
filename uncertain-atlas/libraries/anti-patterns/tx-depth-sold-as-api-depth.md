# 反模式：交易解码深度有界被写成 runtime API 再解整块已安全

> 真值：[Polkadot-SDK 2025-05](../../tracks/failure-museum/polkadot-2025-05-runtime-api-decode-depth.md)、[不变式 97](../invariants/README.md)。亲戚：[maxtxbytes-sold-as-nested-bound](maxtxbytes-sold-as-nested-bound.md)、[autoban-sold-as-bound](autoban-sold-as-bound.md)、[local-error-as-consensus-invalid](local-error-as-consensus-invalid.md)。

## 一句话

看见交易解码深度有上限、或看见出块已经收下，就写成导入时 check_inherents 也能解；解失败就踢邻居。

## 正确写法

「深度计数器只走交易对象。整块当 runtime API 参数不得共用。出块接受不是导入已能解。导入失败不是邻居已经作恶。」
