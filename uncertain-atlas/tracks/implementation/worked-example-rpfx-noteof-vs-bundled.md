# 例：看见新代码以保留首字节开头不是已经是对象格式已经部署不是已经是对象格式已经部署；看见reserved prefix is not already EOF deployed不是已经按新格式验过；看见新代码以保留首字节开头不是已经是对象格式已经部署不是已经 188 bundled

**层次**：实现 / 规范对象。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：Ethereum [EIP-3541](https://eips.ethereum.org/EIPS/eip-3541)（Final, Core, Reject new contract code starting with the reserved format byte）。  
**对应课文**：[L5.1](../../courses/level-05-ethereum/L05-M01-evm-and-gas.md)。  
**不要写进**：`index/03` 共识行、M5.4、L5.4。本页是「EIP-3541 reserved-prefix not already EOF-deployed / not already validated / not already 188-bundled 正式三事（188 余量）/ not 1443 rpfx-noteof interchangeable / not 188 reserved-prefix-vs-eof bundled interchangeable」，不是 reserved prefix vs eof bundled（188），也不是已经 返回代码≠initcode（185），也不是已经 initcode≠运行时代码（176）。不要另写 怎样造以该字节开头的返回代码。

## 官方三件事

1. **看见新代码以保留首字节开头不是已经是对象格式已经部署 / 看见新代码以保留首字节开头不是已经是对象格式已经部署 这份对象 is not already 已经是对象格式已经部署 interchangeable，也不是已经 reserved prefix vs eof bundled（188） interchangeable / 1443 rpfx-noteof interchangeable / 1444 rpfx-notold interchangeable，也不是已经 EIP-3541 reserved-prefix not already EOF-deployed / not already validated / not already 188-bundled 正式三事 bundled（188 item 1 余量） interchangeable / 188 rpfx item 1 interchangeable。**  
   官方把新代码以保留首字节开头不是已经是对象格式已经部署和已经是对象格式已经部署写成两件。看见新代码以保留首字节开头不是已经是对象格式已经部署，不是已经是对象格式已经部署。

2. **看见reserved prefix is not already EOF deployed / 看见新代码以保留首字节开头不是已经是对象格式已经部署 / 这份对象 is not already 已经按新格式验过 interchangeable，也不是已经 reserved prefix vs eof bundled（188） interchangeable / 1443 rpfx-noteof interchangeable / 1445 rpfx-notinit interchangeable，也不是已经 返回代码≠initcode interchangeable / 185 返回代码≠initcode interchangeable。**  
   官方把reserved prefix is not already EOF deployed和已经按新格式验过写成两件。看见reserved prefix is not already EOF deployed，不是已经按新格式验过。

3. **看见新代码以保留首字节开头不是已经是对象格式已经部署 / 看见reserved prefix is not already EOF deployed / 这份对象 is not already 已经 188 bundled interchangeable，也不是已经 reserved prefix vs eof bundled（188） interchangeable / 1443 rpfx-noteof interchangeable / 1444 rpfx-notold interchangeable，也不是已经 initcode≠运行时代码 interchangeable / 176 initcode≠运行时代码 interchangeable。**  
   官方把新代码以保留首字节开头不是已经是对象格式已经部署和已经 188 bundled写成两件。看见新代码以保留首字节开头不是已经是对象格式已经部署，不是已经 188 bundled。

栈怎么写、分隔符、例串是规范里的取值，本页不抄。不要另写 怎样造以该字节开头的返回代码。

## 官方为什么这样拆

- **新代码以保留首字节开头不是已经是对象格式已经部署 interchangeable：官方写本页只占魔法第一字节，对象格式规范是另一份。**
- **看见本页不是已经按新格式验过。**
- **看见读数旋钮不是已经 188 bundled。**

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 已经是对象格式已经部署 | 不是已经是对象格式已经部署 | 不是已经返回代码≠initcode（185） |
| 已经按新格式验过 | 不是已经按新格式验过 | 不是已经initcode≠运行时代码（176） |
| 已经 188 bundled | 不是已经 188 bundled | 不是已经1444 rpfx-notold |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 EIP-3541 reserved-prefix not already EOF-deployed / not already validated / not already 188-bundled 正式三事（188 余量），必须分开是不是已经是对象格式已经部署、是不是已经按新格式验过、是不是已经 188 bundled。可以跳过「占了首字节就是格式已上」。不要另写 怎样造以该字节开头的返回代码。188 reserved-prefix vs eof bundled unbundling 在本页 item 1 启动；续 [`worked-example-rpfx-notold-vs-bundled.md`](worked-example-rpfx-notold-vs-bundled.md)（不变量 1444 item 2）。

## 本页不抄

- 保留字节取值、分叉高度、例串、操作码号。
- 怎样造以该字节开头的返回代码。
