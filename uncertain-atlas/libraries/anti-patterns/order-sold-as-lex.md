# 反模式：看见自家习惯的输入输出顺序就当成已经是字典序标准 / 看见按字典序排了就当成已经是共识 / 看见按字典序排了就当成已经私人

**层次**：应用 / 失败模式。  
**分类**：事实（对象）+ 推断（事故）。  
**来源**：[BIP-69](https://github.com/bitcoin/bips/blob/master/bip-0069.mediawiki)。  
**例**：[自家习惯顺序 ≠ 已经是字典序标准](../../tracks/implementation/worked-example-order-vs-lex.md)。

## 塌法

1. 看见自家习惯的输入输出顺序 / 看见先花后找零，就当成已经是本页，或当成已经没有指纹。
2. 看见按字典序排了，就当成已经是共识，或当成顺序已经决定这笔能不能花。
3. 看见按字典序排了，就当成已经私人，或当成已经是随机打乱，或当成已经是 CoinJoin。
4. 看见随机排，就当成已经是本页，或当成已经可审计。
5. 看见 payjoin 提案不得打乱，就当成已经是本页。

## 为什么会出事

官方写：当时没有标准，习惯排法会漏指纹。本页是信息 BIP，顺序并不影响这笔功能。确定排法是为了可审计，不是已经随机，也不是已经对观察者私人。

## 和相邻反模式

- [original-sold-as-payjoin](original-sold-as-payjoin.md) 是原始包 ≠ 已经是提案，不是本页这种钱包自己交出去的顺序。
- [policy-sold-as-consensus](policy-sold-as-consensus.md) 是策略 ≠ 已经是共识，不是本页。
- [rbf-sold-as-replaced](rbf-sold-as-replaced.md) 是替换信号 ≠ 已经换掉，不是本页。
- [duplicate-txid-sold-as-unique](duplicate-txid-sold-as-unique.md) 是同一标识 ≠ 已经唯一，不是本页。
