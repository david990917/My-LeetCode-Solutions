---
title: medium-240
tags:
  - LeetCode
description: '搜索二维矩阵 II'
urlname: medium-240
date: 2020-03-20 21:35:08
---

# 题目

https://leetcode-cn.com/problems/search-a-2d-matrix-ii/

编写一个高效的算法来搜索 *m* x *n* 矩阵 matrix 中的一个目标值 target。该矩阵具有以下特性：

- 每行的元素从左到右升序排列。
- 每列的元素从上到下升序排列。

**示例:**

现有矩阵 matrix 如下：

```
[
  [1,   4,  7, 11, 15],
  [2,   5,  8, 12, 19],
  [3,   6,  9, 16, 22],
  [10, 13, 14, 17, 24],
  [18, 21, 23, 26, 30]
]
```

给定 target = `5`，返回 `true`。

给定 target = `20`，返回 `false`。



# 解题思路 √

找一个顶点【只有单向可能的移动】

### Python

1. 这种是有特点的

```python
class Solution:
    def searchMatrix(self, matrix, target):
        if not matrix:return False
        if not matrix[0]:return False
        m,n=len(matrix),len(matrix[0])
        row,col=0,n-1

        while row<m and col>=0:
            if target==matrix[row][col]:return True
            elif target>matrix[row][col]:row+=1
            elif target<matrix[row][col]:col-=1
        return False
```


```python

```



### C++

```cpp

```

---



# 整理与总结

1. #### [搜索二维矩阵 II](https://leetcode-cn.com/problems/search-a-2d-matrix-ii/)

