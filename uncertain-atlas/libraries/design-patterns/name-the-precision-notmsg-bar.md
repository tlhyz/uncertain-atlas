# 模式：点名 填了 Precision not already MessageDelay / not already timely / not already settled 正式三事（336 余量）

**层次**：实现 / SynchronyParams。  
**分类**：建议（产品）。  
**对应例**：[worked-example-precision-notmsg-vs-bundled.md](../../tracks/implementation/worked-example-precision-notmsg-vs-bundled.md)。

填了 Precision not already MessageDelay / not already timely / not already settled 正式三事（336 余量） 要先数清问的是哪一件，再决定要不要同一次发布。

- **填了 Precision 不是已经是 MessageDelay：** 看见填了 Precision，不是已经填了 MessageDelay interchangeable / 923 precision-notmsg interchangeable。
- **看见钟偏有界 不是已经 timely：** 看见钟偏有界，不是延迟已经有界 interchangeable。
- **看见能出合法提案 不是已经交差：** 看见能出合法提案，不是已经交差 interchangeable。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看填了 Precision 正式三事（336 余量），先数清问的是是不是已经是 MessageDelay、是不是已经 timely、还是看见能出合法提案是不是已经交差，再决定要不要同一次发布。336 precision vs msgdelay bundled unbundling 在本页 item 1 启动。
