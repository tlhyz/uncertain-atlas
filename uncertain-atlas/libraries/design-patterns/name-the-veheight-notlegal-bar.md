# 模式：把 h < H 带了扩展不是已经合法 not already legal / not already enabled / not already abci20 正式三事（330 余量）说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) List of Parameters / Application configuration required to switch to ABCI 2.0。  
**例**：[h < H 带了扩展 not already legal ≠ bundled（330）](../../tracks/implementation/worked-example-veheight-notlegal-vs-bundled.md)。

## 三个名字

1. **h < H 带了扩展 不是 already legal：** 看见 h < H 带了扩展 / 启用前带了扩展 / 带扩展的预提交，不是已经合法 interchangeable / 已经合法交差 interchangeable，不是 330 veheight bundled interchangeable / 33 four gates interchangeable / veheight-sold-as-prepared interchangeable。

2. **字段在 不是 already enabled：** 看见已经启用 / 字段在 / H 之后不能关，不是已经启用交差 interchangeable / 已经启用交差 interchangeable，不是 58 enable-height interchangeable / 330 veheight item 1 interchangeable。

3. **切到 ABCI 2.0 不是 already abci20：** 看见切到 ABCI 2.0 / 已经是 ABCI 2.0 / 切换完成，不是已经切到 ABCI 2.0 interchangeable / 已经切换交差 interchangeable，不是 346 abci20-upgrade interchangeable / 330 veheight item 2 interchangeable。

官方把 h < H 带了扩展单句、already legal、already enabled、already abci20 写成三个名字。把它们叫成一个「看见 h < H 带了扩展就已经合法 interchangeable / 就已经启用 interchangeable / 就已经切到 ABCI 2.0 interchangeable」，会把 not already legal、not already enabled、not already abci20 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 h < H 带了扩展不是已经合法 not already legal / not already enabled / not already abci20 正式三事（330 余量），先数清问的是 h < H 带了扩展 是不是 already legal / 330 / veheight-sold-as-prepared，是不是字段在 是不是 already enabled，还是切到 ABCI 2.0 是不是 already abci20，再决定要不要同一次发布。330 veheight vs prepare bundled unbundling 在本页 item 3 完成。
