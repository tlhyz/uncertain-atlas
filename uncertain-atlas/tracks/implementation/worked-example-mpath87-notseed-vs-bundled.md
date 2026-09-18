# 例：看见主种子不是已经够找回；看见这份不按脚本拆的树不是已经给单签用；看见主种子不是已经交差

**层次**：应用 / 规范对象。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：Bitcoin [BIP-87](https://github.com/bitcoin/bips/blob/master/bip-0087.mediawiki)（Complete, Applications, Specification）。  
**对应课文**：[L1.4](../../courses/level-01-crypto/L01-M04-canonical-encoding.md)、[L3.6](../../courses/level-03-bitcoin/L03-M06-testing-and-culture.md)。  
**不要写进**：Ethereum 行、L5.1、03 共识、M5.4、L5.4。本页是「BIP-87 master-seed not already enough-to-recover / not already singlesig-default / not already settled 正式三事（285 余量）/ not 1177 mpath87-notseed interchangeable / not 285 multisig-path-vs-script bundled interchangeable」，不是多签派生层次 bundled（285），也不是描述符就已经是地址（184），也不是账户就已经发现完（1116）。不要另写怎样加账户号。

## 官方三件事

1. **看见主种子 / 看见这份不按脚本拆的树 这份树 is not already 已经够找回 interchangeable，也不是已经多签派生层次 bundled（285） interchangeable / 1177 mpath87-notseed interchangeable / 1175 mpath87-nottree interchangeable / 285 mpath item 1 split-not-tree interchangeable，也不是已经 BIP-87 master-seed not already enough-to-recover / not already singlesig-default / not already settled 正式三事 bundled（285 item 3 余量） interchangeable / 285 mpath item 3 interchangeable。**  
   官方另写：按本页做的是描述符钱包，共同签名人必须同时备份私钥信息和描述符，以后才能正确找回。看见主种子，不是已经够找回本页钱包。

2. **看见这份不按脚本拆的树 / 看见主种子 / 这份树 is not already 已经给单签用 interchangeable，也不是已经多签派生层次 bundled（285） interchangeable / 1177 mpath87-notseed interchangeable / 285 mpath item 2 type-not-need interchangeable / 1176 mpath87-notneed interchangeable，也不是已经描述符就已经是地址 interchangeable / 184 descriptor interchangeable。**  
   官方写：这份不按脚本拆的层次只给多签。单签仍可靠主私钥信息找回；若单签也用本页，用户就得另备描述符，或让钱包对每个账户试遍脚本类型。看见本页树，不是已经能当单签默认树。

3. **看见主种子 / 看见这份不按脚本拆的树 / 这份树 is not already 已经交差 interchangeable，也不是已经多签派生层次 bundled（285） interchangeable / 1177 mpath87-notseed interchangeable / 1175 mpath87-nottree interchangeable，也不是已经账户就已经发现完 interchangeable / 1116 acc44-notdone interchangeable。**  
   官方把只给多签和必须同时备描述符写成两句。看见主种子，不是已经交差。

用途号、间隔上限、例路径、例描述符是规范里的取值或做法，本页不抄。

## 官方为什么这样拆

- **主种子 不是已经够找回：** 官方把本页写成必须同时备描述符。
- **这份不按脚本拆的树 不是已经给单签用：** 官方把本页层次写成只给多签。
- **主种子 不是已经交差：** 官方把只给多签和另备描述符写成两句。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 找回 | 不是已经够找回 | 不是已经是地址（184） |
| 单签默认 | 不是已经给单签用 | 不是已经发现完（1116） |
| 交差 | 不是已经交差 | 不是已经必要（1176） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 BIP-87 master-seed not already enough-to-recover / not already singlesig-default / not already settled 正式三事（285 余量），必须分开是不是已经够找回、是不是已经给单签用、是不是已经交差。可以跳过「看见多签就已经该按脚本拆路径」。不要另写怎样加账户号。285 multisig path vs script bundled unbundling 在本页 item 3 完成。

## 本页不抄

- 用途号、间隔上限、例路径、例描述符。
- 怎样加账户号、怎样展开多路径、怎样按间隔停扫。
