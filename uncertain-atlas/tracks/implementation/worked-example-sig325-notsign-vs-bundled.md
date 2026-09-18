# 例：看见头上有合法工作量不是已经签过；看见只加了网络参数不是已经全验证通过；看见同一份创世不是已经交差

**层次**：应用 / 规范对象。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：Bitcoin [BIP-325](https://github.com/bitcoin/bips/blob/master/bip-0325.mediawiki)（Complete, Applications）。  
**对应课文**：[L3.6](../../courses/level-03-bitcoin/L03-M06-testing-and-culture.md)。  
**不要写进**：Ethereum 行、L5.1、05b 当执行层测试网、M5.4、L5.4、03 共识。本页是「BIP-325 header-work not already signed / not already full-valid / not already settled 正式三事（265 余量）/ not 1195 sig325-notsign interchangeable / not 265 signet-vs-testnet bundled interchangeable」，不是 signet bundled（265），也不是会 Testnet 3 就已经能安全跟（1192），也不是进了块的 coinbase 就已经能花（163）。不要另写怎样拼挑战或造假签块。

## 官方三件事

1. **看见头上有合法工作量 / 只加了网络参数就能连上 这份网 is not already 已经签过 interchangeable，也不是已经 signet bundled（265） interchangeable / 1195 sig325-notsign interchangeable / 1193 sig325-nottn interchangeable / 265 sig item 1 not-tn interchangeable，也不是已经 BIP-325 header-work not already signed / not already full-valid / not already settled 正式三事 bundled（265 item 3 余量） interchangeable / 265 sig item 3 interchangeable。**  
   官方写：头上有合法工作量，客户端可以轻易判断这些块大概合法。可是任何人都能挖出会被这种客户端收下的块；这些块没有所需签名，全验证节点会立刻拒。看见工作量过了，不是已经签过。

2. **看见只加了网络参数就能连上 / 看见头上有合法工作量 / 这份网 is not already 已经全验证通过 interchangeable，也不是已经 signet bundled（265） interchangeable / 1195 sig325-notsign interchangeable / 265 sig item 2 not-reg interchangeable / 1194 sig325-notreg interchangeable，也不是已经会 Testnet 3 就已经能安全跟 interchangeable / 1192 tn94-notfollow interchangeable。**  
   官方写：现有软件只要加上网络参数就能连任何一条 signet，不必再改别的。客户端要么自己验 coinbase 里的块签名，要么只连受信任的对等节点。看见只加了参数，不是已经全验证通过。

3. **看见同一份创世 / 看见头上有合法工作量 / 这份网 is not already 已经交差 interchangeable，也不是已经 signet bundled（265） interchangeable / 1195 sig325-notsign interchangeable / 1193 sig325-nottn interchangeable，也不是已经进了块的 coinbase 就已经能花 interchangeable / 163 coinbase interchangeable。**  
   官方写：创世块对所有 signet 相同，消息起始字节由挑战脚本决定。看见同一份创世，不是已经是同一条 signet，也不是已经交差。

挑战怎么承诺、虚拟交易怎么拼、最低难度数字是规范里的取值，本页不抄。

## 官方为什么这样拆

- **头上有合法工作量 不是已经签过：** 官方把大概合法和所需签名写成两件。
- **只加了网络参数 不是已经全验证通过：** 官方把能连和验块签名写成两步。
- **同一份创世 不是已经交差：** 官方把共用创世写成不是已经是同一条网。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 签过 | 不是已经签过 | 不是已经能安全跟（1192） |
| 全验证 | 不是已经全验证通过 | 不是已经能花（163） |
| 交差 | 不是已经交差 | 不是已经是 testnet（1193） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 BIP-325 header-work not already signed / not already full-valid / not already settled 正式三事（265 余量），必须分开是不是已经签过、是不是已经全验证通过、是不是已经交差。可以跳过「看见测试网就已经能当主网预演」。不要另写怎样拼挑战或造假签块。265 signet vs testnet bundled unbundling 在本页 item 3 完成。

## 本页不抄

- 挑战头字节、最低难度、创世哈希、时间戳、例挑战脚本、虚拟交易字段。
- 怎样拼 to_spend / to_sign、怎样磨 nonce 还不重签、怎样让空解当挑战为真。
