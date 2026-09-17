# 模式：把 Commit Usage all nodes remove historical blocks not bootstrap from genesis / not non-zero retain is pruning / not entered consensus has full history 正式三事（491 余量）说成三个名字

**层次**：实现 / 命名。  
**分类**：事实（官方拆法）+ 建议（产品）。  
**来源**：[ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) Commit Usage。  
**例**：[all nodes remove not genesis bootstrap ≠ bundled（491）](../../tracks/implementation/worked-example-commitretaincaution-notgenesis-vs-bundled.md)。

## 三个名字

1. **all nodes remove historical blocks 不是已经能从创世再装：** 看见全网删历史的后果，不是已经从创世装 interchangeable，不是 366 / 323 / 38 interchangeable / 693 commitretaincaution-notgenesis interchangeable。
2. **看见 permanently lost / unless state sync 不是非零 retain 就等于已经在剪：** 看见全网后果，不是已经回了非零高度就等于已经在剪 interchangeable。
3. **看见 no new nodes bootstrap 不是切进共识就已经有完整历史：** 看见 unless state sync，不是已经 323 snaptransition interchangeable。

官方把 Commit Usage 全网后果、从创世再装、非零高度就等于已经在剪、切进共识就有完整历史写成三个名字。把它们叫成一个「看见 caution 段落就已经能从创世再装」，会把 not genesis bootstrap、not non-zero retain is pruning、not entered consensus has full history 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Commit Usage all nodes remove 正式三事（491 余量），先数清问的是 all nodes remove 是不是已经能从创世再装 / 366 / 38、是不是非零高度就等于已经在剪、还是看见 unless state sync 是不是切进共识就有完整历史 / 323，再决定要不要同一次发布。491 commitretaincaution vs kept bundled unbundling 在本页 item 2 续。
