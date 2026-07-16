# 离线算法刷题器

[English](README.md)

我做这个项目，是因为平时刷算法题要在网页、编辑器和在线判题之间来回切换，写完以后还得复制代码提交，调试起来也不太顺手。

所以我把 150 道常见面试题整理到了本地，按数组、链表、树、图、动态规划等专题分类。每道题都有一个 `solution.py` 和本地测试用例，平时的刷题过程就是：

```text
选一道题 -> 写 solution.py -> 运行测试 -> 看失败用例 -> 修改
```

刷题进度会记录在本地 SQLite 文件里，自己写的答案和进度文件都不会被提交到 GitHub。

## 怎么开始

需要 Python 3.12 或更高版本，不用安装第三方依赖。

```bash
git clone https://github.com/pllsparrow/offline-algorithm-trainer.git
cd offline-algorithm-trainer

python train.py list
python train.py show two-sum
python train.py run two-sum
python train.py status
```

`show` 会显示题目说明和 `solution.py` 的位置。打开文件写答案，再用 `run` 执行本地用例。运行失败时会直接显示输入、预期结果和实际结果。

如果只想反复调试某一个失败用例：

```bash
python train.py run two-sum --case 1 --debug
```

也可以按专题或难度找题：

```bash
python train.py list --category graph
python train.py list --difficulty Hard
```

## 常用命令

| 命令 | 用途 |
| --- | --- |
| `python train.py list` | 查看题目和本地进度 |
| `python train.py show <slug>` | 查看题目详情和文件位置 |
| `python train.py run <slug>` | 运行本地测试用例 |
| `python train.py run <slug> --case 1` | 单独复现一个失败用例 |
| `python train.py run <slug> --all` | 某个用例失败后继续往下运行 |
| `python train.py status` | 查看已做和通过数量 |
| `python train.py check` | 检查题库数据是否完整 |

题目都在 `problems/` 目录，一共分为 18 个章节。`judge/` 是本地判题代码，`data/` 保存题目元数据、测试用例和本地进度。

## 关于题目内容

题目名称和链接会指向 LeetCode 和 NeetCode。本仓库只保留我整理的题目摘要、提示、代码模板、测试工具和本地测试数据，不搬运商业平台的完整题面和官方答案。具体说明见 [NOTICE.md](NOTICE.md)。

项目原创代码使用 [MIT License](LICENSE)。
