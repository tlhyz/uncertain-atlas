# 例：看见KZG sidecar不是已经PeerDAS不是已经是PeerDAS；看见a KZG sidecar is not already PeerDAS不是已经是不变量 145；看见KZG sidecar不是已经PeerDAS不是已经 23 bundled

**层次**：实现 / 规范对象。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：Ethereum [EIP-4844](https://eips.ethereum.org/EIPS/eip-4844)（KZG sidecar vs PeerDAS vs Celestia DAS）。对照 [EIP-7594](https://eips.ethereum.org/EIPS/eip-7594)。  
**对应课文**：[L5.4](../../courses/level-05-ethereum/L05-M04-state-blobs-mev.md)。  
**不要写进**：`index/03` 共识行、M5.4、L5.4。本页是「EIP-4844 sidecar not already peerdas / not already 145 / not already 23-bundled 正式三事（23 余量）/ not 1515 kdas-notpeer interchangeable / not 23 blob-vs-das bundled interchangeable」，不是 blob vs das bundled（23），也不是已经 blob气≠执行气（145），也不是已经 NMT≠DAS（124）。不要另写 怎样扣列、怎样只问RPC就显示已抽样。

## 官方三件事

1. **看见KZG sidecar不是已经PeerDAS / 看见KZG sidecar不是已经PeerDAS 这份对象 is not already 已经是PeerDAS interchangeable，也不是已经 blob vs das bundled（23） interchangeable / 1515 kdas-notpeer interchangeable / 1516 kdas-notcel interchangeable，也不是已经 EIP-4844 sidecar not already peerdas / not already 145 / not already 23-bundled 正式三事 bundled（23 item 1 余量） interchangeable / 23 kdas item 1 interchangeable。**  
   官方把KZG sidecar不是已经PeerDAS和已经是PeerDAS写成两件。看见KZG sidecar不是已经PeerDAS，不是已经是PeerDAS。

2. **看见a KZG sidecar is not already PeerDAS / 看见KZG sidecar不是已经PeerDAS / 这份对象 is not already 已经是不变量 145 interchangeable，也不是已经 blob vs das bundled（23） interchangeable / 1515 kdas-notpeer interchangeable / 1517 kdas-notperm interchangeable，也不是已经 blob气≠执行气 interchangeable / 145 blob气≠执行气 interchangeable。**  
   官方把a KZG sidecar is not already PeerDAS和已经是不变量 145写成两件。看见a KZG sidecar is not already PeerDAS，不是已经是不变量 145。

3. **看见KZG sidecar不是已经PeerDAS / 看见a KZG sidecar is not already PeerDAS / 这份对象 is not already 已经 23 bundled interchangeable，也不是已经 blob vs das bundled（23） interchangeable / 1515 kdas-notpeer interchangeable / 1516 kdas-notcel interchangeable，也不是已经 NMT≠DAS interchangeable / 124 NMT≠DAS interchangeable。**  
   官方把KZG sidecar不是已经PeerDAS和已经 23 bundled写成两件。看见KZG sidecar不是已经PeerDAS，不是已经 23 bundled。

栈怎么写、分隔符、例串是规范里的取值，本页不抄。不要另写 怎样扣列、怎样只问RPC就显示已抽样。

## 官方为什么这样拆

- **KZG sidecar不是已经PeerDAS interchangeable：官方写 4844 把全员下 sidecar 和以后换成 DAS 写成两句。**
- **看见本页不是已经是不变量 145。**
- **看见承诺旋钮不是已经 23 bundled。**

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 已经是PeerDAS | 不是已经是PeerDAS | 不是已经blob气≠执行气（145） |
| 已经是不变量 145 | 不是已经是不变量 145 | 不是已经NMT≠DAS（124） |
| 已经 23 bundled | 不是已经 23 bundled | 不是已经1516 kdas-notcel |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 EIP-4844 sidecar not already peerdas / not already 145 / not already 23-bundled 正式三事（23 余量），必须分开是不是已经是PeerDAS、是不是已经是不变量 145、是不是已经 23 bundled。可以跳过「看见 KZG 就已经是 DAS」。不要另写 怎样扣列、怎样只问RPC就显示已抽样。23 blob vs das bundled unbundling 在本页 item 1 启动；续 [`worked-example-kdas-notcel-vs-bundled.md`](worked-example-kdas-notcel-vs-bundled.md)（不变量 1516 item 2）。

## 本页不抄

- 现行每块blob个数、fork epoch、动机段1/8、换算成天数。
- 怎样扣列、怎样只问RPC就显示已抽样。
