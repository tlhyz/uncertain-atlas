# 例：看见类型字节不是已经解开内层字段不是已经解开内层字段；看见type byte is not already unpacked inner fields不是已经是 1559；看见类型字节不是已经解开内层字段不是已经 167 bundled

**层次**：实现 / 规范对象。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：Ethereum [EIP-2718](https://eips.ethereum.org/EIPS/eip-2718)（Final, Core, Typed Transaction Envelope）。  
**对应课文**：[L5.1](../../courses/level-05-ethereum/L05-M01-evm-and-gas.md)。  
**不要写进**：`index/03` 共识行、M5.4、L5.4。本页是「EIP-2718 type-byte not already unpacked / not already 1559 / not already 167-bundled 正式三事（167 余量）/ not 1455 tenv-notinner interchangeable / not 167 typed-vs-legacy bundled interchangeable」，不是 typed vs legacy bundled（167），也不是已经 基础费≠小费（158），也不是已经 列入≠已访问（168）。不要另写 怎样跨类型复用签名。

## 官方三件事

1. **看见类型字节不是已经解开内层字段 / 看见类型字节不是已经解开内层字段 这份对象 is not already 已经解开内层字段 interchangeable，也不是已经 typed vs legacy bundled（167） interchangeable / 1455 tenv-notinner interchangeable / 1456 tenv-notenv interchangeable，也不是已经 EIP-2718 type-byte not already unpacked / not already 1559 / not already 167-bundled 正式三事 bundled（167 item 1 余量） interchangeable / 167 tenv item 1 interchangeable。**  
   官方把类型字节不是已经解开内层字段和已经解开内层字段写成两件。看见类型字节不是已经解开内层字段，不是已经解开内层字段。

2. **看见type byte is not already unpacked inner fields / 看见类型字节不是已经解开内层字段 / 这份对象 is not already 已经是 1559 interchangeable，也不是已经 typed vs legacy bundled（167） interchangeable / 1455 tenv-notinner interchangeable / 1457 tenv-notrcpt interchangeable，也不是已经 基础费≠小费 interchangeable / 158 基础费≠小费 interchangeable。**  
   官方把type byte is not already unpacked inner fields和已经是 1559写成两件。看见type byte is not already unpacked inner fields，不是已经是 1559。

3. **看见类型字节不是已经解开内层字段 / 看见type byte is not already unpacked inner fields / 这份对象 is not already 已经 167 bundled interchangeable，也不是已经 typed vs legacy bundled（167） interchangeable / 1455 tenv-notinner interchangeable / 1456 tenv-notenv interchangeable，也不是已经 列入≠已访问 interchangeable / 168 列入≠已访问 interchangeable。**  
   官方把类型字节不是已经解开内层字段和已经 167 bundled写成两件。看见类型字节不是已经解开内层字段，不是已经 167 bundled。

栈怎么写、分隔符、例串是规范里的取值，本页不抄。不要另写 怎样跨类型复用签名。

## 官方为什么这样拆

- **类型字节不是已经解开内层字段 interchangeable：官方写类型标明格式，载荷由以后的 EIP 定义，是不透明字节。**
- **看见本页不是已经是 1559。**
- **看见读数旋钮不是已经 167 bundled。**

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 已经解开内层字段 | 不是已经解开内层字段 | 不是已经基础费≠小费（158） |
| 已经是 1559 | 不是已经是 1559 | 不是已经列入≠已访问（168） |
| 已经 167 bundled | 不是已经 167 bundled | 不是已经1456 tenv-notenv |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 EIP-2718 type-byte not already unpacked / not already 1559 / not already 167-bundled 正式三事（167 余量），必须分开是不是已经解开内层字段、是不是已经是 1559、是不是已经 167 bundled。可以跳过「带了类型 = 已经是 1559」。不要另写 怎样跨类型复用签名。167 typed vs legacy bundled unbundling 在本页 item 1 启动；续 [`worked-example-tenv-notenv-vs-bundled.md`](worked-example-tenv-notenv-vs-bundled.md)（不变量 1456 item 2）。

## 本页不抄

- 类型取值范围、分叉高度、字段表。
- 怎样跨类型复用签名。
