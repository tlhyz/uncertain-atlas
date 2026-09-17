# 模式：把 InitChain Usage Called once upon genesis not crash then InitChain / not InitChain Usage remainder bundled / not process up is past genesis_time 正式三事（495 余量）说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) InitChain Usage。  
**例**：[once upon genesis not crash ≠ bundled（495）](../../tracks/implementation/worked-example-initchainusage-notcrash-vs-bundled.md)。

## 三个名字

1. **Called once upon genesis 不是崩溃后再调 InitChain：** 看见 Methods Usage 创世只调一次，不是已经崩溃恢复再调 interchangeable，不是 320 crash interchangeable / 695 initchainusage-notcrash interchangeable。
2. **看见创世时只调一次 不是 InitChain Usage 余量 bundled：** 看见 once，不是已经 412 bundled 第一件事 interchangeable。
3. **看见 Usage 这句 不是进程起来就已经过了 genesis_time：** 看见 once 单句，不是已经 303 genesis interchangeable。

官方把 InitChain Usage once、崩溃恢复再调、412 余量 bundled、进程起来就已经过了 genesis_time 写成三个名字。把它们叫成一个「看见 InitChain 了就已经崩溃后再调」，会把 not crash、not remainder bundled、not process up is past genesis_time 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 InitChain Usage once 正式三事（495 余量），先数清问的是 once 是不是崩溃后再调 / 320、是不是 412 bundled、还是看见 Usage 是不是进程起来就已经过了 genesis_time / 303，再决定要不要同一次发布。495 initchainusage vs bundled unbundling 在本页 item 1 启动。
