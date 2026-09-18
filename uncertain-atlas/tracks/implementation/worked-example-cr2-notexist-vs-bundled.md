# 例：看见算出来的盐地址不是已经创建不是已经创建；看见computed salt address is not already created不是已经有那份代码；看见算出来的盐地址不是已经创建不是已经付过创建费

**层次**：实现 / 规范对象。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：Ethereum [EIP-1014](https://eips.ethereum.org/EIPS/eip-1014)（Final, Core, Skinny CREATE2）。  
**对应课文**：[L5.1](../../courses/level-05-ethereum/L05-M01-evm-and-gas.md)。  
**不要写进**：`index/03` 共识行、M5.4、L5.4。本页是「EIP-1014 salt-address not already created / not already has-code / not already paid-create 正式三事（222 余量）/ not 1390 cr2-notexist interchangeable / not 222 create2-vs-created bundled interchangeable」，不是 create2 vs created bundled（222），也不是已经 自毁≠已删（160），也不是已经 代码哈希指令≠已看见代码（221）。不要另写 怎样做通道里的反事实交互、怎样制造碰撞、怎样拆户后再占同址。

## 官方三件事

1. **看见算出来的盐地址不是已经创建 / 看见算出来的盐地址不是已经创建 这份对象 is not already 已经创建 interchangeable，也不是已经 create2 vs created bundled（222） interchangeable / 1390 cr2-notexist interchangeable / 1389 cr2-notcre interchangeable，也不是已经 EIP-1014 salt-address not already created / not already has-code / not already paid-create 正式三事 bundled（222 item 2 余量） interchangeable / 222 cr2 item 2 interchangeable。**  
   官方把算出来的盐地址不是已经创建和已经创建写成两件。看见算出来的盐地址不是已经创建，不是已经创建。

2. **看见computed salt address is not already created / 看见算出来的盐地址不是已经创建 / 这份对象 is not already 已经有那份代码 interchangeable，也不是已经 create2 vs created bundled（222） interchangeable / 1390 cr2-notexist interchangeable / 1391 cr2-notover interchangeable，也不是已经 自毁≠已删 interchangeable / 160 自毁≠已删 interchangeable。**  
   官方把computed salt address is not already created和已经有那份代码写成两件。看见computed salt address is not already created，不是已经有那份代码。

3. **看见算出来的盐地址不是已经创建 / 看见computed salt address is not already created / 这份对象 is not already 已经付过创建费 interchangeable，也不是已经 create2 vs created bundled（222） interchangeable / 1390 cr2-notexist interchangeable / 1389 cr2-notcre interchangeable，也不是已经 代码哈希指令≠已看见代码 interchangeable / 221 代码哈希指令≠已看见代码 interchangeable。**  
   官方把算出来的盐地址不是已经创建和已经付过创建费写成两件。看见算出来的盐地址不是已经创建，不是已经付过创建费。

栈怎么写、分隔符、例串是规范里的取值，本页不抄。不要另写 怎样做通道里的反事实交互、怎样制造碰撞、怎样拆户后再占同址。

## 官方为什么这样拆

- **算出来的盐地址不是已经创建 interchangeable：官方意图是和还不存在的地址交互。**
- **看见能算出地址不是已经有那份代码。**
- **看见能事先算址不是已经付过创建费。**

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 已经创建 | 不是已经创建 | 不是已经自毁≠已删（160） |
| 已经有那份代码 | 不是已经有那份代码 | 不是已经代码哈希指令≠已看见代码（221） |
| 已经付过创建费 | 不是已经付过创建费 | 不是已经1389 cr2-notcre |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 EIP-1014 salt-address not already created / not already has-code / not already paid-create 正式三事（222 余量），必须分开是不是已经创建、是不是已经有那份代码、是不是已经付过创建费。可以跳过「看见盐地址就已经创建」。不要另写 怎样做通道里的反事实交互、怎样制造碰撞、怎样拆户后再占同址。222 CREATE2 salt-address vs created bundled unbundling 在本页 item 2 续；续 [`worked-example-cr2-notover-vs-bundled.md`](worked-example-cr2-notover-vs-bundled.md)（不变量 1391 item 3）。

## 本页不抄

- 操作码号、气价、哈希公式字面量、例址、例盐。
- 怎样做通道里的反事实交互、怎样制造碰撞、怎样拆户后再占同址。
