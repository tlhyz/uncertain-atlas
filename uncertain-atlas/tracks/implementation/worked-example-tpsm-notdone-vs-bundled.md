# 例：看见遇见成功操作码不是已经执行完不是已经执行完；看见encountering a success opcode is not already execution having completed不是已经安全升级；看见遇见成功操作码不是已经执行完不是已经 189 bundled

**层次**：实现 / 规范对象。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：Bitcoin [BIP-342](https://github.com/bitcoin/bips/blob/master/bip-0342.mediawiki)（Validation of Taproot Scripts）。  
**对应课文**：[L3.7](../../courses/level-03-bitcoin/L03-M07-segwit-soft-fork.md)。  
**不要写进**：`index/03` 共识行、M3.7、L3.7。本页是「BIP-342 success-opcode not already executed / not already safe-upgrade / not already 189-bundled 正式三事（189 余量）/ not 1558 tpsm-notdone interchangeable / not 189 tapscript-vs-scriptpath bundled interchangeable」，不是 tapscript vs scriptpath bundled（189），也不是已经 钥匙路径≠揭树（153），也不是已经 Miniscript≠链上脚本（191）。不要另写 怎样拼成功操作码、旧多重签改写、未知钥类型跳过验签。

## 官方三件事

1. **看见遇见成功操作码不是已经执行完 / 看见遇见成功操作码不是已经执行完 这份对象 is not already 已经执行完 interchangeable，也不是已经 tapscript vs scriptpath bundled（189） interchangeable / 1558 tpsm-notdone interchangeable / 1557 tpsm-notsem interchangeable，也不是已经 BIP-342 success-opcode not already executed / not already safe-upgrade / not already 189-bundled 正式三事 bundled（189 item 2 余量） interchangeable / 189 tpsm item 2 interchangeable。**  
   官方把遇见成功操作码不是已经执行完和已经执行完写成两件。看见遇见成功操作码不是已经执行完，不是已经执行完。

2. **看见encountering a success opcode is not already execution having completed / 看见遇见成功操作码不是已经执行完 / 这份对象 is not already 已经安全升级 interchangeable，也不是已经 tapscript vs scriptpath bundled（189） interchangeable / 1558 tpsm-notdone interchangeable / 1559 tpsm-notmin interchangeable，也不是已经 钥匙路径≠揭树 interchangeable / 153 钥匙路径≠揭树 interchangeable。**  
   官方把encountering a success opcode is not already execution having completed和已经安全升级写成两件。看见encountering a success opcode is not already execution having completed，不是已经安全升级。

3. **看见遇见成功操作码不是已经执行完 / 看见encountering a success opcode is not already execution having completed / 这份对象 is not already 已经 189 bundled interchangeable，也不是已经 tapscript vs scriptpath bundled（189） interchangeable / 1558 tpsm-notdone interchangeable / 1557 tpsm-notsem interchangeable，也不是已经 Miniscript≠链上脚本 interchangeable / 191 Miniscript≠链上脚本 interchangeable。**  
   官方把遇见成功操作码不是已经执行完和已经 189 bundled写成两件。看见遇见成功操作码不是已经执行完，不是已经 189 bundled。

栈怎么写、分隔符、例串是规范里的取值，本页不抄。不要另写 怎样拼成功操作码、旧多重签改写、未知钥类型跳过验签。

## 官方为什么这样拆

- **遇见成功操作码不是已经执行完 interchangeable：官方写解码时只要遇见成功操作码，验证直接成功，后面的规则都不跑。**
- **看见成功操作码不是已经安全升级。**
- **看见本页不是已经 189 bundled。**

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 已经执行完 | 不是已经执行完 | 不是已经钥匙路径≠揭树（153） |
| 已经安全升级 | 不是已经安全升级 | 不是已经Miniscript≠链上脚本（191） |
| 已经 189 bundled | 不是已经 189 bundled | 不是已经1557 tpsm-notsem |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 BIP-342 success-opcode not already executed / not already safe-upgrade / not already 189-bundled 正式三事（189 余量），必须分开是不是已经执行完、是不是已经安全升级、是不是已经 189 bundled。可以跳过「看见成功操作码就已经执行完」。不要另写 怎样拼成功操作码、旧多重签改写、未知钥类型跳过验签。189 tapscript vs scriptpath bundled unbundling 在本页 item 2 续；续 [`worked-example-tpsm-notmin-vs-bundled.md`](worked-example-tpsm-notmin-vs-bundled.md)（不变量 1559 item 3）。

## 本页不抄

- 操作码号、叶子版本、资源常数、例脚本。
- 怎样拼成功操作码、旧多重签改写、未知钥类型跳过验签。
