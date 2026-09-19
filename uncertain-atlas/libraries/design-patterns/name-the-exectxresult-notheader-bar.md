# 模式：把 Code Data 不是已经印进本头 not already in this header / not already in LastResultsHash / not already consensus field 正式三事（316 余量）说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Transaction Results / Specifics of `ExecTxResult`。  
**例**：[Code / Data not already in this header ≠ bundled（316）](../../tracks/implementation/worked-example-exectxresult-notheader-vs-bundled.md)。

## 三个名字

1. **Code / Data 不是 already in this header：** 看见回了 Code 和 Data，不是已经印进本头 interchangeable / 已经进本头 LastResultsHash interchangeable，不是 316 exectxresult bundled interchangeable / 147 apphash interchangeable / exectxresult-sold-as-consensus interchangeable。

2. **Events 不是 already in LastResultsHash：** 看见执行里产出了事件 / 按事件查询，不是已经进了那份哈希 interchangeable / 已经编进 LastResultsHash interchangeable，不是 316 exectxresult item 1 interchangeable / 707 exectxresult-notorder interchangeable。

3. **Info / Log 不是 already consensus field：** 看见调试字段 / 非确定调试字段，不是已经是共识字段 interchangeable / 已经进共识 interchangeable，不是 316 exectxresult item 2 interchangeable / 708 exectxresult-notexcluded interchangeable。

官方把 Code / Data 单句、already in this header、already in LastResultsHash、already consensus field 写成三个名字。把它们叫成一个「看见 Code / Data 就已经印进本头 interchangeable / 就已经进了那份哈希 interchangeable / 就已经是共识 interchangeable」，会把 not already in this header、not already in LastResultsHash、not already consensus field 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Code Data 不是已经印进本头 not already in this header / not already in LastResultsHash / not already consensus field 正式三事（316 余量），先数清问的是 Code / Data 是不是 already in this header / 316 / 147，是不是 Events 是不是 already in LastResultsHash，还是 Info / Log 是不是 already consensus field，再决定要不要同一次发布。316 exectxresult vs consensus bundled unbundling 在本页 item 3 完成。
