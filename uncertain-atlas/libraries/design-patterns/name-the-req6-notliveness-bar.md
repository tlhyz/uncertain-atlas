# 模式：点名 Extend 或 Verify 里有确定 bug 会让带无效扩展的 Precommit 被丢掉 not already only liveness / not already block invalid / not already nondet 正式三事（348 余量）

**层次**：实现 / Extend–Verify 一致性。  
**分类**：建议（产品）。  
**对应例**：[worked-example-req6-notliveness-vs-bundled.md](../../tracks/implementation/worked-example-req6-notliveness-vs-bundled.md)。

Extend 或 Verify 里有确定 bug 会让带无效扩展的 Precommit 被丢掉 not already only liveness / not already block invalid / not already nondet 正式三事（348 余量） 要先数清问的是哪一件，再决定要不要同一次发布。

- **确定 bug 不是已经只是活性问题：** 看见有确定 bug，不是已经只是活性问题 interchangeable / 870 req6-notliveness interchangeable。
- **看见 Precommit 被丢掉 不是已经是块非法：** 看见 Precommit 被丢掉，不是已经是块非法 interchangeable。
- **看见有确定 bug 不是已经是非确定 bug：** 看见有确定 bug，不是已经是非确定 bug interchangeable。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Extend 或 Verify 里有确定 bug 会让带无效扩展的 Precommit 被丢掉 正式三事（348 余量），先数清问的是是不是已经只是活性问题、是不是已经是块非法、还是看见有确定 bug 是不是已经是非确定 bug，再决定要不要同一次发布。348 req6 vs accept bundled unbundling 在本页 item 2 续。
