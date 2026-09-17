# 模式：点名 必须 -1 或不超过 100 MB not already default-21 / not already bandwidth-evaluated / not already settled 正式三事（337 余量）

**层次**：实现 / BlockParams.MaxBytes。  
**分类**：建议（产品）。  
**对应例**：[worked-example-maxbytes-cap-not21-vs-bundled.md](../../tracks/implementation/worked-example-maxbytes-cap-not21-vs-bundled.md)。

必须 -1 或不超过 100 MB not already default-21 / not already bandwidth-evaluated / not already settled 正式三事（337 余量） 要先数清问的是哪一件，再决定要不要同一次发布。

- **必须 -1 或不超过 100 MB 不是已经是默认 21 MB：** 看见合法范围，不是已经是默认那档 interchangeable / 919 maxbytes-cap-not21 interchangeable。
- **看见默认能接到 21 MB 不是已经评估过带宽：** 看见默认能接到 21 MB，不是已经对照过 timeout_propose interchangeable。
- **看见建议下调 不是已经交差：** 看见建议下调，不是已经下调 / 已经交差 interchangeable。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看必须 -1 或不超过 100 MB 正式三事（337 余量），先数清问的是是不是已经是默认 21 MB、是不是已经评估过带宽、还是看见建议下调是不是已经交差，再决定要不要同一次发布。337 maxbytes-cap vs unlimited bundled unbundling 在本页 item 3 完成。
