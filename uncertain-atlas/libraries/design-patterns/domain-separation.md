# 模式：域分离（Domain Separation）

**问题：** 同一把钥匙签的字节在错误上下文被当成同意。  
**方案：** 消息前缀写明链、消息类型、版本。  
**适用：** 一切签名，尤其多算法、多客户端。  
**优点：** 挡住跨链、跨类型重放。  
**缺点：** 忘写一次就全废；版本字段本身要规范编码。  
**项目：** EIP-155；几乎所有现代 vote 消息。  
**常见 bug：** 用户交易和验证者投票共用同一裸哈希。  
**不确定：** 必做。后量子共存时更必做。消息前缀是一层；FIPS 204/205 外部 API 的 `ctx` 是第二层，默认空串不算完成。精读：[`../../tracks/crypto/worked-example-domain.md`](../../tracks/crypto/worked-example-domain.md)、[`../../tracks/post-quantum/fips-context.md`](../../tracks/post-quantum/fips-context.md)。
