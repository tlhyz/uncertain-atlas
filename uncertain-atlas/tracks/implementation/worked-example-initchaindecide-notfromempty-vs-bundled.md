# 例：看见 updating the validator set from the empty set is not already empty list means no set interchangeable / not already Response empty/not empty rule interchangeable / not already app decide already used genesis validators interchangeable

**层次**：实现 / InitChain Usage updating from empty set not empty list means no set / not Response empty/not empty rule / not app decide already used genesis validators 正式三事（496 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) InitChain Usage。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「InitChain Usage updating from empty set not empty list means no set / not Response empty/not empty rule / not app decide already used genesis validators 正式三事（496 余量）/ not 700 initchaindecide-notfromempty interchangeable / not 496 initchainusage-decide-vs-emptyset bundled interchangeable」，不是 InitChain Usage app decide 正式三事 bundled（496），也不是空名单就没有集合（318）或 InitChain Usage part 1（495）。不要另写怎样写 InitChain。

## 官方三件事

1. **看见 So, technically, they both are _updating_ the validator set from the empty set / 看见技术上是从空集合更新 / updating is not already 已经 InitChain 回了空名单就没有集合（318） interchangeable / 318 emptyset interchangeable，也不是已经 InitChain Usage app decide 正式三事 bundled（496） interchangeable / 700 initchaindecide-notfromempty interchangeable / 698 initchaindecide-notrule interchangeable / 496 initchaindecide item 1 decide interchangeable，也不是已经 updating from empty set not empty list means no set / not Response empty/not empty rule / not app decide already used genesis validators 正式三事 bundled（496 item 3 余量） interchangeable / 496 initchaindecide item 3 interchangeable。**  
   官方 Usage 写：So, technically, they both are updating the validator set from the empty set。看见 updating from the empty set，不是已经空名单就没有集合 interchangeable——318 钉空名单语义，本页从 496 item 3 侧钉 not empty list means no set 单句。496 initchaindecide vs emptyset bundled unbundling 在本页 item 3 完成。

2. **看见 technically both are updating / 看见 from the empty set / 看见 Usage 这句 is not already 已经 Response Validators empty/not empty 规则（495） interchangeable / 495 initchainusage interchangeable / 696 initchainusage-notempty interchangeable，也不是已经 InitChain Usage app decide 正式三事 bundled（496） interchangeable / 700 initchaindecide-notfromempty interchangeable / 496 initchaindecide item 2 both ValidatorUpdate interchangeable / 699 initchaindecide-notchanged interchangeable。**  
   官方把 Usage 从空集合更新和 495 response 规则分开——496 bundled 第三件事常与 495 混成「看见 from the empty set 就已经 empty → Request interchangeable」，本页钉 not Response empty/not empty rule 单句。

3. **看见 from the empty set / 看见 Usage 这句 / updating is not already 已经 app decide accept or different one 就已经用了创世文件里的验证者 interchangeable / 412 bundled 第三件事 interchangeable / 698 initchaindecide-notrule interchangeable，也不是已经 InitChain Usage app decide 正式三事 bundled（496） interchangeable / 700 initchaindecide-notfromempty interchangeable / 698 initchaindecide-notrule interchangeable。**  
   官方把 Usage 从空集合更新和 app decide 就已经用了创世文件里的验证者路径分开。看见 from the empty set，不是已经改了集合 interchangeable。496 initchaindecide vs emptyset bundled unbundling 在本页 item 3 完成。

怎样写 InitChain、怎样决定接受创世集合、怎样从空集合更新是规范里的做法，本页不抄。

## 官方为什么这样拆

- **updating from empty set not empty list means no set ≠ 318 interchangeable：** 官方把从空集合更新和空名单语义分开。
- **updating from empty set not Response empty/not empty rule ≠ 495 interchangeable：** 官方把 Usage empty set 更新语义和 response 空/非空规则分开。
- **updating from empty set not app decide already used genesis validators ≠ 412 bundled item 3 interchangeable：** 官方把 Usage 从空集合更新和 decide 就已经用了创世验证者路径分开；496 initchaindecide vs emptyset bundled unbundling 在本页 item 3 完成。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| updating from empty set | 不是空名单就没有集合（318） | 不是 app decide 单句（698/496 item 1） |
| 看见 technically both are updating | 不是 Response empty/not empty 规则（495） | 不是 both ValidatorUpdate（699/496 item 2） |
| 看见 Usage 这句 | 不是 app decide 就已经用了创世验证者 | 不是已经改了集合（364） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 InitChain Usage updating from empty set not empty list means no set / not Response empty/not empty rule / not app decide already used genesis validators 正式三事（496 余量），必须分开 updating from empty set 是不是空名单就没有集合 interchangeable / 318、是不是 495 response 规则 interchangeable、是不是 app decide 就已经用了创世验证者。可以跳过「看见 InitChain 了就已经没有集合」。不要另写怎样写 InitChain。496 initchaindecide vs emptyset bundled unbundling 在本页 item 3 完成。

## 本页不抄

- 怎样写 InitChain、怎样决定接受创世集合、怎样从空集合更新。
- InitChain Usage app decide 正式三事 bundled。那是不变量 496。
- app decide accept or different one。那是不变量 496 item 1 余量 / 698。
- Both Validators are ValidatorUpdate。那是不变量 496 item 2 余量 / 699。
- InitChain Usage 正式三事 part 1。那是不变量 495。
- InitChain 回了空名单就已经没有集合。那是不变量 318。
