# 横向地图：工程密码学

课：L1。账本：`../post-quantum/engineering-ledger.md`。  
精读：[`worked-example-domain.md`](worked-example-domain.md)（投票字节被当成转账）。

| 组件 | 挡住 | 挡不住 | 后量子税 |
|---|---|---|---|
| 哈希 | 偷改、内容寻址 | 授权 | 视算法，先测 |
| 签名 | 未授权状态变更 | 偷来的钥、错误域 | 体积/验签，主税 |
| Merkle | 包含证明 | 根来源、DA | 路径变长则另账 |
| 承诺 | 隐藏+绑定（假设下） | 元数据 | 与证明系统绑 |
| zk 证明 | 知识外泄（电路范围内） | 电路写错、DA | 证明系统另账 |
| 规范编码 | 同一对象两种字节 | 语义本身 | 编码必须进共识 |
| 签名随机数 / 超时 / 账户序号 | 各挡各的（L1.6） | 三词混用 | `Apply` 禁本地熵；PQ 盐另账 |
| 有状态哈希签（XMSS/LMS） | 主要靠哈希假设的授权 | 同叶子签两封信；克隆私钥 | 次数封顶 + 状态即安全；见 stateful-hbs.md |

后量子名义长度：[`../post-quantum/nist-size-card.md`](../post-quantum/nist-size-card.md)。有状态体积：RFC 8391 Table 3。CPU 仍空。

禁止：把「有某品牌 ZK」写成结算完成；把 FIPS 表抄成本机 benchmark。
