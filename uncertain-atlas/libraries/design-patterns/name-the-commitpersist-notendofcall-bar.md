# 模式：把 Expected persist at end of this call not Signal persist application state / not Commit empty request bundled / not signal already settled 正式三事（481 余量）说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) Commit Usage。  
**例**：[Expected persist at end of this call not Commit empty request bundled ≠ bundled（481）](../../tracks/implementation/worked-example-commitpersist-notendofcall-vs-bundled.md)。

## 三个名字

1. **Expected persist at end 不是 Signal persist application state：** 看见 Methods Usage 侧 before returning from Commit，不是已经 Signal persist application state interchangeable，不是 680 commitpersist-notfinpersist interchangeable / 481 commitpersist item 1 persist signal interchangeable / 335 finpersist item 2 interchangeable。

2. **before returning from Commit 不是 Commit empty request bundled：** 看见 expected persist at end，不是已经 Commit Request 不带参数 interchangeable / 已经 Commit 空请求 bundled interchangeable / 已经能叫 Commit 就等于已经落盘 interchangeable，不是 399 commit-empty-echo bundled interchangeable / 399 commitnoparam interchangeable。

3. **返回前落盘 不是 signal already settled：** 看见 Application is expected to persist at end of this call，不是已经 signal 就已经交差 interchangeable / 已经 Finalize + Commit interchangeable / 已经四门已经结算 interchangeable，不是 33 four gates interchangeable / 403 finafter interchangeable / 682 commitpersist-nothistoricalblocks interchangeable。

官方把 Commit Usage expected persist at end 单句、Signal persist application state（680）、Commit empty request bundled（399）、signal already settled / Historical blocks required（682）写成三个名字。把它们叫成一个「看见 expected persist at end 就已经 Signal persist interchangeable / 就已经 Commit 不带参数 interchangeable / 就已经 signal 就已经交差 interchangeable」，会把 not Signal persist application state、not Commit empty request bundled、not signal already settled 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Expected persist at end of this call not Signal persist application state / not Commit empty request bundled / not signal already settled 正式三事（481 余量），先数清问的是 expected persist at end 是不是 Signal persist / 680 / 335 item 2，是不是 before returning from Commit 是不是 Commit empty request bundled / 399 / 492，还是返回前落盘 是不是 signal already settled / 33 / 403 / 682，再决定要不要同一次发布。481 commitpersist vs finalize bundled unbundling 在本页 item 2 完成。
