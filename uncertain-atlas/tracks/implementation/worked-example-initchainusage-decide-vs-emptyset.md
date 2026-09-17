# 例：看见 This allows the app to decide to accept the initial validator set or use a different one 不是已经 Response Validators empty/not empty 规则 interchangeable；看见 Both InitChainRequest.Validators and InitChainResponse.Validators are ValidatorUpdate structs 不是已经 ValidatorUpdate 用公钥认人就已经改了集合 interchangeable；看见 Technically updating the validator set from the empty set 不是已经 InitChain 回了空名单就没有集合 interchangeable

**层次**：实现 / InitChain Usage app decide / ValidatorUpdate from empty set 正式三事。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) InitChain Usage。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「app decide accept or different one 不是 Response empty/not empty 规则 interchangeable / Both Request and Response Validators are ValidatorUpdate 不是已经改了集合 / updating from empty set 不是空名单就没有集合」，不是 InitChain Usage 正式三事 part 1（495），也不是 InitChain Usage 余量 bundled（412）。不要另写怎样写 InitChain、怎样决定接受创世集合。

## 官方三件事

规范把 InitChain Usage 后三条核心英文句写成三件独立的实现事，不是「看见 InitChain 了就已经 Response 规则 interchangeable、已经改了集合、已经没有集合」一件事：

1. **看见 This allows the app to decide if it wants to accept the initial validator set proposed by CometBFT (ie. in the genesis file), or if it wants to use a different one (perhaps computed based on some application specific information in the genesis file) / 看见应用可以决定接受创世验证者集合或用创世应用信息算出另一套 不是已经 If InitChainResponse.Validators is empty / not empty 规则（495） interchangeable，也不是已经 InitChain Usage 余量 bundled（412）第二件事 bundled 就代表已经用了创世文件里的验证者 interchangeable，也不是已经 InitChain 创世 app_state 就已经验过应用状态（303） interchangeable。**  
   官方 Usage 写：This allows the app to decide if it wants to accept the initial validator set proposed by CometBFT (ie. in the genesis file), or if it wants to use a different one (perhaps computed based on some application specific information in the genesis file)。看见 app can decide accept or different one，不是已经 Response Validators empty → Request Validators（495 第二件事） interchangeable——495 钉 empty/not empty response 规则，本页钉 app decide 单句。看见 accept proposed by CometBFT or use different one，不是已经 Response not empty regardless of Request（495 第三件事） interchangeable。看见 computed based on application specific information，不是已经创世 app_state 就已经验过应用状态 interchangeable——303 钉 genesis app_state，本页钉 app decide 语境。
2. **看见 Both `InitChainRequest.Validators` and `InitChainResponse.Validators` are [ValidatorUpdate](#validatorupdate) structs / 看见 Request 和 Response 的 Validators 都是 ValidatorUpdate 不是已经 ValidatorUpdate 用公钥认人就已经改了集合（364） interchangeable，也不是已经 InitChain 回了空名单就没有集合（318） interchangeable，也不是已经 Validator 不带 PubKey 就已经带了公钥（364 bundled 第二件事） interchangeable。**  
   官方 Usage 写：Both `InitChainRequest.Validators` and `InitChainResponse.Validators` are [ValidatorUpdate](#validatorupdate) structs。看见 both are ValidatorUpdate structs，不是已经 ValidatorUpdate 用公钥认人就已经改了集合 interchangeable——364 钉 ValidatorUpdate 语义，本页钉 Usage both are ValidatorUpdate 单句。看见 Request 和 Response 都是 ValidatorUpdate，不是已经 InitChain 回了空名单就没有集合 interchangeable——318 钉空名单，本页钉 struct 类型。看见两边都是 ValidatorUpdate 列表，不是已经 Finalize validator_updates 就已经改了集合 interchangeable。
3. **看见 So, technically, they both are _updating_ the validator set from the empty set / 看见技术上是从空集合更新 不是已经 InitChain 回了空名单就没有集合（318） interchangeable，也不是已经 Response Validators empty/not empty 规则（495） interchangeable，也不是已经 app decide accept or different one 就已经用了创世文件里的验证者 interchangeable。**  
   官方 Usage 写：So, technically, they both are _updating_ the validator set from the empty set。看见 updating from the empty set，不是已经 InitChain 回了空名单就没有集合 interchangeable——318 钉空名单语义，本页钉 Usage 从空集合更新单句。看见 technically both are updating，不是已经 Response empty → Request（495） interchangeable——495 钉 response 规则，本页钉 empty set 更新语义。看见 from the empty set，不是已经 app decide 就已经改了集合 interchangeable——412 bundled 第三件事 bundled，本页钉 Usage 单句。

怎样写 InitChain、怎样决定接受创世集合、怎样从空集合更新是规范里的做法，本页不抄。InitChain Usage 正式三事 part 1（495）、InitChain Usage 余量 bundled（412）、InitChain 回了空名单就已经没有集合（318）、ValidatorUpdate 用公钥认人就已经改了集合（364）、创世 app_state 就已经验过应用状态（303）是另外那套，本页不抄。

## 官方为什么这样拆

- **app decide accept or different one ≠ Response empty/not empty 规则：** 官方把 app 决定接受或算另一套和 response 空/非空规则分开。
- **Both Request and Response Validators are ValidatorUpdate ≠ 已经改了集合：** 官方把两边都是 ValidatorUpdate 结构和已经改了集合分开。
- **updating from empty set ≠ 空名单就没有集合：** 官方把从空集合更新和空名单语义分开。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| app decide accept or different one | 不是 Response empty/not empty 规则 | 不是 InitChain Usage 余量 bundled（412） |
| Both Validators are ValidatorUpdate structs | 不是已经改了集合 | 不是空名单就没有集合（318） |
| updating from empty set | 不是空名单就没有集合 | 不是 Response empty → Request（495） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 InitChain Usage app decide / ValidatorUpdate from empty set 正式三事，必须分开 app decide accept or different one 是不是 Response 规则 interchangeable / 已经用了创世文件里的验证者、Both Validators are ValidatorUpdate 是不是已经改了集合 interchangeable、updating from empty set 是不是空名单就没有集合 interchangeable。可以跳过「看见 InitChain 了就已经 Response 规则 interchangeable、已经改了集合」。不要另写怎样写 InitChain。496 initchaindecide vs emptyset bundled unbundling 完成（698 item 1 / 699 item 2 / 700 item 3）；精读 [`worked-example-initchaindecide-notrule-vs-bundled.md`](worked-example-initchaindecide-notrule-vs-bundled.md)（不变量 698 item 1）。

## 本页不抄

- 怎样写 InitChain、怎样决定接受创世集合、怎样从空集合更新。
- InitChain Usage 正式三事 part 1。那是不变量 495。
- InitChain Usage 余量 bundled。那是不变量 412。
- InitChain 回了空名单就已经没有集合。那是不变量 318。
- ValidatorUpdate 用公钥认人就已经改了集合。那是不变量 364。
- 创世 app_state 就已经验过应用状态。那是不变量 303。
