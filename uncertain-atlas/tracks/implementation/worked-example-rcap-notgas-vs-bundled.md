# 例：看见RLP编码硬帽不是已经改了气限不是已经改了气限；看见RLP encoding cap is not already a gas limit change不是已经是不变量 197；看见RLP编码硬帽不是已经改了气限不是已经 202 bundled

**层次**：实现 / 规范对象。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：Ethereum [EIP-7934](https://eips.ethereum.org/EIPS/eip-7934)（RLP Execution Block Size Limit）。  
**对应课文**：[L5.1](../../courses/level-05-ethereum/L05-M01-evm-and-gas.md)。  
**不要写进**：`index/03` 共识行、M5.4、L5.4。本页是「EIP-7934 rlp-cap not already gas-limit / not already 197 / not already 202-bundled 正式三事（202 余量）/ not 1464 rcap-notgas interchangeable / not 202 rlp-cap-vs-gas bundled interchangeable」，不是 rlp cap vs gas bundled（202），也不是已经 calldata地板≠执行气（197），也不是已经 单笔气帽≠已改块气（203）。不要另写 怎样刚好塞进帽下。

## 官方三件事

1. **看见RLP编码硬帽不是已经改了气限 / 看见RLP编码硬帽不是已经改了气限 这份对象 is not already 已经改了气限 interchangeable，也不是已经 rlp cap vs gas bundled（202） interchangeable / 1464 rcap-notgas interchangeable / 1465 rcap-notprop interchangeable，也不是已经 EIP-7934 rlp-cap not already gas-limit / not already 197 / not already 202-bundled 正式三事 bundled（202 item 1 余量） interchangeable / 202 rcap item 1 interchangeable。**  
   官方把RLP编码硬帽不是已经改了气限和已经改了气限写成两件。看见RLP编码硬帽不是已经改了气限，不是已经改了气限。

2. **看见RLP encoding cap is not already a gas limit change / 看见RLP编码硬帽不是已经改了气限 / 这份对象 is not already 已经是不变量 197 interchangeable，也不是已经 rlp cap vs gas bundled（202） interchangeable / 1464 rcap-notgas interchangeable / 1466 rcap-notone interchangeable，也不是已经 calldata地板≠执行气 interchangeable / 197 calldata地板≠执行气 interchangeable。**  
   官方把RLP encoding cap is not already a gas limit change和已经是不变量 197写成两件。看见RLP encoding cap is not already a gas limit change，不是已经是不变量 197。

3. **看见RLP编码硬帽不是已经改了气限 / 看见RLP encoding cap is not already a gas limit change / 这份对象 is not already 已经 202 bundled interchangeable，也不是已经 rlp cap vs gas bundled（202） interchangeable / 1464 rcap-notgas interchangeable / 1465 rcap-notprop interchangeable，也不是已经 单笔气帽≠已改块气 interchangeable / 203 单笔气帽≠已改块气 interchangeable。**  
   官方把RLP编码硬帽不是已经改了气限和已经 202 bundled写成两件。看见RLP编码硬帽不是已经改了气限，不是已经 202 bundled。

栈怎么写、分隔符、例串是规范里的取值，本页不抄。不要另写 怎样刚好塞进帽下。

## 官方为什么这样拆

- **RLP编码硬帽不是已经改了气限 interchangeable：官方写这道帽独立于气相关的尺子，量的是编码字节。**
- **看见本页不是已经是不变量 197。**
- **看见读数旋钮不是已经 202 bundled。**

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 已经改了气限 | 不是已经改了气限 | 不是已经calldata地板≠执行气（197） |
| 已经是不变量 197 | 不是已经是不变量 197 | 不是已经单笔气帽≠已改块气（203） |
| 已经 202 bundled | 不是已经 202 bundled | 不是已经1465 rcap-notprop |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 EIP-7934 rlp-cap not already gas-limit / not already 197 / not already 202-bundled 正式三事（202 余量），必须分开是不是已经改了气限、是不是已经是不变量 197、是不是已经 202 bundled。可以跳过「看见 7934 就已经改了气」。不要另写 怎样刚好塞进帽下。202 rlp-cap vs gas bundled unbundling 在本页 item 1 启动；续 [`worked-example-rcap-notprop-vs-bundled.md`](worked-example-rcap-notprop-vs-bundled.md)（不变量 1465 item 2）。

## 本页不抄

- 编码上限字节、信标边字节、十进制字面量。
- 怎样刚好塞进帽下。
