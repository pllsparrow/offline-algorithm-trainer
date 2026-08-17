# 离线算法刷题器

[English](README.md)

我做这个项目，是因为平时刷算法题要在网页、编辑器和在线判题之间来回切换，写完以后还得复制代码提交，调试起来也不太顺手。

所以我把 150 道常见面试题整理到了本地。所有题目 Python 文件都直接放在 `hot_150/` 中，每道题都是一个 ACM 模式的程序：从标准输入读数据、向标准输出写结果，判题器直接比对输出。这和真实笔试环境一致，平时的刷题过程就是：

```text
选一道题 -> 写对应的 Python 文件 -> 运行测试 -> 看失败用例 -> 修改
```

刷题进度会记录在本地 SQLite 文件里，自己写的答案和进度文件都不会被提交到 GitHub。

如果你是在第一次学习题型，而不只是复习，请先阅读
[`docs/learning_protocol.md`](docs/learning_protocol.md)。其中定义了函数模式到
ACM 模式的迁移、提示阶梯、每日训练流程和掌握标准。

所有题目的 NeetCode 题面链接集中在
[`docs/neetcode_links.md`](docs/neetcode_links.md)。每道题的 Python 文件顶部只保留
简短的 ACM 输入和输出格式英文注释。

## 怎么开始

需要 Python 3.12 或更高版本，不用安装第三方依赖。

```bash
git clone https://github.com/pllsparrow/offline-algorithm-trainer.git
cd offline-algorithm-trainer

python3 train.py list
python3 train.py show two-sum
python3 train.py run two-sum
python3 train.py run 003
python3 train.py status
```

`show` 会显示题目说明、ACM 输入输出格式和题目文件的位置。文件名采用 `qNNN_problem_name.py` 格式，默认只包含两行输入输出注释；输入解析、算法、输出和程序入口都需要自己写。完成后用 `run` 执行本地用例；运行失败时会直接显示输入、预期输出和实际输出。

如果只想反复调试某一个失败用例：

```bash
python3 train.py run two-sum --case 1
```

也可以按专题或难度找题：

```bash
python3 train.py list --category graph
python3 train.py list --difficulty Hard
```

## ACM 文本协议

全部 150 道题使用纯文本协议。每个测试用例包含一段 stdin 和一段期望的
stdout。判题器把你的文件作为独立 Python 进程运行，喂入 stdin，捕获
stdout，然后与期望输出做空白归一化后的精确比对。

其中 148 道题各有 50 个去重用例，覆盖边界、重复值、极值、不同规模和结构
形态。`generate-parentheses` 和 `n-queens` 分别使用 9 个和 10 个穷尽/边界
输入；这两题的合法输入域很小，不用重复输入凑数量。

常见输入格式：

- **整数列表**：第一行个数 `n`，第二行 `n` 个整数。
- **单个整数 / 浮点数 / 字符串**：一行。
- **整行字符串**（可能含空格）：一行，用 `readline` 读取。
- **整数矩阵**：第一行 `r c`，然后 `r` 行每行 `c` 个整数。
- **字符网格**：第一行 `r c`，然后 `r` 行每行 `c` 个字符。
- **二叉树**：第一行个数 `n`，然后 `n` 个层序值（缺失用 `null`）。
- **图邻接表**：第一行节点数 `n`，然后每行度数 `d` 和 `d` 个邻居编号。
- **链表**：第一行个数 `n`，然后 `n` 个整数。
- **操作序列（设计题）**：第一行操作数 `q`，然后 `q` 行 `op args...`。
  输出每个操作的结果（无返回值用 `null`）。

对于有多种合法答案的题目（如 `group-anagrams`、`3sum`、`subsets`），期望
输出已做规范化排序，你也需要按同样的排序输出才能通过。

开始编码前先查看该题的准确输入格式：

```bash
python3 train.py show two-sum
python3 train.py check
```

`scripts/build_acm.py` 可以根据 `data/problems.json` 和 `data/tests.json`
确定性地重新生成全部 150 道题的 ACM 规范。

## 常用命令

| 命令 | 用途 |
| --- | --- |
| `python3 train.py list` | 查看题目和本地进度 |
| `python3 train.py show <slug>` | 查看题目详情、ACM 格式和文件位置 |
| `python3 train.py run <slug>` | 运行本地 ACM 测试用例 |
| `python3 train.py run <题号>` | 按题号运行，例如 `run 001` |
| `python3 train.py run <slug> --case 1` | 单独复现一个失败用例 |
| `python3 train.py run <slug> --all` | 某个用例失败后继续往下运行 |
| `python3 train.py status` | 查看已做和通过数量 |
| `python3 train.py check` | 检查题库数据是否完整 |
| `python3 train.py scaffold --force` | 把全部题目文件重置为输入输出注释 |

PyCharm 用户可以选择项目自带的 `Judge Current Solution` 运行配置。选择一次后，打开 `hot_150/` 中任意题目文件，点击绿色 Run 按钮即可判题。

150 道题全部直接放在 `hot_150/` 目录，文件名类似 `q001_contains_duplicate.py`。`judge/` 是本地判题代码，`data/` 保存题目元数据、测试用例和本地进度。

堆和桶的高频变体练习放在
[`muscle_memory/heapq&buckets/`](muscle_memory/heapq&buckets/README.md)，共 15 道题，
每题包含 99 个可复现用例；允许并列答案的题目使用语义校验器。

## 关于题目内容

题目名称和链接会指向 LeetCode 和 NeetCode。本仓库只保留我整理的题目摘要、提示、代码模板、测试工具和本地测试数据，不搬运商业平台的完整题面和官方答案。具体说明见 [NOTICE.md](NOTICE.md)。

项目原创代码使用 [MIT License](LICENSE)。
