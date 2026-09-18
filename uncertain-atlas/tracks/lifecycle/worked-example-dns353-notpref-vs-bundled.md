# 例：看见可读名字不是已经该走 DNS；看见展示前缀不是已经写进要解析的标签；看见名字像邮箱不是已经是本页

**层次**：应用 / 规范对象。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：Bitcoin [BIP-353](https://github.com/bitcoin/bips/blob/master/bip-0353.mediawiki)（Complete, Applications）。  
**对应课文**：[L0.7](../../courses/level-00-machine/L00-M07-one-payment-lifecycle.md)、[L3.6](../../courses/level-03-bitcoin/L03-M06-testing-and-culture.md)。  
**不要写进**：Ethereum 行、L5.1、03 共识、M5.4、L5.4。本页是「BIP-353 readable-name not already prefer-dns / not already better / not already settled 正式三事（261 余量）/ not 1220 dns353-notpref interchangeable / not 261 dns-name-vs-instruction bundled interchangeable」，不是 DNS 名字 bundled（261），也不是付款 URI 就已经授权（255），也不是地址串就已经有输出（174）。不要另写怎样枚举用户名。不要另写 BIP-21 当现行用户方案。

## 官方三件事

1. **看见可读名字 / 看见 user@domain 这份指示 is not already 已经该走 DNS interchangeable，也不是已经 DNS 名字 bundled（261） interchangeable / 1220 dns353-notpref interchangeable / 1221 dns353-nottxt interchangeable / 261 dns item 2 txt-not-legal interchangeable，也不是已经 BIP-353 readable-name not already prefer-dns / not already better / not already settled 正式三事 bundled（261 item 1 余量） interchangeable / 261 dns item 1 interchangeable。**  
   官方写：只要已经有明确的公钥或地址，钱包不得优先走 DNS。换句话说，若标准比特币地址或直接的付款 URI 已经够用，必须优先用那个。看见可读名字，不是已经该去解析。

2. **看见展示前缀 / 看见可读名字 / 这份指示 is not already 已经写进了要解析的标签 interchangeable，也不是已经 DNS 名字 bundled（261） interchangeable / 1220 dns353-notpref interchangeable / 261 dns item 3 cache-not-uri interchangeable / 1222 dns353-notcache interchangeable，也不是已经付款 URI 就已经授权 interchangeable / 255 uri interchangeable。**  
   官方写：看见展示前缀，不是已经写进了要解析的标签，也不是已经比地址或 URI 更好。

3. **看见名字像邮箱 / 看见可读名字 / 这份指示 is not already 已经是本页 interchangeable，也不是已经 DNS 名字 bundled（261） interchangeable / 1220 dns353-notpref interchangeable / 1221 dns353-nottxt interchangeable，也不是已经地址串就已经有输出 interchangeable / 174 address interchangeable。**  
   官方写：看见名字像邮箱，不是已经是本页，也不是已经交差。

标签怎么拼、例名、PSBT 字段号是规范里的取值，本页不抄。不要另写 BIP-21 当现行用户方案。不要另写怎样枚举用户名。

## 官方为什么这样拆

- **可读名字 不是已经该走 DNS：** 官方把有地址或 URI 就必须优先用那个写成硬规则。
- **展示前缀 不是已经写进要解析的标签：** 官方把展示和要解析的标签写成两件。
- **名字像邮箱 不是已经是本页：** 官方把像邮箱和本页方案写成两件。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 该走 DNS | 不是已经该走 DNS | 不是已经授权（255） |
| 标签 | 不是已经写进要解析的标签 | 不是已经有输出（174） |
| 本页 | 不是已经是本页 | 不是已经合法 TXT（1221） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 BIP-353 readable-name not already prefer-dns / not already better / not already settled 正式三事（261 余量），必须分开是不是已经该走 DNS、是不是已经写进要解析的标签、是不是已经是本页。可以跳过「看见名字就已经能付」。不要另写怎样枚举用户名。不要另写 BIP-21 当现行用户方案。261 dns name vs instruction bundled unbundling 在本页 item 1 启动；续 [`worked-example-dns353-nottxt-vs-bundled.md`](worked-example-dns353-nottxt-vs-bundled.md)（不变量 1221 item 2）。

## 本页不抄

- 标签怎么拼、例名、PSBT 字段号、DNSSEC 算法取值。
- 怎样枚举用户名、怎样让远端解析器代验。
