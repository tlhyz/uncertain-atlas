# 例：看见能重叠拷不是已经是 calldata / 返回数据拷不是已经是 calldata / 返回数据拷；看见overlap copy is not already calldata copy不是已经改了 CALL 的效果；看见能重叠拷不是已经是 calldata / 返回数据拷不是已经是不变量 169

**层次**：实现 / 规范对象。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：Ethereum [EIP-5656](https://eips.ethereum.org/EIPS/eip-5656)（Final, Core, MCOPY instruction）。  
**对应课文**：[L5.1](../../courses/level-05-ethereum/L05-M01-evm-and-gas.md)。  
**不要写进**：`index/03` 共识行、M5.4、L5.4。本页是「EIP-5656 overlap-copy not already calldata-copy / not already CALL-changed / not already 169 正式三事（216 余量）/ not 1412 mcpy-notcd interchangeable / not 216 mcopy-vs-identity bundled interchangeable」，不是 mcopy vs identity bundled（216），也不是已经 冷热访问（169），也不是已经 calldata 地板（197）。不要另写 怎样造真缓冲、怎样打重叠拷、怎样改 CALL 效果。

## 官方三件事

1. **看见能重叠拷不是已经是 calldata / 返回数据拷 / 看见能重叠拷不是已经是 calldata / 返回数据拷 这份对象 is not already 已经是 calldata / 返回数据拷 interchangeable，也不是已经 mcopy vs identity bundled（216） interchangeable / 1412 mcpy-notcd interchangeable / 1410 mcpy-notid interchangeable，也不是已经 EIP-5656 overlap-copy not already calldata-copy / not already CALL-changed / not already 169 正式三事 bundled（216 item 3 余量） interchangeable / 216 mcpy item 3 interchangeable。**  
   官方把能重叠拷不是已经是 calldata / 返回数据拷和已经是 calldata / 返回数据拷写成两件。看见能重叠拷不是已经是 calldata / 返回数据拷，不是已经是 calldata / 返回数据拷。

2. **看见overlap copy is not already calldata copy / 看见能重叠拷不是已经是 calldata / 返回数据拷 / 这份对象 is not already 已经改了 CALL 的效果 interchangeable，也不是已经 mcopy vs identity bundled（216） interchangeable / 1412 mcpy-notcd interchangeable / 1411 mcpy-notbuf interchangeable，也不是已经 冷热访问 interchangeable / 169 冷热访问 interchangeable。**  
   官方把overlap copy is not already calldata copy和已经改了 CALL 的效果写成两件。看见overlap copy is not already calldata copy，不是已经改了 CALL 的效果。

3. **看见能重叠拷不是已经是 calldata / 返回数据拷 / 看见overlap copy is not already calldata copy / 这份对象 is not already 已经是不变量 169 interchangeable，也不是已经 mcopy vs identity bundled（216） interchangeable / 1412 mcpy-notcd interchangeable / 1410 mcpy-notid interchangeable，也不是已经 calldata 地板 interchangeable / 197 calldata 地板 interchangeable。**  
   官方把能重叠拷不是已经是 calldata / 返回数据拷和已经是不变量 169写成两件。看见能重叠拷不是已经是 calldata / 返回数据拷，不是已经是不变量 169。

栈怎么写、分隔符、例串是规范里的取值，本页不抄。不要另写 怎样造真缓冲、怎样打重叠拷、怎样改 CALL 效果。

## 官方为什么这样拆

- **能重叠拷不是已经是 calldata / 返回数据拷 interchangeable：官方写栈顺序一样，本页拷的是内存到内存。**
- **看见只动内存不是已经改了 CALL 的效果。**
- **看见本页不是已经是不变量 169。**

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 已经是 calldata / 返回数据拷 | 不是已经是 calldata / 返回数据拷 | 不是已经冷热访问（169） |
| 已经改了 CALL 的效果 | 不是已经改了 CALL 的效果 | 不是已经calldata 地板（197） |
| 已经是不变量 169 | 不是已经是不变量 169 | 不是已经1410 mcpy-notid |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 EIP-5656 overlap-copy not already calldata-copy / not already CALL-changed / not already 169 正式三事（216 余量），必须分开是不是已经是 calldata / 返回数据拷、是不是已经改了 CALL 的效果、是不是已经是不变量 169。可以跳过「看见 5656 就已经是身份预编译」。不要另写 怎样造真缓冲、怎样打重叠拷、怎样改 CALL 效果。216 MCOPY vs identity bundled unbundling 在本页 item 3 完成；本页收束本批。下一份仍捆着的以太坊官方对象：退款计数器（223）。

## 本页不抄

- 操作码号、气价、百分比、块号区间、测试向量、规范提交哈希。
- 怎样造真缓冲、怎样打重叠拷、怎样改 CALL 效果。
