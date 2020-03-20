---
title: medium-77
tags:
  - LeetCode
description: '组合'
urlname: medium-77
date: 2020-03-20 16:43:33
---

# 题目

https://leetcode-cn.com/problems/combinations/

给定两个整数 *n* 和 *k*，返回 1 ... *n* 中所有可能的 *k* 个数的组合。

**示例:**

```
输入: n = 4, k = 2
输出:
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]
```



# 解题思路 √

### Python

![img](medium-77/0.png)

![img](medium-77/1.png)

1. 回溯

```python
from typing import List
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        if n <= 0 or k <= 0 or k > n:return []
        results = []
        
        def backTrack(curr,start,k):
            if k==0:
                results.append(curr)
                return
            for i in range(start,n-k+2):
                backTrack(curr+[i],i+1,k-1)
        
        backTrack([],1,k)
        return results
```


```python

```



### C++

```cpp

```

---



# 整理与总结

1. 组合

   

