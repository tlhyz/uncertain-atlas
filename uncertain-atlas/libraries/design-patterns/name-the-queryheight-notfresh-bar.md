# 模式：点名 height 默认 0 not already fresh / not already tip / not already handshake 正式三事（371 余量）

**层次**：实现 / Query 高度。  
**分类**：建议（产品）。  
**对应例**：[worked-example-queryheight-notfresh-vs-bundled.md](../../tracks/implementation/worked-example-queryheight-notfresh-vs-bundled.md)。

height 默认 0 not already fresh / not already tip / not already handshake 正式三事（371 余量） 要先数清问的是哪一件，再决定要不要同一次发布。

- **默认 0 不是已经新鲜：** 看见没填高度，不是已经 147 interchangeable / 813 queryheight-notfresh interchangeable。
- **看见回了最新已提交 不是已经跟上尖：** 看见没填高度，不是已经跟上正在跑的块 interchangeable。
- **看见默认 0 不是已经是 Info 握手：** 看见默认 0，不是已经是 Info 握手 interchangeable。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 height 默认 0 正式三事（371 余量），先数清问的是是不是已经新鲜 / 147、是不是已经跟上尖、还是看见默认 0 是不是已经是 Info 握手，再决定要不要同一次发布。371 queryheight vs committed bundled unbundling 在本页 item 2 续。
