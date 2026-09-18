# 例：看见写死了熟路径检查不是已经能互操作；看见熟路径表不是已经挡住乱派生；看见写死了 44 / 49 / 84 不是已经交差

**层次**：应用 / 规范对象。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：Bitcoin [BIP-88](https://github.com/bitcoin/bips/blob/master/bip-0088.mediawiki)（Complete, Applications, Informational）。  
**对应课文**：[L1.4](../../courses/level-01-crypto/L01-M04-canonical-encoding.md)、[L3.6](../../courses/level-03-bitcoin/L03-M06-testing-and-culture.md)。  
**不要写进**：Ethereum 行、L5.1、03 共识、M5.4、L5.4。本页是「BIP-88 hardcoded-check not already interoperable / not already blocks-wild / not already settled 正式三事（288 余量）/ not 1182 tmpl88-nothard interchangeable / not 288 template-vs-path bundled interchangeable」，不是路径模板 bundled（288），也不是自称 compatible 就已经能互操作（1118），也不是部分签名包就已经是跨厂开户（1178）。不要另写怎样解析或匹配模板。

## 官方三件事

1. **看见写死了熟路径检查 / 看见熟路径表 这份模板 is not already 已经能互操作 interchangeable，也不是已经路径模板 bundled（288） interchangeable / 1182 tmpl88-nothard interchangeable / 1181 tmpl88-notpath interchangeable / 288 tmpl item 1 path-not-tmpl interchangeable，也不是已经 BIP-88 hardcoded-check not already interoperable / not already blocks-wild / not already settled 正式三事 bundled（288 item 2 余量） interchangeable / 288 tmpl item 2 interchangeable。**  
   官方写：在软件或固件里写死熟路径检查，互操作会变差。厂家不能为自己那种非通用应用选合适的自定义路径，只能硬塞进熟路径，或去说服别人认自己的路径。看见写死了 44 / 49 / 84，不是已经能换钱包。

2. **看见熟路径表 / 看见写死了熟路径检查 / 这份模板 is not already 已经挡住乱派生 interchangeable，也不是已经路径模板 bundled（288） interchangeable / 1182 tmpl88-nothard interchangeable / 288 tmpl item 3 full-not-half interchangeable / 1183 tmpl88-notfull interchangeable，也不是已经自称 compatible 就已经能互操作 interchangeable / 1118 purp43-notinterop interchangeable。**  
   官方另写：不加限制地用派生路径，在有些场合不安全。尤其是找零打到发送方不认识的路径上，发送方可能丢掉全部找零。本页的灵活做法，是用一份标准记号写下要对路径施加的约束。看见熟路径表，不是已经挡住乱派生。

3. **看见写死了 44 / 49 / 84 / 看见写死了熟路径检查 / 这份模板 is not already 已经交差 interchangeable，也不是已经路径模板 bundled（288） interchangeable / 1182 tmpl88-nothard interchangeable / 1181 tmpl88-notpath interchangeable，也不是已经部分签名包就已经是跨厂开户 interchangeable / 1178 bsms129-notsetup interchangeable。**  
   官方把硬编码熟路径和可声明的约束写成两条扩展性不同的路。看见写死了 44 / 49 / 84，不是已经交差。

语法取值、匹配步骤、形式化状态机、模板例句是规范里的取值或做法，本页不抄。

## 官方为什么这样拆

- **写死了熟路径检查 不是已经能互操作：** 官方把硬编码熟路径写成互操作会变差。
- **熟路径表 不是已经挡住乱派生：** 官方把标准记号写成才能施加约束。
- **写死了 44 / 49 / 84 不是已经交差：** 官方把换钱包和挡住乱派生写成两句。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 互操作 | 不是已经能互操作 | 不是已经自称 compatible（1118） |
| 乱派生 | 不是已经挡住乱派生 | 不是已经开过户（1178） |
| 交差 | 不是已经交差 | 不是已经是模板（1181） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 BIP-88 hardcoded-check not already interoperable / not already blocks-wild / not already settled 正式三事（288 余量），必须分开是不是已经能互操作、是不是已经挡住乱派生、是不是已经交差。可以跳过「看见一条路径就已经能约束派生」。不要另写怎样解析或匹配模板。288 template vs path bundled unbundling 在本页 item 2 续；续 [`worked-example-tmpl88-notfull-vs-bundled.md`](worked-example-tmpl88-notfull-vs-bundled.md)（不变量 1183 item 3）。

## 本页不抄

- 语法取值、匹配步骤、形式化状态机、模板例句、区间数字。
- 怎样解析、怎样匹配、怎样拼完整和半截、怎样比较两份模板是否相等。
