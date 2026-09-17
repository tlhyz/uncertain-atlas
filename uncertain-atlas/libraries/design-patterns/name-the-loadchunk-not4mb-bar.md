# 模式：点名 16 MB 上限 not already 4 MB snapshot message / not already consensus constant / not already restored 正式三事（375 余量）

**层次**：实现 / LoadSnapshotChunk。  
**分类**：建议（产品）。  
**对应例**：[worked-example-loadchunk-not4mb-vs-bundled.md](../../tracks/implementation/worked-example-loadchunk-not4mb-vs-bundled.md)。

16 MB 上限 not already 4 MB snapshot message / not already consensus constant / not already restored 正式三事（375 余量） 要先数清问的是哪一件，再决定要不要同一次发布。

- **16 MB 上限 不是已经是快照报文 4 MB：** 看见有上限，不是已经 321 interchangeable / 802 loadchunk-not4mb interchangeable。
- **看见 10 MB 不是已经是共识常数：** 看见有上限，不是已经是共识常数 interchangeable。
- **看见回了字节 不是已经装完：** 看见 16 MB 上限，不是已经装完 interchangeable。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 16 MB 上限 正式三事（375 余量），先数清问的是是不是已经是快照报文 4 MB、是不是已经是共识常数、还是看见回了字节是不是已经装完，再决定要不要同一次发布。375 loadchunk vs retrieved bundled unbundling 在本页 item 3 完成。
