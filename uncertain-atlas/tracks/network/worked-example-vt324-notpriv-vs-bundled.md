# 例：看见线上在加密不是已经知道对面是谁；看见未认证不是已经私人；看见线上在加密不是已经没有隐私改进

**层次**：网络 / 规范对象。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：Bitcoin [BIP-324](https://github.com/bitcoin/bips/blob/master/bip-0324.mediawiki)（Deployed, Peer Services；替换 151）。  
**对应课文**：[L3.4](../../courses/level-03-bitcoin/L03-M04-network-and-eclipse.md)、[L9.1](../../courses/level-09-systems/L09-M01-p2p.md)。  
**不要写进**：`index/03` 共识行、Ethereum 行、M5.4、L5.1、L5.4、05b。本页是「BIP-324 enc not already private / not already authenticated / not already no-gain 正式三事（242 余量）/ not 1274 vt324-notpriv interchangeable / not 242 v2-transport-vs-private bundled interchangeable」，不是 v2 transport vs private bundled（242），也不是已经 v1-reconnect（112），也不是已经 eip8-new（235）。不要另写 怎样做中间人、怎样降级、怎样按时间认协议、怎样塑形。

## 官方三件事

1. **看见线上在加密 / 看见线上在加密 这份对象 is not already 已经知道对面是谁 interchangeable，也不是已经 v2 transport vs private bundled（242） interchangeable / 1274 vt324-notpriv interchangeable / 1275 vt324-notrand interchangeable，也不是已经 BIP-324 enc not already private / not already authenticated / not already no-gain 正式三事 bundled（242 item 1 余量） interchangeable / 242 v2 item 1 interchangeable。**  
   官方把线上在加密和已经知道对面是谁写成两件。看见线上在加密，不是已经知道对面是谁。

2. **看见未认证 / 看见线上在加密 / 这份对象 is not already 已经私人 interchangeable，也不是已经 v2 transport vs private bundled（242） interchangeable / 1274 vt324-notpriv interchangeable / 1276 vt324-notold interchangeable，也不是已经 v1-reconnect interchangeable / 112 v1-reconnect interchangeable。**  
   官方把未认证和已经私人写成两件。看见未认证，不是已经私人。

3. **看见线上在加密 / 看见未认证 / 这份对象 is not already 已经没有隐私改进 interchangeable，也不是已经 v2 transport vs private bundled（242） interchangeable / 1274 vt324-notpriv interchangeable / 1275 vt324-notrand interchangeable，也不是已经 eip8-new interchangeable / 235 eip8-new interchangeable。**  
   官方把线上在加密和已经没有隐私改进写成两件。看见线上在加密，不是已经没有隐私改进。

栈怎么写、分隔符、例串是规范里的取值，本页不抄。不要另写 怎样做中间人、怎样降级、怎样按时间认协议、怎样塑形。

## 官方为什么这样拆

- **加密 不是已经认证：官方把通道机密和对面是谁写成两件事。**
- **未认证 不是已经没有隐私改进：官方写即使未认证加密也比不加密严格更好。**
- **线上在加密 不是已经私人：官方写网上转发的数据本身是公开的。**

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 已经知道对面是谁 | 不是已经知道对面是谁 | 不是已经v1-reconnect（112） |
| 已经私人 | 不是已经私人 | 不是已经eip8-new（235） |
| 已经没有隐私改进 | 不是已经没有隐私改进 | 不是已经1275 vt324-notrand |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 BIP-324 enc not already private / not already authenticated / not already no-gain 正式三事（242 余量），必须分开是不是已经知道对面是谁、是不是已经私人、是不是已经没有隐私改进。可以跳过「看见机会主义未认证加密就已经私人」。不要另写 怎样做中间人、怎样降级、怎样按时间认协议、怎样塑形。242 v2 transport vs private bundled unbundling 在本页 item 1 启动；续 [`worked-example-vt324-notrand-vs-bundled.md`](worked-example-vt324-notrand-vs-bundled.md)（不变量 1275 item 2）。

## 本页不抄

- 握手长度、垃圾上限、再密钥间隔、曲线编码、测试向量。
- 怎样做中间人、怎样降级、怎样按时间认协议、怎样塑形。
