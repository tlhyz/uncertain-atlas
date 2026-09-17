# 模式：点名 exectx-notheader 杠

**层次**：实现 / Code / Data not already this-header / not already in-hash / not already consensus 正式三事（316 余量）。  
**分类**：建议（产品）。  
**来源**：CometBFT 官方 [Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Transaction Results / ExecTxResult。  
**对应**：[`../tracks/implementation/worked-example-exectx-notheader-vs-bundled.md`](../tracks/implementation/worked-example-exectx-notheader-vs-bundled.md)。

- **Code / Data 不是已经印进本头：** 看见 Code / Data，不是已经印进本头 interchangeable / 1015 exectx-notheader interchangeable。
- **看见 Events 不是已经进了那份哈希：** 看见 Events，不是已经进了那份哈希 interchangeable。
- **看见 Info / Log 不是已经是共识：** 看见 Info / Log，不是已经是共识 interchangeable。

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Code / Data 正式三事（316 余量），先数清问的是是不是已经印进本头、是不是已经进了那份哈希、还是看见 Info / Log 是不是已经是共识，再决定要不要同一次发布。316 exectxresult vs consensus bundled unbundling 在本页 item 3 完成。
