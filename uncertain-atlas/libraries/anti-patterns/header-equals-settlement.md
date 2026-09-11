# 反模式：有头就是结算

验了区块头或 Merkle 路径就放货。  
缺 DA、缺最终性层级、缺独立验证。  
见 L7.2、L9.6。精读：[`../../tracks/light-clients/worked-example.md`](../../tracks/light-clients/worked-example.md)。BFT 亲戚：跳过时只数新集合的 2/3，见 [new-set-quorum-as-light-trust](new-set-quorum-as-light-trust.md)。DA 亲戚：把 KZG / versioned hash 当成永存或当成 Celestia DAS，见 [kzg-sold-as-das](kzg-sold-as-das.md)。
