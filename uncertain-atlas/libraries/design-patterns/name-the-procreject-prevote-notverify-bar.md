# 模式：把 ProcessProposal REJECT prevote nil not Verify whole vote 正式三事说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) ProcessProposal When。  
**例**：[ProcessProposal REJECT prevote nil not Verify whole vote ≠ bundled](../../tracks/implementation/worked-example-procreject-prevote-notverify-vs-bundled.md)。

## 三个名字

1. **Process prevote nil not Verify whole vote 不是 Process REJECT consensus assume bundled：** 看见 When 里 REJECT 后 prevote nil 不是已经 Verify REJECT whole vote，不是 455 bundled interchangeable / 433 whole vote interchangeable / 539 VerifyStatus REJECT interchangeable。
2. **prevote nil not Process resp bundled 不是 status must exclusively depend：** 看见 prevote nil 不是已经 Process 回包栏 bundled interchangeable，不是 455 bundled interchangeable / 430 status must exclusively depend interchangeable / 533 valid/invalid interchangeable。
3. **prevote nil not async can still Reject 不是 REJECT free filter：** 看见 REJECT 后 prevote nil 不是已经 async Process 之后还能 Reject interchangeable，不是 455 bundled interchangeable / 354 async can still Reject interchangeable / 33 free filter interchangeable。

## 为什么要分开叫

官方把 ProcessProposal REJECT prevote nil not Verify whole vote 写成三个名字。把它们叫成一个「看见 Process 回了 REJECT 就已经 Verify REJECT whole vote interchangeable」，会把 Verify 拒整张票、Process 回包栏 bundled、async 之后还能 Reject 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 ProcessProposal REJECT prevote nil not Verify whole vote 正式三事，先数清问的是 Process prevote nil 是不是 Verify REJECT whole vote、prevote nil 是不是 Process resp bundled interchangeable、REJECT after prevote nil 是不是 async can still Reject / 33 free filter interchangeable，再决定要不要同一次发布。
