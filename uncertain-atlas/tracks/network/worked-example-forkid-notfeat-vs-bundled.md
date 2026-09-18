# 例：看见有了分叉标识不是已经改了共识；看见只通告下一次不是三向分叉已经能分开；看见有了分叉标识不是未来分叉清单已经齐

**层次**：网络 / 规范对象。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：Ethereum [EIP-2124](https://eips.ethereum.org/EIPS/eip-2124)（Final, Networking）。  
**对应课文**：[L9.1](../../courses/level-09-systems/L09-M01-p2p.md)。  
**不要写进**：`index/03` 共识行、M5.4、L5.1、L5.4、05b。本页是「EIP-2124 id-scheme not already consensus / not already three-way / not already future-list 正式三事（239 余量）/ not 1288 forkid-notfeat interchangeable / not 239 forkid-vs-same-chain bundled interchangeable」，不是 forkid vs same chain bundled（239），也不是已经 eip8-compat（235），也不是已经 enr-newest（240）。不要另写 怎样伪造分叉标识、怎样假装同一条链、怎样在三向分叉里互踢。

## 官方三件事

1. **看见有了分叉标识 / 看见有了分叉标识 这份对象 is not already 已经改了共识 interchangeable，也不是已经 forkid vs same chain bundled（239） interchangeable / 1288 forkid-notfeat interchangeable / 1286 forkid-notsame interchangeable，也不是已经 EIP-2124 id-scheme not already consensus / not already three-way / not already future-list 正式三事 bundled（239 item 3 余量） interchangeable / 239 forkid item 3 interchangeable。**  
   官方把有了分叉标识和已经改了共识写成两件。看见有了分叉标识，不是已经改了共识。

2. **看见只通告下一次 / 看见有了分叉标识 / 这份对象 is not already 三向分叉已经能分开 interchangeable，也不是已经 forkid vs same chain bundled（239） interchangeable / 1288 forkid-notfeat interchangeable / 1287 forkid-notcompat interchangeable，也不是已经 eip8-compat interchangeable / 235 eip8-compat interchangeable。**  
   官方把只通告下一次和三向分叉已经能分开写成两件。看见只通告下一次，不是三向分叉已经能分开。

3. **看见有了分叉标识 / 看见只通告下一次 / 这份对象 is not already 未来分叉清单已经齐 interchangeable，也不是已经 forkid vs same chain bundled（239） interchangeable / 1288 forkid-notfeat interchangeable / 1286 forkid-notsame interchangeable，也不是已经 enr-newest interchangeable / 240 enr-newest interchangeable。**  
   官方把有了分叉标识和未来分叉清单已经齐写成两件。看见有了分叉标识，不是未来分叉清单已经齐。

栈怎么写、分隔符、例串是规范里的取值，本页不抄。不要另写 怎样伪造分叉标识、怎样假装同一条链、怎样在三向分叉里互踢。

## 官方为什么这样拆

- **有了分叉标识 不是已经改了共识：官方写本页不定义功能变化。**
- **有了分叉标识 不是三向分叉已经能分开：官方故意不处理同一高度三向分叉。**
- **只通告下一次 不是未来分叉清单已经齐：官方写未来还不确定，可能推迟。**

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 已经改了共识 | 不是已经改了共识 | 不是已经eip8-compat（235） |
| 三向分叉已经能分开 | 不是三向分叉已经能分开 | 不是已经enr-newest（240） |
| 未来分叉清单已经齐 | 不是未来分叉清单已经齐 | 不是已经1286 forkid-notsame |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 EIP-2124 id-scheme not already consensus / not already three-way / not already future-list 正式三事（239 余量），必须分开是不是已经改了共识、是不是三向分叉已经能分开、是不是未来分叉清单已经齐。可以跳过「看见分叉标识对上就已经同一条链」。不要另写 怎样伪造分叉标识、怎样假装同一条链、怎样在三向分叉里互踢。239 forkid vs same chain bundled unbundling 在本页 item 3 完成；本页收束本批。

## 本页不抄

- CRC 取值、分叉高度表、编码样例、测试头高度。
- 怎样伪造分叉标识、怎样假装同一条链、怎样在三向分叉里互踢。
