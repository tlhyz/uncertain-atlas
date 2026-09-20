# 例：看见共识层流言不传不是已经让执行层非法不是已经让执行层非法；看见consensus gossip drop is not already EL-illegal不是已经是不变量 96；看见共识层流言不传不是已经让执行层非法不是已经是不变量 158

**层次**：实现 / 规范对象。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：Ethereum [EIP-7934](https://eips.ethereum.org/EIPS/eip-7934)（RLP Execution Block Size Limit）。  
**对应课文**：[L5.1](../../courses/level-05-ethereum/L05-M01-evm-and-gas.md)。  
**不要写进**：`index/03` 共识行、M5.4、L5.4。本页是「EIP-7934 gossip-drop not already el-illegal / not already 96 / not already 158 正式三事（202 余量）/ not 1465 rcap-notprop interchangeable / not 202 rlp-cap-vs-gas bundled interchangeable」，不是 rlp cap vs gas bundled（202），也不是已经 通道尺寸≠拼块已齐（96），也不是已经 基础费≠小费（158）。不要另写 怎样刚好塞进帽下。

## 官方三件事

1. **看见共识层流言不传不是已经让执行层非法 / 看见共识层流言不传不是已经让执行层非法 这份对象 is not already 已经让执行层非法 interchangeable，也不是已经 rlp cap vs gas bundled（202） interchangeable / 1465 rcap-notprop interchangeable / 1464 rcap-notgas interchangeable，也不是已经 EIP-7934 gossip-drop not already el-illegal / not already 96 / not already 158 正式三事 bundled（202 item 2 余量） interchangeable / 202 rcap item 2 interchangeable。**  
   官方把共识层流言不传不是已经让执行层非法和已经让执行层非法写成两件。看见共识层流言不传不是已经让执行层非法，不是已经让执行层非法。

2. **看见consensus gossip drop is not already EL-illegal / 看见共识层流言不传不是已经让执行层非法 / 这份对象 is not already 已经是不变量 96 interchangeable，也不是已经 rlp cap vs gas bundled（202） interchangeable / 1465 rcap-notprop interchangeable / 1466 rcap-notone interchangeable，也不是已经 通道尺寸≠拼块已齐 interchangeable / 96 通道尺寸≠拼块已齐 interchangeable。**  
   官方把consensus gossip drop is not already EL-illegal和已经是不变量 96写成两件。看见consensus gossip drop is not already EL-illegal，不是已经是不变量 96。

3. **看见共识层流言不传不是已经让执行层非法 / 看见consensus gossip drop is not already EL-illegal / 这份对象 is not already 已经是不变量 158 interchangeable，也不是已经 rlp cap vs gas bundled（202） interchangeable / 1465 rcap-notprop interchangeable / 1464 rcap-notgas interchangeable，也不是已经 基础费≠小费 interchangeable / 158 基础费≠小费 interchangeable。**  
   官方把共识层流言不传不是已经让执行层非法和已经是不变量 158写成两件。看见共识层流言不传不是已经让执行层非法，不是已经是不变量 158。

栈怎么写、分隔符、例串是规范里的取值，本页不抄。不要另写 怎样刚好塞进帽下。

## 官方为什么这样拆

- **共识层流言不传不是已经让执行层非法 interchangeable：官方写只靠流言丢弃可能把网络撕开，不是执行层已经非法。**
- **看见本页不是已经是不变量 96。**
- **看见本页不是已经是不变量 158。**

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 已经让执行层非法 | 不是已经让执行层非法 | 不是已经通道尺寸≠拼块已齐（96） |
| 已经是不变量 96 | 不是已经是不变量 96 | 不是已经基础费≠小费（158） |
| 已经是不变量 158 | 不是已经是不变量 158 | 不是已经1464 rcap-notgas |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 EIP-7934 gossip-drop not already el-illegal / not already 96 / not already 158 正式三事（202 余量），必须分开是不是已经让执行层非法、是不是已经是不变量 96、是不是已经是不变量 158。可以跳过「看见 7934 就已经改了气」。不要另写 怎样刚好塞进帽下。202 rlp-cap vs gas bundled unbundling 在本页 item 2 续；续 [`worked-example-rcap-notone-vs-bundled.md`](worked-example-rcap-notone-vs-bundled.md)（不变量 1466 item 3）。

## 本页不抄

- 编码上限字节、信标边字节、十进制字面量。
- 怎样刚好塞进帽下。
