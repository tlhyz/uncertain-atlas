# 例：看见碰撞变得可能不是已经覆盖不是已经覆盖已有代码；看见collision possible is not already overwrite不是已经是 684 本身；看见碰撞变得可能不是已经覆盖不是已经是 3860 分析费

**层次**：实现 / 规范对象。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：Ethereum [EIP-1014](https://eips.ethereum.org/EIPS/eip-1014)（Final, Core, Skinny CREATE2）。  
**对应课文**：[L5.1](../../courses/level-05-ethereum/L05-M01-evm-and-gas.md)。  
**不要写进**：`index/03` 共识行、M5.4、L5.4。本页是「EIP-1014 collision-possible not already overwrite / not already 684 / not already 3860 正式三事（222 余量）/ not 1391 cr2-notover interchangeable / not 222 create2-vs-created bundled interchangeable」，不是 create2 vs created bundled（222），也不是已经 EIP-3860 initcode（176），也不是已经 同一笔拆户重占（160）。不要另写 怎样做通道里的反事实交互、怎样制造碰撞、怎样拆户后再占同址。

## 官方三件事

1. **看见碰撞变得可能不是已经覆盖 / 看见碰撞变得可能不是已经覆盖 这份对象 is not already 已经覆盖已有代码 interchangeable，也不是已经 create2 vs created bundled（222） interchangeable / 1391 cr2-notover interchangeable / 1389 cr2-notcre interchangeable，也不是已经 EIP-1014 collision-possible not already overwrite / not already 684 / not already 3860 正式三事 bundled（222 item 3 余量） interchangeable / 222 cr2 item 3 interchangeable。**  
   官方把碰撞变得可能不是已经覆盖和已经覆盖已有代码写成两件。看见碰撞变得可能不是已经覆盖，不是已经覆盖已有代码。

2. **看见collision possible is not already overwrite / 看见碰撞变得可能不是已经覆盖 / 这份对象 is not already 已经是 684 本身 interchangeable，也不是已经 create2 vs created bundled（222） interchangeable / 1391 cr2-notover interchangeable / 1390 cr2-notexist interchangeable，也不是已经 EIP-3860 initcode interchangeable / 176 EIP-3860 initcode interchangeable。**  
   官方把collision possible is not already overwrite和已经是 684 本身写成两件。看见collision possible is not already overwrite，不是已经是 684 本身。

3. **看见碰撞变得可能不是已经覆盖 / 看见collision possible is not already overwrite / 这份对象 is not already 已经是 3860 分析费 interchangeable，也不是已经 create2 vs created bundled（222） interchangeable / 1391 cr2-notover interchangeable / 1389 cr2-notcre interchangeable，也不是已经 同一笔拆户重占 interchangeable / 160 同一笔拆户重占 interchangeable。**  
   官方把碰撞变得可能不是已经覆盖和已经是 3860 分析费写成两件。看见碰撞变得可能不是已经覆盖，不是已经是 3860 分析费。

栈怎么写、分隔符、例串是规范里的取值，本页不抄。不要另写 怎样做通道里的反事实交互、怎样制造碰撞、怎样拆户后再占同址。

## 官方为什么这样拆

- **碰撞变得可能不是已经覆盖 interchangeable：官方把可能撞上交给 684 立刻失败。**
- **看见本页不是已经是 684 本身。**
- **看见哈希费不是已经是 3860 按字分析费。**

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 已经覆盖已有代码 | 不是已经覆盖已有代码 | 不是已经EIP-3860 initcode（176） |
| 已经是 684 本身 | 不是已经是 684 本身 | 不是已经同一笔拆户重占（160） |
| 已经是 3860 分析费 | 不是已经是 3860 分析费 | 不是已经1389 cr2-notcre |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 EIP-1014 collision-possible not already overwrite / not already 684 / not already 3860 正式三事（222 余量），必须分开是不是已经覆盖已有代码、是不是已经是 684 本身、是不是已经是 3860 分析费。可以跳过「看见盐地址就已经创建」。不要另写 怎样做通道里的反事实交互、怎样制造碰撞、怎样拆户后再占同址。222 CREATE2 salt-address vs created bundled unbundling 在本页 item 3 完成；本页收束本批。下一份仍捆着的以太坊官方对象：EIP-1052 EXTCODEHASH（221）。

## 本页不抄

- 操作码号、气价、哈希公式字面量、例址、例盐。
- 怎样做通道里的反事实交互、怎样制造碰撞、怎样拆户后再占同址。
