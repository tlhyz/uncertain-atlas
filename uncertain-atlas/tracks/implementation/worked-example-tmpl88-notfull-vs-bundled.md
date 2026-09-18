# 例：看见完整模板不是已经是半截模板；看见模板长度对上不是已经是同一条路径；看见以 m/ 开头不是已经交差

**层次**：应用 / 规范对象。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：Bitcoin [BIP-88](https://github.com/bitcoin/bips/blob/master/bip-0088.mediawiki)（Complete, Applications, Informational）。  
**对应课文**：[L1.4](../../courses/level-01-crypto/L01-M04-canonical-encoding.md)、[L3.6](../../courses/level-03-bitcoin/L03-M06-testing-and-culture.md)。  
**不要写进**：Ethereum 行、L5.1、03 共识、M5.4、L5.4。本页是「BIP-88 full-template not already half-template / not already same-path / not already settled 正式三事（288 余量）/ not 1183 tmpl88-notfull interchangeable / not 288 template-vs-path bundled interchangeable」，不是路径模板 bundled（288），也不是扩展公钥就已经能花（182），也不是路径里的脚本类型就已经必要（1176）。不要另写怎样解析或匹配模板。

## 官方三件事

1. **看见以 m/ 开头的完整模板 / 看见模板长度对上 这份模板 is not already 已经是半截模板 interchangeable，也不是已经路径模板 bundled（288） interchangeable / 1183 tmpl88-notfull interchangeable / 1181 tmpl88-notpath interchangeable / 288 tmpl item 1 path-not-tmpl interchangeable，也不是已经 BIP-88 full-template not already half-template / not already same-path / not already settled 正式三事 bundled（288 item 3 余量） interchangeable / 288 tmpl item 3 interchangeable。**  
   官方写：以 m/ 开头的是完整模板，匹配整条路径。不以 m/ 开头的是半截模板，只在合适的场合匹配路径的一段。完整模板不能再和另一份完整模板拼。看见以 m/ 开头，不是已经允许只配后半段。

2. **看见模板长度对上 / 看见完整模板 / 这份模板 is not already 已经是同一条路径 interchangeable，也不是已经路径模板 bundled（288） interchangeable / 1183 tmpl88-notfull interchangeable / 288 tmpl item 2 hard-not-interop interchangeable / 1182 tmpl88-nothard interchangeable，也不是已经扩展公钥就已经能花 interchangeable / 182 xpub interchangeable。**  
   官方另写：路径长度和模板长度对不上就失败。只有单位下标的完整模板，本身也是一条合法 32 路径。看见长度一样，不是已经配上。看见看起来像路径的模板，不是已经带了通配或区间约束。

3. **看见以 m/ 开头 / 看见完整模板 / 这份模板 is not already 已经交差 interchangeable，也不是已经路径模板 bundled（288） interchangeable / 1183 tmpl88-notfull interchangeable / 1181 tmpl88-notpath interchangeable，也不是已经路径里的脚本类型就已经必要 interchangeable / 1176 mpath87-notneed interchangeable。**  
   官方把匹配整条、匹配一段、长度必须对齐写成三道门。看见以 m/ 开头，不是已经交差。

语法取值、匹配步骤、形式化状态机、模板例句是规范里的取值或做法，本页不抄。

## 官方为什么这样拆

- **完整模板 不是已经是半截模板：** 官方把匹配整条和匹配一段写成两件。
- **模板长度对上 不是已经是同一条路径：** 官方把长度对齐写成还不一定配上。
- **以 m/ 开头 不是已经交差：** 官方把三道门写成三句。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 半截 | 不是已经是半截模板 | 不是已经能花（182） |
| 同一条 | 不是已经是同一条路径 | 不是已经必要（1176） |
| 交差 | 不是已经交差 | 不是已经能互操作（1182） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 BIP-88 full-template not already half-template / not already same-path / not already settled 正式三事（288 余量），必须分开是不是已经是半截模板、是不是已经是同一条路径、是不是已经交差。可以跳过「看见一条路径就已经能约束派生」。不要另写怎样解析或匹配模板。288 template vs path bundled unbundling 在本页 item 3 完成。

## 本页不抄

- 语法取值、匹配步骤、形式化状态机、模板例句、区间数字。
- 怎样解析、怎样匹配、怎样拼完整和半截、怎样比较两份模板是否相等。
