# 模式：把 FinalizeBlockResponse next_block_delay each node MAY / wallclock not app_hash MUST be deterministic / not whole response nondeterministic 正式三事（589 余量）说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) FinalizeBlock Response / Usage `next_block_delay`。  
**例**：[FinalizeBlockResponse next_block_delay each node MAY / wallclock not app_hash MUST be deterministic ≠ bundled（589）](../../tracks/implementation/worked-example-fndelay-notwallclock-vs-bundled.md)。

## 三个名字

1. **each node MAY / wallclock 不是 app_hash MUST be deterministic：** 看见各节点可以回不同值，不是已经 app_hash MUST be deterministic interchangeable，不是 470 findet interchangeable / 476 finharddet interchangeable / 404 finapphash interchangeable。
2. **each node MAY / wallclock 不是整门非确定：** 看见 MAY / wallclock，不是已经 Finalize 回包整门非确定 interchangeable，不是 470 findet bundled interchangeable / 581 findet not replication interchangeable / 611 notproctime interchangeable。
3. **each node MAY / wallclock 不是 fndelay bundled：** 看见各节点可以回不同值，不是已经 fndelay bundled interchangeable，不是 617 notslot interchangeable / 619 notsetzero interchangeable / 589 fndelay item 1 Deterministic = No interchangeable / 589 fndelay item 3 set to 0 interchangeable。

## 为什么要分开叫

官方把 Usage 里 each node MAY 回不同值 / depends on local processing / wallclock、Response 表 Deterministic = No、Set to 0 when all precommits and block processed 写成三个名字。把它们叫成一个「看见 MAY 回不同值 就已经 app_hash MUST be deterministic interchangeable、就已经整门非确定 interchangeable」，会把 not app_hash MUST be deterministic、not whole response nondeterministic、not fndelay bundled 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 FinalizeBlockResponse next_block_delay each node MAY / wallclock not app_hash MUST be deterministic / not whole response nondeterministic 正式三事（589 余量），先数清问的是 each node MAY / wallclock 是不是 already app_hash MUST be deterministic / 470 / 476，是不是 already 整门非确定 / 470 bundled / 581，还是 each node MAY / wallclock 是不是 already fndelay bundled / 617 / 619，再决定要不要同一次发布。
