# 例：看见回了 pong 不是已经还活着；看见回了 pong 不是已经不卡；看见测到一次往返不是已经永远响应

**层次**：网络 / 规范对象。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：Bitcoin [BIP-31](https://github.com/bitcoin/bips/blob/master/bip-0031.mediawiki)（Deployed, Peer Services）。  
**对应课文**：[L3.4](../../courses/level-03-bitcoin/L03-M04-network-and-eclipse.md)、[L9.1](../../courses/level-09-systems/L09-M01-p2p.md)。  
**不要写进**：Ethereum 行、L5.1、05b、M5.4、L5.4、03 共识。本页是「BIP-31 pong not already alive / not already unstuck / not already forever 正式三事（262 余量）/ not 1270 pong31-notlive interchangeable / not 262 pong-vs-live bundled interchangeable」，不是 pong bundled（262），也不是已经 disabletx-life（256），也不是已经 feature-enabled（259）。不要另写 怎样叠许多 ping、怎样靠假 pong 认人、怎样用往返选人做日蚀。

## 官方三件事

1. **看见回了 pong / 看见回了 pong 这份对象 is not already 已经还活着 interchangeable，也不是已经 pong bundled（262） interchangeable / 1270 pong31-notlive interchangeable / 1268 pong31-notver interchangeable，也不是已经 BIP-31 pong not already alive / not already unstuck / not already forever 正式三事 bundled（262 item 3 余量） interchangeable / 262 pong item 3 interchangeable。**  
   官方把本页写成用来发现已经死掉的对等连接。动机写了三件独立的病：设备睡醒后 TCP 还在，但对端或地址可能已经废；单线程客户端在重负载下会对网络消息变得很慢；下载大结构时很难测对端有多近。看见回了 pong，不是已经还是睡前那个人，也不是已经不卡，也不是已经选到了近的对等节点。看见测到一次往返，不是已经永远响应。

2. **看见回了 pong / 看见回了 pong / 这份对象 is not already 已经不卡 interchangeable，也不是已经 pong bundled（262） interchangeable / 1270 pong31-notlive interchangeable / 1269 pong31-notmatch interchangeable，也不是已经 disabletx-life interchangeable / 256 disabletx-life interchangeable。**  
   官方把回了 pong 和已经不卡写成两件。看见回了 pong，不是已经不卡。

3. **看见测到一次往返 / 看见回了 pong / 这份对象 is not already 已经永远响应 interchangeable，也不是已经 pong bundled（262） interchangeable / 1270 pong31-notlive interchangeable / 1268 pong31-notver interchangeable，也不是已经 feature-enabled interchangeable / 259 feature-enabled interchangeable。**  
   官方把测到一次往返和已经永远响应写成两件。看见测到一次往返，不是已经永远响应。

协议版本门槛、nonce 宽度是规范里的取值，本页不抄。不要另写 怎样叠许多 ping、怎样靠假 pong 认人、怎样用往返选人做日蚀。

## 官方为什么这样拆

- **回了 不是已经还活着：官方把本页写成测死连接、测负载、测远近的工具，不是一次绿灯。**
- **回了 pong 不是已经不卡：官方写单线程客户端在重负载下会对网络消息变得很慢。**
- **一次往返 不是已经永远响应：官方只把本页写成一次样本，不是永久健康。**

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 已经还活着 | 不是已经还活着 | 不是已经disabletx-life（256） |
| 已经不卡 | 不是已经不卡 | 不是已经feature-enabled（259） |
| 已经永远响应 | 不是已经永远响应 | 不是已经1268 pong31-notver |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 BIP-31 pong not already alive / not already unstuck / not already forever 正式三事（262 余量），必须分开是不是已经还活着、是不是已经不卡、是不是已经永远响应。可以跳过「看见回了 ping 就已经还活着」。不要另写 怎样叠许多 ping、怎样靠假 pong 认人、怎样用往返选人做日蚀。262 pong vs live bundled unbundling 在本页 item 3 完成。

## 本页不抄

- 协议版本门槛数字、nonce 整数宽度、消息字段布局。
- 怎样叠许多 ping、怎样靠假 pong 认人、怎样用往返选人做日蚀。
