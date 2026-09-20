# 例：看见「像用了中间缓冲」不是已经必须真分配一块缓冲不是已经必须真分配一块缓冲；看见as-if-buffer is not already real allocation不是已经是拒绝服务面；看见「像用了中间缓冲」不是已经必须真分配一块缓冲不是已经是不变量 208

**层次**：实现 / 规范对象。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：Ethereum [EIP-5656](https://eips.ethereum.org/EIPS/eip-5656)（Final, Core, MCOPY instruction）。  
**对应课文**：[L5.1](../../courses/level-05-ethereum/L05-M01-evm-and-gas.md)。  
**不要写进**：`index/03` 共识行、M5.4、L5.4。本页是「EIP-5656 as-if-buffer not already real-alloc / not already DoS / not already 208 正式三事（216 余量）/ not 1411 mcpy-notbuf interchangeable / not 216 mcopy-vs-identity bundled interchangeable」，不是 mcopy vs identity bundled（216），也不是已经 数前导零（208），也不是已经 initcode 超界（176）。不要另写 怎样造真缓冲、怎样打重叠拷、怎样改 CALL 效果。

## 官方三件事

1. **看见「像用了中间缓冲」不是已经必须真分配一块缓冲 / 看见「像用了中间缓冲」不是已经必须真分配一块缓冲 这份对象 is not already 已经必须真分配一块缓冲 interchangeable，也不是已经 mcopy vs identity bundled（216） interchangeable / 1411 mcpy-notbuf interchangeable / 1410 mcpy-notid interchangeable，也不是已经 EIP-5656 as-if-buffer not already real-alloc / not already DoS / not already 208 正式三事 bundled（216 item 2 余量） interchangeable / 216 mcpy item 2 interchangeable。**  
   官方把「像用了中间缓冲」不是已经必须真分配一块缓冲和已经必须真分配一块缓冲写成两件。看见「像用了中间缓冲」不是已经必须真分配一块缓冲，不是已经必须真分配一块缓冲。

2. **看见as-if-buffer is not already real allocation / 看见「像用了中间缓冲」不是已经必须真分配一块缓冲 / 这份对象 is not already 已经是拒绝服务面 interchangeable，也不是已经 mcopy vs identity bundled（216） interchangeable / 1411 mcpy-notbuf interchangeable / 1412 mcpy-notcd interchangeable，也不是已经 数前导零 interchangeable / 208 数前导零 interchangeable。**  
   官方把as-if-buffer is not already real allocation和已经是拒绝服务面写成两件。看见as-if-buffer is not already real allocation，不是已经是拒绝服务面。

3. **看见「像用了中间缓冲」不是已经必须真分配一块缓冲 / 看见as-if-buffer is not already real allocation / 这份对象 is not already 已经是不变量 208 interchangeable，也不是已经 mcopy vs identity bundled（216） interchangeable / 1411 mcpy-notbuf interchangeable / 1410 mcpy-notid interchangeable，也不是已经 initcode 超界 interchangeable / 176 initcode 超界 interchangeable。**  
   官方把「像用了中间缓冲」不是已经必须真分配一块缓冲和已经是不变量 208写成两件。看见「像用了中间缓冲」不是已经必须真分配一块缓冲，不是已经是不变量 208。

栈怎么写、分隔符、例串是规范里的取值，本页不抄。不要另写 怎样造真缓冲、怎样打重叠拷、怎样改 CALL 效果。

## 官方为什么这样拆

- **「像用了中间缓冲」不是已经必须真分配一块缓冲 interchangeable：官方写那是重叠语义，实现不要真分配。**
- **看见真缓冲不是已经是拒绝服务面已经发生。**
- **看见本页不是已经是不变量 208。**

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 已经必须真分配一块缓冲 | 不是已经必须真分配一块缓冲 | 不是已经数前导零（208） |
| 已经是拒绝服务面 | 不是已经是拒绝服务面 | 不是已经initcode 超界（176） |
| 已经是不变量 208 | 不是已经是不变量 208 | 不是已经1410 mcpy-notid |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 EIP-5656 as-if-buffer not already real-alloc / not already DoS / not already 208 正式三事（216 余量），必须分开是不是已经必须真分配一块缓冲、是不是已经是拒绝服务面、是不是已经是不变量 208。可以跳过「看见 5656 就已经是身份预编译」。不要另写 怎样造真缓冲、怎样打重叠拷、怎样改 CALL 效果。216 MCOPY vs identity bundled unbundling 在本页 item 2 续；续 [`worked-example-mcpy-notcd-vs-bundled.md`](worked-example-mcpy-notcd-vs-bundled.md)（不变量 1412 item 3）。

## 本页不抄

- 操作码号、气价、百分比、块号区间、测试向量、规范提交哈希。
- 怎样造真缓冲、怎样打重叠拷、怎样改 CALL 效果。
