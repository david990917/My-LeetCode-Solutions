---
title: easy-463
tags:
  - LeetCode
description: ''
urlname: easy-463
date: 2020-03-23 21:12:24
---

# 题目

[岛屿的周长](https://leetcode-cn.com/problems/island-perimeter/)

给定一个包含 0 和 1 的二维网格地图，其中 1 表示陆地 0 表示水域。

网格中的格子水平和垂直方向相连（对角线方向不相连）。整个网格被水完全包围，但其中恰好有一个岛屿（或者说，一个或多个表示陆地的格子相连组成的岛屿）。

岛屿中没有“湖”（“湖” 指水域在岛屿内部且不和岛屿周围的水相连）。格子是边长为 1 的正方形。网格为长方形，且宽度和高度均不超过 100 。计算这个岛屿的周长。

 

示例 :

```
输入:
[[0,1,0,0],
 [1,1,1,0],
 [0,1,0,0],
 [1,1,0,0]]

输出: 16

解释: 它的周长是下面图片中的 16 个黄色的边：
```

![img](easy-463/island.png)

# 解题思路 √

### Python

1. DFS搜索很容易，但是周长我就不会判断了

![岛屿周长的两类划分](easy-463/e0e2314bb62cb06383e6128a6ba2b75e7c942cc5a36dedc32d0b39868a597629.jpg)

```
 // 从一个岛屿方格走向网格边界，周长加 1
 // 从一个岛屿方格走向水域方格，周长加 1
```



```python
class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:return 0
        self.meter=0
        m,n=len(grid),len(grid[0])
        directions=[(1,0),(-1,0),(0,1),(0,-1)]
        visited=[[False for i in range(n)] for j in range(m)]
        
        def dfs(r,c):
            if r<0 or r>=m or c<0 or c>=n or grid[r][c]==0:
                self.meter+=1
                return 
            if visited[r][c]:return
            
            visited[r][c]=True
            for d in directions:
                dfs(r+d[0],c+d[1])
                
        for i in range(m):
            for j in range(n):
                if grid[i][j]==1 and not visited[i][j]:
                    dfs(i,j)
                    return self.meter
```


```python

```



### C++

```cpp

```

---



# 整理与总结

1. 

