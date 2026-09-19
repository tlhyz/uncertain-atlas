# 例：看见库接受某种变形不是共识已经接受不是共识已经接受；看见a library accepting a variant is not already consensus accepting it不是已经是不变量 3；看见库接受某种变形不是共识已经接受不是已经是不变量 152

**层次**：实现 / 规范对象。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：Bitcoin [BIP-66](https://github.com/bitcoin/bips/blob/master/bip-0066.mediawiki)（Strict DER signatures）。  
**对应课文**：[L1.4](../../courses/level-01-crypto/L01-M04-canonical-encoding.md)。  
**不要写进**：`index/03` 共识行、M1.4、L1.4。本页是「BIP-66 library-accept not already consensus-accept / not already 3 / not already 152 正式三事（172 余量）/ not 1549 sder-notlib interchangeable / not 172 valid-vs-der bundled interchangeable」，不是 valid vs der bundled（172），也不是已经 两实现同根（3），也不是已经 txid≠wtxid（152）。不要另写 怎样把非DER改成DER、怎样造能过库过不了共识的签。

## 官方三件事

1. **看见库接受某种变形不是共识已经接受 / 看见库接受某种变形不是共识已经接受 这份对象 is not already 共识已经接受 interchangeable，也不是已经 valid vs der bundled（172） interchangeable / 1549 sder-notlib interchangeable / 1548 sder-notmath interchangeable，也不是已经 BIP-66 library-accept not already consensus-accept / not already 3 / not already 152 正式三事 bundled（172 item 2 余量） interchangeable / 172 sder item 2 interchangeable。**  
   官方把库接受某种变形不是共识已经接受和共识已经接受写成两件。看见库接受某种变形不是共识已经接受，不是共识已经接受。

2. **看见a library accepting a variant is not already consensus accepting it / 看见库接受某种变形不是共识已经接受 / 这份对象 is not already 已经是不变量 3 interchangeable，也不是已经 valid vs der bundled（172） interchangeable / 1549 sder-notlib interchangeable / 1550 sder-notpol interchangeable，也不是已经 两实现同根 interchangeable / 3 两实现同根 interchangeable。**  
   官方把a library accepting a variant is not already consensus accepting it和已经是不变量 3写成两件。看见a library accepting a variant is not already consensus accepting it，不是已经是不变量 3。

3. **看见库接受某种变形不是共识已经接受 / 看见a library accepting a variant is not already consensus accepting it / 这份对象 is not already 已经是不变量 152 interchangeable，也不是已经 valid vs der bundled（172） interchangeable / 1549 sder-notlib interchangeable / 1548 sder-notmath interchangeable，也不是已经 txid≠wtxid interchangeable / 152 txid≠wtxid interchangeable。**  
   官方把库接受某种变形不是共识已经接受和已经是不变量 152写成两件。看见库接受某种变形不是共识已经接受，不是已经是不变量 152。

栈怎么写、分隔符、例串是规范里的取值，本页不抄。不要另写 怎样把非DER改成DER、怎样造能过库过不了共识的签。

## 官方为什么这样拆

- **库接受某种变形不是共识已经接受 interchangeable：官方写参考实现曾靠 OpenSSL，库不是共识合法集。**
- **看见本页不是已经是不变量 3。**
- **看见本页不是已经是不变量 152。**

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 共识已经接受 | 不是共识已经接受 | 不是已经两实现同根（3） |
| 已经是不变量 3 | 不是已经是不变量 3 | 不是已经txid≠wtxid（152） |
| 已经是不变量 152 | 不是已经是不变量 152 | 不是已经1548 sder-notmath |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 BIP-66 library-accept not already consensus-accept / not already 3 / not already 152 正式三事（172 余量），必须分开是不是共识已经接受、是不是已经是不变量 3、是不是已经是不变量 152。可以跳过「看见库验过就已经合法」。不要另写 怎样把非DER改成DER、怎样造能过库过不了共识的签。172 valid vs der bundled unbundling 在本页 item 2 续；续 [`worked-example-sder-notpol-vs-bundled.md`](worked-example-sder-notpol-vs-bundled.md)（不变量 1550 item 3）。

## 本页不抄

- 长度上下限、类型字节、激活票数、例脚本、库版本号。
- 怎样把非DER改成DER、怎样造能过库过不了共识的签。
