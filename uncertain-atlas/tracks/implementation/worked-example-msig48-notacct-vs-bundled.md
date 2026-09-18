# 例：看见 script-type-layer is not already account-layer interchangeable / not already all-future-scripts-fixed interchangeable / not already settled interchangeable

**层次**：应用 / BIP-48 script-type-layer not already account-layer / not already all-future-scripts-fixed / not already settled 正式三事（269 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：Bitcoin [BIP-48](https://github.com/bitcoin/bips/blob/master/bip-0048.mediawiki)（Deployed, Applications）。  
**对应课文**：[L1.4](../../courses/level-01-crypto/L01-M04-canonical-encoding.md)、[L3.6](../../courses/level-03-bitcoin/L03-M06-testing-and-culture.md)。  
**不要写进**：Ethereum 行、L5.1、03 共识、M5.4、L5.4。本页是「BIP-48 script-type-layer not already account-layer / not already all-future-scripts-fixed / not already settled 正式三事（269 余量）/ not 1128 msig48-notacct interchangeable / not 269 script-type-vs-account bundled interchangeable」，不是多签层次 bundled（269），也不是余额为零就已经发现完（1117），也不是账户出现了就已经齐（1126）。不要另写怎样排序公钥或从种子扫多签。

## 官方三件事

1. **看见脚本类型层 / 看见账户层 这份栏 is not already 已经是同一层 interchangeable，也不是已经多签层次 bundled（269） interchangeable / 1128 msig48-notacct interchangeable / 1127 msig48-notmove interchangeable / 269 script item 1 habit-not-migrate interchangeable，也不是已经 BIP-48 script-type-layer not already account-layer / not already all-future-scripts-fixed / not already settled 正式三事 bundled（269 item 2 余量） interchangeable / 269 script item 2 interchangeable。**  
   官方写：这一层把钥空间按脚本类型拆开。看见账户号，不是已经选定脚本类型 interchangeable——本页从 269 item 2 侧钉 not already account-layer 单句。269 script-type vs account bundled unbundling 在本页 item 2 续。

2. **看见本页 / 看见脚本类型层 / 这份栏 is not already 已经把以后的脚本类型都写死 interchangeable，也不是已经多签层次 bundled（269） interchangeable / 1128 msig48-notacct interchangeable / 269 script item 3 msig-not-unsorted interchangeable / 1129 msig48-notsort interchangeable，也不是已经余额为零就已经发现完 interchangeable / 1117 acc44-notdone interchangeable。**  
   官方把给以后的脚本类型留向前兼容写成不必每来一种脚本再另写一份 BIP。看见本页，不是已经把以后的脚本类型都写死 interchangeable。本页钉 not already all-future-scripts-fixed 单句。

3. **看见账户号 / 看见脚本类型层 / 这份栏 is not already 已经交差 interchangeable，也不是已经多签层次 bundled（269） interchangeable / 1128 msig48-notacct interchangeable / 1127 msig48-notmove interchangeable，也不是已经账户出现了就已经齐 interchangeable / 1126 nest49-notbal interchangeable。**  
   官方把眼下只覆盖原生隔离见证脚本哈希和嵌套隔离见证脚本哈希写成取值，不是已经交差。看见账户号，不是已经交差 interchangeable。269 script-type vs account bundled unbundling 在本页 item 2 续。

脚本类型取值、例路径、怎样排序公钥是规范里的取值或另一页的事，本页不抄。

## 官方为什么这样拆

- **BIP-48 script-type-layer not already account-layer ≠ 已经是同一层 interchangeable：** 官方另开一层，好给以后的脚本类型往下加。
- **看见本页 not already all-future-scripts-fixed ≠ 已经把以后的脚本类型都写死 interchangeable：** 官方把向前兼容写成可以接着往下加。
- **看见账户号 not already settled ≠ 已经交差 interchangeable：** 官方把账户号和已经选定脚本类型分开；269 script-type vs account bundled unbundling 在本页 item 2 续。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 脚本类型层 / 账户层 | 不是已经是同一层 | 不是余额为零就已经发现完（1117） |
| 看见本页 | 不是已经把以后的脚本类型都写死 | 不是账户出现了就已经齐（1126） |
| 看见账户号 | 不是已经交差 | 不是本页多签就已经不排序（1129） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 BIP-48 script-type-layer not already account-layer / not already all-future-scripts-fixed / not already settled 正式三事（269 余量），必须分开是不是已经是同一层、是不是已经把以后的脚本类型都写死、是不是已经交差。可以跳过「看见多签路径就已经是账户发现」。不要另写怎样排序公钥或从种子扫多签。269 script-type vs account bundled unbundling 在本页 item 2 续；续 [`worked-example-msig48-notsort-vs-bundled.md`](worked-example-msig48-notsort-vs-bundled.md)（不变量 1129 item 3）。

## 本页不抄

- 用途号、脚本类型取值、例路径、网络编号。
- 怎样按字典序排公钥、怎样从种子扫多签地址。
- 多签层次 bundled。那是不变量 269。
- 余额为零就已经发现完。那是不变量 1117。
