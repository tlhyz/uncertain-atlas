# 反模式：把 ProcessProposal REJECT prevote nil not Verify whole vote 正式三事卖成 Process REJECT consensus assume bundled / 已经 Verify REJECT whole vote / 已经 Process 回包栏 bundled

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[ProcessProposal REJECT prevote nil not Verify whole vote ≠ bundled](../../tracks/implementation/worked-example-procreject-prevote-notverify-vs-bundled.md)。

## 卖法

- 「看见验证者会 prevote nil / 看见 When 里 REJECT: _p_ prevotes nil 就已经 Verify REJECT whole vote interchangeable / 已经 Process REJECT consensus assume bundled interchangeable。」
- 「看见 prevote nil 就已经 Process 回包栏 bundled interchangeable / 已经 status 必须只依赖 interchangeable / 已经 MUST Accept interchangeable。」
- 「看见 REJECT 后 prevote nil 就已经 async Process 之后还能 Reject interchangeable / 已经 REJECT 是免费过滤 interchangeable。」

## 为什么错

官方把 Process prevote nil not Verify whole vote、prevote nil not Process resp bundled、prevote nil not async can still Reject 写成三件独立的实现事。把它们卖成 Process REJECT consensus assume bundled、已经 Verify REJECT whole vote、已经 Process 回包栏 bundled，会把 Verify 拒整张票、Process 回包栏 bundled、async 之后还能 Reject 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 ProcessProposal REJECT prevote nil not Verify whole vote 正式三事，必须分开 Process prevote nil not Verify whole vote、prevote nil not Process resp bundled、prevote nil not async can still Reject 三个名字，不要把它们卖成 Process REJECT consensus assume bundled / 已经 Verify REJECT whole vote / 已经 Process 回包栏 bundled。

## 和相邻反模式

- [procreject-assume-notblockinvalid-sold-as-bundled](procreject-assume-notblockinvalid-sold-as-bundled.md) 是 assumes not valid not block invalid 单句边界，不是本页 When prevote nil 边界。
- [procreject-sold-as-invalid](procreject-sold-as-invalid.md) 是 455 bundled 三事专用，不是本页 prevote nil not Verify whole vote 单句边界。
- [verifystatus-reject-sold-as-bundled](verifystatus-reject-sold-as-bundled.md) 是 VerifyStatus REJECT rejects whole vote 专用，不是本页 Process prevote nil 边界。
