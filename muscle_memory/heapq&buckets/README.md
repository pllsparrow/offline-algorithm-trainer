# Heapq 与 Buckets 心智模型训练

这个专题不是重复 Hot 150 原题，而是训练你看到题面信号后，能够快速选择合适的数据结构。共 15 道高频变体，每题 99 个确定性用例。

## 五个识别信号

### 1. 只需要前 K 个，不需要完整排序

先想到大小固定为 `k` 的堆。扫描过程中只保留当前最有价值的候选，常见复杂度是 `O(n log k)`。

典型措辞：第 K 个、最小的 K 对、Top K、最多选择 K 个项目。

### 2. 多个来源各自有序

先想到多路归并堆。堆里不放全部元素，只放每个来源当前最靠前的候选。

典型措辞：K 个有序数组、K 个有序链表、覆盖每个列表的最小区间、有序矩阵中的第 K 小。

### 3. 资源会在未来某个时刻释放

先想到两个堆：一个保存空闲资源，一个保存 `(释放时间, 资源编号)`。

典型措辞：会议室、机器、服务器、CPU、等待任务、最早可用资源。

### 4. 数据动态进入，同时旧数据离开

中位数类问题先想到双堆；如果滑动窗口会删除任意旧值，还要想到 lazy deletion（延迟删除）。

典型措辞：数据流中位数、滑动窗口中位数、动态第 K 大。

### 5. 数值或频率可以直接映射成索引

先检查能否使用桶。桶不一定是“按值开一个超大数组”，也可以是频率桶、截断桶、区间桶、滑动哈希桶或差分桶。

典型措辞：频率范围不超过 `n`、值域有限、线性时间排序、距离不超过阈值、区间上下车。

## 训练题单

| ID | 题目 | 看到题目时的第一反应 | 对应高频题型 |
| --- | --- | --- | --- |
| `h01` | Top K Frequent Words | 频率优先，平局看字典序 | LeetCode 692 |
| `h02` | K Pairs With Smallest Sums | 不展开笛卡尔积，只扩展候选边界 | LeetCode 373 |
| `h03` | Merge K Sorted Arrays | 每个有序源只放一个候选 | Merge K Lists 变体 |
| `h04` | Kth Smallest in Sorted Matrix | 行是有序源，做多路归并 | LeetCode 378 |
| `h05` | Smallest Range Covering K Lists | 堆顶给左界，同时维护当前右界 | LeetCode 632 |
| `h06` | IPO Maximized Capital | 按资本解锁项目，再从利润堆选择 | LeetCode 502 |
| `h07` | Meeting Rooms III | 空闲房间堆 + 使用中房间堆 | LeetCode 2402 |
| `h08` | Sliding Window Median | 双堆平衡 + 延迟删除 | LeetCode 480 |
| `h09` | Reorganize String | 每次取当前剩余最多且不同的字符 | LeetCode 767 |
| `b01` | Sort Characters by Frequency | 频率就是桶下标 | LeetCode 451 |
| `b02` | H-Index | 大于 `n` 的引用都截断进第 `n` 桶 | LeetCode 274 |
| `b03` | Maximum Gap | 区间桶只保存桶内最小值和最大值 | LeetCode 164 |
| `b04` | Contains Nearby Almost Duplicate | 滑动窗口 + 宽度为阈值的哈希桶 | LeetCode 220 |
| `b05` | Relative Sort Array | 计数后按指定顺序消费桶 | LeetCode 1122 |
| `b06` | Car Pooling | 上车加、下车减的差分桶 | LeetCode 1094 |

## 建议训练顺序

第一轮只建立基础反射：

```text
h01 -> h02 -> h03 -> b01 -> b02 -> b05
```

第二轮练组合模型：

```text
h04 -> h05 -> h06 -> h07 -> h09 -> b06
```

第三轮练容易在面试中卡住的结构：

```text
h08 -> b03 -> b04
```

每道题通过后，必须能回答三个问题：

1. 堆或桶中保存的对象是什么？
2. 为什么不直接完整排序？
3. 哪个输入特征一旦改变，这种做法就不再合适？

## 判题命令

目录名包含 `&`，shell 命令中的路径必须加引号：

```bash
python3 'muscle_memory/heapq&buckets/judge.py' --list
python3 'muscle_memory/heapq&buckets/judge.py' h01
python3 'muscle_memory/heapq&buckets/judge.py' h01 --case 1
python3 'muscle_memory/heapq&buckets/judge.py' h01 --all
```

默认遇到第一个失败用例就停止。`--all` 会继续运行全部 99 个用例。

## 用例与判定规则

- 每题恰好 99 个不重复输入，使用固定随机种子，可稳定复现。
- 每题仅保留 1 到 3 个必要的小边界用例，其余至少 90 个是中到大规模数据。
- 覆盖重复、负数、极值、正序/逆序、稀疏/密集分布、资源竞争和边界并列。
- `h02`、`h09`、`b01` 使用语义校验，接受所有满足题意的答案。
- 其他题通过明确的平局规则消除歧义，并忽略无意义的空白差异。

这些题的 Python 文件只提供统一的 `readline()` 与 `solve()` 输入框架，不包含算法实现。
