# 例：看见 Use CommitResponse.retain_height with caution is not already retain_height defaults to 0 interchangeable / not already returned height is pruning interchangeable / not already persist signal bundled interchangeable

**层次**：实现 / Commit Usage Use retain_height with caution not defaults to 0 retain all / not blocks below may be removed / not persist signal bundled 正式三事（491 余量）。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) Commit Usage。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5、mempool。本页是「Commit Usage Use retain_height with caution not defaults to 0 retain all / not blocks below may be removed / not persist signal bundled 正式三事（491 余量）/ not 692 commitretaincaution-notdefault interchangeable / not 491 commitretaincaution-vs-kept bundled interchangeable」，不是 Commit Usage retain_height caution 正式三事 bundled（491），也不是 Commit 保留高度（366）或 persist signal（481）。不要另写怎样填 retain_height、怎样删块、怎样开 state sync。

## 官方三件事

规范把 Commit Usage 里 Use `CommitResponse.retain_height` with caution! 和「已经 retain_height defaults to 0 (retain all)（366） interchangeable / 已经 blocks below this height may be removed 那种回了高度就等于已经在剪 interchangeable / 已经 Commit Usage persist signal（481） bundled 第三件事 interchangeable」分开写成三件独立的实现事，不是「看见 with caution 就已经默认 0 就等于已经在剪 interchangeable / 就已经回了高度就等于已经在剪 interchangeable / 就已经 persist signal bundled interchangeable」一件事：

1. **看见 Use `CommitResponse.retain_height` with caution! / 看见要慎用 retain_height / caution is not already 已经 retain_height defaults to 0 (retain all)（366） interchangeable / 366 retain interchangeable / 已经没填就等于已经在剪 interchangeable，也不是已经 Commit Usage retain_height caution 正式三事 bundled（491） interchangeable / 692 commitretaincaution-notdefault interchangeable / 693 commitretaincaution-notgenesis interchangeable / 491 commitretaincaution item 2 all nodes interchangeable，也不是已经 Use retain_height with caution not defaults to 0 / not blocks below may be removed / not persist signal bundled 正式三事 bundled（491 item 1 余量） interchangeable / 491 commitretaincaution item 1 interchangeable。**  
   官方 Usage 写：Use `CommitResponse.retain_height` with caution! 看见 with caution，不是已经默认 0 全留（366）那种没填就等于已经在剪 interchangeable——366 钉字段默认全留，本页从 491 item 1 侧钉 not default 0 单句。491 commitretaincaution vs kept bundled unbundling 在本页 item 1 启动。

2. **看见 Use retain_height with caution / 看见要慎用 retain_height / 看见 Usage 这句 is not already 已经 blocks below this height may be removed 那种回了高度就等于已经在剪 interchangeable / 已经 caution 回了非零高度就等于已经在剪 interchangeable，也不是已经 Commit Usage retain_height caution 正式三事 bundled（491） interchangeable / 692 commitretaincaution-notdefault interchangeable / 491 commitretaincaution item 3 Historical blocks interchangeable / 694 commitretaincaution-nothistorical interchangeable。**  
   官方把 Usage caution 单句和「回了高度就等于已经在剪」路径分开——491 bundled 第一件事常与 366 第二件事混成「看见 caution 就已经 blocks below may be removed interchangeable」，本页钉 not blocks below may be removed 单句。看见 with caution，不是已经低于这个高度的块可以被删 interchangeable——366 钉字段语义，本页钉 caution 语气。

3. **看见 Use retain_height with caution / 看见 Usage 这句 / 看见慎用 retain_height is not already 已经 Commit Usage persist signal（481） bundled 第三件事 interchangeable / 481 commitpersist interchangeable / 已经 Signal persist application state 就代表 caution 已经验完 interchangeable，也不是已经 Commit Usage retain_height caution 正式三事 bundled（491） interchangeable / 692 commitretaincaution-notdefault interchangeable / 693 commitretaincaution-notgenesis interchangeable。**  
   官方把 Usage caution 单句和 persist signal bundled 第三件事分开——491 bundled 第一件事常与 481 混成「看见 caution 就已经 persist signal bundled interchangeable」，本页钉 not persist signal bundled 单句。看见 Usage 这句，不是已经 481 item 3 interchangeable——481 钉 persist signal 全段，本页钉 caution 单句。491 commitretaincaution vs kept bundled unbundling 在本页 item 1 启动。

怎样填 retain_height、怎样删块、怎样开 state sync 是规范里的做法，本页不抄。Commit Usage retain_height caution 正式三事 bundled（491）、all nodes remove historical blocks（491 item 2 余量 / 693）、Historical blocks may also be required（491 item 3 余量 / 694）、Commit 保留高度（366）、persist signal（481）是另外那套，本页不抄。

## 官方为什么这样拆

- **caution not defaults to 0 ≠ 366 retain interchangeable：** 官方把 Methods Usage caution 语气和字段默认全留路径分开。
- **caution not blocks below may be removed ≠ 回了高度就等于已经在剪 interchangeable：** 官方把 Usage caution 单句和「低于这个高度的块可以被删」路径分开。
- **caution not persist signal bundled ≠ 481 / commitpersist interchangeable：** 官方把 Usage caution 单句和 persist signal bundled 第三件事分开；491 commitretaincaution vs kept bundled unbundling 在本页 item 1 启动。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| Use retain_height with caution | 不是 retain_height 默认 0 就等于已经在剪（366） | 不是 all nodes remove（693/491 item 2） |
| 看见要慎用 retain_height | 不是回了高度就等于已经在剪 | 不是 Commit 保留高度（366） |
| 看见 Usage 这句 | 不是 persist signal bundled（481） | 不是 Historical blocks required（694/491 item 3） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 Commit Usage Use retain_height with caution not defaults to 0 retain all / not blocks below may be removed / not persist signal bundled 正式三事（491 余量），必须分开 caution 是不是默认 0 就等于已经在剪 interchangeable / 366、是不是回了高度就等于已经在剪、是不是 persist signal bundled interchangeable / 481。可以跳过「看见 caution 段落就已经在剪」。不要另写怎样填 retain_height。491 commitretaincaution vs kept bundled unbundling 在本页 item 1 启动；续 [`worked-example-commitretaincaution-notgenesis-vs-bundled.md`](worked-example-commitretaincaution-notgenesis-vs-bundled.md)（不变量 693 item 2）。

## 本页不抄

- 怎样填 retain_height、怎样删块、怎样开 state sync。
- Commit Usage retain_height caution 正式三事 bundled。那是不变量 491。
- all nodes remove historical blocks。那是不变量 491 item 2 余量 / 693。
- Historical blocks may also be required。那是不变量 491 item 3 余量 / 694。
- Commit 保留高度。那是不变量 366。
- Commit Usage persist signal。那是不变量 481。
