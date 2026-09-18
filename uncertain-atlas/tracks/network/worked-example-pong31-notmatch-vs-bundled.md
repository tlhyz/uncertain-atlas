# 例：看见一条 pong 不是已经对上那一次 ping；看见回显了 nonce 不是已经对上你刚发的那一次；看见 nonce 是零不是已经测过往返

**层次**：网络 / 规范对象。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：Bitcoin [BIP-31](https://github.com/bitcoin/bips/blob/master/bip-0031.mediawiki)（Deployed, Peer Services）。  
**对应课文**：[L3.4](../../courses/level-03-bitcoin/L03-M04-network-and-eclipse.md)、[L9.1](../../courses/level-09-systems/L09-M01-p2p.md)。  
**不要写进**：Ethereum 行、L5.1、05b、M5.4、L5.4、03 共识。本页是「BIP-31 pong not already matched / not already this-ping / not already rtt 正式三事（262 余量）/ not 1269 pong31-notmatch interchangeable / not 262 pong-vs-live bundled interchangeable」，不是 pong bundled（262），也不是已经 enr-request（241），也不是已经 wtxidrelay-have（248）。不要另写 怎样叠许多 ping、怎样靠假 pong 认人、怎样用往返选人做日蚀。

## 官方三件事

1. **看见一条 pong / 看见回显了 nonce 这份对象 is not already 已经对上那一次 ping interchangeable，也不是已经 pong bundled（262） interchangeable / 1269 pong31-notmatch interchangeable / 1268 pong31-notver interchangeable，也不是已经 BIP-31 pong not already matched / not already this-ping / not already rtt 正式三事 bundled（262 item 2 余量） interchangeable / 262 pong item 2 interchangeable。**  
   官方写：发送方应当把 nonce 设成随机值，接收方在新的 pong 里原样回显。若还没听见第一次 pong 就又发了第二次 ping，必须靠 nonce 把两次答复分开。若选择从不重叠发送，应当把 nonce 置零。看见一条 pong，不是已经对上你刚发的那一次 ping。看见 nonce 是零，不是已经测过往返，也不是已经重叠过。

2. **看见回显了 nonce / 看见一条 pong / 这份对象 is not already 已经对上你刚发的那一次 interchangeable，也不是已经 pong bundled（262） interchangeable / 1269 pong31-notmatch interchangeable / 1270 pong31-notlive interchangeable，也不是已经 enr-request interchangeable / 241 enr-request interchangeable。**  
   官方把回显了 nonce 和已经对上你刚发的那一次写成两件。看见回显了 nonce，不是已经对上你刚发的那一次。

3. **看见nonce 是零 / 看见一条 pong / 这份对象 is not already 已经测过往返 interchangeable，也不是已经 pong bundled（262） interchangeable / 1269 pong31-notmatch interchangeable / 1268 pong31-notver interchangeable，也不是已经 wtxidrelay-have interchangeable / 248 wtxidrelay-have interchangeable。**  
   官方把 nonce 是零和已经测过往返写成两件。看见 nonce 是零，不是已经测过往返。

协议版本门槛、nonce 宽度是规范里的取值，本页不抄。不要另写 怎样叠许多 ping、怎样靠假 pong 认人、怎样用往返选人做日蚀。

## 官方为什么这样拆

- **pong 不是已经对上那一次：官方把随机 nonce 和「重叠时必须能分开」写成独立谓词。**
- **回显了 nonce 不是已经对上刚发的那一次：官方写若重叠发送必须靠 nonce 分开。**
- **nonce 是零 不是已经测过往返：官方写从不重叠发送时应当把 nonce 置零。**

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 已经对上那一次 ping | 不是已经对上那一次 ping | 不是已经enr-request（241） |
| 已经对上你刚发的那一次 | 不是已经对上你刚发的那一次 | 不是已经wtxidrelay-have（248） |
| 已经测过往返 | 不是已经测过往返 | 不是已经1268 pong31-notver |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 BIP-31 pong not already matched / not already this-ping / not already rtt 正式三事（262 余量），必须分开是不是已经对上那一次 ping、是不是已经对上你刚发的那一次、是不是已经测过往返。可以跳过「看见回了 ping 就已经还活着」。不要另写 怎样叠许多 ping、怎样靠假 pong 认人、怎样用往返选人做日蚀。262 pong vs live bundled unbundling 在本页 item 2 续；续 [`worked-example-pong31-notlive-vs-bundled.md`](worked-example-pong31-notlive-vs-bundled.md)（不变量 1270 item 3）。

## 本页不抄

- 协议版本门槛数字、nonce 整数宽度、消息字段布局。
- 怎样叠许多 ping、怎样靠假 pong 认人、怎样用往返选人做日蚀。
