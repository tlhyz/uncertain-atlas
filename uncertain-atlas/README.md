# Uncertain Atlas

《全球区块链架构图谱》+《不确定链设计参考库》的第一轮交付。

**最高准则：** [`GOAL.md`](GOAL.md)  
写任何内容之前先读它。审核记录见 [`AUDIT_LOG.md`](AUDIT_LOG.md)。  
每小时定时器 `uncertain-atlas-keepalive` 会唤醒一次，防止任务停在半路。

这个目录是长期资产，不是一次写完的百科。  
第一轮只建立：**总路线图、知识树、研究顺序、资产目录、完整 Level 0 课程**。

更高 Level 会等你学完、提问、并回答测试题后再写。

---

## 这个库和本仓库的关系

当前 GitHub 仓库 `tlhyz/gate-grid-martingale` 本身是 Gate 永续回测框架。  
Atlas 先放在 `uncertain-atlas/`，与交易代码隔离，避免把协议研究混进量化工具。

「不确定 / Uncertain」是你正在构思的链。  
本目录的一切结论，最终都要回答：

> 这个设计是否真的适合「不确定」？

---

## 怎么用

1. 先读 [`GOAL.md`](GOAL.md) 和 [`00-master-roadmap.md`](00-master-roadmap.md)
2. 用 [`01-knowledge-tree.md`](01-knowledge-tree.md) 看依赖关系
3. 用 [`02-research-order.md`](02-research-order.md) 理解为什么不按「谁最有名」学
4. 用 [`03-knowledge-assets.md`](03-knowledge-assets.md) 知道最终会留下什么
5. 进入 [`levels/level-00-blockchain-as-machine/`](levels/level-00-blockchain-as-machine/README.md) 上课
6. 回答每节课末尾的测试题，**先不要看任何外部标准答案**
7. 把答案发回来，再进入下一级

学习规则：

- 不要跳 Level。
- 不要先去搜 TPS 排行榜。
- 不要把官网首页当协议规范。
- 任何重要判断都要标成：**事实 / 推断 / 建议**。

---

## 优先级标记

| 标记 | 含义 |
|---|---|
| 必学 | 不学会，后面所有协议都会变成名词堆砌 |
| 重要 | 「不确定」大概率会直接碰到 |
| 进阶 | 设计时必须懂，实现第一版可以后置 |
| 研究级 | 论文、形式化、后量子或隐私的深水区 |

---

## 第一轮范围

已交付：

- [x] MASTER ROADMAP
- [x] Level 0–10 知识树
- [x] 核心公链研究顺序与理由
- [x] 优先级标注
- [x] 长期知识资产目录
- [x] Level 0 完整课程（含测试题，不含答案）
- [x] 最高准则 Goal + 审核日志 + 每小时保活

刻意未交付：

- Level 1 及以后的完整教材
- 各公链完整 19 节模板报告
- Design Pattern / Anti-Pattern 全文库
- 失败博物馆全文
- 后量子工程手册全文
- 任何币价、空投、营销材料

---

## 目录

```
uncertain-atlas/
  README.md
  GOAL.md
  AUDIT_LOG.md
  00-master-roadmap.md
  01-knowledge-tree.md
  02-research-order.md
  03-knowledge-assets.md
  levels/level-00-blockchain-as-machine/
  tracks/                          # 以后：PQ / 失败博物馆 / 横向专题
  libraries/                       # 以后：pattern / anti-pattern / decision matrix
```
