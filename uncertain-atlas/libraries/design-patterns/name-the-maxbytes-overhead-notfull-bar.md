# 模式：点名 MaxBytes 减去头集合证据才是交易上限 not already whole block holds txs / not already evidence MaxBytes / not already settled 正式三事（344 余量）

**层次**：实现 / BlockParams.MaxBytes 开销与投递。  
**分类**：建议（产品）。  
**对应例**：[worked-example-maxbytes-overhead-notfull-vs-bundled.md](../../tracks/implementation/worked-example-maxbytes-overhead-notfull-vs-bundled.md)。

MaxBytes 减去头集合证据才是交易上限 not already whole block holds txs / not already evidence MaxBytes / not already settled 正式三事（344 余量） 要先数清问的是哪一件，再决定要不要同一次发布。

- **扣开销之后才是交易上限 不是已经整块都能装交易：** 看见填了块上限，不是已经整块都能装交易 interchangeable / 881 maxbytes-overhead-notfull interchangeable。
- **看见能装交易 不是已经是证据 MaxBytes：** 看见能装交易，不是已经是证据 MaxBytes interchangeable。
- **看见扣了开销 不是已经交差：** 看见扣了开销，不是已经交差 interchangeable。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 MaxBytes 减去头集合证据才是交易上限 正式三事（344 余量），先数清问的是是不是已经整块都能装交易、是不是已经是证据 MaxBytes、还是看见扣了开销是不是已经交差，再决定要不要同一次发布。344 maxbytes vs full bundled unbundling 在本页 item 1 启动。
