# 例：看见 same-seed is not already same-coin interchangeable / not already shared-address interchangeable / not already settled interchangeable

**层次**：应用 / BIP-44 same-seed not already same-coin / not already shared-address / not already settled 正式三事（267 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：Bitcoin [BIP-44](https://github.com/bitcoin/bips/blob/master/bip-0044.mediawiki)（Deployed, Applications）。  
**对应课文**：[L1.4](../../courses/level-01-crypto/L01-M04-canonical-encoding.md)、[L3.6](../../courses/level-03-bitcoin/L03-M06-testing-and-culture.md)。  
**不要写进**：Ethereum 行、L5.1、03 共识、M5.4、L5.4。本页是「BIP-44 same-seed not already same-coin / not already shared-address / not already settled 正式三事（267 余量）/ not 1115 acc44-notcoin interchangeable / not 267 account-vs-discovered bundled interchangeable」，不是多账户层次 bundled（267），也不是扩展公钥就已经能花（182），也不是 BIP32 compatible 就已经能互操作（266）。不要另写怎样扫间隙或枚举账户。

## 官方三件事

1. **看见同一份种子 / 同一颗主节点 这份栏 is not already 已经是同一条币 interchangeable，也不是已经多账户层次 bundled（267） interchangeable / 1115 acc44-notcoin interchangeable / 1116 acc44-notpast interchangeable / 267 account item 2 account-not-past interchangeable，也不是已经 BIP-44 same-seed not already same-coin / not already shared-address / not already settled 正式三事 bundled（267 item 1 余量） interchangeable / 267 account item 1 interchangeable。**  
   官方写：一颗主节点可以给无限种独立的币用。可是把不同币挤在同一片空间里有坏处。本层给每一种币单独一棵子树。看见同一份种子，不是已经是同一条币 interchangeable——本页从 267 item 1 侧钉 not already same-coin 单句。267 account vs discovered bundled unbundling 在本页 item 1 启动。

2. **看见还能再长出别的币 / 看见同一份种子 / 这份栏 is not already 已经可以共用地址 interchangeable，也不是已经多账户层次 bundled（267） interchangeable / 1115 acc44-notcoin interchangeable / 267 account item 3 zero-not-done interchangeable / 1117 acc44-notdone interchangeable，也不是已经扩展公钥就已经能花 interchangeable / 182 xpub interchangeable。**  
   官方把还能再长出别的币和已经可以共用地址分开。看见还能再长出别的币，不是已经可以共用地址 interchangeable。本页钉 not already shared-address 单句。

3. **看见单独一棵子树 / 看见同一份种子 / 这份栏 is not already 已经交差 interchangeable，也不是已经多账户层次 bundled（267） interchangeable / 1115 acc44-notcoin interchangeable / 1116 acc44-notpast interchangeable，也不是已经 BIP32 compatible 就已经能互操作 interchangeable / 266 purpose interchangeable。**  
   官方把单独一棵子树和已经交差分开。看见单独一棵子树，不是已经交差 interchangeable。267 account vs discovered bundled unbundling 在本页 item 1 启动。

间隙条数、用途号、币种表、例路径是规范里的取值，本页不抄。

## 官方为什么这样拆

- **BIP-44 same-seed not already same-coin ≠ 已经是同一条币 interchangeable：** 官方把同一片空间给多种币写成有坏处，要求每种币单独一棵子树。
- **看见还能再长出别的币 not already shared-address ≠ 已经可以共用地址 interchangeable：** 官方把还能再长出别的币和已经可以共用地址分开。
- **看见单独一棵子树 not already settled ≠ 已经交差 interchangeable：** 官方把单独一棵子树和已经交差分开；267 account vs discovered bundled unbundling 在本页 item 1 启动。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 同一份种子 / 同一颗主节点 | 不是已经是同一条币 | 不是扩展公钥就已经能花（182） |
| 看见还能再长出别的币 | 不是已经可以共用地址 | 不是 BIP32 compatible 就已经能互操作（266） |
| 看见单独一棵子树 | 不是已经交差 | 不是账户号就已经有过往（1116） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 BIP-44 same-seed not already same-coin / not already shared-address / not already settled 正式三事（267 余量），必须分开是不是已经是同一条币、是不是已经可以共用地址、是不是已经交差。可以跳过「看见余额为零就已经扫完」。不要另写怎样扫间隙或枚举账户。267 account vs discovered bundled unbundling 在本页 item 1 启动；续 [`worked-example-acc44-notpast-vs-bundled.md`](worked-example-acc44-notpast-vs-bundled.md)（不变量 1116 item 2）。

## 本页不抄

- 用途号、间隙条数、币种登记表、例路径。
- 怎样扫外链、怎样从种子枚举账户、怎样按间隙停搜。
- 多账户层次 bundled。那是不变量 267。
- 扩展公钥就已经能花。那是不变量 182。
