# 模式：点名 证据 MaxBytes not already block MaxBytes / not already unlimited-minus-one / not already settled 正式三事（331 余量）

**层次**：实现 / EvidenceParams.MaxBytes。  
**分类**：建议（产品）。  
**对应例**：[worked-example-evidence-maxbytes-notblock-vs-bundled.md](../../tracks/implementation/worked-example-evidence-maxbytes-notblock-vs-bundled.md)。

证据 MaxBytes not already block MaxBytes / not already unlimited-minus-one / not already settled 正式三事（331 余量） 要先数清问的是哪一件，再决定要不要同一次发布。

- **证据 MaxBytes 不是已经是块 MaxBytes：** 看见证据这边有 MaxBytes，不是已经是块上限 interchangeable / 922 evidence-maxbytes-notblock interchangeable。
- **看见填了数 不是已经是写成 -1 的那条：** 看见填了数，不是已经是块 MaxBytes 写成 -1 interchangeable。
- **看见有上限 不是已经交差：** 看见有上限，不是已经对照过第一轮超时 interchangeable。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看证据 MaxBytes 正式三事（331 余量），先数清问的是是不是已经是块 MaxBytes、是不是已经是写成 -1 的那条、还是看见有上限是不是已经交差，再决定要不要同一次发布。331 evidence-maxbytes vs block bundled unbundling 在本页 item 3 完成。
