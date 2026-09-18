# 例：看见创建里回滚不是已经部署不是已经部署；看见create revert is not already deployed不是已经占址；看见创建里回滚不是已经部署不是已经是另一条链的 REVERTED 档

**层次**：实现 / 规范对象。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：Ethereum [EIP-140](https://eips.ethereum.org/EIPS/eip-140)（Final, Core, REVERT instruction）。  
**对应课文**：[L5.1](../../courses/level-05-ethereum/L05-M01-evm-and-gas.md)。  
**不要写进**：`index/03` 共识行、M5.4、L5.4。本页是「EIP-140 create-revert not already deployed / not already occupied / not already starknet-reverted 正式三事（177 余量）/ not 1382 rvert-notdep interchangeable / not 177 revert-vs-invalid bundled interchangeable」，不是 revert vs invalid bundled（177），也不是已经 Starknet REVERTED 档（138），也不是已经 静态帧≠view（178）。不要另写 怎样挑回滚或非法指令去留气或烧气。

## 官方三件事

1. **看见创建里回滚不是已经部署 / 看见创建里回滚不是已经部署 这份对象 is not already 已经部署 interchangeable，也不是已经 revert vs invalid bundled（177） interchangeable / 1382 rvert-notdep interchangeable / 1380 rvert-notburn interchangeable，也不是已经 EIP-140 create-revert not already deployed / not already occupied / not already starknet-reverted 正式三事 bundled（177 item 3 余量） interchangeable / 177 rvert item 3 interchangeable。**  
   官方把创建里回滚不是已经部署和已经部署写成两件。看见创建里回滚不是已经部署，不是已经部署。

2. **看见create revert is not already deployed / 看见创建里回滚不是已经部署 / 这份对象 is not already 已经占址 interchangeable，也不是已经 revert vs invalid bundled（177） interchangeable / 1382 rvert-notdep interchangeable / 1381 rvert-notfee interchangeable，也不是已经 Starknet REVERTED 档 interchangeable / 138 Starknet REVERTED 档 interchangeable。**  
   官方把create revert is not already deployed和已经占址写成两件。看见create revert is not already deployed，不是已经占址。

3. **看见创建里回滚不是已经部署 / 看见create revert is not already deployed / 这份对象 is not already 已经是另一条链的 REVERTED 档 interchangeable，也不是已经 revert vs invalid bundled（177） interchangeable / 1382 rvert-notdep interchangeable / 1380 rvert-notburn interchangeable，也不是已经 静态帧≠view interchangeable / 178 静态帧≠view interchangeable。**  
   官方把创建里回滚不是已经部署和已经是另一条链的 REVERTED 档写成两件。看见创建里回滚不是已经部署，不是已经是另一条链的 REVERTED 档。

栈怎么写、分隔符、例串是规范里的取值，本页不抄。不要另写 怎样挑回滚或非法指令去留气或烧气。

## 官方为什么这样拆

- **创建里回滚不是已经部署 interchangeable：官方写创建上下文回滚不部署。**
- **看见栈上推 0 不是已经占址。**
- **看见原因仍在返回缓冲不是已经是另一条链的 REVERTED 档。**

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 已经部署 | 不是已经部署 | 不是已经Starknet REVERTED 档（138） |
| 已经占址 | 不是已经占址 | 不是已经静态帧≠view（178） |
| 已经是另一条链的 REVERTED 档 | 不是已经是另一条链的 REVERTED 档 | 不是已经1380 rvert-notburn |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 EIP-140 create-revert not already deployed / not already occupied / not already starknet-reverted 正式三事（177 余量），必须分开是不是已经部署、是不是已经占址、是不是已经是另一条链的 REVERTED 档。可以跳过「看见失败就已经烧光剩余气」。不要另写 怎样挑回滚或非法指令去留气或烧气。177 REVERT leftover-gas vs burn bundled unbundling 在本页 item 3 完成；本页收束本批。下一份仍捆着的以太坊官方对象：EIP-214 STATICCALL（178）。

## 本页不抄

- 操作码号、分叉高度、例气数、例返回字节。
- 怎样挑回滚或非法指令去留气或烧气。
