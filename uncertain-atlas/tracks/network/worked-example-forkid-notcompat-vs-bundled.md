# 例：看见通告了下一分叉不是已经兼容；看见远端哈希是子集不是已经陈旧；看见通告了下一分叉不是本地已经该升级

**层次**：网络 / 规范对象。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：Ethereum [EIP-2124](https://eips.ethereum.org/EIPS/eip-2124)（Final, Networking）。  
**对应课文**：[L9.1](../../courses/level-09-systems/L09-M01-p2p.md)。  
**不要写进**：`index/03` 共识行、M5.4、L5.1、L5.4、05b。本页是「EIP-2124 nextfork not already compatible / not already stale / not already must-upgrade 正式三事（239 余量）/ not 1287 forkid-notcompat interchangeable / not 239 forkid-vs-same-chain bundled interchangeable」，不是 forkid vs same chain bundled（239），也不是已经 eip8-compat（235），也不是已经 fork-rpc（210）。不要另写 怎样伪造分叉标识、怎样假装同一条链、怎样在三向分叉里互踢。

## 官方三件事

1. **看见通告了下一分叉 / 看见通告了下一分叉 这份对象 is not already 已经兼容 interchangeable，也不是已经 forkid vs same chain bundled（239） interchangeable / 1287 forkid-notcompat interchangeable / 1286 forkid-notsame interchangeable，也不是已经 EIP-2124 nextfork not already compatible / not already stale / not already must-upgrade 正式三事 bundled（239 item 2 余量） interchangeable / 239 forkid item 2 interchangeable。**  
   官方把通告了下一分叉和已经兼容写成两件。看见通告了下一分叉，不是已经兼容。

2. **看见远端哈希是子集 / 看见通告了下一分叉 / 这份对象 is not already 已经陈旧 interchangeable，也不是已经 forkid vs same chain bundled（239） interchangeable / 1287 forkid-notcompat interchangeable / 1288 forkid-notfeat interchangeable，也不是已经 eip8-compat interchangeable / 235 eip8-compat interchangeable。**  
   官方把远端哈希是子集和已经陈旧写成两件。看见远端哈希是子集，不是已经陈旧。

3. **看见通告了下一分叉 / 看见远端哈希是子集 / 这份对象 is not already 本地已经该升级 interchangeable，也不是已经 forkid vs same chain bundled（239） interchangeable / 1287 forkid-notcompat interchangeable / 1286 forkid-notsame interchangeable，也不是已经 fork-rpc interchangeable / 210 fork-rpc interchangeable。**  
   官方把通告了下一分叉和本地已经该升级写成两件。看见通告了下一分叉，不是本地已经该升级。

栈怎么写、分隔符、例串是规范里的取值，本页不抄。不要另写 怎样伪造分叉标识、怎样假装同一条链、怎样在三向分叉里互踢。

## 官方为什么这样拆

- **通告下一分叉 不是已经兼容：官方要区分还在同步和软件陈旧。**
- **子集 不是已经陈旧：官方写远端哈希是本地已过分叉的子集时按远端还在同步来连。**
- **超集 不是本地已经该升级：官方写能用本地知道的未来分叉补齐时按本地还在同步来连。**

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 已经兼容 | 不是已经兼容 | 不是已经eip8-compat（235） |
| 已经陈旧 | 不是已经陈旧 | 不是已经fork-rpc（210） |
| 本地已经该升级 | 不是本地已经该升级 | 不是已经1286 forkid-notsame |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 EIP-2124 nextfork not already compatible / not already stale / not already must-upgrade 正式三事（239 余量），必须分开是不是已经兼容、是不是已经陈旧、是不是本地已经该升级。可以跳过「看见分叉标识对上就已经同一条链」。不要另写 怎样伪造分叉标识、怎样假装同一条链、怎样在三向分叉里互踢。239 forkid vs same chain bundled unbundling 在本页 item 2 续；续 [`worked-example-forkid-notfeat-vs-bundled.md`](worked-example-forkid-notfeat-vs-bundled.md)（不变量 1288 item 3）。

## 本页不抄

- CRC 取值、分叉高度表、编码样例、测试头高度。
- 怎样伪造分叉标识、怎样假装同一条链、怎样在三向分叉里互踢。
