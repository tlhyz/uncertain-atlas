# 模式：点名 finbar-notrotate 杠

**层次**：实现 / FinalizeBlockResponse.validator_updates not already h1-rotate / not already set-changed / not already four-col 正式三事（431 余量）。  
**分类**：建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) FinalizeBlock Response / Usage。  
**对应**：[`../tracks/implementation/worked-example-finbar-notrotate-vs-bundled.md`](../tracks/implementation/worked-example-finbar-notrotate-vs-bundled.md)。

- **validator_updates 不是已经在 H+1 换人：** 看见回了 validator_updates，不是已经在 H+1 换人 interchangeable / 1072 finbar-notrotate interchangeable。
- **看见有 ValidatorUpdate 不是已经改了集合：** 看见有 ValidatorUpdate，不是已经改了集合 interchangeable。
- **看见能指下一份集合 不是已经必须回四列：** 看见能指下一份集合，不是已经必须回四列那种已经交差 interchangeable。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 validator_updates 正式三事（431 余量），先数清问的是是不是已经在 H+1 换人、是不是已经改了集合、还是看见能指下一份集合是不是已经必须回四列，再决定要不要同一次发布。431 finrespbar vs header bundled unbundling 在本页 item 3 完成。
