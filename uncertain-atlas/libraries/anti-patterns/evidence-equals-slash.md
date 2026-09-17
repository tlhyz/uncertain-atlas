# 反模式：证据上链等于已经罚没

CometBFT 的证据系统发现、流言、上链，再经 `FinalizeBlock` 把 `Misbehavior` 交给应用。  
规范原文：证据本身不惩罚坏人；罚没是应用的裁量。

另一半：若 ≥1/3 仍是拜占庭，证据可被审查，只是 best effort。  
「链上有证据所以经济安全」把协议对象和经济结果焊成一句。

亲戚：[`../threat-model/README.md`](../threat-model/README.md) 第 3、7 行；桥资本不对称精读。  
规范：[`../../tracks/economic/worked-example-evidence.md`](../../tracks/economic/worked-example-evidence.md)。
