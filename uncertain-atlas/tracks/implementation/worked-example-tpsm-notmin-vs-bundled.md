# 例：看见MINIMALIF不是已经只是P2WSH策略不是已经只是P2WSH策略；看见MINIMALIF is not already only a P2WSH policy不是已经是不变量 191；看见MINIMALIF不是已经只是P2WSH策略不是已经是不变量 144

**层次**：实现 / 规范对象。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：Bitcoin [BIP-342](https://github.com/bitcoin/bips/blob/master/bip-0342.mediawiki)（Validation of Taproot Scripts）。  
**对应课文**：[L3.7](../../courses/level-03-bitcoin/L03-M07-segwit-soft-fork.md)。  
**不要写进**：`index/03` 共识行、M3.7、L3.7。本页是「BIP-342 minimalif not already p2wsh-policy-only / not already 191 / not already 144 正式三事（189 余量）/ not 1559 tpsm-notmin interchangeable / not 189 tapscript-vs-scriptpath bundled interchangeable」，不是 tapscript vs scriptpath bundled（189），也不是已经 Miniscript≠链上脚本（191），也不是已经 策略≠共识（144）。不要另写 怎样拼成功操作码、旧多重签改写、未知钥类型跳过验签。

## 官方三件事

1. **看见MINIMALIF不是已经只是P2WSH策略 / 看见MINIMALIF不是已经只是P2WSH策略 这份对象 is not already 已经只是P2WSH策略 interchangeable，也不是已经 tapscript vs scriptpath bundled（189） interchangeable / 1559 tpsm-notmin interchangeable / 1557 tpsm-notsem interchangeable，也不是已经 BIP-342 minimalif not already p2wsh-policy-only / not already 191 / not already 144 正式三事 bundled（189 item 3 余量） interchangeable / 189 tpsm item 3 interchangeable。**  
   官方把MINIMALIF不是已经只是P2WSH策略和已经只是P2WSH策略写成两件。看见MINIMALIF不是已经只是P2WSH策略，不是已经只是P2WSH策略。

2. **看见MINIMALIF is not already only a P2WSH policy / 看见MINIMALIF不是已经只是P2WSH策略 / 这份对象 is not already 已经是不变量 191 interchangeable，也不是已经 tapscript vs scriptpath bundled（189） interchangeable / 1559 tpsm-notmin interchangeable / 1558 tpsm-notdone interchangeable，也不是已经 Miniscript≠链上脚本 interchangeable / 191 Miniscript≠链上脚本 interchangeable。**  
   官方把MINIMALIF is not already only a P2WSH policy和已经是不变量 191写成两件。看见MINIMALIF is not already only a P2WSH policy，不是已经是不变量 191。

3. **看见MINIMALIF不是已经只是P2WSH策略 / 看见MINIMALIF is not already only a P2WSH policy / 这份对象 is not already 已经是不变量 144 interchangeable，也不是已经 tapscript vs scriptpath bundled（189） interchangeable / 1559 tpsm-notmin interchangeable / 1557 tpsm-notsem interchangeable，也不是已经 策略≠共识 interchangeable / 144 策略≠共识 interchangeable。**  
   官方把MINIMALIF不是已经只是P2WSH策略和已经是不变量 144写成两件。看见MINIMALIF不是已经只是P2WSH策略，不是已经是不变量 144。

栈怎么写、分隔符、例串是规范里的取值，本页不抄。不要另写 怎样拼成功操作码、旧多重签改写、未知钥类型跳过验签。

## 官方为什么这样拆

- **MINIMALIF不是已经只是P2WSH策略 interchangeable：官方写在 P2WSH 里 MINIMALIF 只是策略，本页把它写成共识。**
- **看见本页不是已经是不变量 191。**
- **看见本页不是已经是不变量 144。**

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 已经只是P2WSH策略 | 不是已经只是P2WSH策略 | 不是已经Miniscript≠链上脚本（191） |
| 已经是不变量 191 | 不是已经是不变量 191 | 不是已经策略≠共识（144） |
| 已经是不变量 144 | 不是已经是不变量 144 | 不是已经1557 tpsm-notsem |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 BIP-342 minimalif not already p2wsh-policy-only / not already 191 / not already 144 正式三事（189 余量），必须分开是不是已经只是P2WSH策略、是不是已经是不变量 191、是不是已经是不变量 144。可以跳过「看见成功操作码就已经执行完」。不要另写 怎样拼成功操作码、旧多重签改写、未知钥类型跳过验签。189 tapscript vs scriptpath bundled unbundling 在本页 item 3 完成；本页收束本批。下一份仍捆着的官方对象：dummy-vs-empty（264）。

## 本页不抄

- 操作码号、叶子版本、资源常数、例脚本。
- 怎样拼成功操作码、旧多重签改写、未知钥类型跳过验签。
