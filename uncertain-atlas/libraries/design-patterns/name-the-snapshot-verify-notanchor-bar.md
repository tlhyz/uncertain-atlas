# 模式：点名 增量验了 chunk not already the only trusted AppHash / not already unforgeable metadata / not already settled 正式三事（332 余量）

**层次**：实现 / Snapshot Verification。  
**分类**：建议（产品）。  
**对应例**：[worked-example-snapshot-verify-notanchor-vs-bundled.md](../../tracks/implementation/worked-example-snapshot-verify-notanchor-vs-bundled.md)。

增量验了 chunk not already the only trusted AppHash / not already unforgeable metadata / not already settled 正式三事（332 余量） 要先数清问的是哪一件，再决定要不要同一次发布。

- **增量验了 chunk 不是已经是唯一可信的 AppHash：** 看见做了增量验，不是已经是那份唯一可信锚 interchangeable / 936 snapshot-verify-notanchor interchangeable。
- **看见 checksum 过了 不是已经不能被伪造元数据：** 看见 checksum 过了，不是元数据已经不能伪造 interchangeable。
- **看见证明绿了 不是已经交差：** 看见证明绿了，不是已经代替最后那次 Info interchangeable。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看增量验了 chunk 正式三事（332 余量），先数清问的是是不是已经是唯一可信的 AppHash、是不是已经不能被伪造元数据、还是看见证明绿了是不是已经交差，再决定要不要同一次发布。332 snapshot-verify vs early bundled unbundling 在本页 item 2 续。
