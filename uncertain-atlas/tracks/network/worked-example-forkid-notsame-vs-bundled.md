# 例：看见分叉哈希对上不是已经同一条链；看见创世规则已经不是 Frontier不是已经用朴素相等判定同一条链；看见分叉哈希对上不是已经把创世算进已应用分叉

**层次**：网络 / 规范对象。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：Ethereum [EIP-2124](https://eips.ethereum.org/EIPS/eip-2124)（Final, Networking）。  
**对应课文**：[L9.1](../../courses/level-09-systems/L09-M01-p2p.md)。  
**不要写进**：`index/03` 共识行、M5.4、L5.1、L5.4、05b。本页是「EIP-2124 hash not already same-chain / not already naive-eq / not already genesis-counted 正式三事（239 余量）/ not 1286 forkid-notsame interchangeable / not 239 forkid-vs-same-chain bundled interchangeable」，不是 forkid vs same chain bundled（239），也不是已经 eip8-compat（235），也不是已经 history-window（207）。不要另写 怎样伪造分叉标识、怎样假装同一条链、怎样在三向分叉里互踢。

## 官方三件事

1. **看见分叉哈希对上 / 看见分叉哈希对上 这份对象 is not already 已经同一条链 interchangeable，也不是已经 forkid vs same chain bundled（239） interchangeable / 1286 forkid-notsame interchangeable / 1287 forkid-notcompat interchangeable，也不是已经 EIP-2124 hash not already same-chain / not already naive-eq / not already genesis-counted 正式三事 bundled（239 item 1 余量） interchangeable / 239 forkid item 1 interchangeable。**  
   官方把分叉哈希对上和已经同一条链写成两件。看见分叉哈希对上，不是已经同一条链。

2. **看见创世规则已经不是 Frontier / 看见分叉哈希对上 / 这份对象 is not already 已经用朴素相等判定同一条链 interchangeable，也不是已经 forkid vs same chain bundled（239） interchangeable / 1286 forkid-notsame interchangeable / 1288 forkid-notfeat interchangeable，也不是已经 eip8-compat interchangeable / 235 eip8-compat interchangeable。**  
   官方把创世规则已经不是 Frontier和已经用朴素相等判定同一条链写成两件。看见创世规则已经不是 Frontier，不是已经用朴素相等判定同一条链。

3. **看见分叉哈希对上 / 看见创世规则已经不是 Frontier / 这份对象 is not already 已经把创世算进已应用分叉 interchangeable，也不是已经 forkid vs same chain bundled（239） interchangeable / 1286 forkid-notsame interchangeable / 1287 forkid-notcompat interchangeable，也不是已经 history-window interchangeable / 207 history-window interchangeable。**  
   官方把分叉哈希对上和已经把创世算进已应用分叉写成两件。看见分叉哈希对上，不是已经把创世算进已应用分叉。

栈怎么写、分隔符、例串是规范里的取值，本页不抄。不要另写 怎样伪造分叉标识、怎样假装同一条链、怎样在三向分叉里互踢。

## 官方为什么这样拆

- **概括 不是已经同一条链：官方说发现协议本来分不清公网、私网、测试网。**
- **分叉哈希对上 不是已经用朴素相等判定：官方写创世相同、分叉不同应当互拒。**
- **创世规则已经不是 Frontier 不是已经把创世算进已应用分叉：官方写那不算一次分叉。**

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 已经同一条链 | 不是已经同一条链 | 不是已经eip8-compat（235） |
| 已经用朴素相等判定同一条链 | 不是已经用朴素相等判定同一条链 | 不是已经history-window（207） |
| 已经把创世算进已应用分叉 | 不是已经把创世算进已应用分叉 | 不是已经1287 forkid-notcompat |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 EIP-2124 hash not already same-chain / not already naive-eq / not already genesis-counted 正式三事（239 余量），必须分开是不是已经同一条链、是不是已经用朴素相等判定同一条链、是不是已经把创世算进已应用分叉。可以跳过「看见分叉标识对上就已经同一条链」。不要另写 怎样伪造分叉标识、怎样假装同一条链、怎样在三向分叉里互踢。239 forkid vs same chain bundled unbundling 在本页 item 1 启动；续 [`worked-example-forkid-notcompat-vs-bundled.md`](worked-example-forkid-notcompat-vs-bundled.md)（不变量 1287 item 2）。

## 本页不抄

- CRC 取值、分叉高度表、编码样例、测试头高度。
- 怎样伪造分叉标识、怎样假装同一条链、怎样在三向分叉里互踢。
