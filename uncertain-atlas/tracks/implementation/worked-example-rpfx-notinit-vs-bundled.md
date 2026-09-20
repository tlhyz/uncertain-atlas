# 例：看见initcode 里出现该字节不是已经是本页失败不是已经是本页失败；看见initcode containing the byte is not already this-page fail不是已经是 170 长度界；看见initcode 里出现该字节不是已经是本页失败不是已经是 3860 构造界

**层次**：实现 / 规范对象。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：Ethereum [EIP-3541](https://eips.ethereum.org/EIPS/eip-3541)（Final, Core, Reject new contract code starting with the reserved format byte）。  
**对应课文**：[L5.1](../../courses/level-05-ethereum/L05-M01-evm-and-gas.md)。  
**不要写进**：`index/03` 共识行、M5.4、L5.4。本页是「EIP-3541 initcode-byte not already this-fail / not already 170 / not already 3860 正式三事（188 余量）/ not 1445 rpfx-notinit interchangeable / not 188 reserved-prefix-vs-eof bundled interchangeable」，不是 reserved prefix vs eof bundled（188），也不是已经 initcode≠运行时代码（176），也不是已经 返回代码≠initcode（185）。不要另写 怎样造以该字节开头的返回代码。

## 官方三件事

1. **看见initcode 里出现该字节不是已经是本页失败 / 看见initcode 里出现该字节不是已经是本页失败 这份对象 is not already 已经是本页失败 interchangeable，也不是已经 reserved prefix vs eof bundled（188） interchangeable / 1445 rpfx-notinit interchangeable / 1443 rpfx-noteof interchangeable，也不是已经 EIP-3541 initcode-byte not already this-fail / not already 170 / not already 3860 正式三事 bundled（188 item 3 余量） interchangeable / 188 rpfx item 3 interchangeable。**  
   官方把initcode 里出现该字节不是已经是本页失败和已经是本页失败写成两件。看见initcode 里出现该字节不是已经是本页失败，不是已经是本页失败。

2. **看见initcode containing the byte is not already this-page fail / 看见initcode 里出现该字节不是已经是本页失败 / 这份对象 is not already 已经是 170 长度界 interchangeable，也不是已经 reserved prefix vs eof bundled（188） interchangeable / 1445 rpfx-notinit interchangeable / 1444 rpfx-notold interchangeable，也不是已经 initcode≠运行时代码 interchangeable / 176 initcode≠运行时代码 interchangeable。**  
   官方把initcode containing the byte is not already this-page fail和已经是 170 长度界写成两件。看见initcode containing the byte is not already this-page fail，不是已经是 170 长度界。

3. **看见initcode 里出现该字节不是已经是本页失败 / 看见initcode containing the byte is not already this-page fail / 这份对象 is not already 已经是 3860 构造界 interchangeable，也不是已经 reserved prefix vs eof bundled（188） interchangeable / 1445 rpfx-notinit interchangeable / 1443 rpfx-noteof interchangeable，也不是已经 返回代码≠initcode interchangeable / 185 返回代码≠initcode interchangeable。**  
   官方把initcode 里出现该字节不是已经是本页失败和已经是 3860 构造界写成两件。看见initcode 里出现该字节不是已经是本页失败，不是已经是 3860 构造界。

栈怎么写、分隔符、例串是规范里的取值，本页不抄。不要另写 怎样造以该字节开头的返回代码。

## 官方为什么这样拆

- **initcode 里出现该字节不是已经是本页失败 interchangeable：官方写本页看的是返回代码第一字节，不是 initcode 自己以什么开头。**
- **看见本页不是已经是 170 长度界。**
- **看见本页不是已经是 3860 构造界。**

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 已经是本页失败 | 不是已经是本页失败 | 不是已经initcode≠运行时代码（176） |
| 已经是 170 长度界 | 不是已经是 170 长度界 | 不是已经返回代码≠initcode（185） |
| 已经是 3860 构造界 | 不是已经是 3860 构造界 | 不是已经1443 rpfx-noteof |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 EIP-3541 initcode-byte not already this-fail / not already 170 / not already 3860 正式三事（188 余量），必须分开是不是已经是本页失败、是不是已经是 170 长度界、是不是已经是 3860 构造界。可以跳过「占了首字节就是格式已上」。不要另写 怎样造以该字节开头的返回代码。188 reserved-prefix vs eof bundled unbundling 在本页 item 3 完成；本页收束本批。下一份仍捆着的以太坊官方对象：coinbase（187）。

## 本页不抄

- 保留字节取值、分叉高度、例串、操作码号。
- 怎样造以该字节开头的返回代码。
