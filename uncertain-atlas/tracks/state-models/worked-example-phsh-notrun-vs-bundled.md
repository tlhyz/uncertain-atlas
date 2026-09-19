# 例：看见旧节点HASH160 EQUAL通过不是新节点已经再跑赎回不是已经再跑过赎回；看见old-node HASH160 EQUAL passing is not already the new node re-running redeem不是已经是不变量 153；看见旧节点HASH160 EQUAL通过不是新节点已经再跑赎回不是已经是不变量 144

**层次**：实现 / 规范对象。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：Bitcoin [BIP-16](https://github.com/bitcoin/bips/blob/master/bip-0016.mediawiki)（Pay to Script Hash）。  
**对应课文**：[L2.1](../../courses/level-02-state/L02-M01-utxo.md)。  
**不要写进**：`index/03` 共识行、M2.1、L2.1。本页是「BIP-16 old-equal not already new-reran / not already 153 / not already 144 正式三事（170 余量）/ not 1534 phsh-notrun interchangeable / not 170 p2sh-hash-vs-redeem bundled interchangeable」，不是 p2sh hash vs redeem bundled（170），也不是已经 钥匙路径≠揭树（153），也不是已经 策略≠共识（144）。不要另写 怎样构造旧合法新非法的赎回、一确认攻击。

## 官方三件事

1. **看见旧节点HASH160 EQUAL通过不是新节点已经再跑赎回 / 看见旧节点HASH160 EQUAL通过不是新节点已经再跑赎回 这份对象 is not already 已经再跑过赎回 interchangeable，也不是已经 p2sh hash vs redeem bundled（170） interchangeable / 1534 phsh-notrun interchangeable / 1533 phsh-notrev interchangeable，也不是已经 BIP-16 old-equal not already new-reran / not already 153 / not already 144 正式三事 bundled（170 item 2 余量） interchangeable / 170 phsh item 2 interchangeable。**  
   官方把旧节点HASH160 EQUAL通过不是新节点已经再跑赎回和已经再跑过赎回写成两件。看见旧节点HASH160 EQUAL通过不是新节点已经再跑赎回，不是已经再跑过赎回。

2. **看见old-node HASH160 EQUAL passing is not already the new node re-running redeem / 看见旧节点HASH160 EQUAL通过不是新节点已经再跑赎回 / 这份对象 is not already 已经是不变量 153 interchangeable，也不是已经 p2sh hash vs redeem bundled（170） interchangeable / 1534 phsh-notrun interchangeable / 1535 phsh-notinr interchangeable，也不是已经 钥匙路径≠揭树 interchangeable / 153 钥匙路径≠揭树 interchangeable。**  
   官方把old-node HASH160 EQUAL passing is not already the new node re-running redeem和已经是不变量 153写成两件。看见old-node HASH160 EQUAL passing is not already the new node re-running redeem，不是已经是不变量 153。

3. **看见旧节点HASH160 EQUAL通过不是新节点已经再跑赎回 / 看见old-node HASH160 EQUAL passing is not already the new node re-running redeem / 这份对象 is not already 已经是不变量 144 interchangeable，也不是已经 p2sh hash vs redeem bundled（170） interchangeable / 1534 phsh-notrun interchangeable / 1533 phsh-notrev interchangeable，也不是已经 策略≠共识 interchangeable / 144 策略≠共识 interchangeable。**  
   官方把旧节点HASH160 EQUAL通过不是新节点已经再跑赎回和已经是不变量 144写成两件。看见旧节点HASH160 EQUAL通过不是新节点已经再跑赎回，不是已经是不变量 144。

栈怎么写、分隔符、例串是规范里的取值，本页不抄。不要另写 怎样构造旧合法新非法的赎回、一确认攻击。

## 官方为什么这样拆

- **旧节点HASH160 EQUAL通过不是新节点已经再跑赎回 interchangeable：官方写旧实现验块时哈希对上即可、不再做其它验证。**
- **看见本页不是已经是不变量 153。**
- **看见本页不是已经是不变量 144。**

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 已经再跑过赎回 | 不是已经再跑过赎回 | 不是已经钥匙路径≠揭树（153） |
| 已经是不变量 153 | 不是已经是不变量 153 | 不是已经策略≠共识（144） |
| 已经是不变量 144 | 不是已经是不变量 144 | 不是已经1533 phsh-notrev |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 BIP-16 old-equal not already new-reran / not already 153 / not already 144 正式三事（170 余量），必须分开是不是已经再跑过赎回、是不是已经是不变量 153、是不是已经是不变量 144。可以跳过「看见哈希对上就已经验过内层」。不要另写 怎样构造旧合法新非法的赎回、一确认攻击。170 p2sh hash vs redeem bundled unbundling 在本页 item 2 续；续 [`worked-example-phsh-notinr-vs-bundled.md`](worked-example-phsh-notinr-vs-bundled.md)（不变量 1535 item 3）。

## 本页不抄

- 激活票数、字节上限、例脚本、时间戳、操作码号。
- 怎样构造旧合法新非法的赎回、一确认攻击。
