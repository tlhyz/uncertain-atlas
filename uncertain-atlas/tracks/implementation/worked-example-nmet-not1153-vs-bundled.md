# 例：看见净计量不是已经是瞬时存储不是已经是瞬时存储；看见net metering is not already transient storage不是已经是 1153；看见净计量不是已经是瞬时存储不是已经 225 bundled

**层次**：实现 / 规范对象。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：Ethereum [EIP-2200](https://eips.ethereum.org/EIPS/eip-2200)（Final, Core, Structured Definitions for Net Gas Metering）。  
**对应课文**：[L5.1](../../courses/level-05-ethereum/L05-M01-evm-and-gas.md)。  
**不要写进**：`index/03` 共识行、M5.4、L5.4。本页是「EIP-2200 net-meter not already transient / not already 1153 / not already 225-bundled 正式三事（225 余量）/ not 1419 nmet-not1153 interchangeable / not 225 net-meter-vs-transient bundled interchangeable」，不是 net meter vs transient bundled（225），也不是已经 瞬时存储≠账户持久存储（159），也不是已经 退款削减≠已没有退款（223）。不要另写 怎样在津贴帧里改槽、怎样做重入、怎样实现脏图。

## 官方三件事

1. **看见净计量不是已经是瞬时存储 / 看见净计量不是已经是瞬时存储 这份对象 is not already 已经是瞬时存储 interchangeable，也不是已经 net meter vs transient bundled（225） interchangeable / 1419 nmet-not1153 interchangeable / 1420 nmet-notcur interchangeable，也不是已经 EIP-2200 net-meter not already transient / not already 1153 / not already 225-bundled 正式三事 bundled（225 item 1 余量） interchangeable / 225 nmet item 1 interchangeable。**  
   官方把净计量不是已经是瞬时存储和已经是瞬时存储写成两件。看见净计量不是已经是瞬时存储，不是已经是瞬时存储。

2. **看见net metering is not already transient storage / 看见净计量不是已经是瞬时存储 / 这份对象 is not already 已经是 1153 interchangeable，也不是已经 net meter vs transient bundled（225） interchangeable / 1419 nmet-not1153 interchangeable / 1421 nmet-notstip interchangeable，也不是已经 瞬时存储≠账户持久存储 interchangeable / 159 瞬时存储≠账户持久存储 interchangeable。**  
   官方把net metering is not already transient storage和已经是 1153写成两件。看见net metering is not already transient storage，不是已经是 1153。

3. **看见净计量不是已经是瞬时存储 / 看见net metering is not already transient storage / 这份对象 is not already 已经 225 bundled interchangeable，也不是已经 net meter vs transient bundled（225） interchangeable / 1419 nmet-not1153 interchangeable / 1420 nmet-notcur interchangeable，也不是已经 退款削减≠已没有退款 interchangeable / 223 退款削减≠已没有退款 interchangeable。**  
   官方把净计量不是已经是瞬时存储和已经 225 bundled写成两件。看见净计量不是已经是瞬时存储，不是已经 225 bundled。

栈怎么写、分隔符、例串是规范里的取值，本页不抄。不要另写 怎样在津贴帧里改槽、怎样做重入、怎样实现脏图。

## 官方为什么这样拆

- **净计量不是已经是瞬时存储 interchangeable：官方写大体做到瞬时存储想做的事，但不另开一套。**
- **看见规范编号不是已经是 1153。**
- **看见读数旋钮不是已经 225 bundled。**

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 已经是瞬时存储 | 不是已经是瞬时存储 | 不是已经瞬时存储≠账户持久存储（159） |
| 已经是 1153 | 不是已经是 1153 | 不是已经退款削减≠已没有退款（223） |
| 已经 225 bundled | 不是已经 225 bundled | 不是已经1420 nmet-notcur |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 EIP-2200 net-meter not already transient / not already 1153 / not already 225-bundled 正式三事（225 余量），必须分开是不是已经是瞬时存储、是不是已经是 1153、是不是已经 225 bundled。可以跳过「看见 2200 就已经是 1153」。不要另写 怎样在津贴帧里改槽、怎样做重入、怎样实现脏图。225 net-meter vs transient bundled unbundling 在本页 item 1 启动；续 [`worked-example-nmet-notcur-vs-bundled.md`](worked-example-nmet-notcur-vs-bundled.md)（不变量 1420 item 2）。

## 本页不抄

- 气价名取值、津贴数字、测试向量。
- 怎样在津贴帧里改槽、怎样做重入、怎样实现脏图。
