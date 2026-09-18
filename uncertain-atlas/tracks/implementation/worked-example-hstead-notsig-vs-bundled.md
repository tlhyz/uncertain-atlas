# 例：看见交易拒高 s 不是已经让预编译拒不是已经让 ECRECOVER 拒高 s；看见tx rejects high s is not ECRECOVER rejects不是已经是比特币 DER 低 s；看见交易拒高 s 不是已经让预编译拒不是已经把链标识写进签名

**层次**：实现 / 规范对象。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：Ethereum [EIP-2](https://eips.ethereum.org/EIPS/eip-2)（Final, Core, Homestead）。  
**对应课文**：[L5.1](../../courses/level-05-ethereum/L05-M01-evm-and-gas.md)。  
**不要写进**：`index/03` 共识行、M5.4、L5.4。本页是「EIP-2 high-s not already ECRECOVER-rejects / not already BIP-66 / not already EIP-155 正式四事（234 余量）/ not 1347 hstead-notsig interchangeable / not 234 homestead-vs-already-done bundled interchangeable」，不是 homestead vs already done bundled（234），也不是已经 比特币 DER 低 s（172），也不是已经 EIP-155 链标识（161）。不要另写 怎样用创建再自毁做便宜转账、怎样调时间戳磨难度。

## 官方三件事

1. **看见交易拒高 s 不是已经让预编译拒 / 看见交易拒高 s 不是已经让预编译拒 这份对象 is not already 已经让 ECRECOVER 拒高 s interchangeable，也不是已经 homestead vs already done bundled（234） interchangeable / 1347 hstead-notsig interchangeable / 1346 hstead-notfee interchangeable，也不是已经 EIP-2 high-s not already ECRECOVER-rejects / not already BIP-66 / not already EIP-155 正式三事 bundled（234 item 2 余量） interchangeable / 234 hstead item 2 interchangeable。**  
   官方把交易拒高 s 不是已经让预编译拒和已经让 ECRECOVER 拒高 s写成两件。看见交易拒高 s 不是已经让预编译拒，不是已经让 ECRECOVER 拒高 s。

2. **看见tx rejects high s is not ECRECOVER rejects / 看见交易拒高 s 不是已经让预编译拒 / 这份对象 is not already 已经是比特币 DER 低 s interchangeable，也不是已经 homestead vs already done bundled（234） interchangeable / 1347 hstead-notsig interchangeable / 1348 hstead-notfail interchangeable，也不是已经 比特币 DER 低 s interchangeable / 172 比特币 DER 低 s interchangeable。**  
   官方把tx rejects high s is not ECRECOVER rejects和已经是比特币 DER 低 s写成两件。看见tx rejects high s is not ECRECOVER rejects，不是已经是比特币 DER 低 s。

3. **看见交易拒高 s 不是已经让预编译拒 / 看见tx rejects high s is not ECRECOVER rejects / 这份对象 is not already 已经把链标识写进签名 interchangeable，也不是已经 homestead vs already done bundled（234） interchangeable / 1347 hstead-notsig interchangeable / 1346 hstead-notfee interchangeable，也不是已经 EIP-155 链标识 interchangeable / 161 EIP-155 链标识 interchangeable。**  
   官方把交易拒高 s 不是已经让预编译拒和已经把链标识写进签名写成两件。看见交易拒高 s 不是已经让预编译拒，不是已经把链标识写进签名。

栈怎么写、分隔符、例串是规范里的取值，本页不抄。不要另写 怎样用创建再自毁做便宜转账、怎样调时间戳磨难度。

## 官方为什么这样拆

- **交易拒高 s 不是已经让预编译拒：官方把交易验签和 ECRECOVER 预编译分开。**
- **看见交易拒高 s 不是已经是比特币 DER 低 s：172 是比特币，本页是以太坊交易。**
- **看见高 s 无效 不是已经把链标识写进签名：161 是 EIP-155，本页是可延展 s。**

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 已经让 ECRECOVER 拒高 s | 不是已经让 ECRECOVER 拒高 s | 不是已经比特币 DER 低 s（172） |
| 已经是比特币 DER 低 s | 不是已经是比特币 DER 低 s | 不是已经EIP-155 链标识（161） |
| 已经把链标识写进签名 | 不是已经把链标识写进签名 | 不是已经1346 hstead-notfee |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 EIP-2 high-s not already ECRECOVER-rejects / not already BIP-66 / not already EIP-155 正式四事（234 余量），必须分开是不是已经让 ECRECOVER 拒高 s、是不是已经是比特币 DER 低 s、是不是已经把链标识写进签名。可以跳过“看见 Homestead 就已经改了 `CREATE` / 就已经让预编译拒高 `s` / 就已经限制代码 / 就已经没有炸弹”。不要另写 怎样用创建再自毁做便宜转账、怎样调时间戳磨难度。234 Homestead 硬分叉四件事 bundled unbundling 在本页 item 2 续；续 [`worked-example-hstead-notfail-vs-bundled.md`](worked-example-hstead-notfail-vs-bundled.md)（不变量 1348 item 3）。

## 本页不抄

- 主网 / 测试网分叉高度、交易创建费常数、曲线阶一半、难度公式常数。
- 怎样用创建再自毁做便宜转账、怎样调时间戳磨难度。
