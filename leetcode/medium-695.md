---
title: medium-695
tags:
  - LeetCode
description: '岛屿的最大面积'
urlname: medium-695
date: 2020-03-20 10:41:29
---

# 题目

https://leetcode-cn.com/problems/max-area-of-island/

给定一个包含了一些 `0` 和 `1` 的非空二维数组 `grid` 。

一个 **岛屿** 是由一些相邻的 `1` (代表土地) 构成的组合，这里的「相邻」要求两个 `1` 必须在水平或者竖直方向上相邻。你可以假设 `grid` 的四个边缘都被 `0`（代表水）包围着。

找到给定的二维数组中最大的岛屿面积。(如果没有岛屿，则返回面积为 `0` 。)

 

**示例 1:**

```
[[0,0,1,0,0,0,0,1,0,0,0,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,1,1,0,1,0,0,0,0,0,0,0,0],
 [0,1,0,0,1,1,0,0,1,0,1,0,0],
 [0,1,0,0,1,1,0,0,1,1,1,0,0],
 [0,0,0,0,0,0,0,0,0,0,1,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,0,0,0,0,0,0,1,1,0,0,0,0]]
```

对于上面这个给定矩阵应返回 `6`。注意答案不应该是 `11` ，因为岛屿只能包含水平或垂直的四个方向的 `1` 。

**示例 2:**

```
[[0,0,0,0,0,0,0,0]]
```

对于上面这个给定的矩阵, 返回 `0`。

 

**注意:** 给定的矩阵`grid` 的长度和宽度都不超过 50。

# 解题思路 √

### Python

1. DFS搜索

```python
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:return 0
        if not grid[0]:return 0

        m,n=len(grid),len(grid[0])
        maxArea=0
        directions=[(0,1),(0,-1),(1,0),(-1,0)]

        def dfs(x,y):
            if(x<0 or x>=m or y<0 or y>=n or grid[x][y]==0):return 0
            grid[x][y]=0
            area=1
            for direction in directions:
                area+=dfs(x+direction[0],y+direction[1])
            return area

        for i in range(m):
            for j in range(n):
                area=dfs(i,j)
                maxArea=max(maxArea,area)
        return maxArea
```


```python

```



### C++

```cpp

```

---



# 整理与总结

1. 最大连通面积

   DFS可以找到连通的分支：进入的时候要先判断是否继续；标记访问过；之后对于可行的递归操作，返回`area`。

   主干函数调用的时候，比较面积。

   

