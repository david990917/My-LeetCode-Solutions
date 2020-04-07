---
title: interview-1
tags:
  - LeetCode
description: ''
urlname: interview-1
date: 2020-04-07 20:39:17
---

# 题目

[旋转矩阵](https://leetcode-cn.com/problems/rotate-matrix-lcci/)



# 解题思路 √

### Python

1. 

```python
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)
        for i in range(n // 2):
            for j in range((n + 1) // 2):
                matrix[i][j], matrix[n - j - 1][i], matrix[n - i - 1][n - j - 1], matrix[j][n - i - 1] \
                    = matrix[n - j - 1][i], matrix[n - i - 1][n - j - 1], matrix[j][n - i - 1], matrix[i][j]
```


```python

```



### C++

```cpp

```

---



# 整理与总结

1. 

