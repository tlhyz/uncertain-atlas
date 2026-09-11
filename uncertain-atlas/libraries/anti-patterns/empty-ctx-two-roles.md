# 反模式：两个角色共用空 ctx

FIPS 204 / 205 外部 API 的 `ctx` 默认是空串。把用户签和投票签都交给库默认，等于算法层没有角色。

标准允许空 `ctx`，那是**默认**，不是「已经域分离」。  
pure 与 pre-hash 的分隔字节（0 与 1）只分开两种 API，不分开「转账 / 投票」。

FIPS 还建议：一把钥不要既做 ML-DSA 又做 HashML-DSA（SLH 同理）。标识必须写明版本（不变量 11）。

见 [`../../tracks/post-quantum/fips-context.md`](../../tracks/post-quantum/fips-context.md)、不变量 18、语料 C20。
