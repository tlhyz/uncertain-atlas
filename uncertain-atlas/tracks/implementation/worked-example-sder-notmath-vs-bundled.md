# 例：看见ECDSA数学上验得过不是已经是严格DER不是已经是严格DER；看见ECDSA verifying is not already being strict DER不是已经是不变量 144；看见ECDSA数学上验得过不是已经是严格DER不是已经 172 bundled

**层次**：实现 / 规范对象。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：Bitcoin [BIP-66](https://github.com/bitcoin/bips/blob/master/bip-0066.mediawiki)（Strict DER signatures）。  
**对应课文**：[L1.4](../../courses/level-01-crypto/L01-M04-canonical-encoding.md)。  
**不要写进**：`index/03` 共识行、M1.4、L1.4。本页是「BIP-66 ecdsa-valid not already strict-der / not already 144 / not already 172-bundled 正式三事（172 余量）/ not 1548 sder-notmath interchangeable / not 172 valid-vs-der bundled interchangeable」，不是 valid vs der bundled（172），也不是已经 策略≠共识（144），也不是已经 两实现同根（3）。不要另写 怎样把非DER改成DER、怎样造能过库过不了共识的签。

## 官方三件事

1. **看见ECDSA数学上验得过不是已经是严格DER / 看见ECDSA数学上验得过不是已经是严格DER 这份对象 is not already 已经是严格DER interchangeable，也不是已经 valid vs der bundled（172） interchangeable / 1548 sder-notmath interchangeable / 1549 sder-notlib interchangeable，也不是已经 BIP-66 ecdsa-valid not already strict-der / not already 144 / not already 172-bundled 正式三事 bundled（172 item 1 余量） interchangeable / 172 sder item 1 interchangeable。**  
   官方把ECDSA数学上验得过不是已经是严格DER和已经是严格DER写成两件。看见ECDSA数学上验得过不是已经是严格DER，不是已经是严格DER。

2. **看见ECDSA verifying is not already being strict DER / 看见ECDSA数学上验得过不是已经是严格DER / 这份对象 is not already 已经是不变量 144 interchangeable，也不是已经 valid vs der bundled（172） interchangeable / 1548 sder-notmath interchangeable / 1550 sder-notpol interchangeable，也不是已经 策略≠共识 interchangeable / 144 策略≠共识 interchangeable。**  
   官方把ECDSA verifying is not already being strict DER和已经是不变量 144写成两件。看见ECDSA verifying is not already being strict DER，不是已经是不变量 144。

3. **看见ECDSA数学上验得过不是已经是严格DER / 看见ECDSA verifying is not already being strict DER / 这份对象 is not already 已经 172 bundled interchangeable，也不是已经 valid vs der bundled（172） interchangeable / 1548 sder-notmath interchangeable / 1549 sder-notlib interchangeable，也不是已经 两实现同根 interchangeable / 3 两实现同根 interchangeable。**  
   官方把ECDSA数学上验得过不是已经是严格DER和已经 172 bundled写成两件。看见ECDSA数学上验得过不是已经是严格DER，不是已经 172 bundled。

栈怎么写、分隔符、例串是规范里的取值，本页不抄。不要另写 怎样把非DER改成DER、怎样造能过库过不了共识的签。

## 官方为什么这样拆

- **ECDSA数学上验得过不是已经是严格DER interchangeable：官方写交给 CHECKSIG 且会做 ECDSA 验证的签名必须是严格 DER，数学对上不是编码已经合法。**
- **看见本页不是已经是不变量 144。**
- **看见验过不是已经 172 bundled。**

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 已经是严格DER | 不是已经是严格DER | 不是已经策略≠共识（144） |
| 已经是不变量 144 | 不是已经是不变量 144 | 不是已经两实现同根（3） |
| 已经 172 bundled | 不是已经 172 bundled | 不是已经1549 sder-notlib |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 BIP-66 ecdsa-valid not already strict-der / not already 144 / not already 172-bundled 正式三事（172 余量），必须分开是不是已经是严格DER、是不是已经是不变量 144、是不是已经 172 bundled。可以跳过「看见库验过就已经合法」。不要另写 怎样把非DER改成DER、怎样造能过库过不了共识的签。172 valid vs der bundled unbundling 在本页 item 1 启动；续 [`worked-example-sder-notlib-vs-bundled.md`](worked-example-sder-notlib-vs-bundled.md)（不变量 1549 item 2）。

## 本页不抄

- 长度上下限、类型字节、激活票数、例脚本、库版本号。
- 怎样把非DER改成DER、怎样造能过库过不了共识的签。
