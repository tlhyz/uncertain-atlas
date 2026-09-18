# 例：看见 many-xpubs is not already own-index interchangeable / not already offset-child interchangeable / not already settled interchangeable

**层次**：应用 / BIP-383 many-xpubs not already own-index / not already offset-child / not already settled 正式三事（274 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：Bitcoin [BIP-383](https://github.com/bitcoin/bips/blob/master/bip-0383.mediawiki)（Deployed, Applications, Informational）。  
**对应课文**：[L1.4](../../courses/level-01-crypto/L01-M04-canonical-encoding.md)、[L3.6](../../courses/level-03-bitcoin/L03-M06-testing-and-culture.md)。  
**不要写进**：Ethereum 行、L5.1、03 共识、M5.4、L5.4。本页是「BIP-383 many-xpubs not already own-index / not already offset-child / not already settled 正式三事（274 余量）/ not 1144 desc383-notidx interchangeable / not 274 multi-vs-sortedmulti bundled interchangeable」，不是多签描述符 bundled（274），也不是看见描述符就已经是地址（184），也不是看见描述符就已经换了一门语言（191）。不要另写怎样按字节排公钥。

## 官方三件事

1. **看见多把扩展钥 / 看见各钥自己的派生路径 这份栏 is not already 已经可以各走各的下标 interchangeable，也不是已经多签描述符 bundled（274） interchangeable / 1144 desc383-notidx interchangeable / 1142 desc383-notsort interchangeable / 274 multi item 1 multi-not-sorted interchangeable，也不是已经 BIP-383 many-xpubs not already own-index / not already offset-child / not already settled 正式三事 bundled（274 item 3 余量） interchangeable / 274 multi item 3 interchangeable。**  
   官方写：表达式里有一把或多把扩展钥时，派生用同一个子下标。钥会齐步变，好让输出脚本的编号和派生钥的编号对得上。看见多把扩展钥，不是已经可以各走各的下标 interchangeable——本页从 274 item 3 侧钉 not already own-index 单句。274 multi vs sortedmulti bundled unbundling 在本页 item 3 完成。

2. **看见路径写法不同 / 看见多把扩展钥 / 这份栏 is not already 已经能错开子号 interchangeable，也不是已经多签描述符 bundled（274） interchangeable / 1144 desc383-notidx interchangeable / 274 multi item 2 thresh-not-same-cap interchangeable / 1143 desc383-notcap interchangeable，也不是已经看见描述符就已经是地址 interchangeable / 184 descriptor interchangeable。**  
   官方把路径写法不同和已经能错开子号分开。看见路径写法不同，不是已经能错开子号 interchangeable。本页钉 not already offset-child 单句。

3. **看见钥会齐步变 / 看见多把扩展钥 / 这份栏 is not already 已经交差 interchangeable，也不是已经多签描述符 bundled（274） interchangeable / 1144 desc383-notidx interchangeable / 1142 desc383-notsort interchangeable，也不是已经看见描述符就已经换了一门语言 interchangeable / 191 miniscript interchangeable。**  
   官方把同一子下标写成齐步变，不是已经交差。看见钥会齐步变，不是已经交差 interchangeable。274 multi vs sortedmulti bundled unbundling 在本页 item 3 完成。

函数名单、脚本模板、测试向量、怎样按字节排是规范里的取值或做法，本页不抄。

## 官方为什么这样拆

- **BIP-383 many-xpubs not already own-index ≠ 已经可以各走各的下标 interchangeable：** 官方把同一子下标写成齐步变。
- **看见路径写法不同 not already offset-child ≠ 已经能错开子号 interchangeable：** 官方把路径写法不同和已经能错开子号分开。
- **看见钥会齐步变 not already settled ≠ 已经交差 interchangeable：** 官方把齐步变和已经交差分开；274 multi vs sortedmulti bundled unbundling 在本页 item 3 完成。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 多把扩展钥 / 各钥自己的派生路径 | 不是已经可以各走各的下标 | 不是看见描述符就已经是地址（184） |
| 看见路径写法不同 | 不是已经能错开子号 | 不是看见描述符就已经换了一门语言（191） |
| 看见钥会齐步变 | 不是已经交差 | 不是 multi 就已经是 sortedmulti（1142） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 BIP-383 many-xpubs not already own-index / not already offset-child / not already settled 正式三事（274 余量），必须分开是不是已经可以各走各的下标、是不是已经能错开子号、是不是已经交差。可以跳过「看见多签表达式就已经排过」。不要另写怎样按字节排公钥。274 multi vs sortedmulti bundled unbundling 在本页 item 3 完成。

## 本页不抄

- 函数名单、脚本模板、测试向量、例钥、整数编码。
- 怎样按字典序排、怎样数赎回脚本字节、怎样选子下标。
- 多签描述符 bundled。那是不变量 274。
- 看见描述符就已经是地址。那是不变量 184。
