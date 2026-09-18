# 例：看见支持第 2 版不是第 1 版已经退役；看见导出了会话标识不是已经对照过；看见支持第 2 版不是应用消息已经不再公开

**层次**：网络 / 规范对象。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：Bitcoin [BIP-324](https://github.com/bitcoin/bips/blob/master/bip-0324.mediawiki)（Deployed, Peer Services；替换 151）。  
**对应课文**：[L3.4](../../courses/level-03-bitcoin/L03-M04-network-and-eclipse.md)、[L9.1](../../courses/level-09-systems/L09-M01-p2p.md)。  
**不要写进**：`index/03` 共识行、Ethereum 行、M5.4、L5.1、L5.4、05b。本页是「BIP-324 v2 not already v1-retired / not already session-checked / not already app-private 正式三事（242 余量）/ not 1276 vt324-notold interchangeable / not 242 v2-transport-vs-private bundled interchangeable」，不是 v2 transport vs private bundled（242），也不是已经 v1-reconnect（112），也不是已经 ua-protocol（263）。不要另写 怎样做中间人、怎样降级、怎样按时间认协议、怎样塑形。

## 官方三件事

1. **看见支持第 2 版 / 看见支持第 2 版 这份对象 is not already 第 1 版已经退役 interchangeable，也不是已经 v2 transport vs private bundled（242） interchangeable / 1276 vt324-notold interchangeable / 1274 vt324-notpriv interchangeable，也不是已经 BIP-324 v2 not already v1-retired / not already session-checked / not already app-private 正式三事 bundled（242 item 3 余量） interchangeable / 242 v2 item 3 interchangeable。**  
   官方把支持第 2 版和第 1 版已经退役写成两件。看见支持第 2 版，不是第 1 版已经退役。

2. **看见导出了会话标识 / 看见支持第 2 版 / 这份对象 is not already 已经对照过 interchangeable，也不是已经 v2 transport vs private bundled（242） interchangeable / 1276 vt324-notold interchangeable / 1275 vt324-notrand interchangeable，也不是已经 v1-reconnect interchangeable / 112 v1-reconnect interchangeable。**  
   官方把导出了会话标识和已经对照过写成两件。看见导出了会话标识，不是已经对照过。

3. **看见支持第 2 版 / 看见导出了会话标识 / 这份对象 is not already 应用消息已经不再公开 interchangeable，也不是已经 v2 transport vs private bundled（242） interchangeable / 1276 vt324-notold interchangeable / 1274 vt324-notpriv interchangeable，也不是已经 ua-protocol interchangeable / 263 ua-protocol interchangeable。**  
   官方把支持第 2 版和应用消息已经不再公开写成两件。看见支持第 2 版，不是应用消息已经不再公开。

栈怎么写、分隔符、例串是规范里的取值，本页不抄。不要另写 怎样做中间人、怎样降级、怎样按时间认协议、怎样塑形。

## 官方为什么这样拆

- **支持第 2 版 不是第 1 版已经退役：官方为了少切网仍收旧入站。**
- **导出了会话标识 不是已经对照过：官方写运维可以对照，不是已经对照。**
- **传输在加密 不是应用消息已经不再公开：官方把应用层公开数据写成另一件事。**

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 第 1 版已经退役 | 不是第 1 版已经退役 | 不是已经v1-reconnect（112） |
| 已经对照过 | 不是已经对照过 | 不是已经ua-protocol（263） |
| 应用消息已经不再公开 | 不是应用消息已经不再公开 | 不是已经1274 vt324-notpriv |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 BIP-324 v2 not already v1-retired / not already session-checked / not already app-private 正式三事（242 余量），必须分开是不是第 1 版已经退役、是不是已经对照过、是不是应用消息已经不再公开。可以跳过「看见机会主义未认证加密就已经私人」。不要另写 怎样做中间人、怎样降级、怎样按时间认协议、怎样塑形。242 v2 transport vs private bundled unbundling 在本页 item 3 完成；本页收束本批。

## 本页不抄

- 握手长度、垃圾上限、再密钥间隔、曲线编码、测试向量。
- 怎样做中间人、怎样降级、怎样按时间认协议、怎样塑形。
