# 模式：点名 填了证据 MaxBytes not already under block cap / not already overhead-deducted / not already settled 正式三事（331 余量）

**层次**：实现 / EvidenceParams.MaxBytes。  
**分类**：建议（产品）。  
**对应例**：[worked-example-evidence-maxbytes-notunder-vs-bundled.md](../../tracks/implementation/worked-example-evidence-maxbytes-notunder-vs-bundled.md)。

填了证据 MaxBytes not already under block cap / not already overhead-deducted / not already settled 正式三事（331 余量） 要先数清问的是哪一件，再决定要不要同一次发布。

- **填了证据 MaxBytes 不是已经落在块上限下面：** 看见填了字段，不是已经落在块上限下面 interchangeable / 920 evidence-maxbytes-notunder interchangeable。
- **看见有上限 不是已经扣掉开销：** 看见有上限，不是已经从块体积扣掉开销 interchangeable。
- **看见应当落在下面 不是已经交差：** 看见应当落在下面，不是已经交差 interchangeable。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看填了证据 MaxBytes 正式三事（331 余量），先数清问的是是不是已经落在块上限下面、是不是已经扣掉开销、还是看见应当落在下面是不是已经交差，再决定要不要同一次发布。331 evidence-maxbytes vs block bundled unbundling 在本页 item 1 启动。
