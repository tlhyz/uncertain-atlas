# 反模式：把 应用自己卡体积 not already engine-off / not already only-app-ruler / not already settled 正式三事（337 余量） 卖成 已经引擎不管了 / 已经只有应用这一把尺 / 已经交差

**层次**：实现 / BlockParams.MaxBytes。  
**分类**：建议（产品）。  
**对应例**：[worked-example-maxbytes-cap-notapp-vs-bundled.md](../../tracks/implementation/worked-example-maxbytes-cap-notapp-vs-bundled.md)。

官方把 -1 就按 100 MB 验 / 应用自己卡体积 / 必须 -1 或不超过 100 MB 三条核心句写成三件独立的实现事。把它们卖成已经引擎不管了 / 已经只有应用这一把尺 / 已经交差，会把三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看应用自己卡体积 正式三事（337 余量），必须分开 not already engine-off、not already only-app-ruler、not already settled 三件事，不要和 337 / 63 / 344 / 917 / 919 糊成一句。

## 和相邻反模式

- [maxbytes-cap-notunlim-sold-as-bundled](maxbytes-cap-notunlim-sold-as-bundled.md) 是 -1 仍按 100 MB 验单句边界（917 item 1），不是本页应用自己卡引擎仍管边界。
- 仓库默认 MaxBytes 已经是活性 SLA 是不变量 63，不是本页 MAY 写成 -1 仍有 100 MB 尺边界。
