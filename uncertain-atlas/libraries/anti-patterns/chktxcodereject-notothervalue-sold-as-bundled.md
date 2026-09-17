# 反模式：把 CheckTx Usage no other value to the response code not CheckTx Data used / not optional bundled / not validate-no-apply bundled 正式三事（489 余量）说成已经 Data 被用 / 已经 optional bundled / 已经 validate-no-apply bundled

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[no other value not CheckTx Data used ≠ bundled（489）](../../tracks/implementation/worked-example-chktxcodereject-notothervalue-vs-bundled.md)。

## 卖法

把 attributes no other value to the response code / 引擎对回包码不再赋予别的含义 写成已经 CheckTx 回包 Data 就被引擎用了 interchangeable / 317 interchangeable；把看见引擎不再赋予别的含义写成已经 CheckTx 技术上可选 bundled interchangeable / 373 checktxopt interchangeable；把看见 Usage 这句写成已经 validate-no-apply bundled 第三件事 interchangeable / 486 chktxvalidate interchangeable / 682 chktxvalidate-notoptional interchangeable，或已经和 489 chktxcodereject-vs-proposal bundled / chktxcodereject-notothervalue-sold-as-bundled interchangeable / 688 chktxcodereject-notothervalue interchangeable。

## 为什么错

官方把 CheckTx Usage Code 语义、回包 Data、optional bundled、validate-no-apply bundled 写成三件独立的实现事。把它们卖成 Data used interchangeable / optional bundled interchangeable / validate-no-apply bundled interchangeable，会把 not Data used、not optional bundled、not validate-no-apply bundled 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 CheckTx Usage no other value 正式三事（489 余量），必须分开 not Data used、not optional bundled、not validate-no-apply bundled 三件事，不要和 489 / 317 / 373 / 486 / 686 / 687 糊成一句。

## 和相邻反模式

- [chktxcodereject-sold-as-proposal](chktxcodereject-sold-as-proposal.md) 是 CheckTx Usage Code≠0 rejected bundled（489），不是本页 item 3 单句边界。
- [chktxcodereject-notproposal-sold-as-bundled](chktxcodereject-notproposal-sold-as-bundled.md) 是 will not be in proposal 单句边界（687 item 2），不是本页 no other value 边界。
