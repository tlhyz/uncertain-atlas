# 模式：点名 必须回四列 not already changed set / not already settled / not already header AppHash 正式三事（363 余量）

**层次**：实现 / Finalize 回包义务。  
**分类**：建议（产品）。  
**对应例**：[worked-example-finalize-equiv-notchanged-vs-bundled.md](../../tracks/implementation/worked-example-finalize-equiv-notchanged-vs-bundled.md)。

必须回四列 not already changed set / not already settled / not already header AppHash 正式三事（363 余量） 要先数清问的是哪一件，再决定要不要同一次发布。

- **回了四列 不是已经改了集合：** 看见回了四列，不是已经改了集合 interchangeable / 838 finalize-equiv-notchanged interchangeable。
- **看见有 validator_updates 不是已经交差：** 看见回了四列，不是已经交差 interchangeable。
- **看见必须回 不是已经印进本头：** 看见回了四列，不是已经印进本头 interchangeable / 147。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看必须回四列 正式三事（363 余量），先数清问的是是不是已经改了集合 / 364 / 835、是不是已经交差、还是看见必须回是不是已经印进本头 / 147，再决定要不要同一次发布。363 finalize-equiv vs gates bundled unbundling 在本页 item 3 完成。
