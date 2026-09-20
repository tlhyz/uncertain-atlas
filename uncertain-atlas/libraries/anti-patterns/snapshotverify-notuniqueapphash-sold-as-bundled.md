# 反模式：把增量验了 chunk 不是已经是唯一可信的 AppHash not already unique-apphash / not already metadata-unforgeable / not already replaces-final-info 正式三事（332 余量）说成已经是唯一可信的 AppHash / 已经不能伪造元数据 / 已经代替最后那次 Info

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[增量验了 chunk not already unique-apphash ≠ bundled（332）](../../tracks/implementation/worked-example-snapshotverify-notuniqueapphash-vs-bundled.md)。

## 卖法

把增量验了 chunk / 按 chunk 对 AppHash 做增量验 / 绑了默克尔证明 写成已经是唯一可信的 AppHash interchangeable / 已经 unique-apphash interchangeable / 已经唯一可信锚交差 interchangeable / 332 snapshotverify bundled interchangeable / 33 four gates interchangeable / snapshotverify-sold-as-early interchangeable；把 checksum 过了 / checksum / 防盘或网把数据弄坏 写成已经不能伪造元数据 interchangeable / 已经 metadata-unforgeable interchangeable；把证明绿了 / 捆绑的默克尔绿了 / 早发现失败核对绿了 写成已经代替最后那次 Info interchangeable / 已经 replaces-final-info interchangeable，或已经和 332 snapshotverify bundled / snapshotverify-sold-as-early interchangeable / 753 snapshotverify-notuniqueapphash interchangeable。

## 为什么错

官方把增量验了 chunk 单句、already unique-apphash、already metadata-unforgeable、already replaces-final-info 写成三件独立的实现事。把它们卖成 already unique-apphash interchangeable / already metadata-unforgeable interchangeable / already replaces-final-info interchangeable，会把 not already unique-apphash、not already metadata-unforgeable、not already replaces-final-info 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看增量验了 chunk 不是已经是唯一可信的 AppHash not already unique-apphash / not already metadata-unforgeable / not already replaces-final-info 正式三事（332 余量），必须分开 not already unique-apphash、not already metadata-unforgeable、not already replaces-final-info 三件事，不要和 332 / 33 / 38 / 752 / 754 糊成一句。

## 和相邻反模式

- [snapshotverify-sold-as-early](snapshotverify-sold-as-early.md) 是 Snapshot Verification bundled 全段，不是本页唯一可信 AppHash item 2 单句边界。
- [snapshotverify-notduringrestore-sold-as-bundled](snapshotverify-notduringrestore-sold-as-bundled.md) 是装完又对上 item 1，不是本页装回当中增量验边界。
- [snapshot-sold-as-identical](snapshot-sold-as-identical.md) 是快照身份边界，不是本页唯一可信锚边界。
