# 模式：DA 费必须先点名是不是另一套气

**问题：** 产品把「付了 gas」写成已经解释了 blob。用户把 `BLOBHASH` 听成已经读到袋里的字节，或把执行堵听成 DA 也贵了。  
**方案：** 每个 blob 句先点名问的是普通执行 gas、独立的 blob gas、versioned hash，还是 sidecar 字节。blob fee 在执行前烧掉，失败不退。执行层不负责持久化。  
**适用：** 4844 / 任何「执行层挂短时大数据袋」的结算文案。  
**优点：** 用户能指出演算纸和走廊附录不是同一本账。  
**缺点：** 句子变长；不能再用「都叫 gas」交差。  
**项目：** EIP-4844：blob 数据 EVM 不能访问，承诺能；blob gas 独立于普通 gas；共识层持久化 blob，执行层不。  
**常见 bug：** 两套气写成一套；`BLOBHASH` 写成已读字节；付费写成永存。  
**不确定：** 第一版不要把短时 blob 当默认 DA。见 [工作实例](../../tracks/light-clients/worked-example-blob-fee-vs-gas.md)。
