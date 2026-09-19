# 例：看见Bech32地址串不是链上已经有这笔输出不是已经有这笔输出；看见seeing a Bech32 string is not already having that output on chain不是已经是不变量 181；看见Bech32地址串不是链上已经有这笔输出不是已经 174 bundled

**层次**：实现 / 规范对象。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：Bitcoin [BIP-173](https://github.com/bitcoin/bips/blob/master/bip-0173.mediawiki)（Bech32 address format）。  
**对应课文**：[L3.7](../../courses/level-03-bitcoin/L03-M07-segwit-soft-fork.md)。  
**不要写进**：`index/03` 共识行、M3.7、L3.7。本页是「BIP-173 bech32-string not already on-chain-utxo / not already 181 / not already 174-bundled 正式三事（174 余量）/ not 1536 adut-notout interchangeable / not 174 address-vs-utxo bundled interchangeable」，不是 address vs utxo bundled（174），也不是已经 后继校验≠旧方案（181），也不是已经 哈希≠已揭开（170）。不要另写 怎样造能过校验却指错程序的串、怎样靠增删字符撞合法。

## 官方三件事

1. **看见Bech32地址串不是链上已经有这笔输出 / 看见Bech32地址串不是链上已经有这笔输出 这份对象 is not already 已经有这笔输出 interchangeable，也不是已经 address vs utxo bundled（174） interchangeable / 1536 adut-notout interchangeable / 1537 adut-notchk interchangeable，也不是已经 BIP-173 bech32-string not already on-chain-utxo / not already 181 / not already 174-bundled 正式三事 bundled（174 item 1 余量） interchangeable / 174 adut item 1 interchangeable。**  
   官方把Bech32地址串不是链上已经有这笔输出和已经有这笔输出写成两件。看见Bech32地址串不是链上已经有这笔输出，不是已经有这笔输出。

2. **看见seeing a Bech32 string is not already having that output on chain / 看见Bech32地址串不是链上已经有这笔输出 / 这份对象 is not already 已经是不变量 181 interchangeable，也不是已经 address vs utxo bundled（174） interchangeable / 1536 adut-notout interchangeable / 1538 adut-notpay interchangeable，也不是已经 后继校验≠旧方案 interchangeable / 181 后继校验≠旧方案 interchangeable。**  
   官方把seeing a Bech32 string is not already having that output on chain和已经是不变量 181写成两件。看见seeing a Bech32 string is not already having that output on chain，不是已经是不变量 181。

3. **看见Bech32地址串不是链上已经有这笔输出 / 看见seeing a Bech32 string is not already having that output on chain / 这份对象 is not already 已经 174 bundled interchangeable，也不是已经 address vs utxo bundled（174） interchangeable / 1536 adut-notout interchangeable / 1537 adut-notchk interchangeable，也不是已经 哈希≠已揭开 interchangeable / 170 哈希≠已揭开 interchangeable。**  
   官方把Bech32地址串不是链上已经有这笔输出和已经 174 bundled写成两件。看见Bech32地址串不是链上已经有这笔输出，不是已经 174 bundled。

栈怎么写、分隔符、例串是规范里的取值，本页不抄。不要另写 怎样造能过校验却指错程序的串、怎样靠增删字符撞合法。

## 官方为什么这样拆

- **Bech32地址串不是链上已经有这笔输出 interchangeable：官方写这是带校验的收款写法，不是链上已经有这笔输出。**
- **看见本页不是已经是不变量 181。**
- **看见地址串不是已经 174 bundled。**

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 已经有这笔输出 | 不是已经有这笔输出 | 不是已经后继校验≠旧方案（181） |
| 已经是不变量 181 | 不是已经是不变量 181 | 不是已经哈希≠已揭开（170） |
| 已经 174 bundled | 不是已经 174 bundled | 不是已经1537 adut-notchk |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 BIP-173 bech32-string not already on-chain-utxo / not already 181 / not already 174-bundled 正式三事（174 余量），必须分开是不是已经有这笔输出、是不是已经是不变量 181、是不是已经 174 bundled。可以跳过「看见地址就已经有输出」。不要另写 怎样造能过校验却指错程序的串、怎样靠增删字符撞合法。174 address vs utxo bundled unbundling 在本页 item 1 启动；续 [`worked-example-adut-notchk-vs-bundled.md`](worked-example-adut-notchk-vs-bundled.md)（不变量 1537 item 2）。

## 本页不抄

- 字符表、生成式、例地址、网络前缀常数、长度窗。
- 怎样造能过校验却指错程序的串、怎样靠增删字符撞合法。
