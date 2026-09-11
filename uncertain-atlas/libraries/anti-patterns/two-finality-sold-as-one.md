# 反模式：两种最终性卖成一种

头里同时有「较快的确认对象」和「更强的 BFT 最终对象」，产品却只说「最终」。

NEAR 头字段（Nomicon / nearcore 数据结构）同时出现：

- `last_final_block`：注释写 **full BFT finality**  
- `last_ds_final_block`：注释写 **doomslug finality**

Nomicon Consensus 把「final」定义成：链上在 B 之后连续两个高度（B、B+1、B+2）。这与 Doomslug 论文的活性/确认不是同一句话。

**禁止的用户句：** 「NEAR 是秒最终，所以和 CometBFT commit 一样。」  
**应写：** 用户看见的绿勾对应头上哪一个哈希、哪一条谓词。

亲戚：L5.2 的 head / justified / finalized 三词；L3.1 的 k 确认政策。  
「不确定」：若采用双标记，文案必须点名对象，否则就是假最终。
