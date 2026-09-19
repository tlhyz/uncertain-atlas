# 模式：把拉失败换一份不是已经能接着装 not already can-resume / not already same-snapshot / not already prior-usable 正式三事（321 余量）说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Snapshot Restoration。  
**例**：[换了一份 not already can-resume ≠ bundled（321）](../../tracks/implementation/worked-example-snapshotrestore-notresume-vs-bundled.md)。

## 三个名字

1. **换了一份 不是 already can-resume：** 看见拉一块失败换了一份快照 / 拒掉这份再 Offer 换一份，不是已经能接着装 interchangeable / 已经能接着上次交差 interchangeable，不是 321 snapshotrestore bundled interchangeable / 33 four gates interchangeable / snapshotrestore-sold-as-offered interchangeable。

2. **能重试 不是 already same-snapshot：** 看见应用支持重新开始装 / 又能 Offer 一份，不是已经同一份 interchangeable / 已经同一份快照交差 interchangeable，不是 321 snapshotrestore item 1 interchangeable / 719 snapshotrestore-notrestored interchangeable。

3. **失败了 不是 already prior-usable：** 看见拉不到一块失败了 / 拒掉这份快照，不是已经装过的还能用 interchangeable / 已经半装还能接着用 interchangeable，不是 321 snapshotrestore item 2 interchangeable / 720 snapshotrestore-notchunkcomplete interchangeable。

官方把换了一份单句、already can-resume、already same-snapshot、already prior-usable 写成三个名字。把它们叫成一个「看见拉一块失败 / 看见换了一份快照就已经能接着装 interchangeable / 就已经同一份 interchangeable / 就已经装过的还能用 interchangeable」，会把 not already can-resume、not already same-snapshot、not already prior-usable 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看拉失败换一份不是已经能接着装 not already can-resume / not already same-snapshot / not already prior-usable 正式三事（321 余量），先数清问的是换了一份 是不是 already can-resume / 321 / snapshotrestore-sold-as-offered，是不是能重试 是不是 already same-snapshot，还是失败了 是不是 already prior-usable，再决定要不要同一次发布。321 snapshotrestore vs offer bundled unbundling 在本页 item 3 完成。
