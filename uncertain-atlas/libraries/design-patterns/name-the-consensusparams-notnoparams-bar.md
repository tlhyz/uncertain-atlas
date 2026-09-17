# 模式：点名 InitChain 空参数 not already no params / not already app empty params / not already settled 正式三事（319 余量）

**层次**：实现 / ConsensusParams。  
**分类**：建议（产品）。  
**对应例**：[worked-example-consensusparams-notnoparams-vs-bundled.md](../../tracks/implementation/worked-example-consensusparams-notnoparams-vs-bundled.md)。

InitChain 空参数 not already no params / not already app empty params / not already settled 正式三事（319 余量） 要先数清问的是哪一件，再决定要不要同一次发布。

- **InitChain 空参数 不是已经没有参数：** 看见回了空，不是已经没有参数 interchangeable / 908 consensusparams-notnoparams interchangeable。
- **看见没回 不是已经用了应用自己的空参数：** 看见没回，不是已经删掉创世参数 interchangeable。
- **看见能设初始参数 不是已经交差：** 看见能设初始参数，不是已经交差 interchangeable。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 InitChain 空参数 正式三事（319 余量），先数清问的是是不是已经没有参数、是不是已经用了应用自己的空参数、还是看见能设初始参数是不是已经交差，再决定要不要同一次发布。319 consensusparams vs update bundled unbundling 在本页 item 1 启动。
