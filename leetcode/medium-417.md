---
title: medium-417
tags:
  - LeetCode
description: '太平洋大西洋水流问题'
urlname: medium-417
date: 2020-03-20 11:53:10
---

# 题目

https://leetcode-cn.com/problems/pacific-atlantic-water-flow/

给定一个 `m x n` 的非负整数矩阵来表示一片大陆上各个单元格的高度。“太平洋”处于大陆的左边界和上边界，而“大西洋”处于大陆的右边界和下边界。

规定水流只能按照上、下、左、右四个方向流动，且只能从高到低或者在同等高度上流动。

请找出那些水流既可以流动到“太平洋”，又能流动到“大西洋”的陆地单元的坐标。

 

**提示：**

1. 输出坐标的顺序不重要
2. *m* 和 *n* 都小于150

 

**示例：**

 

```
给定下面的 5x5 矩阵:

  太平洋 ~   ~   ~   ~   ~ 
       ~  1   2   2   3  (5) *
       ~  3   2   3  (4) (4) *
       ~  2   4  (5)  3   1  *
       ~ (6) (7)  1   4   5  *
       ~ (5)  1   1   2   4  *
          *   *   *   *   * 大西洋

返回:

[[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]] (上图中带括号的单元).
```



# 解题思路 √

### Python

1. DFS的思想

```python
class Solution:
    def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:
        if not matrix:return []
        if not len(matrix):return []
        m,n=len(matrix),len(matrix[0])
        result=[]
        canReachP=[[False for i in range(n)] for i in range(m)]
        canReachA=[[False for i in range(n)] for i in range(m)]
        directions=[(1,0),(-1,0),(0,1),(0,-1)]

        def dfs(r,c,PA):
            canReach=canReachA if PA=='A' else canReachP
            if canReach[r][c]:return
            canReach[r][c]=True
            for d in directions:
                nextR=r+d[0]
                nextC=c+d[1]
                if nextR<0 or nextR>=m or nextC<0 or nextC>=n or matrix[r][c]>matrix[nextR][nextC]:continue
                dfs(nextR,nextC,PA)
        
        for i in range(m):
            dfs(i,0,'P')
            dfs(i,n-1,'A')
        for i in range(n):
            dfs(0,i,'P')
            dfs(m-1,i,'A')
        for i in range(m):
            for j in range(n):
                if canReachP[i][j] and canReachA[i][j]:
                    result.append([i,j])
        return result
```


```python

```



### C++

```cpp

```

---



# 整理与总结

1. 太平洋大西洋水流问题

   和前面的题目更进一步，需要从双条件来进行判断。

   实际上是一个逆向的想法，从两个洋来找到`可以到达`的点。

2. Python二维数组的初始化

   ```python
   canReachP=[[False for i in range(n)] for i in range(m)]
   ```

3. 函数传参拷贝的问题，越简单越好

