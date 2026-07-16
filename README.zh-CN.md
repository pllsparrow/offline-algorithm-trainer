# 离线算法刷题器

[English](README.md)

一个以 Python 为主、完全离线运行的算法训练环境，包含 150 道面试高频题、
本地测试用例、轻量判题器、调试支持和持久化进度记录。

## 为什么做这个项目

常见刷题流程需要在浏览器、编辑器和远程判题平台之间反复切换。本项目把核心
反馈闭环放到本地：

```text
选题 -> 编辑 solution.py -> 运行测试 -> 查看失败 -> Debug
```

它面向求职面试、刻意练习和算法 Debug，而不只是提交答案。

## 功能

- 18 个章节、150 道面试高频题。
- 按专题组织的 Python 解题模板。
- 完全离线的 JSON 测试用例。
- 自动转换链表、树、图和随机指针结构。
- 支持单用例运行、首错停止和跑完全部失败用例。
- Debug 模式可以保留解答中的 `print()` 输出。
- 使用本地 SQLite 记录尝试次数和 AC 状态。
- 支持按分类和难度筛选。
- 不需要账号、云服务或第三方 Python 包。

## 环境要求

- Python 3.12+

## 快速开始

```bash
git clone https://github.com/pllsparrow/offline-algorithm-trainer.git
cd offline-algorithm-trainer

python train.py list
python train.py show two-sum
python train.py run two-sum
python train.py status
```

第一次运行会在本地创建 `data/progress.sqlite3`。该文件已被 Git 忽略，个人
进度不会进入公开仓库。

## 常用命令

| 命令 | 作用 |
| --- | --- |
| `python train.py list` | 查看题目、状态、尝试次数和分类 |
| `python train.py show two-sum` | 查看元数据、提示、签名和文件路径 |
| `python train.py run two-sum` | 运行一道题的全部本地用例 |
| `python train.py run two-sum --case 1` | 单独复现一个用例 |
| `python train.py run two-sum --case 1 --debug` | 保留单用例调试输出 |
| `python train.py run two-sum --all` | 失败后继续运行其他用例 |
| `python train.py status` | 查看 AC 和已尝试数量 |
| `python train.py check` | 校验题库元数据和测试数据 |

筛选示例：

```bash
python train.py list --category graph
python train.py list --difficulty Hard
```

## 训练流程

每道题都有独立工作区：

```text
problems/
  01-arrays-hashing/
    003-two-sum/
      README.md
      solution.py
```

1. 打开题目的 `solution.py`。
2. 先说明暴力方法和预计复杂度。
3. 编写解答。
4. 运行 `python train.py run <slug>`。
5. 失败时对比 `args`、`expected` 和 `actual`。
6. 使用 `--debug` 或 IDE 断点复现失败用例。
7. 说明最终时间复杂度、空间复杂度和边界情况。

## 目录结构

- `train.py`：命令行入口和进度管理。
- `judge/python_judge.py`：隔离运行的本地 Python 判题器。
- `support.py`：链表、树、图等本地数据结构。
- `problems/`：章节和题目工作区。
- `data/problems.json`：题目元数据和起始模板。
- `data/tests.json`：离线测试用例。
- `data/progress.sqlite3`：运行时创建的本地进度。
- `scripts/build_roadmap.py`：校验并重建题目工作区。

## 测试与校验

```bash
python train.py check
python train.py run contains-duplicate
```

公开仓库不会包含用户已经完成的解答或个人进度数据库。

## 内容说明

题目名称和链接指向 LeetCode 与 NeetCode 上的练习。本仓库提供原创摘要、提示、
模板、测试框架和本地测试数据，不重新发布商业平台完整题面或官方答案。详情见
[NOTICE.md](NOTICE.md)。

## 路线图

- 增加命令行和判题器的回归测试。
- 改进嵌套结构的失败差异展示。
- 支持个人进度导入和导出。
- 保持核心工作流离线、零第三方依赖。

## 许可证

仓库原创软件采用 MIT 许可证，见 [LICENSE](LICENSE) 和 [NOTICE.md](NOTICE.md)。
