# 模式：把 H+1 带了扩展不是已经是本高度刚签的 not already this-height-signed / not already local-e / not already same-h-e 正式三事（330 余量）说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[Requirements for the Application](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_app_requirements.md) List of Parameters / Application configuration required to switch to ABCI 2.0。  
**例**：[H+1 带了扩展 not already this-height-signed ≠ bundled（330）](../../tracks/implementation/worked-example-veheight-notthissigned-vs-bundled.md)。

## 三个名字

1. **H+1 带了扩展 不是 already this-height-signed：** 看见 H+1 带了扩展 / H+1 的 Prepare 带了 / 到了 H+1，不是已经是本高度刚签的 interchangeable / 已经本高刚签交差 interchangeable，不是 330 veheight bundled interchangeable / 33 four gates interchangeable / veheight-sold-as-prepared interchangeable。

2. **本高度刚签的那份 不是 already local-e：** 看见本高度刚签的那份 / 刚签的扩展 / 本高 e，不是已经是本高 e interchangeable / 已经本高 e 交差 interchangeable，不是 34 vote-extension interchangeable / 330 veheight item 1 interchangeable。

3. **Prepare 列表里有扩展 不是 already same-h-e：** 看见 Prepare 列表里有扩展 / 这一高的 e / 同高 e，不是已经是这一高的 e interchangeable / 已经同高 e 交差 interchangeable，不是 35 validator-set interchangeable / 330 veheight item 3 interchangeable。

官方把 H+1 带了扩展单句、already this-height-signed、already local-e、already same-h-e 写成三个名字。把它们叫成一个「看见 H+1 带了扩展就已经是本高度刚签 interchangeable / 就已经是本高 e interchangeable / 就已经是同高 e interchangeable」，会把 not already this-height-signed、not already local-e、not already same-h-e 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 H+1 带了扩展不是已经是本高度刚签的 not already this-height-signed / not already local-e / not already same-h-e 正式三事（330 余量），先数清问的是 H+1 带了扩展 是不是 already this-height-signed / 330 / veheight-sold-as-prepared，是不是本高度刚签的那份 是不是 already local-e，还是 Prepare 列表里有扩展 是不是 already same-h-e，再决定要不要同一次发布。330 veheight vs prepare bundled unbundling 在本页 item 2 续。
