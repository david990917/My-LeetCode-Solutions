# Guidance指南

Author: [David990917](https://github.com/david990917)

Crawler: [LeetCode-CN-Crawler](https://github.com/david990917/LeetCode-CN-Crawler)

Solutions: [My-LeetCode-Solutions](https://github.com/david990917/My-LeetCode-Solutions)

---

### 使用指北

克隆爬虫仓库

```bash
git@github.com:david990917/LeetCode-CN-Crawler.git
```

安装相关依赖：

```bash
pip install -r requirements.txt
```

`Python` 运行，需要添加参数。

此处建议保存命令形式，或者使用 `PyCharm` 进行配置。同时**斜杠**形式需要与我保持一致

```
python leetcode-cn-crawler-raw.py
	-u		$YourUserName$
	-p		$YourPassword$
	-dp		$YourDataBasePath$ e.g. leetcode-cn.db
	-g		$YourWebURL$ e.g. https://github.com/david990917/My-LeetCode-Solutions
	-r      $YourLocalRootPath$ D:\Starky\My-LeetCode-Solutions\    <-需要斜杠
```

### 我的工作流

1. 爬虫主仓库：

   现在的代码是爬取所有题目的代码形式，每次数据库重新建立与否不强制

   目前代码中是使用增量爬取，不重新建数据库

2. **本地代码库 <= 连接 => 题解仓库：**

   1. 力扣完成习题
   2. 运行本地代码库中的爬虫，更新数据库，推送增量更新到题解本地仓库
   3. 本地仓库添加个人代码、分析、总结
   4. 推送本地仓库到远程仓库

**每次运行程序会重新生成 主README 文件。**

**但是没有新 AC 的题目的时候，不会改变数据库信息。**

### 各版本文件区别

都是数据库增量爬虫 - **数据库文件很重要**！

- 爬虫主仓库：**全部题目**，中文版本README为纯题目
  - `leetcode-cn-crawler-raw` 是纯题目，`leetcode-cn-crawler` 是 增加个人定制的模板
  - 减少同步的复杂性，只需要爬虫仓库和本地仓库（PyCharm）分别运行即可。
- 本地代码库：**通过的题目**，中文版本README为**题目 + 个人整理与总结模板**
  - 个人整理与题目总结推送到 [My-LeetCode-Solutions](https://github.com/david990917/My-LeetCode-Solutions)

```python
if not question_status: continue
```

同时目前的版本**对于收费题目封闭**。

```python
if question['paid_only']: continue
```

[题解仓库](https://github.com/david990917/My-LeetCode-Solutions) 使用本地代码库生成题库，注意***文档和数据库文件***的备份。

- **文档中**包含自动化生成的题目之外，``README` 中同时包含了我**手动添加的题解&总结信息**。
- **数据库**包含已经爬取的题目信息，在我的代码库中是已经 `AC` 的题目记录。