# 模式：块上的 Commit 必须先点名是哪一份、印在哪一块

**问题：** 产品把「块上有 LastCommit」写成已经解释了本高度最终。用户把本头票听成本高度已经 +2/3，把本地看见的那份听成链上那一份。  
**方案：** 每个 Commit 句先点名问的是本头里上一块的 canonical LastCommit、某验证者本地的 subjective commit，还是本高度要等下一块才印上去的那份。  
**适用：** CometBFT / 任何「本块带上一块 +2/3、本高度的票进下一块」的结算文案。  
**优点：** 用户能指出昨天签字页、口袋小便签、明天才订上去的那一页不是同一份。  
**缺点：** 句子变长；不能再用「有 Commit」交差。  
**项目：** cometbft `spec/consensus/consensus.md` Canonical vs subjective commit；`spec/core/data_structures.md` LastCommit。  
**常见 bug：** 本头 LastCommit 写成本高度已最终；本地 +2/3 写成已经 canonical。  
**不确定：** 若抄 CometBFT 头，必须写清本块 LastCommit 是上一高度。不要把本地那份写成已经是链上那一份。见 [工作实例](../../tracks/consensus/worked-example-lastcommit-vs-this-block.md)。
