# 模式：点名 local_last_commit 是上一高度的预提交带扩展 not already this-height extension / not already H Prepare has extensions / not already settled 正式三事（359 余量）

**层次**：实现 / Prepare 请求字段。  
**分类**：建议（产品）。  
**对应例**：[worked-example-prepare-fields-notlocal-vs-bundled.md](../../tracks/implementation/worked-example-prepare-fields-notlocal-vs-bundled.md)。

local_last_commit 是上一高度的预提交带扩展 not already this-height extension / not already H Prepare has extensions / not already settled 正式三事（359 余量） 要先数清问的是哪一件，再决定要不要同一次发布。

- **有上一高的票 不是已经是本高度刚签的扩展：** 看见有上一高的票，不是已经是本高度刚签的扩展 interchangeable / 846 prepare-fields-notlocal interchangeable。
- **看见带了扩展 不是已经到了 H 就已经 Prepare 带了扩展：** 看见有上一高的票，不是已经到了 H 就已经 Prepare 带了扩展 interchangeable / 330。
- **看见能用上一高 不是已经交差：** 看见有上一高的票，不是已经交差 interchangeable。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 local_last_commit 是上一高度的预提交带扩展 正式三事（359 余量），先数清问的是是不是已经是本高度刚签的扩展、是不是已经到了 H 就已经 Prepare 带了扩展 / 330、还是看见能用上一高是不是已经交差，再决定要不要同一次发布。359 prepare-fields vs same bundled unbundling 在本页 item 2 续。
