# 例：看见绑到硬分叉发布不是已经改了共识不是已经改了共识；看见binding to a hardfork release is not already consensus-changed不是已经是不变量 202；看见绑到硬分叉发布不是已经改了共识不是已经是不变量 96

**层次**：实现 / 规范对象。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：Ethereum [EIP-7935](https://eips.ethereum.org/EIPS/eip-7935)（Informational, Set default gas limit to 60M）。  
**对应课文**：[L5.1](../../courses/level-05-ethereum/L05-M01-evm-and-gas.md)。  
**不要写进**：`index/03` 共识行、M5.4、L5.4。本页是「EIP-7935 hardfork-bind not already consensus-changed / not already 202 / not already 96 正式三事（211 余量）/ not 1459 dgas-notcons interchangeable / not 211 default-gas-vs-cap bundled interchangeable」，不是 default gas vs cap bundled（211），也不是已经 RLP编码硬帽≠已改气限（202），也不是已经 通道尺寸≠拼块已齐（96）。不要另写 怎样抬气限、怎样灌满块。

## 官方三件事

1. **看见绑到硬分叉发布不是已经改了共识 / 看见绑到硬分叉发布不是已经改了共识 这份对象 is not already 已经改了共识 interchangeable，也不是已经 default gas vs cap bundled（211） interchangeable / 1459 dgas-notcons interchangeable / 1458 dgas-notcap interchangeable，也不是已经 EIP-7935 hardfork-bind not already consensus-changed / not already 202 / not already 96 正式三事 bundled（211 item 2 余量） interchangeable / 211 dgas item 2 interchangeable。**  
   官方把绑到硬分叉发布不是已经改了共识和已经改了共识写成两件。看见绑到硬分叉发布不是已经改了共识，不是已经改了共识。

2. **看见binding to a hardfork release is not already consensus-changed / 看见绑到硬分叉发布不是已经改了共识 / 这份对象 is not already 已经是不变量 202 interchangeable，也不是已经 default gas vs cap bundled（211） interchangeable / 1459 dgas-notcons interchangeable / 1460 dgas-nottx interchangeable，也不是已经 RLP编码硬帽≠已改气限 interchangeable / 202 RLP编码硬帽≠已改气限 interchangeable。**  
   官方把binding to a hardfork release is not already consensus-changed和已经是不变量 202写成两件。看见binding to a hardfork release is not already consensus-changed，不是已经是不变量 202。

3. **看见绑到硬分叉发布不是已经改了共识 / 看见binding to a hardfork release is not already consensus-changed / 这份对象 is not already 已经是不变量 96 interchangeable，也不是已经 default gas vs cap bundled（211） interchangeable / 1459 dgas-notcons interchangeable / 1458 dgas-notcap interchangeable，也不是已经 通道尺寸≠拼块已齐 interchangeable / 96 通道尺寸≠拼块已齐 interchangeable。**  
   官方把绑到硬分叉发布不是已经改了共识和已经是不变量 96写成两件。看见绑到硬分叉发布不是已经改了共识，不是已经是不变量 96。

栈怎么写、分隔符、例串是规范里的取值，本页不抄。不要另写 怎样抬气限、怎样灌满块。

## 官方为什么这样拆

- **绑到硬分叉发布不是已经改了共识 interchangeable：官方写绑到发版日是为了把各家默认齐起来，不是共识已经改了。**
- **看见本页不是已经是不变量 202。**
- **看见本页不是已经是不变量 96。**

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 已经改了共识 | 不是已经改了共识 | 不是已经RLP编码硬帽≠已改气限（202） |
| 已经是不变量 202 | 不是已经是不变量 202 | 不是已经通道尺寸≠拼块已齐（96） |
| 已经是不变量 96 | 不是已经是不变量 96 | 不是已经1458 dgas-notcap |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 EIP-7935 hardfork-bind not already consensus-changed / not already 202 / not already 96 正式三事（211 余量），必须分开是不是已经改了共识、是不是已经是不变量 202、是不是已经是不变量 96。可以跳过「看见 7935 就已经改了块气」。不要另写 怎样抬气限、怎样灌满块。211 default-gas vs cap bundled unbundling 在本页 item 2 续；续 [`worked-example-dgas-nottx-vs-bundled.md`](worked-example-dgas-nottx-vs-bundled.md)（不变量 1460 item 3）。

## 本页不抄

- 默认取值、当时主网取值、单笔建议帽、最坏体积、流言上限。
- 怎样抬气限、怎样灌满块。
