---
title: medium-200
tags:
  - LeetCode
description: '岛屿数量'
urlname: medium-200
date: 2020-03-20 11:16:14
---

# 题目

https://leetcode-cn.com/problems/number-of-islands/

给定一个由 `'1'`（陆地）和 `'0'`（水）组成的的二维网格，计算岛屿的数量。一个岛被水包围，并且它是通过水平方向或垂直方向上相邻的陆地连接而成的。你可以假设网格的四个边均被水包围。

**示例 1:**

```
输入:
11110
11010
11000
00000

输出: 1
```

**示例 2:**

```
输入:
11000
11000
00100
00011

输出: 3
```

# 解题思路 √

### Python

1. 感觉逐步理解了DFS查找连通性【可达性】

```python
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:return 0
        if not grid[0]:return 0
        m,n=len(grid),len(grid[0])
        directions=[(1,0),(-1,0),(0,1),(0,-1)]
        count=0

        def dfs(r,c):
            if (r<0 or r>=m or c<0 or c>=n or grid[r][c]=='0'):return 
            grid[r][c]='0'
            for direction in directions:
                dfs(r+direction[0],c+direction[1])
        
        for i in range(m):
            for j in range(n):
                if grid[i][j]=='1':count+=1
                dfs(i,j)
        return count
```


```python

```



### C++

```cpp

```

---



# 整理与总结

1. 岛屿数量 - “多少个”连通枝的问题

   和前一道面积的题目相比，我们只用在找到新的连通枝的时候count计数就可以了。
