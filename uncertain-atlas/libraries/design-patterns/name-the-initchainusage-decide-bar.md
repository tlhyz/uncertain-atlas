# 模式：把 InitChain Usage app decide / ValidatorUpdate from empty set 正式三事说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) InitChain Usage。  
**例**：[app decide accept or different one ≠ Response 规则](../../tracks/implementation/worked-example-initchainusage-decide-vs-emptyset.md)。

## 三个名字

1. **app decide accept or different one 不是 Response empty/not empty 规则：** 看见 Methods InitChain Usage app decide，不是 495 response 规则 interchangeable。
2. **Both Validators are ValidatorUpdate structs 不是已经改了集合：** 看见两边都是 ValidatorUpdate，不是 364 已经改了集合 interchangeable。
3. **updating from empty set 不是空名单就没有集合：** 看见从空集合更新，不是 318 空名单 interchangeable。

## 为什么要分开叫

官方把 InitChain Usage 后三条、InitChain Usage 正式三事 part 1（495）、InitChain Usage 余量 bundled（412）、InitChain 空名单（318）写成三个名字。把它们叫成一个「看见 InitChain 了就已经 Response 规则 interchangeable、已经改了集合、已经没有集合」，会把 app decide、ValidatorUpdate 结构、empty set 更新三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 InitChain Usage app decide / ValidatorUpdate from empty set 正式三事，先数清问的是 app decide accept or different one 是不是 Response 规则 interchangeable / 已经用了创世文件里的验证者、Both Validators are ValidatorUpdate 是不是已经改了集合 interchangeable、updating from empty set 是不是空名单就没有集合 interchangeable，再决定要不要同一次发布。
