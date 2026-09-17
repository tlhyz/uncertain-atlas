# 模式：点名 retain_height 默认 0 not already pruning / not already settled / not already no history 正式三事（366 余量）

**层次**：实现 / Commit 保留高度。  
**分类**：建议（产品）。  
**对应例**：[worked-example-retain-notpruning-vs-bundled.md](../../tracks/implementation/worked-example-retain-notpruning-vs-bundled.md)。

retain_height 默认 0 not already pruning / not already settled / not already no history 正式三事（366 余量） 要先数清问的是哪一件，再决定要不要同一次发布。

- **没填 不是已经在剪：** 看见没填，不是已经在剪 interchangeable / 827 retain-notpruning interchangeable。
- **看见字段在 不是已经交差：** 看见没填，不是已经交差 interchangeable。
- **看见 Commit 回了 不是已经没有历史：** 看见没填，不是已经没有历史 interchangeable。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 retain_height 默认 0 正式三事（366 余量），先数清问的是是不是已经在剪、是不是已经交差、还是看见 Commit 回了是不是已经没有历史，再决定要不要同一次发布。366 retain vs kept bundled unbundling 在本页 item 1 启动。
