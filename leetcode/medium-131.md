---
title: medium-131
tags:
  - LeetCode
description: ''
urlname: medium-131
date: 2020-03-23 09:57:12
---

# 题目

[分割回文串](https://leetcode-cn.com/problems/palindrome-partitioning/)

给定一个字符串 s，将 s 分割成一些子串，使每个子串都是回文串。

返回 s 所有可能的分割方案。

示例:

输入: "aab"
输出:

```
[
  ["aa","b"],
  ["a","a","b"]
]
```



# 解题思路 √

### Python

1. 正常递归

```python
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        
        def helper(s, tmp):
            if not s:
                res.append(tmp)
            for i in range(1, len(s) + 1):
                if s[:i] == s[:i][::-1]:
                    helper(s[i:], tmp + [s[:i]])
        helper(s, [])
        return res
```


```python

```



### C++

```cpp

```

---



# 整理与总结

1. 

