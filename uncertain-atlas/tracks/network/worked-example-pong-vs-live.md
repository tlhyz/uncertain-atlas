# 例：看见协议版本够了不是已经会带 nonce 的 ping；看见 pong 不是已经对上那一次 ping；看见回了 pong 不是已经还活着

**层次**：网络 / 规范对象。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：Bitcoin [BIP-31](https://github.com/bitcoin/bips/blob/master/bip-0031.mediawiki)（Deployed, Peer Services）。  
**对应课文**：[L3.4](../../courses/level-03-bitcoin/L03-M04-network-and-eclipse.md)、[L9.1](../../courses/level-09-systems/L09-M01-p2p.md)。  
**不要写进**：Ethereum 行、L5.1、05b、M5.4、L5.4、03 共识。本页是「带 nonce 的 ping / pong 不是已经还活着」，不是功能协商已经启用，也不是发现 ping 里的记录序号已经有当前记录。

## 官方三件事

规范把 pong 写成三件独立的对等事，不是「看见回了 ping 就已经还活着」一件事：

1. **看见协议版本够了不是已经会带 nonce 的 ping，也不是已经会回 pong。**  
   官方写：谈妥的协议版本够高时，ping 必须带一个 nonce。必须自己抬版本才能加入本页。旧版本的客户端不被指望在 ping 里放 nonce，也不会被送来 pong。看见协议版本够了，不是已经发了带 nonce 的 ping，也不是对端已经会回 pong，也不是本页已经并进后来的功能协商。
2. **看见 pong / 回显了 nonce 不是已经对上那一次 ping。**  
   官方写：发送方应当把 nonce 设成随机值，接收方在新的 pong 里原样回显。若还没听见第一次 pong 就又发了第二次 ping，必须靠 nonce 把两次答复分开。若选择从不重叠发送，应当把 nonce 置零。看见一条 pong，不是已经对上你刚发的那一次 ping。看见 nonce 是零，不是已经测过往返，也不是已经重叠过。
3. **看见回了 pong 不是已经还活着，也不是已经不卡。**  
   官方把本页写成用来发现已经死掉的对等连接。动机写了三件独立的病：设备睡醒后 TCP 还在，但对端或地址可能已经废；单线程客户端在重负载下会对网络消息变得很慢；下载大结构时很难测对端有多近。看见回了 pong，不是已经还是睡前那个人，也不是已经不卡，也不是已经选到了近的对等节点。看见测到一次往返，不是已经永远响应。

协议版本门槛、nonce 宽度是规范里的取值，本页不抄。

## 官方为什么这样拆

- **版本号 ≠ 已经本页：** 官方把加入写成必须自己抬版本；旧客户端不会被送来 pong。
- **pong ≠ 已经对上那一次：** 官方把随机 nonce 和「重叠时必须能分开」写成独立谓词。
- **回了 ≠ 已经还活着：** 官方把本页写成测死连接、测负载、测远近的工具，不是一次绿灯。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 协议版本 | 只挡会不会发带 nonce 的 ping / 会不会回 pong | 不是已经支持某一项功能 |
| pong / nonce | 用来对上某一次 ping | 不是已经还活着 |
| 往返样本 | 一次时间 | 不是已经不卡 / 已经近 |
| 协议版本 ≠ 已经启用功能 | 另一对象 | 不变量 259 |
| ping 里的记录序号 ≠ 已经有当前记录 | 另一对象 | 不变量 241 |
| 发了 sendheaders ≠ 已经有块 | 另一对象 | 不变量 247 |
| 按 wtxid 通告 ≠ 已经有交易 | 另一对象 | 不变量 248 |
| 停交易转发 ≠ 已经终身只传块 | 另一对象 | 不变量 256 |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果写对等探活，必须分开版本门槛、对上某一次 ping、一次往返样本。可以跳过「看见回了 ping 就已经还活着」。若对照，必须分开加入本页、nonce 对上、样本不是永久健康。不要另写怎样叠 ping 做日蚀。262 pong vs live bundled unbundling 完成（1268 item 1 / 1269 item 2 / 1270 item 3）；精读 [`worked-example-pong31-notver-vs-bundled.md`](worked-example-pong31-notver-vs-bundled.md)（不变量 1268 item 1）、[`worked-example-pong31-notmatch-vs-bundled.md`](worked-example-pong31-notmatch-vs-bundled.md)（不变量 1269 item 2）、[`worked-example-pong31-notlive-vs-bundled.md`](worked-example-pong31-notlive-vs-bundled.md)（不变量 1270 item 3）。

## 本页不抄

- 协议版本门槛数字、nonce 整数宽度、消息字段布局。
- 怎样叠许多 ping、怎样靠假 pong 认人、怎样用往返选人做日蚀。
