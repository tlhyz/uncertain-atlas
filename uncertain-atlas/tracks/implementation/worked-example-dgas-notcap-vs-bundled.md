# 例：看见客户端默认气限不是已经是协议帽不是已经是协议帽；看见client default gas is not already a protocol cap不是已经是不变量 203；看见客户端默认气限不是已经是协议帽不是已经 211 bundled

**层次**：实现 / 规范对象。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：Ethereum [EIP-7935](https://eips.ethereum.org/EIPS/eip-7935)（Informational, Set default gas limit to 60M）。  
**对应课文**：[L5.1](../../courses/level-05-ethereum/L05-M01-evm-and-gas.md)。  
**不要写进**：`index/03` 共识行、M5.4、L5.4。本页是「EIP-7935 default-gas not already protocol-cap / not already 203 / not already 211-bundled 正式三事（211 余量）/ not 1458 dgas-notcap interchangeable / not 211 default-gas-vs-cap bundled interchangeable」，不是 default gas vs cap bundled（211），也不是已经 单笔气帽≠已改块气（203），也不是已经 RLP编码硬帽≠已改气限（202）。不要另写 怎样抬气限、怎样灌满块。

## 官方三件事

1. **看见客户端默认气限不是已经是协议帽 / 看见客户端默认气限不是已经是协议帽 这份对象 is not already 已经是协议帽 interchangeable，也不是已经 default gas vs cap bundled（211） interchangeable / 1458 dgas-notcap interchangeable / 1459 dgas-notcons interchangeable，也不是已经 EIP-7935 default-gas not already protocol-cap / not already 203 / not already 211-bundled 正式三事 bundled（211 item 1 余量） interchangeable / 211 dgas item 1 interchangeable。**  
   官方把客户端默认气限不是已经是协议帽和已经是协议帽写成两件。看见客户端默认气限不是已经是协议帽，不是已经是协议帽。

2. **看见client default gas is not already a protocol cap / 看见客户端默认气限不是已经是协议帽 / 这份对象 is not already 已经是不变量 203 interchangeable，也不是已经 default gas vs cap bundled（211） interchangeable / 1458 dgas-notcap interchangeable / 1460 dgas-nottx interchangeable，也不是已经 单笔气帽≠已改块气 interchangeable / 203 单笔气帽≠已改块气 interchangeable。**  
   官方把client default gas is not already a protocol cap和已经是不变量 203写成两件。看见client default gas is not already a protocol cap，不是已经是不变量 203。

3. **看见客户端默认气限不是已经是协议帽 / 看见client default gas is not already a protocol cap / 这份对象 is not already 已经 211 bundled interchangeable，也不是已经 default gas vs cap bundled（211） interchangeable / 1458 dgas-notcap interchangeable / 1459 dgas-notcons interchangeable，也不是已经 RLP编码硬帽≠已改气限 interchangeable / 202 RLP编码硬帽≠已改气限 interchangeable。**  
   官方把客户端默认气限不是已经是协议帽和已经 211 bundled写成两件。看见客户端默认气限不是已经是协议帽，不是已经 211 bundled。

栈怎么写、分隔符、例串是规范里的取值，本页不抄。不要另写 怎样抬气限、怎样灌满块。

## 官方为什么这样拆

- **客户端默认气限不是已经是协议帽 interchangeable：官方写本页是 Informational，改的是默认配置，不是协议写死的块气帽。**
- **看见本页不是已经是不变量 203。**
- **看见读数旋钮不是已经 211 bundled。**

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 已经是协议帽 | 不是已经是协议帽 | 不是已经单笔气帽≠已改块气（203） |
| 已经是不变量 203 | 不是已经是不变量 203 | 不是已经RLP编码硬帽≠已改气限（202） |
| 已经 211 bundled | 不是已经 211 bundled | 不是已经1459 dgas-notcons |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 EIP-7935 default-gas not already protocol-cap / not already 203 / not already 211-bundled 正式三事（211 余量），必须分开是不是已经是协议帽、是不是已经是不变量 203、是不是已经 211 bundled。可以跳过「看见 7935 就已经改了块气」。不要另写 怎样抬气限、怎样灌满块。211 default-gas vs cap bundled unbundling 在本页 item 1 启动；续 [`worked-example-dgas-notcons-vs-bundled.md`](worked-example-dgas-notcons-vs-bundled.md)（不变量 1459 item 2）。

## 本页不抄

- 默认取值、当时主网取值、单笔建议帽、最坏体积、流言上限。
- 怎样抬气限、怎样灌满块。
