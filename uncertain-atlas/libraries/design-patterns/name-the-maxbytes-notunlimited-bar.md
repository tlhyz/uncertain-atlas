# 模式：把 MaxBytes 写成 -1 就按 100 MB 验不是已经没有上限 not already unlimited / not already no-cap / not already free-return 正式三事（337 余量）说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) List of Parameters / BlockParams.MaxBytes。  
**例**：[写成 -1 not already unlimited ≠ bundled（337）](../../tracks/implementation/worked-example-maxbytes-notunlimited-vs-bundled.md)。

## 三个名字

1. **写成 -1 不是 already unlimited：** 看见 MaxBytes 写成 -1 / 写成 -1 / -1 那一档，不是已经没有上限 interchangeable / 已经无上限交差 interchangeable，不是 337 maxbytescap bundled interchangeable / 299 evidence-reap interchangeable / maxbytescap-sold-as-unlimited interchangeable。

2. **按 100 MB 验 不是 already no-cap：** 看见引擎按 100 MB 验 / 实际要验的值是 100 MB / 100 MB 那把尺，不是已经没有引擎帽 interchangeable / 已经帽没了交差 interchangeable，不是 299 evidence-reap interchangeable / 337 maxbytescap item 2 interchangeable。

3. **能打满 不是 already free-return：** 看见能打满 / 应用已经可以随便回的联想 / 整池都给了 Prepare，不是已经可以随便回 interchangeable / 已经随便交差 interchangeable，不是 299 evidence-reap interchangeable / 337 maxbytescap item 3 interchangeable。

官方把写成 -1 单句、already unlimited、already no-cap、already free-return 写成三个名字。把它们叫成一个「看见写成 -1 就已经没有上限 interchangeable / 就已经没有引擎帽 interchangeable / 就已经可以随便回 interchangeable」，会把 not already unlimited、not already no-cap、not already free-return 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 MaxBytes 写成 -1 就按 100 MB 验不是已经没有上限 not already unlimited / not already no-cap / not already free-return 正式三事（337 余量），先数清问的是写成 -1 是不是 already unlimited / 337 / maxbytescap-sold-as-unlimited，是不是按 100 MB 验 是不是 already no-cap，还是能打满 是不是 already free-return，再决定要不要同一次发布。337 maxbytescap vs unlimited bundled unbundling 在本页 item 1 启动。
