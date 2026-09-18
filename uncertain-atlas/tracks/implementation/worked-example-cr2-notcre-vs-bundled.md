# 例：看见盐创建指令不是已经是按序号占址不是已经是按发送者加序号占址；看见CREATE2 is not already CREATE不是已经能和旧式创建地址撞上；看见盐创建指令不是已经是按序号占址不是已经 222 bundled

**层次**：实现 / 规范对象。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：Ethereum [EIP-1014](https://eips.ethereum.org/EIPS/eip-1014)（Final, Core, Skinny CREATE2）。  
**对应课文**：[L5.1](../../courses/level-05-ethereum/L05-M01-evm-and-gas.md)。  
**不要写进**：`index/03` 共识行、M5.4、L5.4。本页是「EIP-1014 CREATE2 not already CREATE-nonce / not already sender-nonce / not already 222-bundled 正式三事（222 余量）/ not 1389 cr2-notcre interchangeable / not 222 create2-vs-created bundled interchangeable」，不是 create2 vs created bundled（222），也不是已经 CREATE碰到上限≠已经创建（175），也不是已经 initcode超界≠部署超界（176）。不要另写 怎样做通道里的反事实交互、怎样制造碰撞、怎样拆户后再占同址。

## 官方三件事

1. **看见盐创建指令不是已经是按序号占址 / 看见盐创建指令不是已经是按序号占址 这份对象 is not already 已经是按发送者加序号占址 interchangeable，也不是已经 create2 vs created bundled（222） interchangeable / 1389 cr2-notcre interchangeable / 1390 cr2-notexist interchangeable，也不是已经 EIP-1014 CREATE2 not already CREATE-nonce / not already sender-nonce / not already 222-bundled 正式三事 bundled（222 item 1 余量） interchangeable / 222 cr2 item 1 interchangeable。**  
   官方把盐创建指令不是已经是按序号占址和已经是按发送者加序号占址写成两件。看见盐创建指令不是已经是按序号占址，不是已经是按发送者加序号占址。

2. **看见CREATE2 is not already CREATE / 看见盐创建指令不是已经是按序号占址 / 这份对象 is not already 已经能和旧式创建地址撞上 interchangeable，也不是已经 create2 vs created bundled（222） interchangeable / 1389 cr2-notcre interchangeable / 1391 cr2-notover interchangeable，也不是已经 CREATE碰到上限≠已经创建 interchangeable / 175 CREATE碰到上限≠已经创建 interchangeable。**  
   官方把CREATE2 is not already CREATE和已经能和旧式创建地址撞上写成两件。看见CREATE2 is not already CREATE，不是已经能和旧式创建地址撞上。

3. **看见盐创建指令不是已经是按序号占址 / 看见CREATE2 is not already CREATE / 这份对象 is not already 已经 222 bundled interchangeable，也不是已经 create2 vs created bundled（222） interchangeable / 1389 cr2-notcre interchangeable / 1390 cr2-notexist interchangeable，也不是已经 initcode超界≠部署超界 interchangeable / 176 initcode超界≠部署超界 interchangeable。**  
   官方把盐创建指令不是已经是按序号占址和已经 222 bundled写成两件。看见盐创建指令不是已经是按序号占址，不是已经 222 bundled。

栈怎么写、分隔符、例串是规范里的取值，本页不抄。不要另写 怎样做通道里的反事实交互、怎样制造碰撞、怎样拆户后再占同址。

## 官方为什么这样拆

- **盐创建指令不是已经是按序号占址 interchangeable：官方把盐公式和发送者加序号写成两件。**
- **看见保留首字节不是已经能和旧式创建地址撞上。**
- **看见盐创建旋钮不是已经 222 bundled。**

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 已经是按发送者加序号占址 | 不是已经是按发送者加序号占址 | 不是已经CREATE碰到上限≠已经创建（175） |
| 已经能和旧式创建地址撞上 | 不是已经能和旧式创建地址撞上 | 不是已经initcode超界≠部署超界（176） |
| 已经 222 bundled | 不是已经 222 bundled | 不是已经1390 cr2-notexist |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 EIP-1014 CREATE2 not already CREATE-nonce / not already sender-nonce / not already 222-bundled 正式三事（222 余量），必须分开是不是已经是按发送者加序号占址、是不是已经能和旧式创建地址撞上、是不是已经 222 bundled。可以跳过「看见盐地址就已经创建」。不要另写 怎样做通道里的反事实交互、怎样制造碰撞、怎样拆户后再占同址。222 CREATE2 salt-address vs created bundled unbundling 在本页 item 1 启动；续 [`worked-example-cr2-notexist-vs-bundled.md`](worked-example-cr2-notexist-vs-bundled.md)（不变量 1390 item 2）。

## 本页不抄

- 操作码号、气价、哈希公式字面量、例址、例盐。
- 怎样做通道里的反事实交互、怎样制造碰撞、怎样拆户后再占同址。
