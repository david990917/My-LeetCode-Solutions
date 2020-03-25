---
title: offer-4
tags:
  - LeetCode
description: '二维数组中的查找'
urlname: offer-4
date: 2020-03-14 22:03:42
---

# 题目

[ 二维数组中的查找](https://leetcode-cn.com/problems/er-wei-shu-zu-zhong-de-cha-zhao-lcof) 

在一个 n * m 的二维数组中，每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增的顺序排序。请完成一个函数，输入这样的一个二维数组和一个整数，判断数组中是否含有该整数。

**示例:**

```
现有矩阵 matrix 如下：
[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]

给定 target = 5，返回 true。
给定 target = 20，返回 false。
```

 **限制：**

```
0 <= n <= 1000

0 <= m <= 1000
```

# 解题思路 √

### Python

1. 注意找规律

```python
class Solution:
    def findNumberIn2DArray(self, matrix: List[List[int]], target: int) -> bool:
        if not matrix:return False

        n,m=len(matrix),len(matrix[0])
        row,col=0,m-1
        while row<n and col>=0:
            if matrix[row][col]==target:
                return True
            elif matrix[row][col]>target:col-=1
            else:row+=1
        return False
```


```python

```



### C++

```cpp

```

---



# 整理与总结

1. 

