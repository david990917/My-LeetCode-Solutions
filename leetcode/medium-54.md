---
title: medium-54
tags:
  - LeetCode
description: ''
urlname: medium-54
date: 2020-03-26 11:29:42
---

# 题目

[螺旋矩阵](https://leetcode-cn.com/problems/spiral-matrix/)

给定一个包含 m x n 个元素的矩阵（m 行, n 列），请按照顺时针螺旋顺序，返回矩阵中的所有元素。

示例 1:

```
输入:
[
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
输出: [1,2,3,6,9,8,7,4,5]
```


示例 2:

```
输入:
[
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
]
输出: [1,2,3,4,8,12,11,10,9,5,6,7]
```



# 解题思路 √

### Python

1. 螺旋矩阵

```python
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]:return []
        result=[]
        l,r,t,b=0,len(matrix[0])-1,0,len(matrix)-1
        while True:
            for i in range(l,r+1):
                result.append(matrix[t][i])
            t+=1
            if t>b:break
        
            for i in range(t,b+1):
                result.append(matrix[i][r])
            r-=1
            if r<l:break
            
            for i in range(r,l-1,-1):
                result.append(matrix[b][i])
            b-=1
            if b<t:break
            
            for i in range(b,t-1,-1):
                result.append(matrix[i][l])
            l+=1
            if l>r:break
            
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

