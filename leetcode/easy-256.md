---
title: easy-256
tags:
  - LeetCode
description: ''
urlname: easy-256
date: 2020-03-07 11:58:07
---

# 题目

https://leetcode-cn.com/problems/paint-house/

> 假如有一排房子，共 n 个，每个房子可以被粉刷成红色、蓝色或者绿色这三种颜色中的一种，你需要粉刷所有的房子并且使其相邻的两个房子颜色不能相同。
>
> 当然，因为市场上不同颜色油漆的价格不同，所以房子粉刷成不同颜色的花费成本也是不同的。每个房子粉刷成不同颜色的花费是以一个 n x 3 的矩阵来表示的。
>
> 例如，costs[0][0] 表示第 0 号房子粉刷成红色的成本花费；costs[1][2] 表示第 1 号房子粉刷成绿色的花费，以此类推。请你计算出粉刷完所有房子最少的花费成本。
>

# 解题思路 √

一个一个考虑就行了，所以就直接动态规划就可以了。

### Python

1. 进行操作，对于三种颜色作为初始情况，进行操作。

```python
class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        p=[0]*3
        a,b,c=0,0,0
        for i in range(len(costs)):
            a=min(p[1],p[2])+costs[i][0]
            b=min(p[0],p[2])+costs[i][1]
            c=min(p[0],p[1])+costs[i][2]
            p[0],p[1],p[2]=a,b,c
        return min(p[0],min(p[1],p[2]))
```


```python

```



### C++

```cpp

```

---



# 整理与总结

1. 

