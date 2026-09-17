# 模式：点名 height 含根 not already header AppHash / not already proof matched / not already this-height settled 正式三事（371 余量）

**层次**：实现 / Query 高度。  
**分类**：建议（产品）。  
**对应例**：[worked-example-queryheight-notapphash-vs-bundled.md](../../tracks/implementation/worked-example-queryheight-notapphash-vs-bundled.md)。

height 含根 not already header AppHash / not already proof matched / not already this-height settled 正式三事（371 余量） 要先数清问的是哪一件，再决定要不要同一次发布。

- **含根 不是已经印进本头 AppHash：** 看见填了高度，不是已经 325 interchangeable / 814 queryheight-notapphash interchangeable。
- **看见有根 不是已经对上 Proof：** 看见填了高度，不是已经对上 Proof interchangeable。
- **看见 Height-1 不是已经是本高度交差：** 看见含根，不是已经是本高度交差 interchangeable。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 height 含根 正式三事（371 余量），先数清问的是是不是已经印进本头 AppHash / 325、是不是已经对上 Proof、还是看见 Height-1 是不是已经是本高度交差，再决定要不要同一次发布。371 queryheight vs committed bundled unbundling 在本页 item 3 完成。
