# 模式：点名 Finalize 算出的状态必须只依赖上一份状态和决定块 not already Prepare-style other values / not already same ruler as Prepare / not already settled 正式三事（342 余量）

**层次**：实现 / FinalizeBlock 确定性。  
**分类**：建议（产品）。  
**对应例**：[worked-example-finalize-det-notprep-vs-bundled.md](../../tracks/implementation/worked-example-finalize-det-notprep-vs-bundled.md)。

Finalize 算出的状态必须只依赖上一份状态和决定块 not already Prepare-style other values / not already same ruler as Prepare / not already settled 正式三事（342 余量） 要先数清问的是哪一件，再决定要不要同一次发布。

- **状态必须确定 不是已经可以像 Prepare 那样依赖其它值：** 看见必须确定，不是已经可以像 Prepare 那样依赖其它值 interchangeable / 887 finalize-det-notprep interchangeable。
- **看见只依赖上一份状态和决定块 不是已经和 Prepare 同一把尺：** 看见只依赖上一份状态和决定块，不是已经和 Prepare 同一把尺 interchangeable。
- **看见 Finalize 回了 不是已经交差：** 看见 Finalize 回了，不是已经交差 interchangeable。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Finalize 算出的状态必须只依赖上一份状态和决定块 正式三事（342 余量），先数清问的是是不是已经可以像 Prepare 那样依赖其它值、是不是已经和 Prepare 同一把尺、还是看见 Finalize 回了是不是已经交差，再决定要不要同一次发布。342 finalize-det vs prepare bundled unbundling 在本页 item 1 启动。
