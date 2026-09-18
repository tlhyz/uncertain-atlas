# 例：看见 existing-multisig-habit is not already must-migrate interchangeable / not already path-rewritable interchangeable / not already settled interchangeable

**层次**：应用 / BIP-48 existing-multisig-habit not already must-migrate / not already path-rewritable / not already settled 正式三事（269 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：Bitcoin [BIP-48](https://github.com/bitcoin/bips/blob/master/bip-0048.mediawiki)（Deployed, Applications）。  
**对应课文**：[L1.4](../../courses/level-01-crypto/L01-M04-canonical-encoding.md)、[L3.6](../../courses/level-03-bitcoin/L03-M06-testing-and-culture.md)。  
**不要写进**：Ethereum 行、L5.1、03 共识、M5.4、L5.4。本页是「BIP-48 existing-multisig-habit not already must-migrate / not already path-rewritable / not already settled 正式三事（269 余量）/ not 1127 msig48-notmove interchangeable / not 269 script-type-vs-account bundled interchangeable」，不是多签层次 bundled（269），也不是 BIP32 compatible 就已经能互操作（1118），也不是用途层就已经能互操作（266）。不要另写怎样排序公钥或从种子扫多签。

## 官方三件事

1. **看见现有多签派生习惯 / 看见本页 这份栏 is not already 已经要搬家 interchangeable，也不是已经多签层次 bundled（269） interchangeable / 1127 msig48-notmove interchangeable / 1128 msig48-notacct interchangeable / 269 script item 2 type-not-account interchangeable，也不是已经 BIP-48 existing-multisig-habit not already must-migrate / not already path-rewritable / not already settled 正式三事 bundled（269 item 1 余量） interchangeable / 269 script item 1 interchangeable。**  
   官方写：本页要把业界已经在用的那套多签派生习惯写成标准，好让别的实现也能用。本页要维持现有真实用法。看见本页，不是已经要迁移 interchangeable——本页从 269 item 1 侧钉 not already must-migrate 单句。269 script-type vs account bundled unbundling 在本页 item 1 启动。

2. **看见写了标准 / 看见现有多签派生习惯 / 这份栏 is not already 已经可以换路径 interchangeable，也不是已经多签层次 bundled（269） interchangeable / 1127 msig48-notmove interchangeable / 269 script item 3 msig-not-unsorted interchangeable / 1129 msig48-notsort interchangeable，也不是已经 BIP32 compatible 就已经能互操作 interchangeable / 1118 purp43-notinterop interchangeable。**  
   官方把不做破坏性改动写成免得现有用户丢币。看见写了标准，不是已经可以换路径 interchangeable。本页钉 not already path-rewritable 单句。

3. **看见已经在用这套习惯的钱包 / 看见本页 / 这份栏 is not already 已经交差 interchangeable，也不是已经多签层次 bundled（269） interchangeable / 1127 msig48-notmove interchangeable / 1128 msig48-notacct interchangeable，也不是已经用途层就已经能互操作 interchangeable / 266 purpose interchangeable。**  
   官方把已经在用这套习惯的钱包不必为了合规再改写成独立限制。看见已经在用这套习惯的钱包，不是已经交差 interchangeable。269 script-type vs account bundled unbundling 在本页 item 1 启动。

脚本类型取值、例路径、怎样排序公钥是规范里的取值或另一页的事，本页不抄。

## 官方为什么这样拆

- **BIP-48 existing-multisig-habit not already must-migrate ≠ 已经要搬家 interchangeable：** 官方把维持现有真实用法写成免得现有用户丢币。
- **看见写了标准 not already path-rewritable ≠ 已经可以换路径 interchangeable：** 官方把不做破坏性改动和已经可以换路径分开。
- **看见已经在用这套习惯的钱包 not already settled ≠ 已经交差 interchangeable：** 官方把已经在用就不必再改写成独立限制；269 script-type vs account bundled unbundling 在本页 item 1 启动。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 现有多签派生习惯 / 看见本页 | 不是已经要搬家 | 不是 BIP32 compatible 就已经能互操作（1118） |
| 看见写了标准 | 不是已经可以换路径 | 不是用途层就已经能互操作（266） |
| 看见已经在用这套习惯的钱包 | 不是已经交差 | 不是脚本类型层就已经是账户层（1128） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 BIP-48 existing-multisig-habit not already must-migrate / not already path-rewritable / not already settled 正式三事（269 余量），必须分开是不是已经要搬家、是不是已经可以换路径、是不是已经交差。可以跳过「看见多签路径就已经是账户发现」。不要另写怎样排序公钥或从种子扫多签。269 script-type vs account bundled unbundling 在本页 item 1 启动；续 [`worked-example-msig48-notacct-vs-bundled.md`](worked-example-msig48-notacct-vs-bundled.md)（不变量 1128 item 2）。

## 本页不抄

- 用途号、脚本类型取值、例路径、网络编号。
- 怎样按字典序排公钥、怎样从种子扫多签地址。
- 多签层次 bundled。那是不变量 269。
- BIP32 compatible 就已经能互操作。那是不变量 1118。
