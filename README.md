# 对于用户

## 心法选择界面
分为三个部分，选择区，加载区，存储区

点击Load即可加载缓存文件

选择心法后Load将不可用，点击Save将现有配置保存至缓存文件

## Gear界面
Gear是配装界面，Details可显示当前装备总和属性、附加秘籍、附加特殊效果

Select Stone进行选择五彩石

子选项中的Detail可查看当前装备属性，附加秘籍、附加特殊效果

## Loop界面
Section > Record > Buffs, Skills, Dots

- Section可以理解为循环中的小节概念，多个小节组成了一个完整循环；

- Record是小节中由于buff覆盖不同产生的多个片段，多个片段组成一个小节；

- Record由Buffs来表示片段的增益情况，Skills和Dots代表片段中造成伤害的种类

- Buffs分为三类，Both Current Snapshot，Both代表后两者，会在后续Dot计算时进行区分

- Skills会加载所有Current类型的Buff并获取属性进行计算

- Dots会分别加载Current和Snapshot的Buff进行计算，从Current中获取实时属性，从Snapshot中获取快照属性

## Build界面
用于选择奇穴和秘籍相关

# 对于开发者
## 公式组成
- damage: 该技能命中目标伤害
- critical_damage: 该技能命中目标会心伤害
- critical_strike: 该技能命中目标会心率

## 常驻变量：
### rand
定义域[0, 1], 代表随机波动范围；例如取值0代表此次波动为最小值，取值为1代表此次波动为最大值，取值为0.5代表计算期望值。影响基础伤害的波动值、武器伤害的波动值

### target_level
代表目标等级，用于计算目标防御和等级压制减伤

### tick
代表dot的当前跳数，用于计算dot的递增/递减系数，出现于部分心法的dot中

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

## 秘籍变量
形状为 recipe_ID_LEVEL ，代表秘籍的存在与否，取值为0或者1，0代表不存在1代表存在。

秘籍存在于自选秘籍、装备、buff和奇穴以及心法自带中
可以从buffs.json(buff), belongs.json(心法和奇穴)，kungfus/<心法名>/recipes.json(自选秘籍和装备)进行查询

秘籍会影响当前计算中的各个属性来对最后结果直接造成影响，因此会作为自变量的一部分出现在公式中

## 奇穴变量
形状为 talent_ID，代表奇穴的存在与否，取值为0或者1，0代表不存在1代表存在。

奇穴会影响当前计算中的易伤部分来对最后结果直接造成影响，因此会作为自变量的一部分出现在公式中

## Buff变量
形状为 buff_ID_LEVEL，代表特定的buff层数，取值为[0, max_stack]。

这部分通常用于处理部分专属于特定技能的易伤处理，作用域体现在buffs.json中对应buff的skills

## 数字常量
在公式中通常会出现一些神奇的不明数字常量，这部分通常是在链式结算后得到的多个常量计算结果，用于属性的放缩（即将属性值转化为百分比），可以直接进行套用


# 翻译对照表
- base = 基础
- gain = 加成（乘算）
- rate = 加成（加算）
- physical = 外功
- solar = 阳性
- lunar = 阴性
- neutral = 混元
- poison = 毒性
- magical = 内功
- attack_power = 攻击力
- weapon_damage =  武器攻击力
- surplus = 破招
- overcome = 破防
- critical_strike = 会心
- critical_power = 会效
- strain = 无双
- damage_addition = 增伤
- pve_addition = 非侠增伤
- damage_cof = 易伤