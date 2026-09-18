# 例：看见内存拷贝指令不是已经是身份预编译不是已经是身份预编译；看见MCOPY is not already identity precompile不是已经是 2929；看见内存拷贝指令不是已经是身份预编译不是已经 216 bundled

**层次**：实现 / 规范对象。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：Ethereum [EIP-5656](https://eips.ethereum.org/EIPS/eip-5656)（Final, Core, MCOPY instruction）。  
**对应课文**：[L5.1](../../courses/level-05-ethereum/L05-M01-evm-and-gas.md)。  
**不要写进**：`index/03` 共识行、M5.4、L5.4。本页是「EIP-5656 MCOPY not already identity-precompile / not already 2929 / not already 216-bundled 正式三事（216 余量）/ not 1410 mcpy-notid interchangeable / not 216 mcopy-vs-identity bundled interchangeable」，不是 mcopy vs identity bundled（216），也不是已经 本笔第一次碰≠已经热（169），也不是已经 数前导零≠已便宜 ZK（208）。不要另写 怎样造真缓冲、怎样打重叠拷、怎样改 CALL 效果。

## 官方三件事

1. **看见内存拷贝指令不是已经是身份预编译 / 看见内存拷贝指令不是已经是身份预编译 这份对象 is not already 已经是身份预编译 interchangeable，也不是已经 mcopy vs identity bundled（216） interchangeable / 1410 mcpy-notid interchangeable / 1411 mcpy-notbuf interchangeable，也不是已经 EIP-5656 MCOPY not already identity-precompile / not already 2929 / not already 216-bundled 正式三事 bundled（216 item 1 余量） interchangeable / 216 mcpy item 1 interchangeable。**  
   官方把内存拷贝指令不是已经是身份预编译和已经是身份预编译写成两件。看见内存拷贝指令不是已经是身份预编译，不是已经是身份预编译。

2. **看见MCOPY is not already identity precompile / 看见内存拷贝指令不是已经是身份预编译 / 这份对象 is not already 已经是 2929 interchangeable，也不是已经 mcopy vs identity bundled（216） interchangeable / 1410 mcpy-notid interchangeable / 1412 mcpy-notcd interchangeable，也不是已经 本笔第一次碰≠已经热 interchangeable / 169 本笔第一次碰≠已经热 interchangeable。**  
   官方把MCOPY is not already identity precompile和已经是 2929写成两件。看见MCOPY is not already identity precompile，不是已经是 2929。

3. **看见内存拷贝指令不是已经是身份预编译 / 看见MCOPY is not already identity precompile / 这份对象 is not already 已经 216 bundled interchangeable，也不是已经 mcopy vs identity bundled（216） interchangeable / 1410 mcpy-notid interchangeable / 1411 mcpy-notbuf interchangeable，也不是已经 数前导零≠已便宜 ZK interchangeable / 208 数前导零≠已便宜 ZK interchangeable。**  
   官方把内存拷贝指令不是已经是身份预编译和已经 216 bundled写成两件。看见内存拷贝指令不是已经是身份预编译，不是已经 216 bundled。

栈怎么写、分隔符、例串是规范里的取值，本页不抄。不要另写 怎样造真缓冲、怎样打重叠拷、怎样改 CALL 效果。

## 官方为什么这样拆

- **内存拷贝指令不是已经是身份预编译 interchangeable：官方把专用内存拷和靠 CALL 的身份预编译写成两件。**
- **看见 2929 让预编译稍便宜不是已经是 2929。**
- **看见读数旋钮不是已经 216 bundled。**

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 已经是身份预编译 | 不是已经是身份预编译 | 不是已经本笔第一次碰≠已经热（169） |
| 已经是 2929 | 不是已经是 2929 | 不是已经数前导零≠已便宜 ZK（208） |
| 已经 216 bundled | 不是已经 216 bundled | 不是已经1411 mcpy-notbuf |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 EIP-5656 MCOPY not already identity-precompile / not already 2929 / not already 216-bundled 正式三事（216 余量），必须分开是不是已经是身份预编译、是不是已经是 2929、是不是已经 216 bundled。可以跳过「看见 5656 就已经是身份预编译」。不要另写 怎样造真缓冲、怎样打重叠拷、怎样改 CALL 效果。216 MCOPY vs identity bundled unbundling 在本页 item 1 启动；续 [`worked-example-mcpy-notbuf-vs-bundled.md`](worked-example-mcpy-notbuf-vs-bundled.md)（不变量 1411 item 2）。

## 本页不抄

- 操作码号、气价、百分比、块号区间、测试向量、规范提交哈希。
- 怎样造真缓冲、怎样打重叠拷、怎样改 CALL 效果。
