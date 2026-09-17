# 模式：把 InitChain Usage Response Validators not empty regardless of Request not app can decide bundled / not empty list means no set / not duplicate pubkeys already recoverable 正式三事（495 余量）说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) InitChain Usage。  
**例**：[not empty regardless of Request not can decide ≠ bundled（495）](../../tracks/implementation/worked-example-initchainusage-notnonempty-vs-bundled.md)。

## 三个名字

1. **Response Validators not empty regardless of Request 不是应用 can decide bundled：** 看见 not empty 无视 request，不是已经 412 / 496 interchangeable / 697 initchainusage-notnonempty interchangeable。
2. **看见 not empty → Response 不是空名单就没有集合：** 看见 not empty 路径，不是已经 318 interchangeable。
3. **看见 Usage 这句 不是重复公钥就已经能恢复：** 看见 regardless of Request，不是已经 318 bundled 第二件事 interchangeable。

官方把 InitChain Usage not empty 规则、应用 can decide bundled、空名单语义、重复公钥就已经能恢复写成三个名字。把它们叫成一个「看见 InitChain 了就已经改了集合」，会把 not app can decide bundled、not empty list means no set、not duplicate pubkeys already recoverable 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 InitChain Usage not empty 正式三事（495 余量），先数清问的是 not empty 是不是应用 can decide bundled / 412 / 496、是不是空名单就没有集合 / 318、还是看见 Usage 是不是重复公钥就已经能恢复，再决定要不要同一次发布。495 initchainusage vs bundled unbundling 在本页 item 3 完成。
