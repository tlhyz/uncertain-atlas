# 反模式：哨兵有效槽被写成卸载后再编译已经可见

> 真值：[Solana 2024-02-06](../../tracks/failure-museum/solana-2024-02-06-legacy-loader-loop.md)、[不变式 88](../invariants/README.md)。亲戚：[local-rng-in-apply](local-rng-in-apply.md)、[recovery-shred-sold-as-filtered](recovery-shred-sold-as-filtered.md)。

## 一句话

看见旧加载器缓存用 0 当缺省有效槽，或看见「已经再编译过」，就写成主循环已经找得到；或把重启时禁止再部署写成缓存已经修完。

## 正确写法

「插入键必须与查找键是同一对象。哨兵 0 落在卸载条目后面不是已加载。关掉部署入口是拆前提，不是谓词已改。协作加载让交易进块，必须测全网回放，不得只测 leader。」
