# 模式：把增量验了 chunk 不是已经是唯一可信的 AppHash not already unique-apphash / not already metadata-unforgeable / not already replaces-final-info 正式三事（332 余量）说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Snapshot Verification。  
**例**：[增量验了 chunk not already unique-apphash ≠ bundled（332）](../../tracks/implementation/worked-example-snapshotverify-notuniqueapphash-vs-bundled.md)。

## 三个名字

1. **增量验了 chunk 不是 already unique-apphash：** 看见增量验了 chunk / 按 chunk 对 AppHash 做增量验 / 绑了默克尔证明，不是已经是唯一可信的 AppHash interchangeable / 已经唯一可信锚交差 interchangeable，不是 332 snapshotverify bundled interchangeable / 33 four gates interchangeable / snapshotverify-sold-as-early interchangeable。

2. **checksum 过了 不是 already metadata-unforgeable：** 看见 checksum 过了 / checksum / 防盘或网把数据弄坏，不是已经不能伪造元数据 interchangeable / 已经元数据不能伪造交差 interchangeable，不是 38 apphash-only interchangeable / 332 snapshotverify item 1 interchangeable。

3. **证明绿了 不是 already replaces-final-info：** 看见证明绿了 / 捆绑的默克尔绿了 / 早发现失败核对绿了，不是已经代替最后那次 Info interchangeable / 已经代替最后 Info 交差 interchangeable，不是 752 snapshotverify-notduringrestore interchangeable / 332 snapshotverify item 3 interchangeable。

官方把增量验了 chunk 单句、already unique-apphash、already metadata-unforgeable、already replaces-final-info 写成三个名字。把它们叫成一个「看见增量验了 chunk 就已经是唯一可信的 AppHash interchangeable / 就已经不能伪造元数据 interchangeable / 就已经代替最后那次 Info interchangeable」，会把 not already unique-apphash、not already metadata-unforgeable、not already replaces-final-info 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看增量验了 chunk 不是已经是唯一可信的 AppHash not already unique-apphash / not already metadata-unforgeable / not already replaces-final-info 正式三事（332 余量），先数清问的是增量验了 chunk 是不是 already unique-apphash / 332 / snapshotverify-sold-as-early，是不是 checksum 过了 是不是 already metadata-unforgeable，还是证明绿了 是不是 already replaces-final-info，再决定要不要同一次发布。332 snapshotverify vs early bundled unbundling 在本页 item 2 续。
