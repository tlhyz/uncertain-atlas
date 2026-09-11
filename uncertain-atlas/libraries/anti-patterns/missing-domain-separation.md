# 反模式：签名无域分离

投票、交易、登录挑战共用同一裸消息。  
跨链、跨类型重放。  
见模式 domain-separation。

FIPS 204/205 的亲戚：两个角色都走库默认空 `ctx`，算法层同样没有角色。见 [empty-ctx-two-roles](empty-ctx-two-roles.md)、不变量 18、语料 C20。

BFT 亲戚：prevote 的印拿去验 precommit。见 [`../../tracks/consensus/worked-example-vote-signbytes.md`](../../tracks/consensus/worked-example-vote-signbytes.md)、不变量 19、语料 C21。
