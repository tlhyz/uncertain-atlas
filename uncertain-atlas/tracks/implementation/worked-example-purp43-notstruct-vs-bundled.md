# 例：看见 BIPxx-compatible-subset is not already that-BIP-structure interchangeable / not already full-capability interchangeable / not already settled interchangeable

**层次**：应用 / BIP-43 BIPxx-compatible-subset not already that-BIP-structure / not already full-capability / not already settled 正式三事（266 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：Bitcoin [BIP-43](https://github.com/bitcoin/bips/blob/master/bip-0043.mediawiki)（Deployed, Applications）。  
**对应课文**：[L1.4](../../courses/level-01-crypto/L01-M04-canonical-encoding.md)、[L3.6](../../courses/level-03-bitcoin/L03-M06-testing-and-culture.md)。  
**不要写进**：Ethereum 行、L5.1、03 共识、M5.4、L5.4。本页是「BIP-43 BIPxx-compatible-subset not already that-BIP-structure / not already full-capability / not already settled 正式三事（266 余量）/ not 1119 purp43-notstruct interchangeable / not 266 purpose-vs-compatible bundled interchangeable」，不是用途层 bundled（266），也不是描述符就已经是脚本（184），也不是已经是链上脚本（191）。不要另写怎样选用途号或从种子扫账户。

## 官方三件事

1. **看见自称 BIPxx compatible / 只实现了其中一部分 这份栏 is not already 已经是那份 BIP 写的结构 interchangeable，也不是已经用途层 bundled（266） interchangeable / 1119 purp43-notstruct interchangeable / 1118 purp43-notinterop interchangeable / 266 purpose item 1 compat-not-interop interchangeable，也不是已经 BIP-43 BIPxx-compatible-subset not already that-BIP-structure / not already full-capability / not already settled 正式三事 bundled（266 item 2 余量） interchangeable / 266 purpose item 2 interchangeable。**  
   官方写：第一层应当当「用途」。用途决定这颗节点下面还长什么样。与其随便抽子集还自称 BIPxx compatible，需要有限结构的软件应当另写一份 BIP，并换一个用途值。看见自称兼容，不是已经是那份结构 interchangeable——本页从 266 item 2 侧钉 not already that-BIP-structure 单句。266 purpose vs compatible bundled unbundling 在本页 item 2 续。

2. **看见用途号 / 看见自称兼容 / 这份栏 is not already 已经支持那份 BIP 的全部能力 interchangeable，也不是已经用途层 bundled（266） interchangeable / 1119 purp43-notstruct interchangeable / 266 purpose item 3 prefix-not-btc interchangeable / 1120 purp43-notbtc interchangeable，也不是已经描述符就已经是脚本 interchangeable / 184 descriptor interchangeable。**  
   官方把用途号和已经支持那份 BIP 的全部能力分开。看见用途号，不是已经支持那份 BIP 的全部能力 interchangeable。本页钉 not already full-capability 单句。

3. **看见另写一份 BIP / 看见自称兼容 / 这份栏 is not already 已经交差 interchangeable，也不是已经用途层 bundled（266） interchangeable / 1119 purp43-notstruct interchangeable / 1118 purp43-notinterop interchangeable，也不是已经是链上脚本 interchangeable / 191 script interchangeable。**  
   官方把另写一份 BIP 和已经交差分开。看见另写一份 BIP，不是已经交差 interchangeable。266 purpose vs compatible bundled unbundling 在本页 item 2 续。

用途号怎么取、魔数怎么写、SLIP 预留段是规范里的取值，本页不抄。

## 官方为什么这样拆

- **BIP-43 BIPxx-compatible-subset not already that-BIP-structure ≠ 已经是那份 BIP 写的结构 interchangeable：** 官方要求有限结构另写 BIP、另给用途，而不是抽子集还挂原名。
- **看见用途号 not already full-capability ≠ 已经支持那份 BIP 的全部能力 interchangeable：** 官方把用途号和已经支持那份 BIP 的全部能力分开。
- **看见另写一份 BIP not already settled ≠ 已经交差 interchangeable：** 官方把另写一份 BIP 和已经交差分开；266 purpose vs compatible bundled unbundling 在本页 item 2 续。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 自称 BIPxx compatible / 只实现了其中一部分 | 不是已经是那份结构 | 不是描述符就已经是脚本（184） |
| 看见用途号 | 不是已经支持那份 BIP 的全部能力 | 不是已经是链上脚本（191） |
| 看见另写一份 BIP | 不是已经交差 | 不是同一套前缀就已经是比特币专用（1120） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 BIP-43 BIPxx-compatible-subset not already that-BIP-structure / not already full-capability / not already settled 正式三事（266 余量），必须分开是不是已经是那份结构、是不是已经支持全部能力、是不是已经交差。可以跳过「看见 BIP32 compatible 就已经能互操作」。不要另写怎样选用途号或从种子扫账户。266 purpose vs compatible bundled unbundling 在本页 item 2 续；续 [`worked-example-purp43-notbtc-vs-bundled.md`](worked-example-purp43-notbtc-vs-bundled.md)（不变量 1120 item 3）。

## 本页不抄

- 用途号取值、例路径、扩展钥版本魔数、SLIP 预留段。
- 怎样给新方案申请用途、怎样从种子枚举账户。
- 用途层 bundled。那是不变量 266。
- 描述符就已经是脚本。那是不变量 184。
