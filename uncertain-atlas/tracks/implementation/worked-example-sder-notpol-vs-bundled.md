# 例：看见转发策略已经要DER不是共识已经要不是共识已经要；看见relay already requiring DER is not already consensus requiring it不是已经是不变量 144；看见转发策略已经要DER不是共识已经要不是已经是不变量 171

**层次**：实现 / 规范对象。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：Bitcoin [BIP-66](https://github.com/bitcoin/bips/blob/master/bip-0066.mediawiki)（Strict DER signatures）。  
**对应课文**：[L1.4](../../courses/level-01-crypto/L01-M04-canonical-encoding.md)。  
**不要写进**：`index/03` 共识行、M1.4、L1.4。本页是「BIP-66 relay-der not already consensus-der / not already 144 / not already 171 正式三事（172 余量）/ not 1550 sder-notpol interchangeable / not 172 valid-vs-der bundled interchangeable」，不是 valid vs der bundled（172），也不是已经 策略≠共识（144），也不是已经 版本位≠已激活（171）。不要另写 怎样把非DER改成DER、怎样造能过库过不了共识的签。

## 官方三件事

1. **看见转发策略已经要DER不是共识已经要 / 看见转发策略已经要DER不是共识已经要 这份对象 is not already 共识已经要 interchangeable，也不是已经 valid vs der bundled（172） interchangeable / 1550 sder-notpol interchangeable / 1548 sder-notmath interchangeable，也不是已经 BIP-66 relay-der not already consensus-der / not already 144 / not already 171 正式三事 bundled（172 item 3 余量） interchangeable / 172 sder item 3 interchangeable。**  
   官方把转发策略已经要DER不是共识已经要和共识已经要写成两件。看见转发策略已经要DER不是共识已经要，不是共识已经要。

2. **看见relay already requiring DER is not already consensus requiring it / 看见转发策略已经要DER不是共识已经要 / 这份对象 is not already 已经是不变量 144 interchangeable，也不是已经 valid vs der bundled（172） interchangeable / 1550 sder-notpol interchangeable / 1549 sder-notlib interchangeable，也不是已经 策略≠共识 interchangeable / 144 策略≠共识 interchangeable。**  
   官方把relay already requiring DER is not already consensus requiring it和已经是不变量 144写成两件。看见relay already requiring DER is not already consensus requiring it，不是已经是不变量 144。

3. **看见转发策略已经要DER不是共识已经要 / 看见relay already requiring DER is not already consensus requiring it / 这份对象 is not already 已经是不变量 171 interchangeable，也不是已经 valid vs der bundled（172） interchangeable / 1550 sder-notpol interchangeable / 1548 sder-notmath interchangeable，也不是已经 版本位≠已激活 interchangeable / 171 版本位≠已激活 interchangeable。**  
   官方把转发策略已经要DER不是共识已经要和已经是不变量 171写成两件。看见转发策略已经要DER不是共识已经要，不是已经是不变量 171。

栈怎么写、分隔符、例串是规范里的取值，本页不抄。不要另写 怎样把非DER改成DER、怎样造能过库过不了共识的签。

## 官方为什么这样拆

- **转发策略已经要DER不是共识已经要 interchangeable：官方写转发策略可以早就只要 DER，那不是共识已经只要 DER。**
- **看见本页不是已经是不变量 144。**
- **看见本页不是已经是不变量 171。**

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 共识已经要 | 不是共识已经要 | 不是已经策略≠共识（144） |
| 已经是不变量 144 | 不是已经是不变量 144 | 不是已经版本位≠已激活（171） |
| 已经是不变量 171 | 不是已经是不变量 171 | 不是已经1548 sder-notmath |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 BIP-66 relay-der not already consensus-der / not already 144 / not already 171 正式三事（172 余量），必须分开是不是共识已经要、是不是已经是不变量 144、是不是已经是不变量 171。可以跳过「看见库验过就已经合法」。不要另写 怎样把非DER改成DER、怎样造能过库过不了共识的签。172 valid vs der bundled unbundling 在本页 item 3 完成；本页收束本批。下一份仍捆着的官方对象：txid-vs-wtxid（152）。

## 本页不抄

- 长度上下限、类型字节、激活票数、例脚本、库版本号。
- 怎样把非DER改成DER、怎样造能过库过不了共识的签。
