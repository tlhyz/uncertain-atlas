# 例：看见脚本各走各的路径不是已经是多签该有的树；看见 45 那种只认一种脚本不是已经是本页；看见单签那套拆法不是已经交差

**层次**：应用 / 规范对象。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：Bitcoin [BIP-87](https://github.com/bitcoin/bips/blob/master/bip-0087.mediawiki)（Complete, Applications, Specification）。  
**对应课文**：[L1.4](../../courses/level-01-crypto/L01-M04-canonical-encoding.md)、[L3.6](../../courses/level-03-bitcoin/L03-M06-testing-and-culture.md)。  
**不要写进**：Ethereum 行、L5.1、03 共识、M5.4、L5.4。本页是「BIP-87 per-script-path not already the-multisig-tree / not already no-descriptor / not already settled 正式三事（285 余量）/ not 1175 mpath87-nottree interchangeable / not 285 multisig-path-vs-script bundled interchangeable」，不是多签派生层次 bundled（285），也不是脚本类型层就已经是账户层（1127），也不是联合签名人就已经发现完（1130）。不要另写怎样加账户号。

## 官方三件事

1. **看见 44 / 49 / 84 那种脚本各走各的路径 / 看见 45 那种只认一种脚本 这份树 is not already 已经是多签该有的树 interchangeable，也不是已经多签派生层次 bundled（285） interchangeable / 1175 mpath87-nottree interchangeable / 1176 mpath87-notneed interchangeable / 285 mpath item 2 type-not-need interchangeable，也不是已经 BIP-87 per-script-path not already the-multisig-tree / not already no-descriptor / not already settled 正式三事 bundled（285 item 1 余量） interchangeable / 285 mpath item 1 interchangeable。**  
   官方写：单签按脚本拆路径，备份时只靠私钥信息就能找回。多签还要所有共同签名人的公钥。有了描述符之后，这种按脚本拆路径对多签是多余的。看见单签那套拆法，不是已经是本页。

2. **看见 45 那种只认一种脚本 / 看见脚本各走各的路径 / 这份树 is not already 已经不必再带描述符 interchangeable，也不是已经多签派生层次 bundled（285） interchangeable / 1175 mpath87-nottree interchangeable / 285 mpath item 3 seed-not-enough interchangeable / 1177 mpath87-notseed interchangeable，也不是已经联合签名人就已经发现完 interchangeable / 1130 cos45-notdone interchangeable。**  
   官方另写：45 那种树不必要地只认一种脚本；在送给协调人之前先按公钥排序再定路径，也是多余的，因为描述符自己能定顺序或按字典序排。看见 45，不是已经是本页，也不是已经不必再带描述符。

3. **看见单签那套拆法 / 看见脚本各走各的路径 / 这份树 is not already 已经交差 interchangeable，也不是已经多签派生层次 bundled（285） interchangeable / 1175 mpath87-nottree interchangeable / 1176 mpath87-notneed interchangeable，也不是已经脚本类型层就已经是账户层 interchangeable / 1127 msig48-notacct interchangeable。**  
   官方把单签那套拆法和 45 那种只认一种脚本写成对多签多余。看见单签那套拆法，不是已经交差。

用途号、间隔上限、例路径、例描述符是规范里的取值或做法，本页不抄。

## 官方为什么这样拆

- **脚本各走各的路径 不是已经是多签该有的树：** 官方把单签那套拆法写成对多签多余。
- **45 那种只认一种脚本 不是已经不必再带描述符：** 官方把只认一种脚本和先排序再定路径写成多余。
- **单签那套拆法 不是已经交差：** 官方把拆法和 45 写成两句。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 多签树 | 不是已经是多签该有的树 | 不是已经是 48 那种账户层（1127） |
| 描述符 | 不是已经不必再带描述符 | 不是已经发现完（1130） |
| 交差 | 不是已经交差 | 不是已经必要（1176） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 BIP-87 per-script-path not already the-multisig-tree / not already no-descriptor / not already settled 正式三事（285 余量），必须分开是不是已经是多签该有的树、是不是已经不必再带描述符、是不是已经交差。可以跳过「看见多签就已经该按脚本拆路径」。不要另写怎样加账户号。285 multisig path vs script bundled unbundling 在本页 item 1 启动；续 [`worked-example-mpath87-notneed-vs-bundled.md`](worked-example-mpath87-notneed-vs-bundled.md)（不变量 1176 item 2）。

## 本页不抄

- 用途号、间隔上限、例路径、例描述符。
- 怎样加账户号、怎样展开多路径、怎样按间隔停扫。
