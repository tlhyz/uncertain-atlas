# 反模式：新委员会的 2/3 当成轻客户端信任

跳过中间高度时，只检查「新头上的验证者集合自己投满 2/3」。

规范要的是：这些签名里，属于**已信任头的 `NextValidators`** 的投票权必须超过约 1/3（`LCV-FUNC-VALID.1` 的跳过分支）。  
新集合可以是攻击者刚写进去的。自嗨的 2/3 挡不住 lunatic 头。

紧邻后继才用旧 `NextValidators` 的 +2/3，且两份集合哈希必须接得上。  
亲戚：[`header-equals-settlement.md`](header-equals-settlement.md)、[`rpc-as-verification.md`](rpc-as-verification.md)。  
精读：[`../../tracks/light-clients/worked-example-bft-skip.md`](../../tracks/light-clients/worked-example-bft-skip.md)。
