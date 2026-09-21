# 反模式：把应用自己卡体积不是已经引擎不管了 not already engine-off / not already app-only-cap / not already no-100mb-ruler 正式三事（337 余量）说成已经引擎不管了 / 已经只有应用这一把尺 / 已经没有 100 MB 那把尺

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[应用自己卡体积 not already engine-off ≠ bundled（337）](../../tracks/implementation/worked-example-maxbytes-notengineoff-vs-bundled.md)。

## 卖法

把应用自己卡体积 / 应用侧设了字节上限 / Prepare 卡住回包 写成已经引擎不管了 interchangeable / 已经 engine-off interchangeable / 已经引擎关掉交差 interchangeable / 337 maxbytescap bundled interchangeable / 63 maxbytes-sla interchangeable / maxbytescap-sold-as-unlimited interchangeable；把 MAY 写成 -1 / 这时可以写成 -1 / 应用自己卡时写 -1 写成已经只有应用这一把尺 interchangeable / 已经 app-only-cap interchangeable；把 Process 会拒 / ProcessProposal 拒超限块 / 应用会拒超限 写成已经没有 100 MB 那把尺 interchangeable / 已经 no-100mb-ruler interchangeable，或已经和 337 maxbytescap bundled / maxbytescap-sold-as-unlimited interchangeable / 765 maxbytes-notengineoff interchangeable。

## 为什么错

官方把应用自己卡体积单句、already engine-off、already app-only-cap、already no-100mb-ruler 写成三件独立的实现事。把它们卖成 already engine-off interchangeable / already app-only-cap interchangeable / already no-100mb-ruler interchangeable，会把 not already engine-off、not already app-only-cap、not already no-100mb-ruler 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看应用自己卡体积不是已经引擎不管了 not already engine-off / not already app-only-cap / not already no-100mb-ruler 正式三事（337 余量），必须分开 not already engine-off、not already app-only-cap、not already no-100mb-ruler 三件事，不要和 337 / 299 / 63 / 331 / 764 / 766 糊成一句。

## 和相邻反模式

- [maxbytescap-sold-as-unlimited](maxbytescap-sold-as-unlimited.md) 是 MaxBytes cap bundled 全段，不是本页应用自己卡体积 item 2 单句边界。
- [maxbytes-notunlimited-sold-as-bundled](maxbytes-notunlimited-sold-as-bundled.md) 是写成 -1 ≠ 已经没有上限（337 item 1），不是本页应用自己卡 ≠ 已经引擎不管了 边界。
- [maxbytes-sold-as-sla](maxbytes-sold-as-sla.md) 是仓库默认 MaxBytes ≠ 已经是活性 SLA（63），不是本页 MAY 写成 -1 边界。
- [evidence-sold-as-full-block](evidence-sold-as-full-block.md) 是整池都给 Prepare ≠ 已经没有上限（299），不是本页 Process 会拒边界。
