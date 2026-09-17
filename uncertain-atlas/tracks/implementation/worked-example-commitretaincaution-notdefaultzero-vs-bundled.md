# 例：看见 Use CommitResponse.retain_height with caution is not already retain_height defaults to 0 retain all interchangeable / blocks below height may be removed interchangeable / Commit Usage persist signal bundled interchangeable

**层次**：实现 / Commit Usage Use retain_height with caution not retain_height defaults to 0 retain all / not blocks below height may be removed / not Commit Usage persist signal bundled 正式三事（491 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) Commit Usage。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「Commit Usage Use retain_height with caution not retain_height defaults to 0 retain all / not blocks below height may be removed / not Commit Usage persist signal bundled 正式三事（491 余量）/ not 677 commitretaincaution-notdefaultzero interchangeable / not 491 commitretaincaution-vs-kept bundled interchangeable」，不是 Commit Usage retain_height caution 正式三事 bundled（491），也不是 Commit 保留高度 bundled（366）或 Commit Usage persist signal bundled（481）。不要另写怎样填 retain_height、怎样删块、怎样开 state sync。

## 官方三件事

规范把 Commit Usage 里 Use `CommitResponse.retain_height` with caution! 和「已经是 retain_height defaults to 0 (retain all)（366） interchangeable / 已经是 blocks below this height may be removed 那种回了高度就等于已经在剪 interchangeable / 已经是 Commit Usage persist signal（481） bundled 第三件事 interchangeable / 已经 caution 段落就已经在剪 interchangeable」分开写成三件独立的实现事，不是「看见 Use retain_height with caution 就已经 retain_height 默认 0 全留 interchangeable / 就已经 blocks below may be removed interchangeable / 就已经 persist signal bundled interchangeable」一件事：

1. **看见 Use `CommitResponse.retain_height` with caution! / 看见要慎用 retain_height / with caution is not already 已经 retain_height defaults to 0 (retain all)（366） interchangeable / 366 retain-height bundled interchangeable / 366 retain bundled item 1 interchangeable / 已经 default 0 retain all interchangeable / 已经 retain_height 默认 0 全留 interchangeable / 335 finpersist interchangeable，也不是已经 Commit Usage retain_height caution 正式三事 bundled（491） interchangeable / 677 commitretaincaution-notdefaultzero interchangeable / 491 commitretaincaution-vs-kept bundled interchangeable / 491 commitretaincaution item 2 all nodes remove interchangeable / 491 commitretaincaution item 3 Historical blocks interchangeable，也不是已经 Use retain_height with caution not retain_height defaults to 0 retain all / not blocks below height may be removed / not Commit Usage persist signal bundled 正式三事 bundled（491 item 1 余量） interchangeable / 491 commitretaincaution item 1 interchangeable，也不是已经 If all nodes remove historical blocks bundled（491 item 2 余量 / 678） interchangeable / 481 commitpersist bundled interchangeable / 492 echousage bundled interchangeable。**  
   官方 Usage 写：Use `CommitResponse.retain_height` with caution! 看见 with caution，不是已经 retain_height defaults to 0 retain all interchangeable——366 钉字段默认全留，本页从 491 item 1 侧钉 not defaults to 0 retain all 单句。看见要慎用 retain_height，不是已经 Commit Usage retain_height caution 正式三事 bundled（491） interchangeable——491 钉 bundled 三事，本页钉 Methods Commit Usage caution 语气单句。看见 caution 这句，不是已经 If all nodes remove historical blocks（491 item 2 余量） interchangeable——678 另钉 item 2，本页钉 item 1 第一件事。491 commitretaincaution vs kept bundled unbundling 在本页 item 1 启动。

2. **看见 Use retain_height with caution / 看见要慎用 retain_height / 看见 caution 段落 is not already 已经 blocks below this height may be removed 那种回了高度就等于已经在剪 interchangeable / 366 retain-height bundled interchangeable / 366 retain bundled item 2 interchangeable / 已经 blocks below may be removed interchangeable / 已经回了 retain_height 就等于已经在剪 interchangeable / 已经 non-zero retain_height 就等于已经在剪 interchangeable，也不是已经 Commit Usage retain_height caution 正式三事 bundled（491） interchangeable / 677 commitretaincaution-notdefaultzero interchangeable / 491 commitretaincaution item 1 with caution interchangeable / 491 commitretaincaution item 3 Historical blocks interchangeable，也不是已经 Use retain_height with caution not retain_height defaults to 0 retain all / not blocks below height may be removed / not Commit Usage persist signal bundled 正式三事 bundled（491 item 1 余量） interchangeable / 491 commitretaincaution item 1 interchangeable，也不是已经 Historical blocks required for auditing bundled（491 item 3 余量 / 679） interchangeable / 323 full-history interchangeable / 38 genesis-replay interchangeable，也不是已经 Commit 保留高度 bundled（366）第三件事 interchangeable / 587 finreturn interchangeable。**  
   官方把 Usage with caution 单句和 blocks below this height may be removed 路径分开——491 bundled 第一件事常与 366 混成「看见 Use retain_height with caution 就已经 blocks below may be removed interchangeable / 就已经回了高度就等于已经在剪 interchangeable / 就已经 non-zero retain_height 就等于已经在剪 interchangeable」，本页钉 not blocks below height may be removed 单句。看见 caution 段落，不是已经 blocks below this height may be removed interchangeable——366 钉字段语义第二件事，本页钉 caution 语气。看见要慎用 retain_height，不是已经 If all nodes remove historical blocks（678） interchangeable——678 另钉 item 2，本页钉 item 1 第二件事。

3. **看见 Use retain_height with caution / 看见 caution 段落 / 看见要慎用 retain_height is not already 已经 Commit Usage persist signal（481） bundled 第三件事 interchangeable / 481 commitpersist bundled interchangeable / 481 commitpersist item 3 Historical blocks interchangeable / 已经 Signal persist application state interchangeable / 已经 persist signal 就代表 caution 已经验完 interchangeable / 679 commitretaincaution-notpersist interchangeable，也不是已经 Commit Usage retain_height caution 正式三事 bundled（491） interchangeable / 677 commitretaincaution-notdefaultzero interchangeable / 491 commitretaincaution item 2 all nodes remove interchangeable / 491 commitretaincaution item 1 with caution interchangeable，也不是已经 Use retain_height with caution not retain_height defaults to 0 retain all / not blocks below height may be removed / not Commit Usage persist signal bundled 正式三事 bundled（491 item 1 余量） interchangeable / 491 commitretaincaution item 1 interchangeable，也不是已经 Historical blocks required for auditing bundled（491 item 3 余量 / 679） interchangeable / 665 infousage-notcommitpersist interchangeable / 497 infousage-persist interchangeable，也不是已经 retain_height defaults to 0 retain all bundled（366 item 1 余量） interchangeable / 335 finpersist interchangeable / 399 commit-empty-echo bundled interchangeable。**  
   官方把 Usage with caution 单句和 Commit Usage persist signal bundled 路径分开——491 bundled 第一件事常与 481 混成「看见 Use retain_height with caution 就已经 persist signal bundled interchangeable / 就已经 Signal persist application state interchangeable / 就已经 caution 已经验完 interchangeable」，本页钉 not Commit Usage persist signal bundled 单句。看见 caution 段落，不是已经 Commit Usage persist signal bundled interchangeable——481 钉 persist signal 语境，本页钉 caution 语气单句。看见要慎用 retain_height，不是已经 Historical blocks required for auditing（679 item 3 余量） interchangeable——679 另钉 item 3，本页钉 item 1 第三件事。491 commitretaincaution vs kept bundled unbundling 在本页 item 1 启动。

怎样填 retain_height、怎样删块、怎样开 state sync 是规范里的做法，本页不抄。Commit Usage retain_height caution 正式三事 bundled（491）、If all nodes remove historical blocks → permanently lost / no bootstrap unless state sync（491 item 2 余量 / 678）、Historical blocks required for auditing / replay / light client not persist signal bundled（491 item 3 余量 / 679）、Commit 保留高度 bundled（366）、Commit Usage persist signal bundled（481）、切进共识就已经有完整历史（323）、应用快照就已经从创世重放（38）是另外那套，本页不抄。

## 官方为什么这样拆

- **Use retain_height with caution not retain_height defaults to 0 retain all ≠ 366 retain-height bundled interchangeable：** 官方把 Methods Commit Usage caution 语气单句和 retain_height defaults to 0 retain all 路径分开。
- **Use retain_height with caution not blocks below height may be removed ≠ 366 retain bundled item 2 interchangeable：** 官方把 Usage with caution 单句和 blocks below this height may be removed 路径分开。
- **Use retain_height with caution not Commit Usage persist signal bundled ≠ 481 commitpersist bundled interchangeable：** 官方把 Usage with caution 单句和 persist signal bundled 路径分开；491 commitretaincaution vs kept bundled unbundling 在本页 item 1 完成。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| Use retain_height with caution | 不是 retain_height defaults to 0 retain all（366） | 不是 all nodes remove → no bootstrap（678/491 item 2） |
| caution 段落 / 要慎用 retain_height | 不是 blocks below height may be removed（366 item 2） | 不是 Historical blocks required（679/491 item 3） |
| with caution 单句 | 不是 Commit Usage persist signal bundled（481） | 不是 Commit 保留高度 bundled 全段（366） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Commit Usage Use retain_height with caution not retain_height defaults to 0 retain all / not blocks below height may be removed / not Commit Usage persist signal bundled 正式三事（491 余量），必须分开 Use retain_height with caution 是不是 retain_height defaults to 0 retain all interchangeable / 366 retain-height bundled interchangeable / 335 finpersist interchangeable、要慎用 retain_height / caution 段落 是不是 blocks below height may be removed interchangeable / 366 retain bundled item 2 interchangeable / 678 commitretaincaution-notbootstrap interchangeable、with caution 单句 是不是 Commit Usage persist signal bundled interchangeable / 481 commitpersist bundled interchangeable / 679 commitretaincaution-notpersist interchangeable。可以跳过「看见 Use retain_height with caution 就已经 retain_height 默认 0 全留 interchangeable / 就已经 blocks below may be removed interchangeable / 就已经 persist signal bundled interchangeable」。不要另写怎样填 retain_height。491 commitretaincaution vs kept bundled unbundling 在本页 item 1 完成；续 [`worked-example-commitretaincaution-notbootstrap-vs-bundled.md`](worked-example-commitretaincaution-notbootstrap-vs-bundled.md)（不变量 678 item 2）。

## 本页不抄

- 怎样填 retain_height、怎样删块、怎样开 state sync。
- Commit Usage retain_height caution 正式三事 bundled。那是不变量 491。
- If all nodes remove historical blocks → permanently lost / no bootstrap unless state sync。那是不变量 491 item 2 余量 / 678。
- Historical blocks required for auditing / replay / light client not persist signal bundled。那是不变量 491 item 3 余量 / 679。
- Commit 保留高度 bundled。那是不变量 366。
- Commit Usage persist signal bundled。那是不变量 481。
- 切进共识就已经有完整历史。那是不变量 323。
- 应用快照就已经从创世重放。那是不变量 38。
