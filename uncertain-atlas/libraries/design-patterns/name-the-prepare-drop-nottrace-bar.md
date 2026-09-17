# 模式：点名 把 t1 改成 t2 not already can look up t1 / not already someone knows t2 from t1 / not already settled 正式三事（355 余量）

**层次**：实现 / Prepare 改列表。  
**分类**：建议（产品）。  
**对应例**：[worked-example-prepare-drop-nottrace-vs-bundled.md](../../tracks/implementation/worked-example-prepare-drop-nottrace-vs-bundled.md)。

把 t1 改成 t2 not already can look up t1 / not already someone knows t2 from t1 / not already settled 正式三事（355 余量） 要先数清问的是哪一件，再决定要不要同一次发布。

- **t1 没进块 不是已经还能按 t1 查到：** 看见 t1 没进块，不是已经还能按 t1 查到 interchangeable / 856 prepare-drop-nottrace interchangeable。
- **看见 t2 进了块 不是已经有人知道来源：** 看见 t1 没进块，不是已经有人知道 t2 来自 t1 interchangeable。
- **看见改了 不是已经交差：** 看见 t1 没进块，不是已经交差 interchangeable。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看把 t1 改成 t2 正式三事（355 余量），先数清问的是是不是已经还能按 t1 查到、是不是已经有人知道 t2 来自 t1、还是看见改了是不是已经交差，再决定要不要同一次发布。355 prepare-drop vs mempool bundled unbundling 在本页 item 3 完成。
