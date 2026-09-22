# 模式：把诚实验证者 MAY 出满 MaxBytes 不是已经只会出默认 21 MB not already default-21 / not already unlimited / not already may-is-must 正式三事（344 余量）说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) List of Parameters / BlockParams.MaxBytes。  
**例**：[诚实验证者 MAY 出满 MaxBytes not already default-21 ≠ bundled（344）](../../tracks/implementation/worked-example-maxbytes-notonly21-vs-bundled.md)。

## 三个名字

1. **诚实验证者 MAY 出满 不是 already default-21：** 看见诚实验证者 MAY 出满 MaxBytes / 能广播到配置上限 / 默认能接到 21 MB，不是已经只会出默认 21 MB interchangeable / 已经 default-21 interchangeable / 已经只会出那一档交差 interchangeable，不是 344 maxbytesoverhead bundled interchangeable / maxbytesoverhead-sold-as-full interchangeable / 766 maxbytes-notdefault21 interchangeable。

2. **能打到配置上限 不是 already unlimited：** 看见能打到配置上限 / 配置上限在 / 能广播到配置上限，不是已经没有上限 interchangeable / 已经 unlimited interchangeable / 已经无上限交差 interchangeable，不是 337 maxbytescap interchangeable / maxbytescap-sold-as-unlimited interchangeable。

3. **写了 MAY 不是 already may-is-must：** 看见写了 MAY / 可以出满 / 诚实验证者可以造满，不是已经必须打满 interchangeable / 已经 may-is-must interchangeable / 已经打满交差 interchangeable，不是 785 maxbytes-notfulltx interchangeable / 787 maxbytes-nottimeoutfit interchangeable。

官方把配置上限、默认 21 MB 那一档、MAY 不是必须打满写成三个名字。把它们叫成一个「看见诚实验证者 MAY 出满就已经只会出默认 21 MB interchangeable / 就已经没有上限 interchangeable / 就已经必须打满 interchangeable」，会把 not already default-21、not already unlimited、not already may-is-must 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看诚实验证者 MAY 出满 MaxBytes 不是已经只会出默认 21 MB not already default-21 / not already unlimited / not already may-is-must 正式三事（344 余量），先数清问的是诚实验证者 MAY 出满 是不是 already default-21 / 344 / maxbytesoverhead-sold-as-full，是不是能打到配置上限 是不是 already unlimited，还是写了 MAY 是不是 already may-is-must，再决定要不要同一次发布。344 maxbytesoverhead vs full bundled unbundling 在本页 item 2 续。
