# 例：看见 TXT 不是已经是合法付款指示；看见解析器说绿不是已经核过；看见一条 TXT 不是已经是一条能付的 URI

**层次**：应用 / 规范对象。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：Bitcoin [BIP-353](https://github.com/bitcoin/bips/blob/master/bip-0353.mediawiki)（Complete, Applications）。  
**对应课文**：[L0.7](../../courses/level-00-machine/L00-M07-one-payment-lifecycle.md)、[L3.6](../../courses/level-03-bitcoin/L03-M06-testing-and-culture.md)。  
**不要写进**：Ethereum 行、L5.1、03 共识、M5.4、L5.4。本页是「BIP-353 txt not already legal / not already remote-verified / not already settled 正式三事（261 余量）/ not 1221 dns353-nottxt interchangeable / not 261 dns-name-vs-instruction bundled interchangeable」，不是 DNS 名字 bundled（261），也不是远程取单就已经验证（55），也不是静默付款地址就已经有输出（260）。不要另写怎样枚举用户名。不要另写 BIP-21 当现行用户方案。

## 官方三件事

1. **看见 TXT / 看见一条 TXT 这份指示 is not already 已经是合法付款指示 interchangeable，也不是已经 DNS 名字 bundled（261） interchangeable / 1221 dns353-nottxt interchangeable / 1220 dns353-notpref interchangeable / 261 dns item 1 name-not-pref interchangeable，也不是已经 BIP-353 txt not already legal / not already remote-verified / not already settled 正式三事 bundled（261 item 2 余量） interchangeable / 261 dns item 2 interchangeable。**  
   官方写：必须以「bitcoin:」开头的 TXT 才看；同一标签上有多条这样的记录，整组非法，一条都不能用。必须把这一条 TXT 里的字段按顺序拼回一条 URI，中间不得另插分隔。不得跨多条 TXT 去拼。看见一条 TXT，不是已经是合法付款指示。

2. **看见解析器说绿 / 看见 TXT / 这份指示 is not already 已经核过 interchangeable，也不是已经 DNS 名字 bundled（261） interchangeable / 1221 dns353-nottxt interchangeable / 261 dns item 3 cache-not-uri interchangeable / 1222 dns353-notcache interchangeable，也不是已经远程取单就已经验证 interchangeable / 55 remote interchangeable。**  
   官方写：所有付款指示必须带 DNSSEC 签。必须自己把 DNSSEC 验到根，不得让远端解析器代验。看见解析器说绿，不是已经核过。

3. **看见一条 TXT / 看见 TXT / 这份指示 is not already 已经是一条能付的 URI interchangeable，也不是已经 DNS 名字 bundled（261） interchangeable / 1221 dns353-nottxt interchangeable / 1220 dns353-notpref interchangeable，也不是已经静默付款地址就已经有输出 interchangeable / 260 silent interchangeable。**  
   官方写：看见一条 TXT，不是已经是一条能付的 URI，也不是已经交差。

标签怎么拼、例名、PSBT 字段号是规范里的取值，本页不抄。不要另写 BIP-21 当现行用户方案。不要另写怎样枚举用户名。

## 官方为什么这样拆

- **TXT 不是已经是合法付款指示：** 官方把拼装、多条非法写成独立谓词。
- **解析器说绿 不是已经核过：** 官方把必须自己验到根写成硬规则。
- **一条 TXT 不是已经是一条能付的 URI：** 官方把 TXT 和能付的 URI 写成两件。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 合法 | 不是已经是合法付款指示 | 不是已经验证（55） |
| 核过 | 不是已经核过 | 不是已经有输出（260） |
| 能付 URI | 不是已经是一条能付的 URI | 不是已经该走 DNS（1220） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 BIP-353 txt not already legal / not already remote-verified / not already settled 正式三事（261 余量），必须分开是不是已经是合法付款指示、是不是已经核过、是不是已经是一条能付的 URI。可以跳过「看见名字就已经能付」。不要另写怎样枚举用户名。不要另写 BIP-21 当现行用户方案。261 dns name vs instruction bundled unbundling 在本页 item 2 续；续 [`worked-example-dns353-notcache-vs-bundled.md`](worked-example-dns353-notcache-vs-bundled.md)（不变量 1222 item 3）。

## 本页不抄

- 标签怎么拼、例名、PSBT 字段号、DNSSEC 算法取值。
- 怎样枚举用户名、怎样让远端解析器代验。
