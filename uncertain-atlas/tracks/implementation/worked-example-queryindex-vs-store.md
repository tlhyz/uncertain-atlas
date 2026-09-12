# 例：看见 Query 回包 index 是树里这个键的下标不是已经是按键查；看见 Query 回包 key 是对上的那份数据的键不是已经是 Query 高度；看见 Query 回包 value 是对上的那份数据的值不是已经对上 AppHash

**层次**：实现 / Query 回包。  
**分类**：事实（对象边界）+ 推断（产品）+ 建议（产品）。  
**来源**：CometBFT 官方 [ABCI++ Methods](https://github.com/cometbft/cometbft/blob/main/spec/abci/abci++_methods.md) Query Response。  
**对应课文**：[L4.4](../../courses/level-04-bft/L04-M04-abci-and-wal.md)。  
**不要写进**：Ethereum 行、L5.1、M5.4、L5.4、03 共识图谱、Bitcoin 行、L4.5。本页是「Query 回包 index 是树里这个键的下标不是已经是按键查 / Query 回包 key 是对上的那份数据的键不是已经是 Query 高度 / Query 回包 value 是对上的那份数据的值不是已经对上 AppHash」，不是 path /store 就必须按键查就已经是引擎在用，也不是 Query 回了 Proof 就已经对上 AppHash。不要另写怎样写 Query 回包。

## 官方三件事

规范把 Query 回包 `index` 是树里这个键的下标、`key` 是对上的那份数据的键、`value` 是对上的那份数据的值写成三件独立的实现事，不是「看见 Query 回了键值就已经是按键查、已经是 Query 高度、已经对上 AppHash」一件事：

1. **看见 Query 回包 `index` 是树里这个键的下标 / 看见有下标 不是已经是按键查，也不是已经对上 AppHash。**  
   官方写：`index` 是树里这个键的下标。看见有下标，不是已经按 `/store` 按键查。看见填了下标，不是已经对上 AppHash。看见有数，不是已经交差。
2. **看见 Query 回包 `key` 是对上的那份数据的键 / 看见回了键 不是已经是 Query 高度，也不是已经新鲜。**  
   官方写：`key` 是对上的那份数据的键。看见回了键，不是已经填了高度。看见有键，不是已经新鲜。看见能回，不是已经交差。
3. **看见 Query 回包 `value` 是对上的那份数据的值 / 看见回了值 不是已经对上 AppHash，也不是已经复制到各节点。**  
   官方写：`value` 是对上的那份数据的值。看见回了值，不是已经对上 AppHash。看见有字节，不是已经复制到各节点。看见能读，不是已经交差。

怎样写 Query 回包、怎样填下标、怎样对键值是规范里的做法，本页不抄。path /store 就必须按键查就已经是引擎在用是不变量 377，本页不抄。

## 官方为什么这样拆

- **Query 回包 index 是树里这个键的下标 ≠ 已经是按键查：** 官方把回包下标和请求必须按键查分开。
- **Query 回包 key 是对上的那份数据的键 ≠ 已经是 Query 高度：** 官方把回包键和查询高度分开。
- **Query 回包 value 是对上的那份数据的值 ≠ 已经对上 AppHash：** 官方把回包值和证明对上 AppHash 分开。

## 和相邻页的边界

| 对象 | 本页 | 那一页 |
|---|---|---|
| Query 回包 index 是树里这个键的下标 | 不是已经是按键查 | 不是 path /store 就必须按键查就已经是引擎在用（377） |
| Query 回包 key 是对上的那份数据的键 | 不是已经是 Query 高度 | 不是 Query 可以对当前或过去高度查就已经是 QueryState（371） |
| Query 回包 value 是对上的那份数据的值 | 不是已经对上 AppHash | 不是 Query 回了 Proof 就已经对上 AppHash（325） |

## 产品

**建议（产品，不是事实）**：不确定第一条结算机如果给人看「看见 Query 回了键值就已经是按键查、已经是 Query 高度、已经对上 AppHash」，必须分开 Query 回包 index 是树里这个键的下标是不是已经是按键查、Query 回包 key 是对上的那份数据的键是不是已经是 Query 高度、Query 回包 value 是对上的那份数据的值是不是已经对上 AppHash。可以跳过「看见 Query 回了键值就已经是按键查」。不要另写怎样写 Query 回包。

## 本页不抄

- 怎样写 Query 回包、怎样填下标、怎样对键值。
- path /store 就必须按键查就已经是引擎在用。那是不变量 377。
- Query 可以对当前或过去高度查就已经是 QueryState。那是不变量 371。
- Query 回了 Proof 就已经对上 AppHash。那是不变量 325。
