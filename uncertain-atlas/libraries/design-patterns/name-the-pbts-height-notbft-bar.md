# 模式：点名 H 之前仍用 BFT Time not already switched to PBTS / not already MTP / not already settled 正式三事（343 余量）

**层次**：实现 / PbtsEnableHeight。  
**分类**：建议（产品）。  
**对应例**：[worked-example-pbts-height-notbft-vs-bundled.md](../../tracks/implementation/worked-example-pbts-height-notbft-vs-bundled.md)。

H 之前仍用 BFT Time not already switched to PBTS / not already MTP / not already settled 正式三事（343 余量） 要先数清问的是哪一件，再决定要不要同一次发布。

- **H 之前仍用 BFT Time 不是已经切到 PBTS：** 看见写了用于 PBTS，不是已经切到 PBTS interchangeable / 885 pbts-height-notbft interchangeable。
- **看见到了 H 不是已经是 MTP：** 看见到了 H，不是已经是 MTP interchangeable。
- **看见还能出合法提案 不是已经交差：** 看见还能出合法提案，不是已经交差 interchangeable。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 H 之前仍用 BFT Time 正式三事（343 余量），先数清问的是是不是已经切到 PBTS、是不是已经是 MTP、还是看见还能出合法提案是不是已经交差，再决定要不要同一次发布。343 pbts vs params bundled unbundling 在本页 item 2 续。
