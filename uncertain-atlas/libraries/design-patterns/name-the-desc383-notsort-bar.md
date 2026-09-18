# 模式：点名 desc383-notsort 杠

**层次**：应用 / BIP-383 multi not already sortedmulti / not already lex-sorted / not already settled 正式三事（274 余量）。  
**分类**：建议（产品）。  
**来源**：Bitcoin [BIP-383](https://github.com/bitcoin/bips/blob/master/bip-0383.mediawiki)（Deployed, Applications, Informational）。  
**对应**：[`../tracks/implementation/worked-example-desc383-notsort-vs-bundled.md`](../tracks/implementation/worked-example-desc383-notsort-vs-bundled.md)。

- **multi 不是已经是 sortedmulti：** 看见写了多签表达式，不是已经排过 interchangeable / 1142 desc383-notsort interchangeable。
- **看见门限一样 不是已经按字典序排：** 看见门限一样，不是已经是同一种表达式 interchangeable。
- **看见这种排序排的是即将写进输出脚本的那些钥 不是已经交差：** 看见这种排序排的是即将写进输出脚本的那些钥，不是已经交差 interchangeable。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 multi 正式三事（274 余量），先数清问的是是不是已经是 sortedmulti、是不是已经按字典序排、还是看见这种排序排的是即将写进输出脚本的那些钥是不是已经交差，再决定要不要同一次发布。274 multi vs sortedmulti bundled unbundling 在本页 item 1 启动。
