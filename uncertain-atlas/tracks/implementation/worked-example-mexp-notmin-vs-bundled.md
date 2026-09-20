# 例：看见最低气价不是已经能对小输入无限便宜不是已经能对小输入无限便宜；看见min gas is not already infinitely cheap不是已经不伤安全；看见最低气价不是已经能对小输入无限便宜不是已经是签名产品

**层次**：实现 / 规范对象。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：Ethereum [EIP-2565](https://eips.ethereum.org/EIPS/eip-2565)（Final, Core, ModExp Gas Cost）。  
**对应课文**：[L5.1](../../courses/level-05-ethereum/L05-M01-evm-and-gas.md)。  
**不要写进**：`index/03` 共识行、M5.4、L5.4。本页是「EIP-2565 min-gas not already infinitely-cheap / not already no-DoS / not already product-live 正式三事（227 余量）/ not 1427 mexp-notmin interchangeable / not 227 modexp-price-vs-bound bundled interchangeable」，不是 modexp price vs bound bundled（227），也不是已经 回滚≠烧光（177），也不是已经 预编译算术≠已验 BLS（199）。不要另写 怎样造便宜模幂、怎样打满一块、怎样按新价实现签名或可验证延迟函数。

## 官方三件事

1. **看见最低气价不是已经能对小输入无限便宜 / 看见最低气价不是已经能对小输入无限便宜 这份对象 is not already 已经能对小输入无限便宜 interchangeable，也不是已经 modexp price vs bound bundled（227） interchangeable / 1427 mexp-notmin interchangeable / 1425 mexp-not198 interchangeable，也不是已经 EIP-2565 min-gas not already infinitely-cheap / not already no-DoS / not already product-live 正式三事 bundled（227 item 3 余量） interchangeable / 227 mexp item 3 interchangeable。**  
   官方把最低气价不是已经能对小输入无限便宜和已经能对小输入无限便宜写成两件。看见最低气价不是已经能对小输入无限便宜，不是已经能对小输入无限便宜。

2. **看见min gas is not already infinitely cheap / 看见最低气价不是已经能对小输入无限便宜 / 这份对象 is not already 已经不伤安全 interchangeable，也不是已经 modexp price vs bound bundled（227） interchangeable / 1427 mexp-notmin interchangeable / 1426 mexp-notiface interchangeable，也不是已经 回滚≠烧光 interchangeable / 177 回滚≠烧光 interchangeable。**  
   官方把min gas is not already infinitely cheap和已经不伤安全写成两件。看见min gas is not already infinitely cheap，不是已经不伤安全。

3. **看见最低气价不是已经能对小输入无限便宜 / 看见min gas is not already infinitely cheap / 这份对象 is not already 已经是签名产品 interchangeable，也不是已经 modexp price vs bound bundled（227） interchangeable / 1427 mexp-notmin interchangeable / 1425 mexp-not198 interchangeable，也不是已经 预编译算术≠已验 BLS interchangeable / 199 预编译算术≠已验 BLS interchangeable。**  
   官方把最低气价不是已经能对小输入无限便宜和已经是签名产品写成两件。看见最低气价不是已经能对小输入无限便宜，不是已经是签名产品。

栈怎么写、分隔符、例串是规范里的取值，本页不抄。不要另写 怎样造便宜模幂、怎样打满一块、怎样按新价实现签名或可验证延迟函数。

## 官方为什么这样拆

- **最低气价不是已经能对小输入无限便宜 interchangeable：官方写设最低气价是为了防止小输入被标得过低。**
- **看见降价不是已经不伤安全。**
- **看见动机写签名不是已经是签名产品。**

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 已经能对小输入无限便宜 | 不是已经能对小输入无限便宜 | 不是已经回滚≠烧光（177） |
| 已经不伤安全 | 不是已经不伤安全 | 不是已经预编译算术≠已验 BLS（199） |
| 已经是签名产品 | 不是已经是签名产品 | 不是已经1425 mexp-not198 |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 EIP-2565 min-gas not already infinitely-cheap / not already no-DoS / not already product-live 正式三事（227 余量），必须分开是不是已经能对小输入无限便宜、是不是已经不伤安全、是不是已经是签名产品。可以跳过「看见 2565 就已经加了帽」。不要另写 怎样造便宜模幂、怎样打满一块、怎样按新价实现签名或可验证延迟函数。227 modexp-price vs bound bundled unbundling 在本页 item 3 完成；本页收束本批。下一份仍捆着的以太坊官方对象：bn128 降价（228）。

## 本页不抄

- 预编译地址、最低气价、除数常数、复杂度公式、测试向量数字。
- 怎样造便宜模幂、怎样打满一块、怎样按新价实现签名或可验证延迟函数。
