# 模式：点名 tr386-notxonly 杠

**层次**：应用 / BIP-386 compressed-key not already x-only / not already uncompressed-ok / not already settled 正式三事（275 余量）。  
**分类**：建议（产品）。  
**来源**：Bitcoin [BIP-386](https://github.com/bitcoin/bips/blob/master/bip-0386.mediawiki)（Deployed, Applications, Informational）。  
**对应**：[`../tracks/implementation/worked-example-tr386-notxonly-vs-bundled.md`](../tracks/implementation/worked-example-tr386-notxonly-vs-bundled.md)。

- **压缩钥 不是已经是 x-only：** 看见压缩钥，不是已经是 x-only interchangeable / 1147 tr386-notxonly interchangeable。
- **看见未压缩钥 不是已经允许未压缩：** 看见未压缩钥，不是已经是本页 interchangeable。
- **看见从扩展钥派生出来的钥也必须按 x-only 序列化 不是已经交差：** 看见从扩展钥派生出来的钥也必须按 x-only 序列化，不是已经交差 interchangeable。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看压缩钥 正式三事（275 余量），先数清问的是是不是已经是 x-only、是不是已经允许未压缩、还是看见从扩展钥派生出来的钥也必须按 x-only 序列化是不是已经交差，再决定要不要同一次发布。275 tr vs tree bundled unbundling 在本页 item 3 完成。
