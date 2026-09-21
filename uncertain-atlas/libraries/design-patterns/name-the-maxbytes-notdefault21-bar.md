# 模式：把必须 -1 或不超过 100 MB 不是已经是默认 21 MB not already default-21 / not already bandwidth-assessed / not already tuned-down 正式三事（337 余量）说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) List of Parameters / BlockParams.MaxBytes。  
**例**：[合法范围 not already default-21 ≠ bundled（337）](../../tracks/implementation/worked-example-maxbytes-notdefault21-vs-bundled.md)。

## 三个名字

1. **合法范围 不是 already default-21：** 看见必须 MaxBytes == -1 或 0 < MaxBytes <= 100 MB / 合法取值范围 / 合法范围那一档，不是已经是默认 21 MB interchangeable / 已经默认那档交差 interchangeable，不是 337 maxbytescap bundled interchangeable / 63 maxbytes-sla interchangeable / maxbytescap-sold-as-unlimited interchangeable。

2. **默认能接到 21 MB 不是 already bandwidth-assessed：** 看见默认能接到 21 MB / 默认值把最大 21 MB 当成合法 / 默认 21 MB，不是已经评估过带宽 interchangeable / 已经对照过 timeout_propose 交差 interchangeable，不是 63 maxbytes-sla interchangeable / 337 maxbytescap item 2 interchangeable。

3. **建议下调 不是 already tuned-down：** 看见建议下调 / 强烈建议把默认往下调 / 建议调小，不是已经下调 interchangeable / 已经调小交差 interchangeable，不是 63 maxbytes-sla interchangeable / 337 maxbytescap item 1 interchangeable。

官方把合法范围单句、already default-21、already bandwidth-assessed、already tuned-down 写成三个名字。把它们叫成一个「看见必须 -1 或不超过 100 MB 就已经是默认 21 MB interchangeable / 就已经评估过带宽 interchangeable / 就已经下调 interchangeable」，会把 not already default-21、not already bandwidth-assessed、not already tuned-down 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看必须 -1 或不超过 100 MB 不是已经是默认 21 MB not already default-21 / not already bandwidth-assessed / not already tuned-down 正式三事（337 余量），先数清问的是合法范围 是不是 already default-21 / 337 / maxbytescap-sold-as-unlimited，是不是默认能接到 21 MB 是不是 already bandwidth-assessed，还是建议下调 是不是 already tuned-down，再决定要不要同一次发布。337 maxbytescap vs unlimited bundled unbundling 在本页 item 3 完成。
