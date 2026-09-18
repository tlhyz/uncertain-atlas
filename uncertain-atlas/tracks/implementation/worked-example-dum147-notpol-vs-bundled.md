# 例：看见转发已经拒不是块里已经拒；看见 BIP-62 菜谱不是已经是本页这一条；看见非兼容签能改成兼容不是已经没有功能损失

**层次**：共识 / 规范对象。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：Bitcoin [BIP-147](https://github.com/bitcoin/bips/blob/master/bip-0147.mediawiki)（Deployed, Consensus soft fork）。  
**对应课文**：[L1.4](../../courses/level-01-crypto/L01-M04-canonical-encoding.md)、[L3.3](../../courses/level-03-bitcoin/L03-M03-conservative-evolution.md)、[L3.7](../../courses/level-03-bitcoin/L03-M07-segwit-soft-fork.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4。本页是「BIP-147 policy not already consensus / not already bip62 / not already settled 正式三事（264 余量）/ not 1231 dum147-notpol interchangeable / not 264 dummy-vs-empty bundled interchangeable」，不是 dummy bundled（264），也不是版本位就已经激活（171），也不是策略就已经是共识（144）。不要另写怎样改 dummy 撞身份。

## 官方三件事

1. **看见转发已经拒 / 看见转发策略已经要空 dummy 这份门 is not already 已经是共识 interchangeable，也不是已经 dummy bundled（264） interchangeable / 1231 dum147-notpol interchangeable / 1229 dum147-notany interchangeable / 264 dummy item 1 dum-not-any interchangeable，也不是已经 BIP-147 policy not already consensus / not already bip62 / not already settled 正式三事 bundled（264 item 3 余量） interchangeable / 264 dummy item 3 interchangeable。**  
   官方写：参考客户端一开始就会出兼容的签；这条空 dummy 规则从某次发布起就当转发策略在执行。本页才把它写成共识。看见转发已经拒，不是块里已经拒。

2. **看见 BIP-62 菜谱 / 看见转发已经拒 / 这份门 is not already 已经是本页这一条 interchangeable，也不是已经 dummy bundled（264） interchangeable / 1231 dum147-notpol interchangeable / 264 dummy item 2 wit-not-gone interchangeable / 1230 dum147-notwit interchangeable，也不是已经版本位就已经激活 interchangeable / 171 versionbit interchangeable。**  
   官方写：本页是从 BIP-62 提案里抽出来的。看见 BIP-62 菜谱，不是已经是本页这一条。

3. **看见非兼容签能改成兼容 / 看见转发已经拒 / 这份门 is not already 已经没有功能损失 interchangeable，也不是已经 dummy bundled（264） interchangeable / 1231 dum147-notpol interchangeable / 1229 dum147-notany interchangeable，也不是已经策略就已经是共识 interchangeable / 144 policy interchangeable。**  
   官方写：看见非兼容签能改成兼容，不是已经没有功能损失——官方要求设计古怪脚本的人必须额外注意本页。看见转发策略已经要空 dummy，不是已经交差。

激活日程、版本位编号是规范里的取值，本页不抄。不要另写怎样改 dummy 撞身份。

## 官方为什么这样拆

- **转发已经拒 不是块里已经拒：** 官方把早就当转发策略执行写成兼容事实。
- **BIP-62 菜谱 不是已经是本页这一条：** 官方把本页写成从 BIP-62 抽出来的一条。
- **非兼容签能改成兼容 不是已经没有功能损失：** 官方要求古怪脚本必须额外注意本页。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 共识 | 不是已经是共识 | 不是已经激活（171） |
| 本页这一条 | 不是已经是本页这一条 | 不是已经是共识（144） |
| 没有功能损失 | 不是已经没有功能损失 | 不是已经随便填（1229） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 BIP-147 policy not already consensus / not already bip62 / not already settled 正式三事（264 余量），必须分开是不是已经是共识、是不是已经是本页这一条、是不是已经没有功能损失。可以跳过「看见多重签验过就已经不可延展」。不要另写怎样改 dummy 撞身份。264 dummy vs empty bundled unbundling 在本页 item 3 完成。

## 本页不抄

- 激活时间、版本位编号、部署名、参考客户端版本号。
- 怎样造非空 dummy、怎样把非兼容签改成兼容、怎样靠改 dummy 挡紧凑块。
