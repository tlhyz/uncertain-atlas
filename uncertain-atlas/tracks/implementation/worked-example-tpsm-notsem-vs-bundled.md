# 例：看见走脚本路径不是已经是本页这种脚本语义不是已经是本页这种脚本语义；看见taking the script path is not already this page's script semantics不是已经是不变量 153；看见走脚本路径不是已经是本页这种脚本语义不是已经 189 bundled

**层次**：实现 / 规范对象。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：Bitcoin [BIP-342](https://github.com/bitcoin/bips/blob/master/bip-0342.mediawiki)（Validation of Taproot Scripts）。  
**对应课文**：[L3.7](../../courses/level-03-bitcoin/L03-M07-segwit-soft-fork.md)。  
**不要写进**：`index/03` 共识行、M3.7、L3.7。本页是「BIP-342 scriptpath not already tapscript-semantics / not already 153 / not already 189-bundled 正式三事（189 余量）/ not 1557 tpsm-notsem interchangeable / not 189 tapscript-vs-scriptpath bundled interchangeable」，不是 tapscript vs scriptpath bundled（189），也不是已经 钥匙路径≠揭树（153），也不是已经 哈希≠已揭开赎回（170）。不要另写 怎样拼成功操作码、旧多重签改写、未知钥类型跳过验签。

## 官方三件事

1. **看见走脚本路径不是已经是本页这种脚本语义 / 看见走脚本路径不是已经是本页这种脚本语义 这份对象 is not already 已经是本页这种脚本语义 interchangeable，也不是已经 tapscript vs scriptpath bundled（189） interchangeable / 1557 tpsm-notsem interchangeable / 1558 tpsm-notdone interchangeable，也不是已经 BIP-342 scriptpath not already tapscript-semantics / not already 153 / not already 189-bundled 正式三事 bundled（189 item 1 余量） interchangeable / 189 tpsm item 1 interchangeable。**  
   官方把走脚本路径不是已经是本页这种脚本语义和已经是本页这种脚本语义写成两件。看见走脚本路径不是已经是本页这种脚本语义，不是已经是本页这种脚本语义。

2. **看见taking the script path is not already this page's script semantics / 看见走脚本路径不是已经是本页这种脚本语义 / 这份对象 is not already 已经是不变量 153 interchangeable，也不是已经 tapscript vs scriptpath bundled（189） interchangeable / 1557 tpsm-notsem interchangeable / 1559 tpsm-notmin interchangeable，也不是已经 钥匙路径≠揭树 interchangeable / 153 钥匙路径≠揭树 interchangeable。**  
   官方把taking the script path is not already this page's script semantics和已经是不变量 153写成两件。看见taking the script path is not already this page's script semantics，不是已经是不变量 153。

3. **看见走脚本路径不是已经是本页这种脚本语义 / 看见taking the script path is not already this page's script semantics / 这份对象 is not already 已经 189 bundled interchangeable，也不是已经 tapscript vs scriptpath bundled（189） interchangeable / 1557 tpsm-notsem interchangeable / 1558 tpsm-notdone interchangeable，也不是已经 哈希≠已揭开赎回 interchangeable / 170 哈希≠已揭开赎回 interchangeable。**  
   官方把走脚本路径不是已经是本页这种脚本语义和已经 189 bundled写成两件。看见走脚本路径不是已经是本页这种脚本语义，不是已经 189 bundled。

栈怎么写、分隔符、例串是规范里的取值，本页不抄。不要另写 怎样拼成功操作码、旧多重签改写、未知钥类型跳过验签。

## 官方为什么这样拆

- **走脚本路径不是已经是本页这种脚本语义 interchangeable：官方写本页规则只在隔离见证、341 taproot、脚本路径、叶子版本标成 tapscript 花费时适用。**
- **看见本页不是已经是不变量 153。**
- **看见脚本路径不是已经 189 bundled。**

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| 已经是本页这种脚本语义 | 不是已经是本页这种脚本语义 | 不是已经钥匙路径≠揭树（153） |
| 已经是不变量 153 | 不是已经是不变量 153 | 不是已经哈希≠已揭开赎回（170） |
| 已经 189 bundled | 不是已经 189 bundled | 不是已经1558 tpsm-notdone |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看 BIP-342 scriptpath not already tapscript-semantics / not already 153 / not already 189-bundled 正式三事（189 余量），必须分开是不是已经是本页这种脚本语义、是不是已经是不变量 153、是不是已经 189 bundled。可以跳过「看见成功操作码就已经执行完」。不要另写 怎样拼成功操作码、旧多重签改写、未知钥类型跳过验签。189 tapscript vs scriptpath bundled unbundling 在本页 item 1 启动；续 [`worked-example-tpsm-notdone-vs-bundled.md`](worked-example-tpsm-notdone-vs-bundled.md)（不变量 1558 item 2）。

## 本页不抄

- 操作码号、叶子版本、资源常数、例脚本。
- 怎样拼成功操作码、旧多重签改写、未知钥类型跳过验签。
