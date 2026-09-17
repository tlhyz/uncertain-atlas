# 例：看见 app decide accept or different one is not already Response empty/not empty rule interchangeable / not already InitChain Usage remainder bundled interchangeable / not already genesis app_state already verified interchangeable

**层次**：实现 / InitChain Usage app decide accept or different one not Response empty/not empty rule / not InitChain Usage remainder bundled / not genesis app_state already verified 正式三事（496 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) InitChain Usage。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「InitChain Usage app decide accept or different one not Response empty/not empty rule / not InitChain Usage remainder bundled / not genesis app_state already verified 正式三事（496 余量）/ not 698 initchaindecide-notrule interchangeable / not 496 initchainusage-decide-vs-emptyset bundled interchangeable」，不是 InitChain Usage app decide 正式三事 bundled（496），也不是 InitChain Usage part 1（495）或余量（412）。不要另写怎样写 InitChain。

## 官方三件事

1. **看见 This allows the app to decide if it wants to accept the initial validator set proposed by CometBFT (ie. in the genesis file), or if it wants to use a different one (perhaps computed based on some application specific information in the genesis file) / 看见应用可以决定接受创世验证者集合或用创世应用信息算出另一套 / decide is not already 已经 If InitChainResponse.Validators is empty / not empty 规则（495） interchangeable / 495 initchainusage interchangeable / 696 initchainusage-notempty interchangeable / 697 initchainusage-notnonempty interchangeable，也不是已经 InitChain Usage app decide 正式三事 bundled（496） interchangeable / 698 initchaindecide-notrule interchangeable / 699 initchaindecide-notchanged interchangeable / 496 initchaindecide item 2 both ValidatorUpdate interchangeable，也不是已经 app decide not Response empty/not empty rule / not InitChain Usage remainder bundled / not genesis app_state already verified 正式三事 bundled（496 item 1 余量） interchangeable / 496 initchaindecide item 1 interchangeable。**  
   官方 Usage 写：This allows the app to decide if it wants to accept the initial validator set … or use a different one。看见 app can decide，不是已经 495 empty/not empty 规则 interchangeable——495 钉 response 规则，本页从 496 item 1 侧钉 not Response rule 单句。496 initchaindecide vs emptyset bundled unbundling 在本页 item 1 启动。

2. **看见 app decide accept or different one / 看见 accept proposed by CometBFT or use different one / 看见 Usage 这句 is not already 已经 InitChain Usage 余量 bundled（412）第二件事 bundled 就代表已经用了创世文件里的验证者 interchangeable / 412 initonce interchangeable，也不是已经 InitChain Usage app decide 正式三事 bundled（496） interchangeable / 698 initchaindecide-notrule interchangeable / 496 initchaindecide item 3 from empty interchangeable / 700 initchaindecide-notfromempty interchangeable。**  
   官方把 Usage app decide 单句和 412 余量 bundled 第二件事分开——496 bundled 第一件事常与 412 混成「看见 decide 就已经用了创世文件里的验证者 interchangeable」，本页钉 not remainder bundled 单句。

3. **看见 computed based on application specific information / 看见 Usage 这句 / 看见 decide is not already 已经 InitChain 创世 app_state 就已经验过应用状态（303） interchangeable / 303 genesis interchangeable，也不是已经 InitChain Usage app decide 正式三事 bundled（496） interchangeable / 698 initchaindecide-notrule interchangeable / 699 initchaindecide-notchanged interchangeable。**  
   官方把 Usage app decide 单句和创世 app_state 就已经验过路径分开——496 bundled 第一件事常与 303 混成「看见 decide 就已经验过应用状态 interchangeable」，本页钉 not genesis app_state already verified 单句。496 initchaindecide vs emptyset bundled unbundling 在本页 item 1 启动。

怎样写 InitChain、怎样决定接受创世集合、怎样从空集合更新是规范里的做法，本页不抄。

## 官方为什么这样拆

- **app decide not Response empty/not empty rule ≠ 495 interchangeable：** 官方把 app 决定接受或算另一套和 response 空/非空规则分开。
- **app decide not InitChain Usage remainder bundled ≠ 412 interchangeable：** 官方把 Usage decide 单句和 412 余量 bundled 第二件事分开。
- **app decide not genesis app_state already verified ≠ 303 interchangeable：** 官方把 Usage decide 单句和创世 app_state 就已经验过路径分开；496 initchaindecide vs emptyset bundled unbundling 在本页 item 1 启动。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| app decide accept or different one | 不是 Response empty/not empty 规则（495） | 不是 both ValidatorUpdate（699/496 item 2） |
| 看见 accept or different one | 不是 InitChain Usage 余量 bundled（412） | 不是 InitChain Usage part 1 bundled（495） |
| 看见 Usage 这句 | 不是创世 app_state 就已经验过（303） | 不是 updating from empty set（700/496 item 3） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 InitChain Usage app decide accept or different one not Response empty/not empty rule / not InitChain Usage remainder bundled / not genesis app_state already verified 正式三事（496 余量），必须分开 decide 是不是 495 response 规则 interchangeable、是不是 412 bundled interchangeable、是不是创世 app_state 就已经验过 interchangeable / 303。可以跳过「看见 InitChain 了就已经 Response 规则」。不要另写怎样写 InitChain。496 initchaindecide vs emptyset bundled unbundling 在本页 item 1 启动；续 [`worked-example-initchaindecide-notchanged-vs-bundled.md`](worked-example-initchaindecide-notchanged-vs-bundled.md)（不变量 699 item 2）。

## 本页不抄

- 怎样写 InitChain、怎样决定接受创世集合、怎样从空集合更新。
- InitChain Usage app decide 正式三事 bundled。那是不变量 496。
- Both Validators are ValidatorUpdate。那是不变量 496 item 2 余量 / 699。
- updating from empty set。那是不变量 496 item 3 余量 / 700。
- InitChain Usage 正式三事 part 1。那是不变量 495。
- InitChain Usage 余量 bundled。那是不变量 412。
