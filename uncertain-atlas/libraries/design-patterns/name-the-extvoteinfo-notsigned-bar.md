# 模式：点名 验过的签交给应用 not already signed as-is / not already replay protected / not already must-fill 正式三事（369 余量）

**层次**：实现 / ExtendedVoteInfo。  
**分类**：建议（产品）。  
**对应例**：[worked-example-extvoteinfo-notsigned-vs-bundled.md](../../tracks/implementation/worked-example-extvoteinfo-notsigned-vs-bundled.md)。

验过的签交给应用 not already signed as-is / not already replay protected / not already must-fill 正式三事（369 余量） 要先数清问的是哪一件，再决定要不要同一次发布。

- **有签 不是已经按原样签：** 看见有签，不是已经 358 interchangeable / 819 extvoteinfo-notsigned interchangeable。
- **看见交给应用 不是已经有重放保护：** 看见有签，不是已经有重放保护 interchangeable。
- **看见签了空切片 不是已经必须填：** 看见有签，不是已经必须填 interchangeable。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看验过的签交给应用 正式三事（369 余量），先数清问的是是不是已经按原样签 / 358、是不是已经有重放保护、还是看见签了空切片是不是已经必须填，再决定要不要同一次发布。369 extvoteinfo vs local bundled unbundling 在本页 item 2 续。
