# 例：看见一条派生路径不是已经是一份路径模板；看见写了 44 不是已经能被软件无歧义解析；看见一条路径不是已经交差

**层次**：应用 / 规范对象。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：Bitcoin [BIP-88](https://github.com/bitcoin/bips/blob/master/bip-0088.mediawiki)（Complete, Applications, Informational）。  
**对应课文**：[L1.4](../../courses/level-01-crypto/L01-M04-canonical-encoding.md)、[L3.6](../../courses/level-03-bitcoin/L03-M06-testing-and-culture.md)。  
**不要写进**：Ethereum 行、L5.1、03 共识、M5.4、L5.4。本页是「BIP-88 one-path not already path-template / not already unambiguous / not already settled 正式三事（288 余量）/ not 1181 tmpl88-notpath interchangeable / not 288 template-vs-path bundled interchangeable」，不是路径模板 bundled（288），也不是自称 compatible 就已经能互操作（1118），也不是路径里的脚本类型就已经必要（1176）。不要另写怎样解析或匹配模板。

## 官方三件事

1. **看见一条派生路径 / 看见 43 / 44 / 45 / 49 / 84 那种方案 这份模板 is not already 已经是一份路径模板 interchangeable，也不是已经路径模板 bundled（288） interchangeable / 1181 tmpl88-notpath interchangeable / 1182 tmpl88-nothard interchangeable / 288 tmpl item 2 hard-not-interop interchangeable，也不是已经 BIP-88 one-path not already path-template / not already unambiguous / not already settled 正式三事 bundled（288 item 1 余量） interchangeable / 288 tmpl item 1 interchangeable。**  
   官方写：32 那种路径写法很通用，后面又出了 43 和别的派生方案。可是就算用了这些方案，各家钱包用得并不齐。看见一条路径，不是已经有约束。

2. **看见写了 44 / 看见一条派生路径 / 这份模板 is not already 已经能被软件无歧义解析 interchangeable，也不是已经路径模板 bundled（288） interchangeable / 1181 tmpl88-notpath interchangeable / 288 tmpl item 3 full-not-half interchangeable / 1183 tmpl88-notfull interchangeable，也不是已经自称 compatible 就已经能互操作 interchangeable / 1118 purp43-notinterop interchangeable。**  
   官方另写：有人用竖线把几条路径或几个下标写在一起，只是给人看的临时写法，没有写成给软件解析的规范。本页这份格式既要给人一眼看出哪一段是模板，也要让软件无歧义解析。看见写了 44，不是各家已经对齐。

3. **看见一条路径 / 看见一条派生路径 / 这份模板 is not already 已经交差 interchangeable，也不是已经路径模板 bundled（288） interchangeable / 1181 tmpl88-notpath interchangeable / 1182 tmpl88-nothard interchangeable，也不是已经路径里的脚本类型就已经必要 interchangeable / 1176 mpath87-notneed interchangeable。**  
   官方把给人看的临时写法和给软件解析的模板写成两件东西。看见一条路径，不是已经交差。

语法取值、匹配步骤、形式化状态机、模板例句是规范里的取值或做法，本页不抄。

## 官方为什么这样拆

- **一条派生路径 不是已经是一份路径模板：** 官方把各家用得不齐写成还没有模板。
- **写了 44 不是已经能被软件无歧义解析：** 官方把竖线临时写法写成不是规范。
- **一条路径 不是已经交差：** 官方把约束和解析写成两句。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 模板 | 不是已经是一份路径模板 | 不是已经能互操作（1118） |
| 解析 | 不是已经能被软件无歧义解析 | 不是已经必要（1176） |
| 交差 | 不是已经交差 | 不是已经写死就能换钱包（1182） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 BIP-88 one-path not already path-template / not already unambiguous / not already settled 正式三事（288 余量），必须分开是不是已经是一份路径模板、是不是已经能被软件无歧义解析、是不是已经交差。可以跳过「看见一条路径就已经能约束派生」。不要另写怎样解析或匹配模板。288 template vs path bundled unbundling 在本页 item 1 启动；续 [`worked-example-tmpl88-nothard-vs-bundled.md`](worked-example-tmpl88-nothard-vs-bundled.md)（不变量 1182 item 2）。

## 本页不抄

- 语法取值、匹配步骤、形式化状态机、模板例句、区间数字。
- 怎样解析、怎样匹配、怎样拼完整和半截、怎样比较两份模板是否相等。
