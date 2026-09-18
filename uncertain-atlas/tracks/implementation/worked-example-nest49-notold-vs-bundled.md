# 例：看见 same-BIP44-account is not already recover-nested interchangeable / not already same-keys-rewritten interchangeable / not already settled interchangeable

**层次**：应用 / BIP-49 same-BIP44-account not already recover-nested / not already same-keys-rewritten / not already settled 正式三事（268 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：Bitcoin [BIP-49](https://github.com/bitcoin/bips/blob/master/bip-0049.mediawiki)（Deployed, Applications）。  
**对应课文**：[L1.4](../../courses/level-01-crypto/L01-M04-canonical-encoding.md)、[L3.6](../../courses/level-03-bitcoin/L03-M06-testing-and-culture.md)。  
**不要写进**：Ethereum 行、L5.1、03 共识、M5.4、L5.4。本页是「BIP-49 same-BIP44-account not already recover-nested / not already same-keys-rewritten / not already settled 正式三事（268 余量）/ not 1124 nest49-notold interchangeable / not 268 nested-vs-same-account bundled interchangeable」，不是嵌套隔离见证挂在旧账户上 bundled（268），也不是扩展公钥就已经能花（182），也不是同一份种子就已经是同一条币（1115）。不要另写怎样套脚本或从种子扫嵌套地址。

## 官方三件事

1. **看见同一套 BIP44 账户 / 同一批钥再加隔离见证写法 这份栏 is not already 已经能找回这些币 interchangeable，也不是已经嵌套挂旧账户 bundled（268） interchangeable / 1124 nest49-notold interchangeable / 1125 nest49-notback interchangeable / 268 nested item 2 dedicated-not-compat interchangeable，也不是已经 BIP-49 same-BIP44-account not already recover-nested / not already same-keys-rewritten / not already settled 正式三事 bundled（268 item 1 余量） interchangeable / 268 nested item 1 interchangeable。**  
   官方写：已经会 BIP44 的钱包大致有两条路。一条是继续用原来的账户，只是再给同一批钥或同一棵账户根加上隔离见证编码。看见旧账户还在，不是嵌套隔离见证已经找回 interchangeable——本页从 268 item 1 侧钉 not already recover-nested 单句。268 nested vs same-account bundled unbundling 在本页 item 1 启动。

2. **看见同一批钥能编出付款脚本哈希地址 / 看见同一套 BIP44 账户 / 这份栏 is not already 已经看见那些币 interchangeable，也不是已经嵌套挂旧账户 bundled（268） interchangeable / 1124 nest49-notold interchangeable / 268 nested item 3 appeared-not-complete interchangeable / 1126 nest49-notbal interchangeable，也不是已经扩展公钥就已经能花 interchangeable / 182 xpub interchangeable。**  
   官方把同一批钥能编出付款脚本哈希地址和已经看见那些币分开。看见同一批钥能编出付款脚本哈希地址，不是已经看见那些币 interchangeable。本页钉 not already same-keys-rewritten 单句。

3. **看见把本页兼容的种子导进不会本页的钱包 / 看见同一套 BIP44 账户 / 这份栏 is not already 已经交差 interchangeable，也不是已经嵌套挂旧账户 bundled（268） interchangeable / 1124 nest49-notold interchangeable / 1125 nest49-notback interchangeable，也不是已经同一份种子就已经是同一条币 interchangeable / 1115 acc44-notcoin interchangeable。**  
   官方把账户也许会出现、也可能漏掉一部分未花输出写成第一条路的共同坏处。看见把本页兼容的种子导进不会本页的钱包，不是已经交差 interchangeable。268 nested vs same-account bundled unbundling 在本页 item 1 启动。

用途号、扩展钥前缀、脚本套法、测试向量是规范里的取值，本页不抄。

## 官方为什么这样拆

- **BIP-49 same-BIP44-account not already recover-nested ≠ 已经能找回这些币 interchangeable：** 官方把旧账户再加编码写成可能漏未花输出。
- **看见同一批钥能编出付款脚本哈希地址 not already same-keys-rewritten ≠ 已经看见那些币 interchangeable：** 官方把同一批钥能编出地址和已经看见那些币分开。
- **看见把本页兼容的种子导进不会本页的钱包 not already settled ≠ 已经交差 interchangeable：** 官方把账户出现但漏未花输出写成第一条路的共同坏处；268 nested vs same-account bundled unbundling 在本页 item 1 启动。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 同一套 BIP44 账户 / 同一批钥再加隔离见证写法 | 不是已经能找回这些币 | 不是扩展公钥就已经能花（182） |
| 看见同一批钥能编出付款脚本哈希地址 | 不是已经看见那些币 | 不是同一份种子就已经是同一条币（1115） |
| 看见把本页兼容的种子导进不会本页的钱包 | 不是已经交差 | 不是专用账户就已经向后兼容（1125） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 BIP-49 same-BIP44-account not already recover-nested / not already same-keys-rewritten / not already settled 正式三事（268 余量），必须分开是不是已经能找回这些币、是不是已经看见那些币、是不是已经交差。可以跳过「看见旧账户还在就已经找回新脚本」。不要另写怎样套脚本或从种子扫嵌套地址。268 nested vs same-account bundled unbundling 在本页 item 1 启动；续 [`worked-example-nest49-notback-vs-bundled.md`](worked-example-nest49-notback-vs-bundled.md)（不变量 1125 item 2）。

## 本页不抄

- 用途号、扩展钥版本魔数、脚本套法、测试向量、例地址。
- 怎样从同一批钥编出嵌套地址、怎样扫未花输出。
- 嵌套隔离见证挂在旧账户上 bundled。那是不变量 268。
- 扩展公钥就已经能花。那是不变量 182。
