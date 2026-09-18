# 例：看见字节看起来随机不是防火墙已经认不出；看见协议允许垃圾或诱饵不是已经塑过形；看见字节看起来随机不是流量分析已经失效

**层次**：网络 / 规范对象。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：Bitcoin [BIP-324](https://github.com/bitcoin/bips/blob/master/bip-0324.mediawiki)（Deployed, Peer Services；替换 151）。  
**对应课文**：[L3.4](../../courses/level-03-bitcoin/L03-M04-network-and-eclipse.md)、[L9.1](../../courses/level-09-systems/L09-M01-p2p.md)。  
**不要写进**：`index/03` 共识行、Ethereum 行、M5.4、L5.1、L5.4、05b。本页是「BIP-324 randstream not already unrecognized / not already shaped / not already analysis-dead 正式三事（242 余量）/ not 1275 vt324-notrand interchangeable / not 242 v2-transport-vs-private bundled interchangeable」，不是 v2 transport vs private bundled（242），也不是已经 enr-request（241），也不是已经 enr-newest（240）。不要另写 怎样做中间人、怎样降级、怎样按时间认协议、怎样塑形。

## 官方三件事

1. **看见字节看起来随机 / 看见字节看起来随机 这份对象 is not already 防火墙已经认不出 interchangeable，也不是已经 v2 transport vs private bundled（242） interchangeable / 1275 vt324-notrand interchangeable / 1274 vt324-notpriv interchangeable，也不是已经 BIP-324 randstream not already unrecognized / not already shaped / not already analysis-dead 正式三事 bundled（242 item 2 余量） interchangeable / 242 v2 item 2 interchangeable。**  
   官方把字节看起来随机和防火墙已经认不出写成两件。看见字节看起来随机，不是防火墙已经认不出。

2. **看见协议允许垃圾或诱饵 / 看见字节看起来随机 / 这份对象 is not already 已经塑过形 interchangeable，也不是已经 v2 transport vs private bundled（242） interchangeable / 1275 vt324-notrand interchangeable / 1276 vt324-notold interchangeable，也不是已经 enr-request interchangeable / 241 enr-request interchangeable。**  
   官方把协议允许垃圾或诱饵和已经塑过形写成两件。看见协议允许垃圾或诱饵，不是已经塑过形。

3. **看见字节看起来随机 / 看见协议允许垃圾或诱饵 / 这份对象 is not already 流量分析已经失效 interchangeable，也不是已经 v2 transport vs private bundled（242） interchangeable / 1275 vt324-notrand interchangeable / 1274 vt324-notpriv interchangeable，也不是已经 enr-newest interchangeable / 240 enr-newest interchangeable。**  
   官方把字节看起来随机和流量分析已经失效写成两件。看见字节看起来随机，不是流量分析已经失效。

栈怎么写、分隔符、例串是规范里的取值，本页不抄。不要另写 怎样做中间人、怎样降级、怎样按时间认协议、怎样塑形。

## 官方为什么这样拆

- **伪随机 不是已经认不出：官方承认看包长、看时间、以及主动攻击仍可能认出来。**
- **允许垃圾或诱饵 不是已经塑过形：官方把怎样用、何时用写成范围外。**
- **没有固定魔数开头 不是审查已经失效：官方把流量分析仍可能认出来写成独立谓词。**

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 防火墙已经认不出 | 不是防火墙已经认不出 | 不是已经enr-request（241） |
| 已经塑过形 | 不是已经塑过形 | 不是已经enr-newest（240） |
| 流量分析已经失效 | 不是流量分析已经失效 | 不是已经1274 vt324-notpriv |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 BIP-324 randstream not already unrecognized / not already shaped / not already analysis-dead 正式三事（242 余量），必须分开是不是防火墙已经认不出、是不是已经塑过形、是不是流量分析已经失效。可以跳过「看见机会主义未认证加密就已经私人」。不要另写 怎样做中间人、怎样降级、怎样按时间认协议、怎样塑形。242 v2 transport vs private bundled unbundling 在本页 item 2 续；续 [`worked-example-vt324-notold-vs-bundled.md`](worked-example-vt324-notold-vs-bundled.md)（不变量 1276 item 3）。

## 本页不抄

- 握手长度、垃圾上限、再密钥间隔、曲线编码、测试向量。
- 怎样做中间人、怎样降级、怎样按时间认协议、怎样塑形。
