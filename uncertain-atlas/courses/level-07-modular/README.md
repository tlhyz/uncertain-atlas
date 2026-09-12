# Level 7 · 模块化、DA、共享安全

优先级：重要  
先修：L1.3 Merkle、L3.1、L4 commit 语义、L5.4  
档案：Celestia、Polkadot、[乐观 rollup](../../protocols/optimistic-rollup/README.md)

| 课 | 文件 | 覆盖 | 核心问题 |
|---|---|---|---|
| 7.1 | [L07-M01-four-layers.md](L07-M01-four-layers.md) | M7.1 | 四层为什么要拆 |
| 7.2 | [L07-M02-data-availability.md](L07-M02-data-availability.md) | M7.2 | 有头为什么还不够；NMT 齐 ≠ 方阵可用 |
| 7.3 | [L07-M03-shared-security.md](L07-M03-shared-security.md) | M7.4 / M7.5 入口 | 借安全借到什么；backed ≠ 可用 |
| 7.4 | [L07-M04-rollup-tenant.md](L07-M04-rollup-tenant.md) | M7.3 | 乐观/ZK 租户与提款三条件 |

M7.5 restaking 等：只收独特思想，不因有名展开。  
Polkadot / Kusama 事故：博物馆 2025-05 交易深度套错对象（不变量 97）；2025-08 组下标≠票下标（不变量 98）；2024-02 Active≠Confirmed（不变量 99）；2025-05-09 链下禁用≠已确认不参与（不变量 100）；2026-06 选举地板≠已配对（不变量 110）；2026-03 preserve_origin≠出站已绑（不变量 113）；2026-03 废弃 API≠编码兼容（不变量 114）。
