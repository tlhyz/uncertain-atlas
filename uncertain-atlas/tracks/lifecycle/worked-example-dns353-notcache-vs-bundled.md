# 例：看见复制了可读名字不是已经复制了 URI；看见 DNS 还没过期不是里面的报价还有效；看见指示里有链上地址不是已经不复用

**层次**：应用 / 规范对象。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：Bitcoin [BIP-353](https://github.com/bitcoin/bips/blob/master/bip-0353.mediawiki)（Complete, Applications）。  
**对应课文**：[L0.7](../../courses/level-00-machine/L00-M07-one-payment-lifecycle.md)、[L3.6](../../courses/level-03-bitcoin/L03-M06-testing-and-culture.md)。  
**不要写进**：Ethereum 行、L5.1、03 共识、M5.4、L5.4。本页是「BIP-353 cache-copy not already current-uri / not already quote-live / not already settled 正式三事（261 余量）/ not 1222 dns353-notcache interchangeable / not 261 dns-name-vs-instruction bundled interchangeable」，不是 DNS 名字 bundled（261），也不是签过就已经控制资金（258），也不是付款 URI 就已经授权（255）。不要另写怎样枚举用户名。不要另写 BIP-21 当现行用户方案。

## 官方三件事

1. **看见复制了可读名字 / 看见缓存了名字 这份指示 is not already 已经复制了 URI interchangeable，也不是已经 DNS 名字 bundled（261） interchangeable / 1222 dns353-notcache interchangeable / 1220 dns353-notpref interchangeable / 261 dns item 1 name-not-pref interchangeable，也不是已经 BIP-353 cache-copy not already current-uri / not already quote-live / not already settled 正式三事 bundled（261 item 3 余量） interchangeable / 261 dns item 3 interchangeable。**  
   官方写：可以缓存，但不得超过解析器给的 TTL，也不得超过整条 DNSSEC 链上签过的最短初始 TTL。复制时应当直接复制底下的 URI，不要复制可读名字。看见复制了可读名字，不是已经复制了 URI。

2. **看见 DNS 还没过期 / 看见复制了可读名字 / 这份指示 is not already 已经是当前那条 URI interchangeable，也不是已经 DNS 名字 bundled（261） interchangeable / 1222 dns353-notcache interchangeable / 261 dns item 2 txt-not-legal interchangeable / 1221 dns353-nottxt interchangeable，也不是已经签过就已经控制资金 interchangeable / 258 signed interchangeable。**  
   官方写：带过期时间的指示（例如闪电报价）必须让 DNS 记录先过期，否则发送方手里可能还是过期指示。看见 DNS 还没过期，不是里面的报价还有效。

3. **看见指示里有链上地址 / 看见复制了可读名字 / 这份指示 is not already 已经不复用 interchangeable，也不是已经 DNS 名字 bundled（261） interchangeable / 1222 dns353-notcache interchangeable / 1220 dns353-notpref interchangeable，也不是已经付款 URI 就已经授权 interchangeable / 255 uri interchangeable。**  
   官方写：看见指示里有链上地址，不是已经不复用，也不是已经交差。

标签怎么拼、例名、PSBT 字段号是规范里的取值，本页不抄。不要另写 BIP-21 当现行用户方案。不要另写怎样枚举用户名。

## 官方为什么这样拆

- **复制了可读名字 不是已经复制了 URI：** 官方把复制 URI 而不是名字写成独立对象。
- **DNS 还没过期 不是里面的报价还有效：** 官方把 TTL 和报价有效写成两件。
- **指示里有链上地址 不是已经不复用：** 官方把有地址和已经不复用写成两件。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 当前 URI | 不是已经复制了 URI | 不是已经控制资金（258） |
| 报价有效 | 不是里面的报价还有效 | 不是已经授权（255） |
| 不复用 | 不是已经不复用 | 不是已经该走 DNS（1220） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 BIP-353 cache-copy not already current-uri / not already quote-live / not already settled 正式三事（261 余量），必须分开是不是已经复制了 URI、是不是里面的报价还有效、是不是已经不复用。可以跳过「看见名字就已经能付」。不要另写怎样枚举用户名。不要另写 BIP-21 当现行用户方案。261 dns name vs instruction bundled unbundling 在本页 item 3 完成。

## 本页不抄

- 标签怎么拼、例名、PSBT 字段号、DNSSEC 算法取值。
- 怎样枚举用户名、怎样让远端解析器代验。
