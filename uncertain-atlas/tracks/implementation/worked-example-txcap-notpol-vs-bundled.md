# 例：看见块里有一笔超帽不是已经只是策略拒绝不是已经只是策略拒绝；看见one over-cap in a block is not already policy-only不是已经更安全；看见块里有一笔超帽不是已经只是策略拒绝不是已经是不变量 101

**层次**：实现 / 规范对象。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：Ethereum [EIP-7825](https://eips.ethereum.org/EIPS/eip-7825)（Transaction Gas Limit Cap）。  
**对应课文**：[L5.1](../../courses/level-05-ethereum/L05-M01-evm-and-gas.md)。  
**不要写进**：`index/03` 共识行、M5.4、L5.4。本页是「EIP-7825 one-over-cap not already policy-only / not already safer / not already 101 正式三事（203 余量）/ not 1463 txcap-notpol interchangeable / not 203 tx-gas-cap-vs-block bundled interchangeable」，不是 tx gas cap vs block bundled（203），也不是已经 客户端默认≠协议帽（211），也不是已经 气≠墙钟（101）。不要另写 怎样把一笔拆到帽下。

## 官方三件事

1. **看见块里有一笔超帽不是已经只是策略拒绝 / 看见块里有一笔超帽不是已经只是策略拒绝 这份对象 is not already 已经只是策略拒绝 interchangeable，也不是已经 tx gas cap vs block bundled（203） interchangeable / 1463 txcap-notpol interchangeable / 1461 txcap-notblk interchangeable，也不是已经 EIP-7825 one-over-cap not already policy-only / not already safer / not already 101 正式三事 bundled（203 item 3 余量） interchangeable / 203 txcap item 3 interchangeable。**  
   官方把块里有一笔超帽不是已经只是策略拒绝和已经只是策略拒绝写成两件。看见块里有一笔超帽不是已经只是策略拒绝，不是已经只是策略拒绝。

2. **看见one over-cap in a block is not already policy-only / 看见块里有一笔超帽不是已经只是策略拒绝 / 这份对象 is not already 已经更安全 interchangeable，也不是已经 tx gas cap vs block bundled（203） interchangeable / 1463 txcap-notpol interchangeable / 1462 txcap-notpool interchangeable，也不是已经 客户端默认≠协议帽 interchangeable / 211 客户端默认≠协议帽 interchangeable。**  
   官方把one over-cap in a block is not already policy-only和已经更安全写成两件。看见one over-cap in a block is not already policy-only，不是已经更安全。

3. **看见块里有一笔超帽不是已经只是策略拒绝 / 看见one over-cap in a block is not already policy-only / 这份对象 is not already 已经是不变量 101 interchangeable，也不是已经 tx gas cap vs block bundled（203） interchangeable / 1463 txcap-notpol interchangeable / 1461 txcap-notblk interchangeable，也不是已经 气≠墙钟 interchangeable / 101 气≠墙钟 interchangeable。**  
   官方把块里有一笔超帽不是已经只是策略拒绝和已经是不变量 101写成两件。看见块里有一笔超帽不是已经只是策略拒绝，不是已经是不变量 101。

栈怎么写、分隔符、例串是规范里的取值，本页不抄。不要另写 怎样把一笔拆到帽下。

## 官方为什么这样拆

- **块里有一笔超帽不是已经只是策略拒绝 interchangeable：官方写处理之前整块非法，不是只是策略拒绝、块还可以收。**
- **看见整块非法不是已经更安全。**
- **看见本页不是已经是不变量 101。**

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 已经只是策略拒绝 | 不是已经只是策略拒绝 | 不是已经客户端默认≠协议帽（211） |
| 已经更安全 | 不是已经更安全 | 不是已经气≠墙钟（101） |
| 已经是不变量 101 | 不是已经是不变量 101 | 不是已经1461 txcap-notblk |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 EIP-7825 one-over-cap not already policy-only / not already safer / not already 101 正式三事（203 余量），必须分开是不是已经只是策略拒绝、是不是已经更安全、是不是已经是不变量 101。可以跳过「看见 7825 就已经改了块气」。不要另写 怎样把一笔拆到帽下。203 tx-gas-cap vs block bundled unbundling 在本页 item 3 完成；本页收束本批。下一份仍捆着的以太坊官方对象：rlp-cap（202）。

## 本页不抄

- 单笔气帽取值、二次幂字面量、典型块气区间。
- 怎样把一笔拆到帽下。
