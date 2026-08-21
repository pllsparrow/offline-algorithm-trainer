# Recursion 递归专项训练

这套题不追求“所有题都强行递归”，而是训练递归最重要的四个动作：定义函数职责、写清终止条件、缩小问题规模、处理返回阶段。

共 20 道题，其中 10 道是树形递归。每题 49 个确定性用例，总计 980 个。题型已与仓库 Hot 150 去重。建议先手写递归含义，再写代码；不要一上来追踪几十层调用栈。

## 训练题单

| 阶段 | ID | 题目 | 核心心智模型 |
| --- | --- | --- | --- |
| 基础 | `r01` | Sum of Digits | 单参数持续缩小 |
| 基础 | `r02` | Reverse String | 返回阶段组合答案 |
| 基础 | `r03` | Recursive Array Sum | 当前元素 + 更小问题 |
| 基础 | `r04` | Recursive Array Maximum | 合并当前值与递归返回值 |
| 基础 | `r05` | Count Target Occurrences | 每层贡献 0 或 1 |
| 基础 | `r06` | Remove Adjacent Duplicates | 相邻状态与返回结果 |
| 递推 | `r07` | Tower of Hanoi Move Count | 从动作过程提炼递推式 |
| 搜索 | `r08` | Restore IP Addresses | 切分选择与合法性校验 |
| 分治 | `r09` | Merge Sort | 拆分后合并返回值 |
| 分治 | `r10` | Count Inversions | 在归并阶段统计跨区间答案 |
| 树形入门 | `r11` | Recursive Tree Traversals | 递归调用前、中、后的访问位置 |
| 树形 | `r12` | Root-to-Leaf Path Sums | 携带路径状态到叶子 |
| 树形 | `r13` | Count Leaf Nodes | 合并左右子树计数 |
| 树形 | `r14` | Sum of Left Leaves | 向下携带父子关系 |
| 树形 | `r15` | Nodes at Depth K | 向下携带深度状态 |
| 树形进阶 | `r16` | Deepest Leaves Sum | 一次返回深度与聚合值 |
| 树形进阶 | `r17` | Root-to-Leaf Numbers | 路径状态的十进制累积 |
| 树形进阶 | `r18` | Prune Zero-Only Subtrees | 后序递归修改结构 |
| 树形进阶 | `r19` | Evaluate Expression Tree | 子树返回值驱动当前运算 |
| 树形进阶 | `r20` | Binary Tree Tilt | 返回子树和并累积全局答案 |

## 建议顺序

```text
r01 -> r02 -> r03 -> r04 -> r05 -> r06
r07 -> r08 -> r09 -> r10
r11 -> r13 -> r15 -> r12 -> r14
r17 -> r16 -> r19 -> r20 -> r18
```

每道题动手前先回答：

1. 这个递归函数接收什么，并承诺返回什么？
2. 最小问题是什么，什么时候必须停止？
3. 本层如何把问题缩小？返回时还要做什么？

## 判题命令

```bash
python3 muscle_memory/recursion/judge.py --list
python3 muscle_memory/recursion/judge.py r01
python3 muscle_memory/recursion/judge.py r01 --case 1
python3 muscle_memory/recursion/judge.py r01 --all
```

多答案题已规定规范输出：IP 地址按字典序排列，每行一个答案；树节点按题目要求保持从左到右顺序。

## 与 Hot 150 的边界

本专题不重复已有的二分查找、回文判断、子集、排列、组合总和、最大深度、翻转树、验证 BST、树直径、平衡树、相同树、子树、最近公共祖先、层序遍历、右视图、好节点、构造树、最大路径和及序列化题。

这里的树题专注于为上述综合题铺路的递归能力：遍历时机、子树聚合、路径状态、多个返回量和后序结构修改。
