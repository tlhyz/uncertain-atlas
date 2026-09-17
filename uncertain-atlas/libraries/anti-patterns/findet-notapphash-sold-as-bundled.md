# 反模式：把 app_hash MUST be deterministic not 印进本头 正式三事（470 余量）卖成 findet bundled / 已经印进本头 / next_block_delay 非确定就代表整门非确定

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[app_hash MUST be deterministic not 印进本头 ≠ bundled（470）](../../tracks/implementation/worked-example-findet-notapphash-vs-bundled.md)。

## 卖法

- 「看见 app_hash MUST be deterministic 就已经印进本头 interchangeable / 已经本头 AppHash 交差 interchangeable。」
- 「看见 next_block_delay 非确定 就已经 Finalize 回包整门都可以非确定 interchangeable。」
- 「看见 Usage 写了 app_hash 必须确定 就已经 findet bundled interchangeable / 已经 executes txs deterministically interchangeable。」

## 为什么错

官方把 app_hash MUST be deterministic、本头 AppHash 交差、next_block_delay 非确定例外、executes txs / implementation 三句 bundled 写成独立的实现事。把它们卖成 findet bundled、已经印进本头、next_block_delay 非确定就代表整门非确定，会把 not 印进本头、not next_block_delay nondet、not findet item 1/3 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 app_hash MUST be deterministic not 印进本头 正式三事（470 余量），必须分开 not 印进本头、not next_block_delay nondet、not findet item 1/3 三个名字，不要把它们卖成 findet bundled / 已经印进本头 / next_block_delay 非确定就代表整门非确定。

## 和相邻反模式

- [findet-sold-as-prepare](findet-sold-as-prepare.md) 是 470 bundled 三事专用，不是本页 app_hash 单句边界。
- [findet-notlikeprepare-sold-as-bundled](findet-notlikeprepare-sold-as-bundled.md) 是 579 executes txs not like Prepare 专用，不是本页 item 2/3 边界。
