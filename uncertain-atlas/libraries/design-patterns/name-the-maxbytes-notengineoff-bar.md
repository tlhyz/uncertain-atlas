# 模式：把应用自己卡体积不是已经引擎不管了 not already engine-off / not already app-only-cap / not already no-100mb-ruler 正式三事（337 余量）说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) List of Parameters / BlockParams.MaxBytes。  
**例**：[应用自己卡体积 not already engine-off ≠ bundled（337）](../../tracks/implementation/worked-example-maxbytes-notengineoff-vs-bundled.md)。

## 三个名字

1. **应用自己卡体积 不是 already engine-off：** 看见应用自己卡体积 / 应用侧设了字节上限 / Prepare 卡住回包，不是已经引擎不管了 interchangeable / 已经引擎关掉交差 interchangeable，不是 337 maxbytescap bundled interchangeable / 63 maxbytes-sla interchangeable / maxbytescap-sold-as-unlimited interchangeable。

2. **MAY 写成 -1 不是 already app-only-cap：** 看见 MAY 写成 -1 / 这时可以写成 -1 / 应用自己卡时写 -1，不是已经只有应用这一把尺 interchangeable / 已经只有应用交差 interchangeable，不是 299 evidence-reap interchangeable / 337 maxbytescap item 1 interchangeable。

3. **Process 会拒 不是 already no-100mb-ruler：** 看见 Process 会拒 / ProcessProposal 拒超限块 / 应用会拒超限，不是已经没有 100 MB 那把尺 interchangeable / 已经 100 MB 尺没了交差 interchangeable，不是 764 maxbytes-notunlimited interchangeable / 337 maxbytescap item 3 interchangeable。

官方把应用自己卡体积单句、already engine-off、already app-only-cap、already no-100mb-ruler 写成三个名字。把它们叫成一个「看见应用自己卡体积就已经引擎不管了 interchangeable / 就已经只有应用这一把尺 interchangeable / 就已经没有 100 MB 那把尺 interchangeable」，会把 not already engine-off、not already app-only-cap、not already no-100mb-ruler 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看应用自己卡体积不是已经引擎不管了 not already engine-off / not already app-only-cap / not already no-100mb-ruler 正式三事（337 余量），先数清问的是应用自己卡体积 是不是 already engine-off / 337 / maxbytescap-sold-as-unlimited，是不是 MAY 写成 -1 是不是 already app-only-cap，还是 Process 会拒 是不是 already no-100mb-ruler，再决定要不要同一次发布。337 maxbytescap vs unlimited bundled unbundling 在本页 item 2 续。
