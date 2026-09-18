# 例：看见忽略 hello 版本不是已经在说新协议；看见能吞多余字段不是已经谈成新线协议；看见忽略 hello 版本不是新功能已经启用

**层次**：网络 / 规范对象。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：Bitcoin [EIP-8](https://eips.ethereum.org/EIPS/eip-8)（Final, Networking, Homestead 时期）。  
**对应课文**：[L9.1](../../courses/level-09-systems/L09-M01-p2p.md)。  
**不要写进**：`index/03` 共识行、M5.4、L5.1、L5.4。本页是「EIP-8 hello not already new-proto / not already negotiated / not already extra-enabled 正式三事（235 余量）/ not 1283 eip8-nothello interchangeable / not 235 eip8-vs-already-new bundled interchangeable」，不是 eip8 vs already new bundled（235），也不是已经 homestead-core（234），也不是已经 history-window（207）。不要另写 怎样同时认旧握手和新握手、怎样垫垃圾、怎样按头两个字节过滤连接。

## 官方三件事

1. **看见忽略 hello 版本 / 看见忽略 hello 版本 这份对象 is not already 已经在说新协议 interchangeable，也不是已经 eip8 vs already new bundled（235） interchangeable / 1283 eip8-nothello interchangeable / 1284 eip8-notdisc interchangeable，也不是已经 EIP-8 hello not already new-proto / not already negotiated / not already extra-enabled 正式三事 bundled（235 item 1 余量） interchangeable / 235 eip8 item 1 interchangeable。**  
   官方把忽略 hello 版本和已经在说新协议写成两件。看见忽略 hello 版本，不是已经在说新协议。

2. **看见能吞多余字段 / 看见忽略 hello 版本 / 这份对象 is not already 已经谈成新线协议 interchangeable，也不是已经 eip8 vs already new bundled（235） interchangeable / 1283 eip8-nothello interchangeable / 1285 eip8-nothand interchangeable，也不是已经 homestead-core interchangeable / 234 homestead-core interchangeable。**  
   官方把能吞多余字段和已经谈成新线协议写成两件。看见能吞多余字段，不是已经谈成新线协议。

3. **看见忽略 hello 版本 / 看见能吞多余字段 / 这份对象 is not already 新功能已经启用 interchangeable，也不是已经 eip8 vs already new bundled（235） interchangeable / 1283 eip8-nothello interchangeable / 1284 eip8-notdisc interchangeable，也不是已经 history-window interchangeable / 207 history-window interchangeable。**  
   官方把忽略 hello 版本和新功能已经启用写成两件。看见忽略 hello 版本，不是新功能已经启用。

栈怎么写、分隔符、例串是规范里的取值，本页不抄。不要另写 怎样同时认旧握手和新握手、怎样垫垃圾、怎样按头两个字节过滤连接。

## 官方为什么这样拆

- **忽略 hello 版本 不是已经在说新协议：官方写应忽略对方版本号并写自己支持的最高版本。**
- **能吞多余字段 不是已经谈成新线协议：官方写忽略 hello 列表末尾多出来的元素。**
- **没因版本断开 不是新功能已经启用：官方写旧客户端会盲目假定对端向后兼容。**

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 已经在说新协议 | 不是已经在说新协议 | 不是已经homestead-core（234） |
| 已经谈成新线协议 | 不是已经谈成新线协议 | 不是已经history-window（207） |
| 新功能已经启用 | 不是新功能已经启用 | 不是已经1284 eip8-notdisc |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 EIP-8 hello not already new-proto / not already negotiated / not already extra-enabled 正式三事（235 余量），必须分开是不是已经在说新协议、是不是已经谈成新线协议、是不是新功能已经启用。可以跳过「看见能吞多余字段就已经在说新协议」。不要另写 怎样同时认旧握手和新握手、怎样垫垃圾、怎样按头两个字节过滤连接。235 eip8 vs already new bundled unbundling 在本页 item 1 启动；续 [`worked-example-eip8-notdisc-vs-bundled.md`](worked-example-eip8-notdisc-vs-bundled.md)（不变量 1284 item 2）。

## 本页不抄

- hello / 发现 / 握手的测试向量、密钥、随机数、版本号取值、发现包最大长度、填充长度区间、旧包固定长度。
- 怎样同时认旧握手和新握手、怎样垫垃圾、怎样按头两个字节过滤连接。
