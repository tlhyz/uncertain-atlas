# 模式：点名 没调 Prepare not already packed another raw proposal / not already dropped tx from proposal / not already settled 正式三事（356 余量）

**层次**：实现 / validValue 跳过 Prepare。  
**分类**：建议（产品）。  
**对应例**：[worked-example-validvalue-notraw-vs-bundled.md](../../tracks/implementation/worked-example-validvalue-notraw-vs-bundled.md)。

没调 Prepare not already packed another raw proposal / not already dropped tx from proposal / not already settled 正式三事（356 余量） 要先数清问的是哪一件，再决定要不要同一次发布。

- **没调 Prepare 不是已经又装了一份 raw 提案：** 看见没调 Prepare，不是已经又装了一份 raw 提案 interchangeable / 853 validvalue-notraw interchangeable。
- **看见用了 validValue 不是已经从提案拿掉 tx：** 看见没调 Prepare，不是已经从提案拿掉 tx interchangeable / 355。
- **看见跳过了 不是已经交差：** 看见没调 Prepare，不是已经交差 interchangeable。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看没调 Prepare 正式三事（356 余量），先数清问的是是不是已经又装了一份 raw 提案、是不是已经从提案拿掉 tx / 355、还是看见跳过了是不是已经交差，再决定要不要同一次发布。356 validvalue vs prepare bundled unbundling 在本页 item 3 完成。
