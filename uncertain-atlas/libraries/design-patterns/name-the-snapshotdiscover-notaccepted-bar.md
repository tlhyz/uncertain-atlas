# 模式：把挑了最高不是已经收下 not already accepted / not already restored / not already app-format 正式三事（322 余量）说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) Snapshot Discovery。  
**例**：[挑了 not already accepted ≠ bundled（322）](../../tracks/implementation/worked-example-snapshotdiscover-notaccepted-vs-bundled.md)。

## 三个名字

1. **挑了 不是 already accepted：** 看见挑了最高 / 挑一份最合适的，不是已经收下 interchangeable / 已经是应用收下的那份 interchangeable，不是 322 snapshotdiscover bundled interchangeable / 33 four gates interchangeable / snapshotdiscover-sold-as-listed interchangeable。

2. **最高 不是 already restored：** 看见按高度排了 / 挑了最高那份，不是已经装完 interchangeable / 已经装回交差 interchangeable，不是 321 snapshotrestore interchangeable / 719 snapshotrestore-notrestored interchangeable。

3. **排过了 不是 already app-format：** 看见按高度、格式、邻居数排了 / 按格式排了，不是已经是应用要的格式 interchangeable / 已经格式交差 interchangeable，不是 322 snapshotdiscover item 3 interchangeable / 724 snapshotdiscover-notstop interchangeable。

官方把挑了单句、already accepted、already restored、already app-format 写成三个名字。把它们叫成一个「看见挑了最高就已经收下 interchangeable / 就已经装完 interchangeable / 就已经是应用要的格式 interchangeable」，会把 not already accepted、not already restored、not already app-format 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看挑了最高不是已经收下 not already accepted / not already restored / not already app-format 正式三事（322 余量），先数清问的是挑了 是不是 already accepted / 322 / snapshotdiscover-sold-as-listed，是不是最高 是不是 already restored，还是排过了 是不是 already app-format，再决定要不要同一次发布。322 snapshotdiscover vs offer bundled unbundling 在本页 item 2 续。
