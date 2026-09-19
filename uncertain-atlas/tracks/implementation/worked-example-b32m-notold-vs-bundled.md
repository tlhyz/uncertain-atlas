# 例：看见后继校验过了不是已经是旧校验那套地址不是已经是旧校验那套地址；看见passing Bech32m is not already being a Bech32 address不是已经是不变量 174；看见后继校验过了不是已经是旧校验那套地址不是已经 181 bundled

**层次**：实现 / 规范对象。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：Bitcoin [BIP-350](https://github.com/bitcoin/bips/blob/master/bip-0350.mediawiki)（Bech32m format for v1+ witness addresses）。  
**对应课文**：[L3.7](../../courses/level-03-bitcoin/L03-M07-segwit-soft-fork.md)。  
**不要写进**：`index/03` 共识行、M3.7、L3.7。本页是「BIP-350 successor-pass not already old-bech32 / not already 174 / not already 181-bundled 正式三事（181 余量）/ not 1539 b32m-notold interchangeable / not 181 bech32m-vs-bech32 bundled interchangeable」，不是 bech32m vs bech32 bundled（181），也不是已经 地址≠已有输出（174），也不是已经 哈希≠已揭开（170）。不要另写 怎样插删字符让旧校验仍过、怎样造版本与编码不对的串。

## 官方三件事

1. **看见后继校验过了不是已经是旧校验那套地址 / 看见后继校验过了不是已经是旧校验那套地址 这份对象 is not already 已经是旧校验那套地址 interchangeable，也不是已经 bech32m vs bech32 bundled（181） interchangeable / 1539 b32m-notold interchangeable / 1540 b32m-notv0 interchangeable，也不是已经 BIP-350 successor-pass not already old-bech32 / not already 174 / not already 181-bundled 正式三事 bundled（181 item 1 余量） interchangeable / 181 b32m item 1 interchangeable。**  
   官方把后继校验过了不是已经是旧校验那套地址和已经是旧校验那套地址写成两件。看见后继校验过了不是已经是旧校验那套地址，不是已经是旧校验那套地址。

2. **看见passing Bech32m is not already being a Bech32 address / 看见后继校验过了不是已经是旧校验那套地址 / 这份对象 is not already 已经是不变量 174 interchangeable，也不是已经 bech32m vs bech32 bundled（181） interchangeable / 1539 b32m-notold interchangeable / 1541 b32m-notutx interchangeable，也不是已经 地址≠已有输出 interchangeable / 174 地址≠已有输出 interchangeable。**  
   官方把passing Bech32m is not already being a Bech32 address和已经是不变量 174写成两件。看见passing Bech32m is not already being a Bech32 address，不是已经是不变量 174。

3. **看见后继校验过了不是已经是旧校验那套地址 / 看见passing Bech32m is not already being a Bech32 address / 这份对象 is not already 已经 181 bundled interchangeable，也不是已经 bech32m vs bech32 bundled（181） interchangeable / 1539 b32m-notold interchangeable / 1540 b32m-notv0 interchangeable，也不是已经 哈希≠已揭开 interchangeable / 170 哈希≠已揭开 interchangeable。**  
   官方把后继校验过了不是已经是旧校验那套地址和已经 181 bundled写成两件。看见后继校验过了不是已经是旧校验那套地址，不是已经 181 bundled。

栈怎么写、分隔符、例串是规范里的取值，本页不抄。不要另写 怎样插删字符让旧校验仍过、怎样造版本与编码不对的串。

## 官方为什么这样拆

- **后继校验过了不是已经是旧校验那套地址 interchangeable：官方写版本 1 及以后用 Bech32m，版本 0 仍用 Bech32，不是已经是同一套。**
- **看见本页不是已经是不变量 174。**
- **看见后继校验不是已经 181 bundled。**

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 已经是旧校验那套地址 | 不是已经是旧校验那套地址 | 不是已经地址≠已有输出（174） |
| 已经是不变量 174 | 不是已经是不变量 174 | 不是已经哈希≠已揭开（170） |
| 已经 181 bundled | 不是已经 181 bundled | 不是已经1540 b32m-notv0 |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 BIP-350 successor-pass not already old-bech32 / not already 174 / not already 181-bundled 正式三事（181 余量），必须分开是不是已经是旧校验那套地址、是不是已经是不变量 174、是不是已经 181 bundled。可以跳过「看见过了校验就已经是同一套」。不要另写 怎样插删字符让旧校验仍过、怎样造版本与编码不对的串。181 bech32m vs bech32 bundled unbundling 在本页 item 1 启动；续 [`worked-example-b32m-notv0-vs-bundled.md`](worked-example-b32m-notv0-vs-bundled.md)（不变量 1540 item 2）。

## 本页不抄

- 校验常数、字符表、例地址、长度窗、可读前缀。
- 怎样插删字符让旧校验仍过、怎样造版本与编码不对的串。
