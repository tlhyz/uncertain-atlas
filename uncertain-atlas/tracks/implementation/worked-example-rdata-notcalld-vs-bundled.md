# 例：看见本页不是已经是 calldata不是已经是 calldata；看见this page is not already calldata不是已经用两次调用先问长度；看见本页不是已经是 calldata不是下一次类调用之后缓冲还在

**层次**：实现 / 规范对象。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：Ethereum [EIP-211](https://eips.ethereum.org/EIPS/eip-211)（Final, Core, RETURNDATASIZE / RETURNDATACOPY）。  
**对应课文**：[L5.1](../../courses/level-05-ethereum/L05-M01-evm-and-gas.md)。  
**不要写进**：`index/03` 共识行、M5.4、L5.4。本页是「EIP-211 this-page not already calldata / not already two-call-length / not already still-after-next 正式三事（232 余量）/ not 1387 rdata-notcalld interchangeable / not 232 returndata-vs-memory bundled interchangeable」，不是 returndata vs memory bundled（232），也不是已经 压零≠PUSH0（217），也不是已经 原生移位≠算术拼（231）。不要另写 怎样做通用转发合约、怎样在失败后再抽超长回滚数据、怎样把缓冲和内存叠成同一块后备。

## 官方三件事

1. **看见本页不是已经是 calldata / 看见本页不是已经是 calldata 这份对象 is not already 已经是 calldata interchangeable，也不是已经 returndata vs memory bundled（232） interchangeable / 1387 rdata-notcalld interchangeable / 1386 rdata-notmem interchangeable，也不是已经 EIP-211 this-page not already calldata / not already two-call-length / not already still-after-next 正式三事 bundled（232 item 2 余量） interchangeable / 232 rdata item 2 interchangeable。**  
   官方把本页不是已经是 calldata和已经是 calldata写成两件。看见本页不是已经是 calldata，不是已经是 calldata。

2. **看见this page is not already calldata / 看见本页不是已经是 calldata / 这份对象 is not already 已经用两次调用先问长度 interchangeable，也不是已经 returndata vs memory bundled（232） interchangeable / 1387 rdata-notcalld interchangeable / 1388 rdata-not140 interchangeable，也不是已经 压零≠PUSH0 interchangeable / 217 压零≠PUSH0 interchangeable。**  
   官方把this page is not already calldata和已经用两次调用先问长度写成两件。看见this page is not already calldata，不是已经用两次调用先问长度。

3. **看见本页不是已经是 calldata / 看见this page is not already calldata / 这份对象 is not already 下一次类调用之后缓冲还在 interchangeable，也不是已经 returndata vs memory bundled（232） interchangeable / 1387 rdata-notcalld interchangeable / 1386 rdata-notmem interchangeable，也不是已经 原生移位≠算术拼 interchangeable / 231 原生移位≠算术拼 interchangeable。**  
   官方把本页不是已经是 calldata和下一次类调用之后缓冲还在写成两件。看见本页不是已经是 calldata，不是下一次类调用之后缓冲还在。

栈怎么写、分隔符、例串是规范里的取值，本页不抄。不要另写 怎样做通用转发合约、怎样在失败后再抽超长回滚数据、怎样把缓冲和内存叠成同一块后备。

## 官方为什么这样拆

- **本页不是已经是 calldata interchangeable：官方写很像 calldata，不是已经是 calldata。**
- **看见能拆成两次调用不是已经是本页。**
- **看见缓冲不是下一次类调用之后还在。**

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 已经是 calldata | 不是已经是 calldata | 不是已经压零≠PUSH0（217） |
| 已经用两次调用先问长度 | 不是已经用两次调用先问长度 | 不是已经原生移位≠算术拼（231） |
| 下一次类调用之后缓冲还在 | 不是下一次类调用之后缓冲还在 | 不是已经1386 rdata-notmem |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 EIP-211 this-page not already calldata / not already two-call-length / not already still-after-next 正式三事（232 余量），必须分开是不是已经是 calldata、是不是已经用两次调用先问长度、是不是下一次类调用之后缓冲还在。可以跳过「看见返回数据缓冲就已经是内存」。不要另写 怎样做通用转发合约、怎样在失败后再抽超长回滚数据、怎样把缓冲和内存叠成同一块后备。232 returndata buffer vs memory bundled unbundling 在本页 item 2 续；续 [`worked-example-rdata-not140-vs-bundled.md`](worked-example-rdata-not140-vs-bundled.md)（不变量 1388 item 3）。

## 本页不抄

- 操作码号、气价公式、分叉块号。
- 怎样做通用转发合约、怎样在失败后再抽超长回滚数据、怎样把缓冲和内存叠成同一块后备。
