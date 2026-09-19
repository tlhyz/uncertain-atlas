# 例：看见入池拒掉不是已经验过块不是已经验过块；看见pool reject is not already block-verified不是已经是不变量 197；看见入池拒掉不是已经验过块不是已经是不变量 96

**层次**：实现 / 规范对象。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：Ethereum [EIP-7825](https://eips.ethereum.org/EIPS/eip-7825)（Transaction Gas Limit Cap）。  
**对应课文**：[L5.1](../../courses/level-05-ethereum/L05-M01-evm-and-gas.md)。  
**不要写进**：`index/03` 共识行、M5.4、L5.4。本页是「EIP-7825 pool-reject not already block-verified / not already 197 / not already 96 正式三事（203 余量）/ not 1462 txcap-notpool interchangeable / not 203 tx-gas-cap-vs-block bundled interchangeable」，不是 tx gas cap vs block bundled（203），也不是已经 calldata地板≠执行气（197），也不是已经 通道尺寸≠拼块已齐（96）。不要另写 怎样把一笔拆到帽下。

## 官方三件事

1. **看见入池拒掉不是已经验过块 / 看见入池拒掉不是已经验过块 这份对象 is not already 已经验过块 interchangeable，也不是已经 tx gas cap vs block bundled（203） interchangeable / 1462 txcap-notpool interchangeable / 1461 txcap-notblk interchangeable，也不是已经 EIP-7825 pool-reject not already block-verified / not already 197 / not already 96 正式三事 bundled（203 item 2 余量） interchangeable / 203 txcap item 2 interchangeable。**  
   官方把入池拒掉不是已经验过块和已经验过块写成两件。看见入池拒掉不是已经验过块，不是已经验过块。

2. **看见pool reject is not already block-verified / 看见入池拒掉不是已经验过块 / 这份对象 is not already 已经是不变量 197 interchangeable，也不是已经 tx gas cap vs block bundled（203） interchangeable / 1462 txcap-notpool interchangeable / 1463 txcap-notpol interchangeable，也不是已经 calldata地板≠执行气 interchangeable / 197 calldata地板≠执行气 interchangeable。**  
   官方把pool reject is not already block-verified和已经是不变量 197写成两件。看见pool reject is not already block-verified，不是已经是不变量 197。

3. **看见入池拒掉不是已经验过块 / 看见pool reject is not already block-verified / 这份对象 is not already 已经是不变量 96 interchangeable，也不是已经 tx gas cap vs block bundled（203） interchangeable / 1462 txcap-notpool interchangeable / 1461 txcap-notblk interchangeable，也不是已经 通道尺寸≠拼块已齐 interchangeable / 96 通道尺寸≠拼块已齐 interchangeable。**  
   官方把入池拒掉不是已经验过块和已经是不变量 96写成两件。看见入池拒掉不是已经验过块，不是已经是不变量 96。

栈怎么写、分隔符、例串是规范里的取值，本页不抄。不要另写 怎样把一笔拆到帽下。

## 官方为什么这样拆

- **入池拒掉不是已经验过块 interchangeable：官方写入池校验超帽不进池，不是块已经验过。**
- **看见本页不是已经是不变量 197。**
- **看见本页不是已经是不变量 96。**

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 已经验过块 | 不是已经验过块 | 不是已经calldata地板≠执行气（197） |
| 已经是不变量 197 | 不是已经是不变量 197 | 不是已经通道尺寸≠拼块已齐（96） |
| 已经是不变量 96 | 不是已经是不变量 96 | 不是已经1461 txcap-notblk |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 EIP-7825 pool-reject not already block-verified / not already 197 / not already 96 正式三事（203 余量），必须分开是不是已经验过块、是不是已经是不变量 197、是不是已经是不变量 96。可以跳过「看见 7825 就已经改了块气」。不要另写 怎样把一笔拆到帽下。203 tx-gas-cap vs block bundled unbundling 在本页 item 2 续；续 [`worked-example-txcap-notpol-vs-bundled.md`](worked-example-txcap-notpol-vs-bundled.md)（不变量 1463 item 3）。

## 本页不抄

- 单笔气帽取值、二次幂字面量、典型块气区间。
- 怎样把一笔拆到帽下。
