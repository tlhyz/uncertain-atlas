# 例：看见 Both Request and Response Validators are ValidatorUpdate is not already ValidatorUpdate already changed set interchangeable / not already empty list means no set interchangeable / not already Validator without PubKey already has PubKey interchangeable

**层次**：实现 / InitChain Usage Both Validators are ValidatorUpdate not already changed set / not empty list means no set / not Validator without PubKey already has PubKey 正式三事（496 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) InitChain Usage。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「InitChain Usage Both Validators are ValidatorUpdate not already changed set / not empty list means no set / not Validator without PubKey already has PubKey 正式三事（496 余量）/ not 699 initchaindecide-notchanged interchangeable / not 496 initchainusage-decide-vs-emptyset bundled interchangeable」，不是 InitChain Usage app decide 正式三事 bundled（496），也不是 ValidatorUpdate 已经改了集合（364）或空名单就没有集合（318）。不要另写怎样写 InitChain。

## 官方三件事

1. **看见 Both `InitChainRequest.Validators` and `InitChainResponse.Validators` are [ValidatorUpdate](#validatorupdate) structs / 看见 Request 和 Response 的 Validators 都是 ValidatorUpdate / both is not already 已经 ValidatorUpdate 用公钥认人就已经改了集合（364） interchangeable / 364 validatorupdate interchangeable，也不是已经 InitChain Usage app decide 正式三事 bundled（496） interchangeable / 699 initchaindecide-notchanged interchangeable / 698 initchaindecide-notrule interchangeable / 496 initchaindecide item 1 decide interchangeable，也不是已经 Both Validators are ValidatorUpdate not already changed set / not empty list means no set / not Validator without PubKey already has PubKey 正式三事 bundled（496 item 2 余量） interchangeable / 496 initchaindecide item 2 interchangeable。**  
   官方 Usage 写：Both InitChainRequest.Validators and InitChainResponse.Validators are ValidatorUpdate structs。看见 both are ValidatorUpdate，不是已经改了集合 interchangeable——364 钉 ValidatorUpdate 语义，本页从 496 item 2 侧钉 not already changed set 单句。496 initchaindecide vs emptyset bundled unbundling 在本页 item 2 续。

2. **看见 Request 和 Response 都是 ValidatorUpdate / 看见 Usage 这句 / both is not already 已经 InitChain 回了空名单就没有集合（318） interchangeable / 318 emptyset interchangeable，也不是已经 InitChain Usage app decide 正式三事 bundled（496） interchangeable / 699 initchaindecide-notchanged interchangeable / 496 initchaindecide item 3 from empty interchangeable / 700 initchaindecide-notfromempty interchangeable。**  
   官方把 Usage both are ValidatorUpdate 单句和空名单就没有集合路径分开——496 bundled 第二件事常与 318 混成「看见两边都是 ValidatorUpdate 就已经没有集合 interchangeable」，本页钉 not empty list means no set 单句。

3. **看见两边都是 ValidatorUpdate 列表 / 看见 Usage 这句 / both is not already 已经 Validator 不带 PubKey 就已经带了公钥（364 bundled 第二件事） interchangeable / 已经 Finalize validator_updates 就已经改了集合 interchangeable，也不是已经 InitChain Usage app decide 正式三事 bundled（496） interchangeable / 699 initchaindecide-notchanged interchangeable / 698 initchaindecide-notrule interchangeable。**  
   官方把 Usage both are ValidatorUpdate 单句和 Validator 不带 PubKey 就已经带了公钥路径分开。看见两边都是 ValidatorUpdate，不是已经 Finalize validator_updates 就已经改了集合 interchangeable。496 initchaindecide vs emptyset bundled unbundling 在本页 item 2 续。

怎样写 InitChain、怎样决定接受创世集合、怎样从空集合更新是规范里的做法，本页不抄。

## 官方为什么这样拆

- **both ValidatorUpdate not already changed set ≠ 364 interchangeable：** 官方把两边都是 ValidatorUpdate 结构和已经改了集合分开。
- **both ValidatorUpdate not empty list means no set ≠ 318 interchangeable：** 官方把 Usage struct 类型和空名单语义分开。
- **both ValidatorUpdate not Validator without PubKey already has PubKey ≠ 364 bundled item 2 interchangeable：** 官方把 Usage both are ValidatorUpdate 和 Validator 不带 PubKey 就已经带了公钥分开；496 initchaindecide vs emptyset bundled unbundling 在本页 item 2 续。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| Both Validators are ValidatorUpdate structs | 不是已经改了集合（364） | 不是 app decide 单句（698/496 item 1） |
| 看见两边都是 ValidatorUpdate | 不是空名单就没有集合（318） | 不是 updating from empty set（700/496 item 3） |
| 看见 Usage 这句 | 不是 Validator 不带 PubKey 就已经带了公钥 | 不是 Finalize validator_updates 就已经改了集合 |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 InitChain Usage Both Validators are ValidatorUpdate not already changed set / not empty list means no set / not Validator without PubKey already has PubKey 正式三事（496 余量），必须分开 both are ValidatorUpdate 是不是已经改了集合 interchangeable / 364、是不是空名单就没有集合 interchangeable / 318、是不是 Validator 不带 PubKey 就已经带了公钥。可以跳过「看见 InitChain 了就已经改了集合」。不要另写怎样写 InitChain。496 initchaindecide vs emptyset bundled unbundling 在本页 item 2 续；完成 [`worked-example-initchaindecide-notfromempty-vs-bundled.md`](worked-example-initchaindecide-notfromempty-vs-bundled.md)（不变量 700 item 3）。

## 本页不抄

- 怎样写 InitChain、怎样决定接受创世集合、怎样从空集合更新。
- InitChain Usage app decide 正式三事 bundled。那是不变量 496。
- app decide accept or different one。那是不变量 496 item 1 余量 / 698。
- updating from empty set。那是不变量 496 item 3 余量 / 700。
- ValidatorUpdate 用公钥认人就已经改了集合。那是不变量 364。
- InitChain 回了空名单就已经没有集合。那是不变量 318。
