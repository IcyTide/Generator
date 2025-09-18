## 公式组成
- defense: 该技能命中目标防御
- damage: 该技能命中目标伤害
- critical_damage: 该技能命中目标会心伤害
- critical_strike: 该技能命中目标会心率

## 常驻变量：

### rand
定义域[0, 1], 代表随机波动范围；例如取值0代表此次波动为最小值，取值为1代表此次波动为最大值，取值为0.5代表计算期望值。影响基础伤害的波动值、武器伤害的波动值

### target_level
代表目标等级，用于计算目标防御和等级压制减伤


## 属性变量
主要存在三种值

### 基础属性值
形如base_something或者something_base，需要代入伤害的基础属性值

### 额外属性值
形如extra_something，来自于心法或buff带来的**额外**主属性转化，例如额外的破防和额外的攻击力，会心不作区分

### 百分比乘算属性值
形如something_gain，这部分值会直接对基础属性值进行百分比加成，但是额外属性值不参与计算

### 百分比加算属性值
形如something_rate，这部分值直接以百分比的形式加算到最后的计算结果，不会与基础属性进行互动

### 对照表
- attack_power = 攻击力
- weapon_damage =  武器攻击力
- surplus = 破招
- overcome = 破防
- critical_strike = 会心
- critical_power = 会效
- strain = 无双
- damage_addition = 增伤
- move_state_damage_addition = 特殊增伤
- pve_addition = 非侠增伤
- damage_cof = 易伤

## 秘籍变量
形状为 _ID_LEVEL ，代表秘籍的存在与否，取值为0或者1，0代表不存在1代表存在。

秘籍存在于自选秘籍、装备、buff和奇穴以及心法自带中
可以从buffs.json(buff), talents.json(奇穴)，attributes.json(心法)，kungfus/<心法名>/recipes.json(自选秘籍和装备)进行查询

秘籍会会影响当前计算中的各个属性来对最后结果直接造成影响，因此会作为自变量的一部分出现在公式中

## 数字常量
在公式中通常会出现一些神奇的不明数字常量，这部分通常是在链式结算后得到的多个常量计算结果，用于属性的放缩（即将属性值转化为百分比），可以直接进行套用