# 模式：把 InitChain Usage Both Validators are ValidatorUpdate not already changed set / not empty list means no set / not Validator without PubKey already has PubKey 正式三事（496 余量） 说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) InitChain Usage。  
**例**：[both ValidatorUpdate not changed set ≠ bundled（496）](../../tracks/implementation/worked-example-initchaindecide-notchanged-vs-bundled.md)。

## 三个名字

1. **Both Validators are ValidatorUpdate 不是已经改了集合：** 看见两边都是 ValidatorUpdate，不是已经 364 interchangeable / 699 initchaindecide-notchanged interchangeable。
2. **看见两边都是 ValidatorUpdate 不是空名单就没有集合：** 看见 struct 类型，不是已经 318 interchangeable。
3. **看见 Usage 这句 不是 Validator 不带 PubKey 就已经带了公钥：** 看见 both are ValidatorUpdate，不是已经 364 bundled 第二件事 interchangeable。

官方把 InitChain Usage 后三条核心句拆成三个名字。把它们叫成一个「看见 InitChain 了就已经 Response 规则 / 已经改了集合 / 已经没有集合」，会把三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 InitChain Usage both ValidatorUpdate 正式三事（496 余量），先数清问的是 both are ValidatorUpdate 是不是已经改了集合 / 364、是不是空名单就没有集合 / 318、还是看见 Usage 是不是 Validator 不带 PubKey 就已经带了公钥，再决定要不要同一次发布。496 initchaindecide vs emptyset bundled unbundling 在本页 item 2 续。
