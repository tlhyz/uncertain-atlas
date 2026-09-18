# 例：看见能收新握手编码不是旧握手已经退役；看见仍收旧握手不是已经改了共识；看见能收新握手编码不是旧格式已经退役

**层次**：网络 / 规范对象。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：Bitcoin [EIP-8](https://eips.ethereum.org/EIPS/eip-8)（Final, Networking, Homestead 时期）。  
**对应课文**：[L9.1](../../courses/level-09-systems/L09-M01-p2p.md)。  
**不要写进**：`index/03` 共识行、M5.4、L5.1、L5.4。本页是「EIP-8 handshake not already old-retired / not already homestead-consensus / not already new-proto 正式三事（235 余量）/ not 1285 eip8-nothand interchangeable / not 235 eip8-vs-already-new bundled interchangeable」，不是 eip8 vs already new bundled（235），也不是已经 homestead-core（234），也不是已经 v2-private（242）。不要另写 怎样同时认旧握手和新握手、怎样垫垃圾、怎样按头两个字节过滤连接。

## 官方三件事

1. **看见能收新握手编码 / 看见能收新握手编码 这份对象 is not already 旧握手已经退役 interchangeable，也不是已经 eip8 vs already new bundled（235） interchangeable / 1285 eip8-nothand interchangeable / 1283 eip8-nothello interchangeable，也不是已经 EIP-8 handshake not already old-retired / not already homestead-consensus / not already new-proto 正式三事 bundled（235 item 3 余量） interchangeable / 235 eip8 item 3 interchangeable。**  
   官方把能收新握手编码和旧握手已经退役写成两件。看见能收新握手编码，不是旧握手已经退役。

2. **看见仍收旧握手 / 看见能收新握手编码 / 这份对象 is not already 已经改了共识 interchangeable，也不是已经 eip8 vs already new bundled（235） interchangeable / 1285 eip8-nothand interchangeable / 1284 eip8-notdisc interchangeable，也不是已经 homestead-core interchangeable / 234 homestead-core interchangeable。**  
   官方把仍收旧握手和已经改了共识写成两件。看见仍收旧握手，不是已经改了共识。

3. **看见能收新握手编码 / 看见仍收旧握手 / 这份对象 is not already 旧格式已经退役 interchangeable，也不是已经 eip8 vs already new bundled（235） interchangeable / 1285 eip8-nothand interchangeable / 1283 eip8-nothello interchangeable，也不是已经 v2-private interchangeable / 242 v2-private interchangeable。**  
   官方把能收新握手编码和旧格式已经退役写成两件。看见能收新握手编码，不是旧格式已经退役。

栈怎么写、分隔符、例串是规范里的取值，本页不抄。不要另写 怎样同时认旧握手和新握手、怎样垫垃圾、怎样按头两个字节过滤连接。

## 官方为什么这样拆

- **能收新握手编码 不是旧握手已经退役：官方写所有合法的旧第 4 版包仍被接受。**
- **跟 Homestead 一起上 不是已经改了共识：官方把本页钉在 Networking，不是 Core。**
- **仍收旧握手 不是旧格式已经退役：官方写本页向后兼容。**

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 旧握手已经退役 | 不是旧握手已经退役 | 不是已经homestead-core（234） |
| 已经改了共识 | 不是已经改了共识 | 不是已经v2-private（242） |
| 旧格式已经退役 | 不是旧格式已经退役 | 不是已经1283 eip8-nothello |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 EIP-8 handshake not already old-retired / not already homestead-consensus / not already new-proto 正式三事（235 余量），必须分开是不是旧握手已经退役、是不是已经改了共识、是不是旧格式已经退役。可以跳过「看见能吞多余字段就已经在说新协议」。不要另写 怎样同时认旧握手和新握手、怎样垫垃圾、怎样按头两个字节过滤连接。235 eip8 vs already new bundled unbundling 在本页 item 3 完成；本页收束本批。

## 本页不抄

- hello / 发现 / 握手的测试向量、密钥、随机数、版本号取值、发现包最大长度、填充长度区间、旧包固定长度。
- 怎样同时认旧握手和新握手、怎样垫垃圾、怎样按头两个字节过滤连接。
