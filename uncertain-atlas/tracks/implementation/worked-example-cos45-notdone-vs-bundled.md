# 例：看见 earlier-cosigner-branch is not already discovery-done interchangeable / not already first-branch-enough interchangeable / not already settled interchangeable

**层次**：应用 / BIP-45 earlier-cosigner-branch not already discovery-done / not already first-branch-enough / not already settled 正式三事（271 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：Bitcoin [BIP-45](https://github.com/bitcoin/bips/blob/master/bip-0045.mediawiki)（Complete, Applications）。  
**对应课文**：[L1.4](../../courses/level-01-crypto/L01-M04-canonical-encoding.md)、[L3.6](../../courses/level-03-bitcoin/L03-M06-testing-and-culture.md)。  
**不要写进**：Ethereum 行、L5.1、03 共识、M5.4、L5.4。本页是「BIP-45 earlier-cosigner-branch not already discovery-done / not already first-branch-enough / not already settled 正式三事（271 余量）/ not 1132 cos45-notdone interchangeable / not 271 cosigner-vs-discovered bundled interchangeable」，不是分层确定性多签结构 bundled（271），也不是余额为零就已经发现完（1117），也不是账户出现了就已经齐（1126）。不要另写怎样按用途公钥排下标，也不要另写 BIP-11 / BIP-67。

## 官方三件事

1. **看见前面的联合签名人分支没有交易 这份栏 is not already 已经扫完 interchangeable，也不是已经多方多签 bundled（271） interchangeable / 1132 cos45-notdone interchangeable / 1130 cos45-notmaster interchangeable / 271 cosigner item 1 master-not-this interchangeable，也不是已经 BIP-45 earlier-cosigner-branch not already discovery-done / not already first-branch-enough / not already settled 正式三事 bundled（271 item 3 余量） interchangeable / 271 cosigner item 3 interchangeable。**  
   官方写：发现看过往、不看余额。和 BIP-44 相反，即使前面的分支没有交易，也必须检查每一个联合签名人分支。看见前面一支没有交易，不是已经扫完 interchangeable——本页从 271 item 3 侧钉 not already discovery-done 单句。271 cosigner vs discovered bundled unbundling 在本页 item 3 完成。

2. **看见余额为零 / 看见前面的联合签名人分支没有交易 / 这份栏 is not already 已经没有这一支 interchangeable，也不是已经多方多签 bundled（271） interchangeable / 1132 cos45-notdone interchangeable / 271 cosigner item 2 addr-not-sign interchangeable / 1131 cos45-notsign interchangeable，也不是已经余额为零就已经发现完 interchangeable / 1117 acc44-notdone interchangeable。**  
   官方把余额为零和已经没有这一支分开。看见余额为零，不是已经没有这一支 interchangeable。本页钉 not already first-branch-enough 单句。

3. **看见每个联合签名人只在自己的分支上长地址 / 看见前面分支没有交易 / 这份栏 is not already 已经交差 interchangeable，也不是已经多方多签 bundled（271） interchangeable / 1132 cos45-notdone interchangeable / 1130 cos45-notmaster interchangeable，也不是已经账户出现了就已经齐 interchangeable / 1126 nest49-notbal interchangeable。**  
   官方把每个联合签名人只在自己的分支上长地址写成免得两个人同时长出同一条地址。看见每个联合签名人只在自己的分支上长地址，不是已经交差 interchangeable。271 cosigner vs discovered bundled unbundling 在本页 item 3 完成。

用途号、间隙条数、例路径、怎样按用途公钥排联合签名人下标是规范里的取值或做法，本页不抄。

## 官方为什么这样拆

- **BIP-45 earlier-cosigner-branch not already discovery-done ≠ 已经扫完 interchangeable：** 官方明确写成和 BIP-44 相反，每一支都要查。
- **看见余额为零 not already first-branch-enough ≠ 已经没有这一支 interchangeable：** 官方把发现写成看过往、不看余额。
- **看见每个联合签名人只在自己的分支上长地址 not already settled ≠ 已经交差 interchangeable：** 官方把只在自己分支上长地址写成免得同时长出同一条地址；271 cosigner vs discovered bundled unbundling 在本页 item 3 完成。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 前面的联合签名人分支没有交易 | 不是已经扫完 | 不是余额为零就已经发现完（1117） |
| 看见余额为零 | 不是已经没有这一支 | 不是账户出现了就已经齐（1126） |
| 看见每个联合签名人只在自己的分支上长地址 | 不是已经交差 | 不是共享主公钥就已经是本页（1130） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 BIP-45 earlier-cosigner-branch not already discovery-done / not already first-branch-enough / not already settled 正式三事（271 余量），必须分开是不是已经扫完、是不是已经没有这一支、是不是已经交差。可以跳过「看见多签路径就已经能扫完」。不要另写怎样按用途公钥排下标，也不要另写 BIP-11 / BIP-67。271 cosigner vs discovered bundled unbundling 在本页 item 3 完成。

## 本页不抄

- 用途号、间隙条数、例路径、例压缩钥。
- 怎样按用途公钥排联合签名人下标、怎样从种子扫每一支。
- 分层确定性多签结构 bundled。那是不变量 271。
- 余额为零就已经发现完。那是不变量 1117。
