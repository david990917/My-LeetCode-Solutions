---
title: medium-498
tags:
  - LeetCode
description: '对角线遍历'
urlname: medium-498
date: 2020-03-21 17:07:17
---

# 题目

[对角线遍历](https://leetcode-cn.com/problems/diagonal-traverse/)

给定一个含有 M x N 个元素的矩阵（M 行，N 列），请以对角线遍历的顺序返回这个矩阵中的所有元素，对角线遍历如下图所示。

 

示例:

```
输入:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]

输出:  [1,2,4,7,5,3,6,8,9]
```



# 解题思路 √

![img](medium-498/img1.png)

![img](medium-498/img3.png)

### Python

1. 正常思想逐列向下，然后判断

```python
class Solution:
    def findDiagonalOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]:return []
        m,n=len(matrix),len(matrix[0])
        result=[]
        for i in range(m+n-1):
            r,c=0 if i<n else 1+i-n,i if i<n else n-1
            curr=[]
            while r<m and c>=0:
                curr.append(matrix[r][c])
                r,c=r+1,c-1
            if i%2: result.extend(curr)
            else:result.extend(curr[::-1])
            
        return result
```


```python

```



### C++

```cpp

```

---



# 整理与总结

1. 

