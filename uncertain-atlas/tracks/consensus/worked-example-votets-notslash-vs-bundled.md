# 例：看见非法票被断开 is not already slashed interchangeable / not already on-chain interchangeable / not already doublesign interchangeable

**层次**：共识 / 断开 not already slashed / not already on-chain / not already doublesign 正式三事（304 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [Validator Signing](https://github.com/cometbft/cometbft/blob/main/spec/consensus/signing.md) validator signing / vote timestamp。  
**对应课文**：[L4.2](../../courses/level-04-bft/L04-M02-rounds-and-steps.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行。本页是「断开 not already slashed / not already on-chain / not already doublesign 正式三事（304 余量）/ not 1000 votets-notslash interchangeable / not 304 vote-ts-vs-checked bundled interchangeable」，不是签字校验 bundled（304），也不是签名器已经记住上次高度轮类型（19），也不是证据窗已经盖住解绑（46）。不要另写怎样记上次签过的高度轮类型。本页不写 amnesia 分类。

## 官方三件事

1. **看见非法票被断开 / 看见没过基本校验 这份校验 is not already 已经罚了签的人 interchangeable，也不是已经签字校验 bundled（304） interchangeable / 1000 votets-notslash interchangeable / 998 votets-notcheck interchangeable / 304 vote item 1 Timestamp interchangeable，也不是已经断开 not already slashed / not already on-chain / not already doublesign 正式三事 bundled（304 item 3 余量） interchangeable / 304 vote item 3 interchangeable。**  
   官方写：不过基本校验的票和提案算非法。流言它们的对等节点可能被断开。但目前没有明确机制，去罚签了这种非法对象的验证者。看见被断开，不是已经罚了 interchangeable——本页从 304 item 3 侧钉 not already slashed 单句。304 vote-ts vs checked bundled unbundling 在本页 item 3 完成。

2. **看见非法 / 看见断开 / 这份校验 is not already 已经上链 interchangeable，也不是已经签字校验 bundled（304） interchangeable / 1000 votets-notslash interchangeable / 304 vote item 2 冲突提案 interchangeable / 999 votets-notevid interchangeable，也不是已经签名器已经记住上次高度轮类型 interchangeable / 19 last-sign interchangeable。**  
   官方把非法和已经上链分开。看见非法，不是已经上链 interchangeable。本页钉 not already on-chain 单句。

3. **看见没过基本校验 / 看见断开 / 这份校验 is not already 已经是双签 interchangeable，也不是已经签字校验 bundled（304） interchangeable / 1000 votets-notslash interchangeable / 998 votets-notcheck interchangeable，也不是已经证据窗已经盖住解绑 interchangeable / 46 evidence-window interchangeable。**  
   官方把没过基本校验和已经是双签分开。看见没过基本校验，不是已经是双签 interchangeable。304 vote-ts vs checked bundled unbundling 在本页 item 3 完成。

类型字节、链号长度、可恢复签编码是规范里的取值或做法，本页不抄。

## 官方为什么这样拆

- **断开 not already slashed ≠ 已经罚了签的人 interchangeable：** 官方把对等路径踢人和验证者惩罚分开。
- **看见非法 not already on-chain ≠ 已经上链 interchangeable：** 官方把非法和已经上链分开。
- **看见没过基本校验 not already doublesign ≠ 已经是双签 interchangeable：** 官方把没过基本校验和已经是双签分开；304 vote-ts vs checked bundled unbundling 在本页 item 3 完成。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 非法被断开 | 不是已经罚了签的人 | 不是签名器已经记住上次高度轮类型（19） |
| 看见非法 | 不是已经上链 | 不是证据窗已经盖住解绑（46） |
| 看见没过基本校验 | 不是已经是双签 | 不是带了 Timestamp 就已经验过（998） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看断开 not already slashed / not already on-chain / not already doublesign 正式三事（304 余量），必须分开是不是已经罚了、是不是已经上链、是不是已经是双签。可以跳过「看见签过就已经验过时间」。不要另写怎样记上次签过的高度轮类型。不要写 amnesia 分类。304 vote-ts vs checked bundled unbundling 在本页 item 3 完成。

## 本页不抄

- 类型字节、链号长度、可恢复签编码、1 ms 增量。
- 签字校验 bundled。那是不变量 304。
- 签名器已经记住上次高度轮类型。那是不变量 19。
- 证据窗已经盖住解绑。那是不变量 46。
- amnesia 分类、解锁谓词。
