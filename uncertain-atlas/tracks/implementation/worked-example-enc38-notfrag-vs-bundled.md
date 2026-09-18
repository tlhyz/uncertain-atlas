# 例：看见地址哈希片段不是已经是地址；看见这种打印前缀不是已经解开；看见本页已部署不是已经交差

**层次**：应用 / 规范对象。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：Bitcoin [BIP-38](https://github.com/bitcoin/bips/blob/master/bip-0038.mediawiki)（Deployed, Applications, Specification）。评论摘要：一致不鼓励实现。  
**对应课文**：[L1.4](../../courses/level-01-crypto/L01-M04-canonical-encoding.md)、[L3.6](../../courses/level-03-bitcoin/L03-M06-testing-and-culture.md)。  
**不要写进**：Ethereum 行、L5.1、03 共识、M5.4、L5.4。本页是「BIP-38 address-fragment not already address / not already decrypted / not already recommended 正式三事（296 余量）/ not 1207 enc38-notfrag interchangeable / not 296 encrypted-key-vs-usable bundled interchangeable」，不是加密私钥 bundled（296），也不是地址串就已经有输出（174），也不是签过就已经控制资金（258）。不要另写怎样用口令解开或怎样做椭圆曲线倍点。

## 官方三件事

1. **看见明文里的地址哈希片段 / 看见这种打印前缀 这份记录 is not already 已经是地址 interchangeable，也不是已经加密私钥 bundled（296） interchangeable / 1207 enc38-notfrag interchangeable / 1205 enc38-notuse interchangeable / 296 enc item 1 rec-not-key interchangeable，也不是已经 BIP-38 address-fragment not already address / not already decrypted / not already recommended 正式三事 bundled（296 item 3 余量） interchangeable / 296 enc item 3 interchangeable。**  
   官方写：结果地址的一小段哈希以明文放进记录，不知道口令的人也能按一定概率把记录对上某条地址；完整地址要解开之后才能得到。看见能对上某条地址，不是已经是地址。

2. **看见这种打印前缀 / 看见明文里的地址哈希片段 / 这份记录 is not already 已经解开 interchangeable，也不是已经加密私钥 bundled（296） interchangeable / 1207 enc38-notfrag interchangeable / 296 enc item 2 factory-not-redeem interchangeable / 1206 enc38-notmint interchangeable，也不是已经地址串就已经有输出 interchangeable / 174 address interchangeable。**  
   官方写：看见这种前缀，不是已经是未加密的钱包导入格式。看见能对上某条地址，不是已经解开。

3. **看见本页已部署 / 看见明文里的地址哈希片段 / 这份记录 is not already 已经交差 interchangeable，也不是已经加密私钥 bundled（296） interchangeable / 1207 enc38-notfrag interchangeable / 1205 enc38-notuse interchangeable，也不是已经签过就已经控制资金 interchangeable / 258 signed-is-control interchangeable。**  
   官方评论摘要写：一致不鼓励实现。看见本页已部署，不是已经推荐拿来当第一版备份，也不是已经交差。

加密步骤、口令派生参数、前缀取值、例串、标志位是规范里的取值或做法，本页不抄。

## 官方为什么这样拆

- **地址哈希片段 不是已经是地址：** 官方把明文片段写成还要解开才有完整地址。
- **这种打印前缀 不是已经解开：** 官方把这种前缀写成不是未加密导入格式。
- **本页已部署 不是已经交差：** 官方评论写成一致不鼓励实现。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 地址 | 不是已经是地址 | 不是已经有输出（174） |
| 解开 | 不是已经解开 | 不是已经控制资金（258） |
| 交差 | 不是已经交差 | 不是已经能用（1205） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 BIP-38 address-fragment not already address / not already decrypted / not already recommended 正式三事（296 余量），必须分开是不是已经是地址、是不是已经解开、是不是已经交差。可以跳过「看见加密串就已经能花」。官方评论已写一致不鼓励实现；第一版不要抄本页当默认备份。不要另写怎样用口令解开或怎样做椭圆曲线倍点。296 encrypted key vs usable bundled unbundling 在本页 item 3 完成。

## 本页不抄

- 加密步骤、口令派生参数、前缀取值、例串、标志位。
- 怎样用口令解开、怎样做椭圆曲线倍点、怎样造确认码。
