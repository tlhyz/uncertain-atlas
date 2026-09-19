# 例：看见对等节点宣布历史窗不是已经改了共识历史不是已经改了共识历史；看见peer history window is not already consensus history changed不是已经是不变量 23；看见对等节点宣布历史窗不是已经改了共识历史不是已经 207 bundled

**层次**：实现 / 规范对象。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：Ethereum [EIP-7642](https://eips.ethereum.org/EIPS/eip-7642)（history expiry and simpler receipts）。  
**对应课文**：[L5.3](../../courses/level-05-ethereum/L05-M03-multi-client.md)。  
**不要写进**：`index/03` 共识行、M5.4、L5.4。本页是「EIP-7642 history-window not already consensus-pruned / not already 23 / not already 207-bundled 正式三事（207 余量）/ not 1488 hwin-notcons interchangeable / not 207 history-window-vs-consensus bundled interchangeable」，不是 history window vs consensus bundled（207），也不是已经 短时承诺≠永存DA（23），也不是已经 跳过须点名（25）。不要另写 怎样丢历史、怎样谎报最早块。

## 官方三件事

1. **看见对等节点宣布历史窗不是已经改了共识历史 / 看见对等节点宣布历史窗不是已经改了共识历史 这份对象 is not already 已经改了共识历史 interchangeable，也不是已经 history window vs consensus bundled（207） interchangeable / 1488 hwin-notcons interchangeable / 1489 hwin-notenc interchangeable，也不是已经 EIP-7642 history-window not already consensus-pruned / not already 23 / not already 207-bundled 正式三事 bundled（207 item 1 余量） interchangeable / 207 hwin item 1 interchangeable。**  
   官方把对等节点宣布历史窗不是已经改了共识历史和已经改了共识历史写成两件。看见对等节点宣布历史窗不是已经改了共识历史，不是已经改了共识历史。

2. **看见peer history window is not already consensus history changed / 看见对等节点宣布历史窗不是已经改了共识历史 / 这份对象 is not already 已经是不变量 23 interchangeable，也不是已经 history window vs consensus bundled（207） interchangeable / 1488 hwin-notcons interchangeable / 1490 hwin-notsync interchangeable，也不是已经 短时承诺≠永存DA interchangeable / 23 短时承诺≠永存DA interchangeable。**  
   官方把peer history window is not already consensus history changed和已经是不变量 23写成两件。看见peer history window is not already consensus history changed，不是已经是不变量 23。

3. **看见对等节点宣布历史窗不是已经改了共识历史 / 看见peer history window is not already consensus history changed / 这份对象 is not already 已经 207 bundled interchangeable，也不是已经 history window vs consensus bundled（207） interchangeable / 1488 hwin-notcons interchangeable / 1489 hwin-notenc interchangeable，也不是已经 跳过须点名 interchangeable / 25 跳过须点名 interchangeable。**  
   官方把对等节点宣布历史窗不是已经改了共识历史和已经 207 bundled写成两件。看见对等节点宣布历史窗不是已经改了共识历史，不是已经 207 bundled。

栈怎么写、分隔符、例串是规范里的取值，本页不抄。不要另写 怎样丢历史、怎样谎报最早块。

## 官方为什么这样拆

- **对等节点宣布历史窗不是已经改了共识历史 interchangeable：官方写本页是让还想靠 eth 协议拉历史的人先知道对等节点还服不服，不是共识已经删历史。**
- **看见本页不是已经是不变量 23。**
- **看见读数旋钮不是已经 207 bundled。**

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 已经改了共识历史 | 不是已经改了共识历史 | 不是已经短时承诺≠永存DA（23） |
| 已经是不变量 23 | 不是已经是不变量 23 | 不是已经跳过须点名（25） |
| 已经 207 bundled | 不是已经 207 bundled | 不是已经1489 hwin-notenc |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 EIP-7642 history-window not already consensus-pruned / not already 23 / not already 207-bundled 正式三事（207 余量），必须分开是不是已经改了共识历史、是不是已经是不变量 23、是不是已经 207 bundled。可以跳过「看见 7642 就已经改了共识历史」。不要另写 怎样丢历史、怎样谎报最早块。207 history-window vs consensus bundled unbundling 在本页 item 1 启动；续 [`worked-example-hwin-notenc-vs-bundled.md`](worked-example-hwin-notenc-vs-bundled.md)（不变量 1489 item 2）。

## 本页不抄

- 服务截止日期、带宽估算、每纪元块数、消息号、布隆宽度。
- 怎样丢历史、怎样谎报最早块。
