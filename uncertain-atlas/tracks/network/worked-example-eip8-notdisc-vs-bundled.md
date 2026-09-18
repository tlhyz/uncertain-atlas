# 例：看见发现能吞多余字段不是发现已经升级；看见不认识的发现包类型被丢掉不是已经在说新协议；看见发现能吞多余字段不是已经升级发现

**层次**：网络 / 规范对象。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：Bitcoin [EIP-8](https://eips.ethereum.org/EIPS/eip-8)（Final, Networking, Homestead 时期）。  
**对应课文**：[L9.1](../../courses/level-09-systems/L09-M01-p2p.md)。  
**不要写进**：`index/03` 共识行、M5.4、L5.1、L5.4。本页是「EIP-8 disc not already upgraded / not already new-proto / not already unknown-accepted 正式三事（235 余量）/ not 1284 eip8-notdisc interchangeable / not 235 eip8-vs-already-new bundled interchangeable」，不是 eip8 vs already new bundled（235），也不是已经 enr-request（241），也不是已经 homestead-core（234）。不要另写 怎样同时认旧握手和新握手、怎样垫垃圾、怎样按头两个字节过滤连接。

## 官方三件事

1. **看见发现能吞多余字段 / 看见发现能吞多余字段 这份对象 is not already 发现已经升级 interchangeable，也不是已经 eip8 vs already new bundled（235） interchangeable / 1284 eip8-notdisc interchangeable / 1283 eip8-nothello interchangeable，也不是已经 EIP-8 disc not already upgraded / not already new-proto / not already unknown-accepted 正式三事 bundled（235 item 2 余量） interchangeable / 235 eip8 item 2 interchangeable。**  
   官方把发现能吞多余字段和发现已经升级写成两件。看见发现能吞多余字段，不是发现已经升级。

2. **看见不认识的发现包类型被丢掉 / 看见发现能吞多余字段 / 这份对象 is not already 已经在说新协议 interchangeable，也不是已经 eip8 vs already new bundled（235） interchangeable / 1284 eip8-notdisc interchangeable / 1285 eip8-nothand interchangeable，也不是已经 enr-request interchangeable / 241 enr-request interchangeable。**  
   官方把不认识的发现包类型被丢掉和已经在说新协议写成两件。看见不认识的发现包类型被丢掉，不是已经在说新协议。

3. **看见发现能吞多余字段 / 看见不认识的发现包类型被丢掉 / 这份对象 is not already 已经升级发现 interchangeable，也不是已经 eip8 vs already new bundled（235） interchangeable / 1284 eip8-notdisc interchangeable / 1283 eip8-nothello interchangeable，也不是已经 homestead-core interchangeable / 234 homestead-core interchangeable。**  
   官方把发现能吞多余字段和已经升级发现写成两件。看见发现能吞多余字段，不是已经升级发现。

栈怎么写、分隔符、例串是规范里的取值，本页不抄。不要另写 怎样同时认旧握手和新握手、怎样垫垃圾、怎样按头两个字节过滤连接。

## 官方为什么这样拆

- **发现能吞多余字段 不是发现已经升级：官方写任何包都忽略多出来的列表元素。**
- **不认识的包类型被丢掉 不是已经升级发现：官方写不认识的包类型应静默丢掉。**
- **不应校验 ping 版本 不是已经在说新协议：官方把发现写成独立一层。**

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 发现已经升级 | 不是发现已经升级 | 不是已经enr-request（241） |
| 已经在说新协议 | 不是已经在说新协议 | 不是已经homestead-core（234） |
| 已经升级发现 | 不是已经升级发现 | 不是已经1283 eip8-nothello |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 EIP-8 disc not already upgraded / not already new-proto / not already unknown-accepted 正式三事（235 余量），必须分开是不是发现已经升级、是不是已经在说新协议、是不是已经升级发现。可以跳过「看见能吞多余字段就已经在说新协议」。不要另写 怎样同时认旧握手和新握手、怎样垫垃圾、怎样按头两个字节过滤连接。235 eip8 vs already new bundled unbundling 在本页 item 2 续；续 [`worked-example-eip8-nothand-vs-bundled.md`](worked-example-eip8-nothand-vs-bundled.md)（不变量 1285 item 3）。

## 本页不抄

- hello / 发现 / 握手的测试向量、密钥、随机数、版本号取值、发现包最大长度、填充长度区间、旧包固定长度。
- 怎样同时认旧握手和新握手、怎样垫垃圾、怎样按头两个字节过滤连接。
