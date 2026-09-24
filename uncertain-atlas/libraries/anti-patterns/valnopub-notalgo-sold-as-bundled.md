# 反模式：把不带 PubKey 不是已经选型 not already algo / not already no-pq / not already settled 正式三事（364 余量）说成已经选型 / 已经没有后量子钥 / 已经交差

**层次**：实现 / 文案。  
**分类**：推断（产品）+ 建议（产品）。  
**例**：[省了字段 not already algo ≠ bundled（364）](../../tracks/implementation/worked-example-valnopub-notalgo-vs-bundled.md)。

## 卖法

把省了字段 / 不带 PubKey 是为了不在 ABCI 上传大后量子公钥 / 省了 PubKey 字段 写成已经选型 interchangeable / 已经 algo interchangeable / 已经选型交差 interchangeable / 364 validator bundled interchangeable / validator-sold-as-update interchangeable；把提到后量子公钥 / 可能很大的后量子公钥 / 提到后量子钥 写成已经没有后量子钥 interchangeable / 已经 no-pq interchangeable / 已经没有后量子钥交差 interchangeable；把 ABCI 不传公钥 / ABCI 上不传送公钥 / 不在 ABCI 上传公钥 写成已经交差 interchangeable / 已经 settled interchangeable / 已经交差交差 interchangeable，或已经和 364 validator bundled / validator-sold-as-update interchangeable / 840 valnopub-notalgo interchangeable。

## 为什么错

官方把省了字段、不是已经没有后量子钥、不是已经交差写成三件独立的实现事。把它们卖成 already algo interchangeable / already no-pq interchangeable / already settled interchangeable，会把 not already algo、not already no-pq、not already settled 三条路一起吞掉。

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看不带 PubKey 不是已经选型 not already algo / not already no-pq / not already settled 正式三事（364 余量），必须分开 not already algo、not already no-pq、not already settled 三件事，不要和 364 / 318 / 839 / 841 糊成一句。

## 和相邻反模式

- [validator-sold-as-update](validator-sold-as-update.md) 是 Validator 类型 bundled 全段，不是本页省了字段 item 2 单句边界。
- [validatorupdate-sold-as-set](validatorupdate-sold-as-set.md) 是 InitChain 空名单就已经没有集合（318），不是本页 not already algo 边界。
- [valaddr-notpubkey-sold-as-bundled](valaddr-notpubkey-sold-as-bundled.md) 是 Validator 用 address 认人 not already pubkey（364 item 1），不是本页 not already no-pq 边界。
