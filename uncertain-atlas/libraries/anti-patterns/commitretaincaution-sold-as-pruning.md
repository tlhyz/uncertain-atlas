# 反模式：把 Commit Usage retain_height caution 正式三事卖成已经在剪 / 已经能从创世再装 / persist signal 已经交差

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[Use retain_height with caution ≠ retain_height 默认 0 就等于已经在剪](../../tracks/implementation/worked-example-commitretaincaution-vs-kept.md)。

## 卖法

- 「看见 Use CommitResponse.retain_height with caution / 要慎用 retain_height 就已经 retain_height 默认 0 全留 interchangeable / 已经 blocks below may be removed 那种回了高度就等于已经在剪 / persist signal bundled 第三件事 interchangeable。」
- 「看见 all nodes remove historical blocks / permanently lost / no new nodes bootstrap unless state sync 就已经能从创世再装 / 已经开了 state sync 就交差 / 已经切进共识就有完整历史。」
- 「看见 Historical blocks may also be required for auditing / replay / light client verification 就已经 persist signal bundled interchangeable / 已经 retain_height 默认 0 就等于已经在剪 / caution 已经验完。」

## 为什么错

官方把 Use retain_height with caution、If all nodes remove historical blocks …、Historical blocks may also be required … 写成三件独立的实现事。把它们卖成已经在剪 / 已经能从创世再装 / persist signal 已经交差，会把 caution 语气、全网后果、other purposes 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Commit Usage retain_height caution，必须分开 Use retain_height with caution、all nodes remove historical blocks → permanently lost / no bootstrap unless state sync、Historical blocks required for auditing / replay / light client 三个名字，不要把它们卖成已经在剪 / 已经能从创世再装 / persist signal 已经交差。

## 和相邻反模式

- [retain-sold-as-pruned](retain-sold-as-pruned.md) 是 Commit 保留高度 bundled 全段，不是本页 Usage retain_height caution 专用三事。
- [commitpersist-sold-as-finalize](commitpersist-sold-as-finalize.md) 是 persist signal 就等于已经在 Finalize 落了，不是本页 caution 段 Historical blocks 专用边界。
- [commitnoparam-sold-as-persist](commitnoparam-sold-as-persist.md) 是 Commit 不带参数就等于已经落盘，不是本页 with caution 单句。
