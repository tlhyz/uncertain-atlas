# 模式：把 CheckTx Usage no other value to the response code not CheckTx Data used / not optional bundled / not validate-no-apply bundled 正式三事（489 余量）说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) CheckTx Usage。  
**例**：[no other value not CheckTx Data used ≠ bundled（489）](../../tracks/implementation/worked-example-chktxcodereject-notothervalue-vs-bundled.md)。

## 三个名字

1. **no other value 不是 CheckTx Data 已被引擎用了：** 看见 Methods Usage 引擎对回包码不再赋予别的含义，不是已经 Data 栏就被引擎读 interchangeable，不是 317 interchangeable / 688 chktxcodereject-notothervalue interchangeable。
2. **看见引擎不再赋予别的含义 不是 optional bundled：** 看见 response code，不是已经 Technically optional bundled interchangeable，不是 373 checktxopt interchangeable。
3. **看见 Usage 这句 不是 validate-no-apply bundled：** 看见 Code 语义，不是已经 486 bundled 第三件事 interchangeable，不是 682 chktxvalidate-notoptional interchangeable。

官方把 CheckTx Usage Code 语义、回包 Data、optional bundled、validate-no-apply bundled 写成三个名字。把它们叫成一个「看见引擎不再赋予别的含义就已经交差」，会把 not Data used、not optional bundled、not validate-no-apply bundled 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 CheckTx Usage no other value 正式三事（489 余量），先数清问的是 no other value 是不是 Data 已被引擎用了 / 317、是不是 optional bundled / 373、还是看见 Usage 是不是 validate-no-apply bundled / 486，再决定要不要同一次发布。489 chktxcodereject vs proposal bundled unbundling 在本页 item 3 完成。
