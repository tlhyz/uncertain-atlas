# 例：看见单笔气帽不是已经改了块气限不是已经改了块气限；看见tx gas cap is not already the block gas limit不是已经是不变量 202；看见单笔气帽不是已经改了块气限不是已经 203 bundled

**层次**：实现 / 规范对象。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：Ethereum [EIP-7825](https://eips.ethereum.org/EIPS/eip-7825)（Transaction Gas Limit Cap）。  
**对应课文**：[L5.1](../../courses/level-05-ethereum/L05-M01-evm-and-gas.md)。  
**不要写进**：`index/03` 共识行、M5.4、L5.4。本页是「EIP-7825 tx-gas-cap not already block-gas / not already 202 / not already 203-bundled 正式三事（203 余量）/ not 1461 txcap-notblk interchangeable / not 203 tx-gas-cap-vs-block bundled interchangeable」，不是 tx gas cap vs block bundled（203），也不是已经 RLP编码硬帽≠已改气限（202），也不是已经 客户端默认≠协议帽（211）。不要另写 怎样把一笔拆到帽下。

## 官方三件事

1. **看见单笔气帽不是已经改了块气限 / 看见单笔气帽不是已经改了块气限 这份对象 is not already 已经改了块气限 interchangeable，也不是已经 tx gas cap vs block bundled（203） interchangeable / 1461 txcap-notblk interchangeable / 1462 txcap-notpool interchangeable，也不是已经 EIP-7825 tx-gas-cap not already block-gas / not already 202 / not already 203-bundled 正式三事 bundled（203 item 1 余量） interchangeable / 203 txcap item 1 interchangeable。**  
   官方把单笔气帽不是已经改了块气限和已经改了块气限写成两件。看见单笔气帽不是已经改了块气限，不是已经改了块气限。

2. **看见tx gas cap is not already the block gas limit / 看见单笔气帽不是已经改了块气限 / 这份对象 is not already 已经是不变量 202 interchangeable，也不是已经 tx gas cap vs block bundled（203） interchangeable / 1461 txcap-notblk interchangeable / 1463 txcap-notpol interchangeable，也不是已经 RLP编码硬帽≠已改气限 interchangeable / 202 RLP编码硬帽≠已改气限 interchangeable。**  
   官方把tx gas cap is not already the block gas limit和已经是不变量 202写成两件。看见tx gas cap is not already the block gas limit，不是已经是不变量 202。

3. **看见单笔气帽不是已经改了块气限 / 看见tx gas cap is not already the block gas limit / 这份对象 is not already 已经 203 bundled interchangeable，也不是已经 tx gas cap vs block bundled（203） interchangeable / 1461 txcap-notblk interchangeable / 1462 txcap-notpool interchangeable，也不是已经 客户端默认≠协议帽 interchangeable / 211 客户端默认≠协议帽 interchangeable。**  
   官方把单笔气帽不是已经改了块气限和已经 203 bundled写成两件。看见单笔气帽不是已经改了块气限，不是已经 203 bundled。

栈怎么写、分隔符、例串是规范里的取值，本页不抄。不要另写 怎样把一笔拆到帽下。

## 官方为什么这样拆

- **单笔气帽不是已经改了块气限 interchangeable：官方写这道帽不论出块者把块气限设成多少都适用，独立于块气限。**
- **看见本页不是已经是不变量 202。**
- **看见读数旋钮不是已经 203 bundled。**

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 已经改了块气限 | 不是已经改了块气限 | 不是已经RLP编码硬帽≠已改气限（202） |
| 已经是不变量 202 | 不是已经是不变量 202 | 不是已经客户端默认≠协议帽（211） |
| 已经 203 bundled | 不是已经 203 bundled | 不是已经1462 txcap-notpool |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 EIP-7825 tx-gas-cap not already block-gas / not already 202 / not already 203-bundled 正式三事（203 余量），必须分开是不是已经改了块气限、是不是已经是不变量 202、是不是已经 203 bundled。可以跳过「看见 7825 就已经改了块气」。不要另写 怎样把一笔拆到帽下。203 tx-gas-cap vs block bundled unbundling 在本页 item 1 启动；续 [`worked-example-txcap-notpool-vs-bundled.md`](worked-example-txcap-notpool-vs-bundled.md)（不变量 1462 item 2）。

## 本页不抄

- 单笔气帽取值、二次幂字面量、典型块气区间。
- 怎样把一笔拆到帽下。
