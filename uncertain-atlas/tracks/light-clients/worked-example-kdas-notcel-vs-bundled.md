# 例：看见PeerDAS不是已经Celestia二维DAS不是已经是Celestia二维DAS；看见PeerDAS is not already Celestia 2D DAS不是已经是不变量 124；看见PeerDAS不是已经Celestia二维DAS不是已经是不变量 200

**层次**：实现 / 规范对象。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：Ethereum [EIP-4844](https://eips.ethereum.org/EIPS/eip-4844)（KZG sidecar vs PeerDAS vs Celestia DAS）。对照 [EIP-7594](https://eips.ethereum.org/EIPS/eip-7594)。  
**对应课文**：[L5.4](../../courses/level-05-ethereum/L05-M04-state-blobs-mev.md)。  
**不要写进**：`index/03` 共识行、M5.4、L5.4。本页是「EIP-4844 peerdas not already celestia-das / not already 124 / not already 200 正式三事（23 余量）/ not 1516 kdas-notcel interchangeable / not 23 blob-vs-das bundled interchangeable」，不是 blob vs das bundled（23），也不是已经 NMT≠DAS（124），也不是已经 抬高日程≠已改气种（200）。不要另写 怎样扣列、怎样只问RPC就显示已抽样。

## 官方三件事

1. **看见PeerDAS不是已经Celestia二维DAS / 看见PeerDAS不是已经Celestia二维DAS 这份对象 is not already 已经是Celestia二维DAS interchangeable，也不是已经 blob vs das bundled（23） interchangeable / 1516 kdas-notcel interchangeable / 1515 kdas-notpeer interchangeable，也不是已经 EIP-4844 peerdas not already celestia-das / not already 124 / not already 200 正式三事 bundled（23 item 2 余量） interchangeable / 23 kdas item 2 interchangeable。**  
   官方把PeerDAS不是已经Celestia二维DAS和已经是Celestia二维DAS写成两件。看见PeerDAS不是已经Celestia二维DAS，不是已经是Celestia二维DAS。

2. **看见PeerDAS is not already Celestia 2D DAS / 看见PeerDAS不是已经Celestia二维DAS / 这份对象 is not already 已经是不变量 124 interchangeable，也不是已经 blob vs das bundled（23） interchangeable / 1516 kdas-notcel interchangeable / 1517 kdas-notperm interchangeable，也不是已经 NMT≠DAS interchangeable / 124 NMT≠DAS interchangeable。**  
   官方把PeerDAS is not already Celestia 2D DAS和已经是不变量 124写成两件。看见PeerDAS is not already Celestia 2D DAS，不是已经是不变量 124。

3. **看见PeerDAS不是已经Celestia二维DAS / 看见PeerDAS is not already Celestia 2D DAS / 这份对象 is not already 已经是不变量 200 interchangeable，也不是已经 blob vs das bundled（23） interchangeable / 1516 kdas-notcel interchangeable / 1515 kdas-notpeer interchangeable，也不是已经 抬高日程≠已改气种 interchangeable / 200 抬高日程≠已改气种 interchangeable。**  
   官方把PeerDAS不是已经Celestia二维DAS和已经是不变量 200写成两件。看见PeerDAS不是已经Celestia二维DAS，不是已经是不变量 200。

栈怎么写、分隔符、例串是规范里的取值，本页不抄。不要另写 怎样扣列、怎样只问RPC就显示已抽样。

## 官方为什么这样拆

- **PeerDAS不是已经Celestia二维DAS interchangeable：官方写 PeerDAS 是一维扩列按 node-id 保管，不是二维随机抽格。**
- **看见本页不是已经是不变量 124。**
- **看见本页不是已经是不变量 200。**

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 已经是Celestia二维DAS | 不是已经是Celestia二维DAS | 不是已经NMT≠DAS（124） |
| 已经是不变量 124 | 不是已经是不变量 124 | 不是已经抬高日程≠已改气种（200） |
| 已经是不变量 200 | 不是已经是不变量 200 | 不是已经1515 kdas-notpeer |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 EIP-4844 peerdas not already celestia-das / not already 124 / not already 200 正式三事（23 余量），必须分开是不是已经是Celestia二维DAS、是不是已经是不变量 124、是不是已经是不变量 200。可以跳过「看见 KZG 就已经是 DAS」。不要另写 怎样扣列、怎样只问RPC就显示已抽样。23 blob vs das bundled unbundling 在本页 item 2 续；续 [`worked-example-kdas-notperm-vs-bundled.md`](worked-example-kdas-notperm-vs-bundled.md)（不变量 1517 item 3）。

## 本页不抄

- 现行每块blob个数、fork epoch、动机段1/8、换算成天数。
- 怎样扣列、怎样只问RPC就显示已抽样。
