# 例：看见建议目标不是已经是协议帽；看见软限制不是官网吞吐已经是事实；看见建议目标不是已经改了共识帽

**层次**：实现 / 规范对象。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：Ethereum [EIP-150](https://eips.ethereum.org/EIPS/eip-150)（Final, Core；Tangerine Whistle）。  
**对应课文**：[L5.1](../../courses/level-05-ethereum/L05-M01-evm-and-gas.md)。  
**不要写进**：`index/03` 共识行、M5.4、L5.4。本页是「EIP-150 gaslimit not already protocol-cap / not already throughput / not already consensus-cap 正式三事（237 余量）/ not 1300 c63-notcap interchangeable / not 237 call-63rds-vs-oog bundled interchangeable」，不是 call 63rds vs oog bundled（237），也不是已经 default-gas（211），也不是已经 selfdestruct（160）。不要另写 怎样造读树垃圾交易，怎样按「剩下的再减一截」复刻旧合约，怎样打满一块。

## 官方三件事

1. **看见建议目标 / 看见建议目标 这份对象 is not already 已经是协议帽 interchangeable，也不是已经 call 63rds vs oog bundled（237） interchangeable / 1300 c63-notcap interchangeable / 1298 c63-notprice interchangeable，也不是已经 EIP-150 gaslimit not already protocol-cap / not already throughput / not already consensus-cap 正式三事 bundled（237 item 3 余量） interchangeable / 237 c63 item 3 interchangeable。**  
   官方把建议目标和已经是协议帽写成两件。看见建议目标，不是已经是协议帽。

2. **看见软限制 / 看见建议目标 / 这份对象 is not already 官网吞吐已经是事实 interchangeable，也不是已经 call 63rds vs oog bundled（237） interchangeable / 1300 c63-notcap interchangeable / 1299 c63-notoog interchangeable，也不是已经 default-gas interchangeable / 211 default-gas interchangeable。**  
   官方把软限制和官网吞吐已经是事实写成两件。看见软限制，不是官网吞吐已经是事实。

3. **看见建议目标 / 看见软限制 / 这份对象 is not already 已经改了共识帽 interchangeable，也不是已经 call 63rds vs oog bundled（237） interchangeable / 1300 c63-notcap interchangeable / 1298 c63-notprice interchangeable，也不是已经 selfdestruct interchangeable / 160 selfdestruct interchangeable。**  
   官方把建议目标和已经改了共识帽写成两件。看见建议目标，不是已经改了共识帽。

栈怎么写、分隔符、例串是规范里的取值，本页不抄。不要另写 怎样造读树垃圾交易，怎样按「剩下的再减一截」复刻旧合约，怎样打满一块。

## 官方为什么这样拆

- **建议目标 不是已经是协议帽：官方写抬高是建议，动机是保住吞吐。**
- **建议 不是官网吞吐已经是事实：官网吞吐不得当事实。**
- **建议 不是已经改了共识帽：看见建议，不是已经改了共识帽。**

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 已经是协议帽 | 不是已经是协议帽 | 不是已经default-gas（211） |
| 官网吞吐已经是事实 | 不是官网吞吐已经是事实 | 不是已经selfdestruct（160） |
| 已经改了共识帽 | 不是已经改了共识帽 | 不是已经1298 c63-notprice |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 EIP-150 gaslimit not already protocol-cap / not already throughput / not already consensus-cap 正式三事（237 余量），必须分开是不是已经是协议帽、是不是官网吞吐已经是事实、是不是已经改了共识帽。可以跳过「看见读树涨价就已经齐了」。不要另写 怎样造读树垃圾交易，怎样按「剩下的再减一截」复刻旧合约，怎样打满一块。237 call 63rds vs oog bundled unbundling 在本页 item 3 完成；本页收束本批。

## 本页不抄

- 分叉高度、操作码新旧气价、建议气限取值、读盘字节估计、软深度大约能到几层。
- 怎样造读树垃圾交易，怎样按「剩下的再减一截」复刻旧合约，怎样打满一块。
