# 模式：点名 tap86-notout 杠

**层次**：应用 / BIP-86 derived-key not already output-key / not already witness-32 / not already settled 正式三事（272 余量）。  
**分类**：建议（产品）。  
**来源**：Bitcoin [BIP-86](https://github.com/bitcoin/bips/blob/master/bip-0086.mediawiki)（Deployed, Applications）。  
**对应**：[`../tracks/implementation/worked-example-tap86-notout-vs-bundled.md`](../tracks/implementation/worked-example-tap86-notout-vs-bundled.md)。

- **派生钥 不是已经是输出钥：** 看见路径对上了，不是已经对上了输出钥 interchangeable / 1136 tap86-notout interchangeable。
- **看见内部钥 不是已经是见证里那 32 字节：** 看见内部钥，不是已经是见证里那 32 字节 interchangeable。
- **看见路径对上了 不是已经交差：** 看见路径对上了，不是已经交差 interchangeable。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看派生钥 正式三事（272 余量），先数清问的是是不是已经是输出钥、是不是已经是见证里那 32 字节、还是看见路径对上了是不是已经交差，再决定要不要同一次发布。272 derived vs output-key bundled unbundling 在本页 item 1 启动。
