# 例：看见assumevalid不是已经弱主观检查点不是已经是弱主观；看见assumevalid is not already a weak-subjectivity checkpoint不是已经是不变量 24；看见assumevalid不是已经弱主观检查点不是已经是不变量 23

**层次**：实现 / 规范对象。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：Bitcoin Core [assumevalid](https://bitcoincore.org/en/2017/03/08/release-0.14.0/)（0.14.0 skip ancestor scripts without forcing the chain）。  
**对应课文**：[L3.5](../../courses/level-03-bitcoin/L03-M05-full-node-and-spv.md)。  
**不要写进**：`index/03` 共识行、M3.5、L3.5。本页是「assumevalid assumevalid not already weak-subjectivity / not already 24 / not already 23 正式三事（25 余量）/ not 1520 asv-notws interchangeable / not 25 assumevalid bundled interchangeable」，不是 assumevalid bundled（25），也不是已经 检查点须在信任期（24），也不是已经 KZG≠DAS（23）。不要另写 怎样设一个无效历史里的哈希、怎样在背景验完前当已从创世验证。

## 官方三件事

1. **看见assumevalid不是已经弱主观检查点 / 看见assumevalid不是已经弱主观检查点 这份对象 is not already 已经是弱主观 interchangeable，也不是已经 assumevalid bundled（25） interchangeable / 1520 asv-notws interchangeable / 1518 asv-notchk interchangeable，也不是已经 assumevalid assumevalid not already weak-subjectivity / not already 24 / not already 23 正式三事 bundled（25 item 3 余量） interchangeable / 25 asv item 3 interchangeable。**  
   官方把assumevalid不是已经弱主观检查点和已经是弱主观写成两件。看见assumevalid不是已经弱主观检查点，不是已经是弱主观。

2. **看见assumevalid is not already a weak-subjectivity checkpoint / 看见assumevalid不是已经弱主观检查点 / 这份对象 is not already 已经是不变量 24 interchangeable，也不是已经 assumevalid bundled（25） interchangeable / 1520 asv-notws interchangeable / 1519 asv-notutxo interchangeable，也不是已经 检查点须在信任期 interchangeable / 24 检查点须在信任期 interchangeable。**  
   官方把assumevalid is not already a weak-subjectivity checkpoint和已经是不变量 24写成两件。看见assumevalid is not already a weak-subjectivity checkpoint，不是已经是不变量 24。

3. **看见assumevalid不是已经弱主观检查点 / 看见assumevalid is not already a weak-subjectivity checkpoint / 这份对象 is not already 已经是不变量 23 interchangeable，也不是已经 assumevalid bundled（25） interchangeable / 1520 asv-notws interchangeable / 1518 asv-notchk interchangeable，也不是已经 KZG≠DAS interchangeable / 23 KZG≠DAS interchangeable。**  
   官方把assumevalid不是已经弱主观检查点和已经是不变量 23写成两件。看见assumevalid不是已经弱主观检查点，不是已经是不变量 23。

栈怎么写、分隔符、例串是规范里的取值，本页不抄。不要另写 怎样设一个无效历史里的哈希、怎样在背景验完前当已从创世验证。

## 官方为什么这样拆

- **assumevalid不是已经弱主观检查点 interchangeable：官方写这是实现开关，不是 PoS 信任期。**
- **看见本页不是已经是不变量 24。**
- **看见本页不是已经是不变量 23。**

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 已经是弱主观 | 不是已经是弱主观 | 不是已经检查点须在信任期（24） |
| 已经是不变量 24 | 不是已经是不变量 24 | 不是已经KZG≠DAS（23） |
| 已经是不变量 23 | 不是已经是不变量 23 | 不是已经1518 asv-notchk |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 assumevalid assumevalid not already weak-subjectivity / not already 24 / not already 23 正式三事（25 余量），必须分开是不是已经是弱主观、是不是已经是不变量 24、是不是已经是不变量 23。可以跳过「看见同步快就已经从创世验了脚本」。不要另写 怎样设一个无效历史里的哈希、怎样在背景验完前当已从创世验证。25 assumevalid vs checkpoint bundled unbundling 在本页 item 3 完成；本页收束本批。下一份仍捆着的官方对象：policy-vs-consensus。

## 本页不抄

- IBD小时数、电费、某次发行的默认哈希、未在官方说明出现的两周埋葬。
- 怎样设一个无效历史里的哈希、怎样在背景验完前当已从创世验证。
