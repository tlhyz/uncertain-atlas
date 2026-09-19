# 例：看见assumevalid不是已经assumeutxo不是已经是assumeutxo；看见assumevalid is not already assumeutxo不是已经是不变量 38；看见assumevalid不是已经assumeutxo不是已经是不变量 207

**层次**：实现 / 规范对象。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：Bitcoin Core [assumevalid](https://bitcoincore.org/en/2017/03/08/release-0.14.0/)（0.14.0 skip ancestor scripts without forcing the chain）。  
**对应课文**：[L3.5](../../courses/level-03-bitcoin/L03-M05-full-node-and-spv.md)。  
**不要写进**：`index/03` 共识行、M3.5、L3.5。本页是「assumevalid assumevalid not already assumeutxo / not already 38 / not already 207 正式三事（25 余量）/ not 1519 asv-notutxo interchangeable / not 25 assumevalid bundled interchangeable」，不是 assumevalid bundled（25），也不是已经 快照≠创世重放（38），也不是已经 对等窗≠已改共识（207）。不要另写 怎样设一个无效历史里的哈希、怎样在背景验完前当已从创世验证。

## 官方三件事

1. **看见assumevalid不是已经assumeutxo / 看见assumevalid不是已经assumeutxo 这份对象 is not already 已经是assumeutxo interchangeable，也不是已经 assumevalid bundled（25） interchangeable / 1519 asv-notutxo interchangeable / 1518 asv-notchk interchangeable，也不是已经 assumevalid assumevalid not already assumeutxo / not already 38 / not already 207 正式三事 bundled（25 item 2 余量） interchangeable / 25 asv item 2 interchangeable。**  
   官方把assumevalid不是已经assumeutxo和已经是assumeutxo写成两件。看见assumevalid不是已经assumeutxo，不是已经是assumeutxo。

2. **看见assumevalid is not already assumeutxo / 看见assumevalid不是已经assumeutxo / 这份对象 is not already 已经是不变量 38 interchangeable，也不是已经 assumevalid bundled（25） interchangeable / 1519 asv-notutxo interchangeable / 1520 asv-notws interchangeable，也不是已经 快照≠创世重放 interchangeable / 38 快照≠创世重放 interchangeable。**  
   官方把assumevalid is not already assumeutxo和已经是不变量 38写成两件。看见assumevalid is not already assumeutxo，不是已经是不变量 38。

3. **看见assumevalid不是已经assumeutxo / 看见assumevalid is not already assumeutxo / 这份对象 is not already 已经是不变量 207 interchangeable，也不是已经 assumevalid bundled（25） interchangeable / 1519 asv-notutxo interchangeable / 1518 asv-notchk interchangeable，也不是已经 对等窗≠已改共识 interchangeable / 207 对等窗≠已改共识 interchangeable。**  
   官方把assumevalid不是已经assumeutxo和已经是不变量 207写成两件。看见assumevalid不是已经assumeutxo，不是已经是不变量 207。

栈怎么写、分隔符、例串是规范里的取值，本页不抄。不要另写 怎样设一个无效历史里的哈希、怎样在背景验完前当已从创世验证。

## 官方为什么这样拆

- **assumevalid不是已经assumeutxo interchangeable：官方写本页跳祖先脚本，不是暂时跳 UTXO 重放。**
- **看见本页不是已经是不变量 38。**
- **看见本页不是已经是不变量 207。**

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 已经是assumeutxo | 不是已经是assumeutxo | 不是已经快照≠创世重放（38） |
| 已经是不变量 38 | 不是已经是不变量 38 | 不是已经对等窗≠已改共识（207） |
| 已经是不变量 207 | 不是已经是不变量 207 | 不是已经1518 asv-notchk |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 assumevalid assumevalid not already assumeutxo / not already 38 / not already 207 正式三事（25 余量），必须分开是不是已经是assumeutxo、是不是已经是不变量 38、是不是已经是不变量 207。可以跳过「看见同步快就已经从创世验了脚本」。不要另写 怎样设一个无效历史里的哈希、怎样在背景验完前当已从创世验证。25 assumevalid vs checkpoint bundled unbundling 在本页 item 2 续；续 [`worked-example-asv-notws-vs-bundled.md`](worked-example-asv-notws-vs-bundled.md)（不变量 1520 item 3）。

## 本页不抄

- IBD小时数、电费、某次发行的默认哈希、未在官方说明出现的两周埋葬。
- 怎样设一个无效历史里的哈希、怎样在背景验完前当已从创世验证。
