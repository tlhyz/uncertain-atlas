# 模式：外链 BTC 质押必须点名锁在哪、哪一档给票权

**问题：** 产品把「BTC 质押」写成已经 wrap，或把 k-deep 包含证明写成租户已经 commit，或把解绑签名写成和激活同一把 k。  
**方案：** 每个「到了」先点名问的是 Bitcoin 上的 UTXO 锁、k-deep 票权、解绑意图，还是租户 commit。激活与解绑不得偷用同一确认深度。  
**适用：** 抵押物仍留在另一条链、用包含证明登记的结算文案。  
**优点：** 用户能指出箱子还在总行，还是分行已经 commit；不会把浅重组听成票权回来。  
**缺点：** 句子变长；不能再用「BTC 所以更安全」交差。  
**项目：** Babylon `x/btcstaking`：不必桥走 bitcoin；k-deep 才给票权；普通解绑是意图，不要求 k-deep。  
**常见 bug：** wrap 与留在 Bitcoin 糊成一句；包含证明写成 commit；解绑写成可被浅重组撤销。  
**不确定：** 第一版不要靠外链 BTC 当质押。若对照，必须点名锁与确认档。见 [工作实例](../../tracks/economic/worked-example-btc-lock-vs-commit.md)。
