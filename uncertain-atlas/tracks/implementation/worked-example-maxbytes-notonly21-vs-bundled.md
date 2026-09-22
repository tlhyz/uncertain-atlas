# 例：看见诚实验证者 MAY 出满 MaxBytes / 看见能广播到配置上限 / 看见写了 MAY is not already already default-21 interchangeable / already unlimited interchangeable / already may-is-must interchangeable

**层次**：实现 / 诚实验证者 MAY 出满 MaxBytes 不是已经只会出默认 21 MB not already default-21 / not already unlimited / not already may-is-must 正式三事（344 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) List of Parameters / BlockParams.MaxBytes。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「诚实验证者 MAY 出满 MaxBytes 不是已经只会出默认 21 MB not already default-21 / not already unlimited / not already may-is-must 正式三事（344 余量）/ not 786 maxbytes-notonly21 interchangeable / not 344 maxbytesoverhead bundled interchangeable」，不是 MaxBytes 开销与投递 bundled（344），也不是 MaxBytes 减去头集合证据才是交易上限不是已经整块都能装交易（785 item 1 余量）或 timeout 必须按满块投递不是已经填了 TimeoutPropose 就装得下（787 item 3 余量），也不是必须 -1 或不超过 100 MB 不是已经是默认 21 MB（766）。不要另写怎样算头和证据开销。

## 官方三件事

规范把 Requirements 里诚实验证者可以造出并广播达到配置 `MaxBytes` 的块 和「已经是默认能接到 21 MB 就已经只会出默认 21 MB interchangeable / 已经是能打到配置上限就已经没有上限 interchangeable / 已经是写了 MAY 就已经必须打满 interchangeable / 已经是 maxbytesoverhead bundled interchangeable」分开写成三件独立的实现事，不是「看见诚实验证者 MAY 出满就已经只会出默认 21 MB interchangeable / 就已经没有上限 interchangeable / 就已经必须打满 interchangeable」一件事：

1. **看见诚实验证者 MAY 出满 MaxBytes / 看见能广播到配置上限 / 看见默认能接到 21 MB is not already 已经只会出默认 21 MB interchangeable / 已经 default-21 interchangeable / 已经只会出那一档交差 interchangeable / 344 maxbytesoverhead bundled interchangeable / 337 maxbytescap interchangeable / maxbytesoverhead-sold-as-full interchangeable，也不是已经 MaxBytes 开销与投递 bundled（344） interchangeable / 786 maxbytes-notonly21 interchangeable / 344 maxbytesoverhead item 2 interchangeable，也不是已经诚实验证者 MAY 出满 MaxBytes 不是已经只会出默认 21 MB not already default-21 / not already unlimited / not already may-is-must 正式三事 bundled（344 item 2 余量） interchangeable / 344 maxbytesoverhead item 2 interchangeable，也不是已经完整块上限不是已经整块装交易（785） interchangeable / 787 maxbytes-nottimeoutfit interchangeable / 766 maxbytes-notdefault21 interchangeable，也不是已经 -1 就按 100 MB 验已经没有上限（337） interchangeable。**  
   官方写：应用应当知道，**诚实验证者可以**造出并广播达到配置 `MaxBytes` 的块。看见默认能接到 21 MB，不是诚实者已经只会出那一档。看见诚实验证者 MAY 出满，不是已经 default-21 interchangeable——344 钉 bundled 三事，本页从 item 2 侧钉 not already default-21 单句。看见能广播到配置上限，不是已经 MaxBytes 开销与投递 bundled（344） interchangeable——344 钉 bundled，本页钉 item 2 第一件事。看见默认能接到 21 MB，不是已经必须 -1 或不超过 100 MB 不是已经是默认 21 MB（766） interchangeable——766 另钉 337 item 3。344 maxbytesoverhead vs full bundled unbundling 在本页 item 2 续。

2. **看见能打到配置上限 / 看见配置上限在 / 看见能广播到配置上限 is not already 已经没有上限 interchangeable / 已经 unlimited interchangeable / 已经无上限交差 interchangeable / 344 maxbytesoverhead bundled interchangeable / maxbytescap-sold-as-unlimited interchangeable / 337 maxbytescap interchangeable，也不是已经 MaxBytes 开销与投递 bundled（344） interchangeable / 786 maxbytes-notonly21 interchangeable / 344 maxbytesoverhead item 1 扣开销 interchangeable / 344 maxbytesoverhead item 3 timeout interchangeable，也不是已经诚实验证者 MAY 出满 MaxBytes 不是已经只会出默认 21 MB not already default-21 / not already unlimited / not already may-is-must 正式三事 bundled（344 item 2 余量） interchangeable / 344 maxbytesoverhead item 2 interchangeable，也不是已经只会出默认 21 MB（本页第一件事） interchangeable。**  
   官方写：看见能打到配置上限，不是已经写成 -1、已经没有上限。看见配置上限在，不是已经 unlimited interchangeable——本页钉 not already unlimited 单句。看见能广播到配置上限，不是已经只会出默认 21 MB（本页第一件事） interchangeable——三件事分开钉。344 maxbytesoverhead vs full bundled unbundling 在本页 item 2 续。

3. **看见写了 MAY / 看见可以出满 / 看见诚实验证者可以造满 is not already 已经必须打满 interchangeable / 已经 may-is-must interchangeable / 已经打满交差 interchangeable / 344 maxbytesoverhead bundled interchangeable / 785 maxbytes-notfulltx interchangeable，也不是已经 MaxBytes 开销与投递 bundled（344） interchangeable / 786 maxbytes-notonly21 interchangeable / 344 maxbytesoverhead item 1 / 344 maxbytesoverhead item 3，也不是已经诚实验证者 MAY 出满 MaxBytes 不是已经只会出默认 21 MB not already default-21 / not already unlimited / not already may-is-must 正式三事 bundled（344 item 2 余量） interchangeable / 344 maxbytesoverhead item 2 interchangeable，也不是已经只会出默认 21 MB（本页第一件事） interchangeable / 已经没有上限（本页第二件事） interchangeable。**  
   官方写：看见写了 MAY，不是已经打满。看见可以出满，不是已经 may-is-must interchangeable——本页钉 not already may-is-must 单句。看见诚实验证者可以造满，不是已经没有上限（本页第二件事） interchangeable——三件事分开钉。344 maxbytesoverhead vs full bundled unbundling 在本页 item 2 续。

怎样算头 / 集合 / 证据开销、默认秒数、怎样设 `MaxBytes` 是规范里的做法，本页不抄。MaxBytes 开销与投递 bundled（344）、MaxBytes 减去头集合证据才是交易上限不是已经整块都能装交易（344 item 1 余量 / 785）、timeout 必须按满块投递不是已经填了 TimeoutPropose 就装得下（344 item 3 余量 / 787）、必须 -1 或不超过 100 MB 不是已经是默认 21 MB（766）、-1 就按 100 MB 验不是已经没有上限（337）、证据 MaxBytes 已经是块 MaxBytes（331）是另外那套，本页不抄。

## 官方为什么这样拆

- **诚实验证者 MAY 出满 not already default-21 ≠ 344 / 766 interchangeable：** 官方把配置上限上诚实者可打满和「必须 -1 或不超过 100 MB 不是默认 21 MB」那条尺分开。
- **能打到配置上限 not already unlimited ≠ 已经没有上限 interchangeable：** 官方把能打到配置上限和已经写成 -1 没有上限分开。
- **写了 MAY not already may-is-must ≠ 已经必须打满 interchangeable：** 官方把 MAY 和已经打满分开；344 maxbytesoverhead vs full bundled unbundling 在本页 item 2 续。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 诚实验证者 MAY 出满 | 不是 already default-21 | 不是必须 -1 或不超过 100 MB 不是默认 21 MB alone（766） |
| 能打到配置上限 | 不是 already unlimited | 不是完整块上限就已经整块装交易 alone（785） |
| 写了 MAY | 不是 already may-is-must | 不是 timeout 按满块投递 alone（787） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看诚实验证者 MAY 出满 MaxBytes 不是已经只会出默认 21 MB not already default-21 / not already unlimited / not already may-is-must 正式三事（344 余量），必须分开诚实验证者 MAY 出满 是不是 already default-21 interchangeable / 344 maxbytesoverhead bundled interchangeable / maxbytesoverhead-sold-as-full interchangeable、能打到配置上限 是不是 already unlimited interchangeable、写了 MAY 是不是 already may-is-must interchangeable。可以跳过「看见诚实验证者 MAY 出满就已经只会出默认 21 MB interchangeable / 就已经没有上限 interchangeable / 就已经必须打满 interchangeable」。不要把 21 MB 当不确定常数。不要另写怎样算头和证据开销。344 maxbytesoverhead vs full bundled unbundling 在本页 item 2 续（785 + 786）；续 [`worked-example-maxbytes-nottimeoutfit-vs-bundled.md`](worked-example-maxbytes-nottimeoutfit-vs-bundled.md)（不变量 787 item 3）已写；完成见 787。

## 本页不抄

- 怎样算头 / 集合 / 证据开销、默认秒数、怎样设 `MaxBytes`。
- MaxBytes 开销与投递 bundled。那是不变量 344。
- MaxBytes 减去头集合证据才是交易上限不是已经整块都能装交易。那是不变量 344 item 1 余量 / 785。
- timeout 必须按满块投递不是已经填了 TimeoutPropose 就装得下。那是不变量 344 item 3 余量 / 787。
- 必须 -1 或不超过 100 MB 不是已经是默认 21 MB。那是不变量 766。
- -1 就按 100 MB 验已经没有上限。那是不变量 337。
- 证据 MaxBytes 已经是块 MaxBytes。那是不变量 331。
