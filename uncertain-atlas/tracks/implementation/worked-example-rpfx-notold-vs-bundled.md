# 例：看见已有同首字节代码不是已经被本页改语义不是已经被本页改语义；看见existing same-prefix code is not already rewritten不是已经按新格式重验；看见已有同首字节代码不是已经被本页改语义不是已经做完 3541

**层次**：实现 / 规范对象。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：Ethereum [EIP-3541](https://eips.ethereum.org/EIPS/eip-3541)（Final, Core, Reject new contract code starting with the reserved format byte）。  
**对应课文**：[L5.1](../../courses/level-05-ethereum/L05-M01-evm-and-gas.md)。  
**不要写进**：`index/03` 共识行、M5.4、L5.4。本页是「EIP-3541 existing-code not already rewritten / not already revalidated / not already 3541-done 正式三事（188 余量）/ not 1444 rpfx-notold interchangeable / not 188 reserved-prefix-vs-eof bundled interchangeable」，不是 reserved prefix vs eof bundled（188），也不是已经 返回代码≠initcode（185），也不是已经 回滚≠烧光（177）。不要另写 怎样造以该字节开头的返回代码。

## 官方三件事

1. **看见已有同首字节代码不是已经被本页改语义 / 看见已有同首字节代码不是已经被本页改语义 这份对象 is not already 已经被本页改语义 interchangeable，也不是已经 reserved prefix vs eof bundled（188） interchangeable / 1444 rpfx-notold interchangeable / 1443 rpfx-noteof interchangeable，也不是已经 EIP-3541 existing-code not already rewritten / not already revalidated / not already 3541-done 正式三事 bundled（188 item 2 余量） interchangeable / 188 rpfx item 2 interchangeable。**  
   官方把已有同首字节代码不是已经被本页改语义和已经被本页改语义写成两件。看见已有同首字节代码不是已经被本页改语义，不是已经被本页改语义。

2. **看见existing same-prefix code is not already rewritten / 看见已有同首字节代码不是已经被本页改语义 / 这份对象 is not already 已经按新格式重验 interchangeable，也不是已经 reserved prefix vs eof bundled（188） interchangeable / 1444 rpfx-notold interchangeable / 1445 rpfx-notinit interchangeable，也不是已经 返回代码≠initcode interchangeable / 185 返回代码≠initcode interchangeable。**  
   官方把existing same-prefix code is not already rewritten和已经按新格式重验写成两件。看见existing same-prefix code is not already rewritten，不是已经按新格式重验。

3. **看见已有同首字节代码不是已经被本页改语义 / 看见existing same-prefix code is not already rewritten / 这份对象 is not already 已经做完 3541 interchangeable，也不是已经 reserved prefix vs eof bundled（188） interchangeable / 1444 rpfx-notold interchangeable / 1443 rpfx-noteof interchangeable，也不是已经 回滚≠烧光 interchangeable / 177 回滚≠烧光 interchangeable。**  
   官方把已有同首字节代码不是已经被本页改语义和已经做完 3541写成两件。看见已有同首字节代码不是已经被本页改语义，不是已经做完 3541。

栈怎么写、分隔符、例串是规范里的取值，本页不抄。不要另写 怎样造以该字节开头的返回代码。

## 官方为什么这样拆

- **已有同首字节代码不是已经被本页改语义 interchangeable：官方写账户树里已经存在、以该字节开头的代码，语义不被本页改动。**
- **看见已有代码不是已经按新格式重验。**
- **看见规范编号不是已经做完 3541。**

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 已经被本页改语义 | 不是已经被本页改语义 | 不是已经返回代码≠initcode（185） |
| 已经按新格式重验 | 不是已经按新格式重验 | 不是已经回滚≠烧光（177） |
| 已经做完 3541 | 不是已经做完 3541 | 不是已经1443 rpfx-noteof |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 EIP-3541 existing-code not already rewritten / not already revalidated / not already 3541-done 正式三事（188 余量），必须分开是不是已经被本页改语义、是不是已经按新格式重验、是不是已经做完 3541。可以跳过「占了首字节就是格式已上」。不要另写 怎样造以该字节开头的返回代码。188 reserved-prefix vs eof bundled unbundling 在本页 item 2 续；续 [`worked-example-rpfx-notinit-vs-bundled.md`](worked-example-rpfx-notinit-vs-bundled.md)（不变量 1445 item 3）。

## 本页不抄

- 保留字节取值、分叉高度、例串、操作码号。
- 怎样造以该字节开头的返回代码。
