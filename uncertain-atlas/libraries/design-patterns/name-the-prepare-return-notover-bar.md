# 模式：点名 聚合体积可以超过 max_tx_bytes not already can return oversize / not already pool already trimmed / not already settled 正式三事（345 余量）

**层次**：实现 / PrepareProposal 回包上限。  
**分类**：建议（产品）。  
**对应例**：[worked-example-prepare-return-notover-vs-bundled.md](../../tracks/implementation/worked-example-prepare-return-notover-vs-bundled.md)。

聚合体积可以超过 max_tx_bytes not already can return oversize / not already pool already trimmed / not already settled 正式三事（345 余量） 要先数清问的是哪一件，再决定要不要同一次发布。

- **池子可以超这次上限 不是已经能回超限列表：** 看见池子比上限大，不是已经能回超限列表 interchangeable / 879 prepare-return-notover interchangeable。
- **看见请求里带了上限 不是已经按这个上限裁过：** 看见请求里带了上限，不是已经按这个上限裁过 interchangeable。
- **看见能看见超限的池 不是已经交差：** 看见能看见超限的池，不是已经交差 interchangeable。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看聚合体积可以超过 max_tx_bytes 正式三事（345 余量），先数清问的是是不是已经能回超限列表、是不是已经按这个上限裁过、还是看见能看见超限的池是不是已经交差，再决定要不要同一次发布。345 prepare-return vs pool bundled unbundling 在本页 item 2 续。
