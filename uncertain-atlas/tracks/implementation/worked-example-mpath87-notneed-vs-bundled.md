# 例：看见路径里的脚本类型不是已经必要；看见 48 那种多插一层不是已经不必再带描述符；看见路径里写了脚本类型不是已经交差

**层次**：应用 / 规范对象。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：Bitcoin [BIP-87](https://github.com/bitcoin/bips/blob/master/bip-0087.mediawiki)（Complete, Applications, Specification）。  
**对应课文**：[L1.4](../../courses/level-01-crypto/L01-M04-canonical-encoding.md)、[L3.6](../../courses/level-03-bitcoin/L03-M06-testing-and-culture.md)。  
**不要写进**：Ethereum 行、L5.1、03 共识、M5.4、L5.4。本页是「BIP-87 script-type-in-path not already necessary / not already no-descriptor / not already settled 正式三事（285 余量）/ not 1176 mpath87-notneed interchangeable / not 285 multisig-path-vs-script bundled interchangeable」，不是多签派生层次 bundled（285），也不是脚本类型层就已经是账户层（1127），也不是钱包策略就已经是一条描述符（1160）。不要另写怎样加账户号。

## 官方三件事

1. **看见路径里的脚本类型 / 看见 48 那种多插一层 这份树 is not already 已经必要 interchangeable，也不是已经多签派生层次 bundled（285） interchangeable / 1176 mpath87-notneed interchangeable / 1175 mpath87-nottree interchangeable / 285 mpath item 1 split-not-tree interchangeable，也不是已经 BIP-87 script-type-in-path not already necessary / not already no-descriptor / not already settled 正式三事 bundled（285 item 2 余量） interchangeable / 285 mpath item 2 interchangeable。**  
   官方写：不该把钥和脚本混在同一层。钱包先造与脚本类型无关的扩展钥，描述符再告诉钱包该看哪一种多签输出。看见路径里写了脚本类型，不是已经是本页。

2. **看见 48 那种多插一层 / 看见路径里的脚本类型 / 这份树 is not already 已经不必再带描述符 interchangeable，也不是已经多签派生层次 bundled（285） interchangeable / 1176 mpath87-notneed interchangeable / 285 mpath item 3 seed-not-enough interchangeable / 1177 mpath87-notseed interchangeable，也不是已经脚本类型层就已经是账户层 interchangeable / 1127 msig48-notacct interchangeable。**  
   官方另写：48 把脚本类型插进路径是不必要的，因为描述符已经定了脚本；那样做仍要维护一份多余的脚本类型名单。看见 48 那一层，不是已经不必再带描述符。

3. **看见路径里写了脚本类型 / 看见路径里的脚本类型 / 这份树 is not already 已经交差 interchangeable，也不是已经多签派生层次 bundled（285） interchangeable / 1176 mpath87-notneed interchangeable / 1175 mpath87-nottree interchangeable，也不是已经钱包策略就已经是一条描述符 interchangeable / 1160 pol388-notdesc interchangeable。**  
   官方把脚本交给描述符，不让它和钥混在同一层。看见路径里写了脚本类型，不是已经交差。

用途号、间隔上限、例路径、例描述符是规范里的取值或做法，本页不抄。

## 官方为什么这样拆

- **路径里的脚本类型 不是已经必要：** 官方把钥和脚本写成不该混层。
- **48 那种多插一层 不是已经不必再带描述符：** 官方把插进路径写成仍要维护名单。
- **路径里写了脚本类型 不是已经交差：** 官方把混层和名单写成两句。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 必要 | 不是已经必要 | 不是已经是账户层（1127） |
| 描述符 | 不是已经不必再带描述符 | 不是已经是一条策略（1160） |
| 交差 | 不是已经交差 | 不是已经是多签树（1175） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 BIP-87 script-type-in-path not already necessary / not already no-descriptor / not already settled 正式三事（285 余量），必须分开是不是已经必要、是不是已经不必再带描述符、是不是已经交差。可以跳过「看见多签就已经该按脚本拆路径」。不要另写怎样加账户号。285 multisig path vs script bundled unbundling 在本页 item 2 续；续 [`worked-example-mpath87-notseed-vs-bundled.md`](worked-example-mpath87-notseed-vs-bundled.md)（不变量 1177 item 3）。

## 本页不抄

- 用途号、间隔上限、例路径、例描述符。
- 怎样加账户号、怎样展开多路径、怎样按间隔停扫。
