# 例：看见厂家代生成不是已经能兑；看见同一种打印串不是已经能分辨编法；看见共享生成不是已经交差

**层次**：应用 / 规范对象。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：Bitcoin [BIP-38](https://github.com/bitcoin/bips/blob/master/bip-0038.mediawiki)（Deployed, Applications, Specification）。评论摘要：一致不鼓励实现。  
**对应课文**：[L1.4](../../courses/level-01-crypto/L01-M04-canonical-encoding.md)、[L3.6](../../courses/level-03-bitcoin/L03-M06-testing-and-culture.md)。  
**不要写进**：Ethereum 行、L5.1、03 共识、M5.4、L5.4。本页是「BIP-38 factory-generated not already redeemable / not already same-path / not already settled 正式三事（296 余量）/ not 1206 enc38-notmint interchangeable / not 296 encrypted-key-vs-usable bundled interchangeable」，不是加密私钥 bundled（296），也不是扩展公钥就已经能花（182），也不是地址串就已经有输出（174）。不要另写怎样用口令解开或怎样做椭圆曲线倍点。

## 官方三件事

1. **看见厂家代生成 / 看见椭圆曲线倍点那条路 这份记录 is not already 已经能兑 interchangeable，也不是已经加密私钥 bundled（296） interchangeable / 1206 enc38-notmint interchangeable / 1205 enc38-notuse interchangeable / 296 enc item 1 rec-not-key interchangeable，也不是已经 BIP-38 factory-generated not already redeemable / not already same-path / not already settled 正式三事 bundled（296 item 2 余量） interchangeable / 296 enc item 2 interchangeable。**  
   官方写：本页给两种编法。一种是：任何人拿已知私钥、配任意口令，编出记录。另一种是共享生成：编出最终记录和对应地址的那一方（例如实物币厂家）只知道从口令派生出来的一串，真正兑付还要原来的口令。看见厂家编得出地址，不是厂家已经能兑。

2. **看见同一种打印串 / 看见厂家代生成 / 这份记录 is not already 已经能分辨走了哪条编法 interchangeable，也不是已经加密私钥 bundled（296） interchangeable / 1206 enc38-notmint interchangeable / 296 enc item 3 frag-not-addr interchangeable / 1207 enc38-notfrag interchangeable，也不是已经扩展公钥就已经能花 interchangeable / 182 xpub interchangeable。**  
   官方动机写：不能被发行方连坐的实物币，比能被发行方拿走的更值。看见同一种打印串，不是已经能分辨走了哪条编法。

3. **看见共享生成 / 看见厂家代生成 / 这份记录 is not already 已经交差 interchangeable，也不是已经加密私钥 bundled（296） interchangeable / 1206 enc38-notmint interchangeable / 1205 enc38-notuse interchangeable，也不是已经地址串就已经有输出 interchangeable / 174 address interchangeable。**  
   官方把共享生成写成不是已经是「先有私钥再加密」。看见共享生成，不是已经交差。

加密步骤、口令派生参数、前缀取值、例串、标志位是规范里的取值或做法，本页不抄。

## 官方为什么这样拆

- **厂家代生成 不是已经能兑：** 官方把厂家只知道派生串写成还要原来的口令。
- **同一种打印串 不是已经能分辨编法：** 官方把两种编法写成同一类打印串。
- **共享生成 不是已经交差：** 官方把共享生成写成不是先有私钥再加密。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 兑 | 不是已经能兑 | 不是已经能花（182） |
| 编法 | 不是已经能分辨编法 | 不是已经有输出（174） |
| 交差 | 不是已经交差 | 不是已经能用（1205） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 BIP-38 factory-generated not already redeemable / not already same-path / not already settled 正式三事（296 余量），必须分开是不是已经能兑、是不是已经能分辨编法、是不是已经交差。可以跳过「看见加密串就已经能花」。官方评论已写一致不鼓励实现；第一版不要抄本页当默认备份。不要另写怎样用口令解开或怎样做椭圆曲线倍点。296 encrypted key vs usable bundled unbundling 在本页 item 2 续；续 [`worked-example-enc38-notfrag-vs-bundled.md`](worked-example-enc38-notfrag-vs-bundled.md)（不变量 1207 item 3）。

## 本页不抄

- 加密步骤、口令派生参数、前缀取值、例串、标志位。
- 怎样用口令解开、怎样做椭圆曲线倍点、怎样造确认码。
