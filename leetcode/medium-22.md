---
title: medium-22
tags:
  - LeetCode
description: ''
urlname: medium-22
date: 2020-03-27 09:38:21
---

# 题目

[括号生成](https://leetcode-cn.com/problems/generate-parentheses/)

给出 *n* 代表生成括号的对数，请你写出一个函数，使其能够生成所有可能的并且**有效的**括号组合。

例如，给出 *n* = 3，生成结果为：

```
[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]
```

# 解题思路 √

### Python

1. 

```python
class Solution(object):
    def generateParenthesis(self, N):
        ans = []
        def backtrack(S = '', left = 0, right = 0):
            if len(S) == 2 * N:
                ans.append(S)
                return
            if left < N:
                backtrack(S+'(', left+1, right)
            if right < left:
                backtrack(S+')', left, right+1)

        backtrack()
        return ans

```


```python

```



### C++

```cpp

```

---



# 整理与总结

1. 

