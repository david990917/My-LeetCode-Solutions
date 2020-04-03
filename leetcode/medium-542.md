---
title: medium-542
tags:
  - LeetCode
description: ''
urlname: medium-542
date: 2020-04-03 23:27:47
---

# 题目

[01 矩阵](https://leetcode-cn.com/problems/01-matrix/)

给定一个由 0 和 1 组成的矩阵，找出每个元素到最近的 0 的距离。

两个相邻元素间的距离为 1 。

示例 1:

```
输入:

0 0 0
0 1 0
0 0 0
输出:

0 0 0
0 1 0
0 0 0
```

示例 2:

示例 2:

```
输入:

0 0 0
0 1 0
1 1 1
输出:

0 0 0
0 1 0
1 2 1
```

注意:

注意:

```
给定矩阵的元素个数不超过 10000。
给定矩阵中至少有一个元素是 0。
矩阵中的元素只在四个方向上相邻: 上、下、左、右。
```



# 解题思路 √

### Python

1. 多源BFS模板，注意添加进元素的时候避免重复：
   - 扫描向队列添加源点的时候，就设置`visited[i][j]=True`
   - 访问的时候，只对可行的元素继续搜索
   - 添加元素进队列的时候，同步设置`visited[i][j]=True`
     - 为了避免重复添加相同元素：就是需要添加的时候同步设置已经访问过
     - 如果像之前那样等下一层再去设置，就晚了（有可能已经添加过了）

```python
class Solution:
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:
        if not matrix or not matrix[0]:return matrix
        
        m,n=len(matrix),len(matrix[0])
        queue=collections.deque()
        visited=[[False for i in range(n)] for j in range(m)]
        directions=[(1,0),(-1,0),(0,1),(0,-1)]
        step=0
        
        for i in range(m):
            for j in range(n):
                if matrix[i][j]==0:
                    queue.append((i,j))
                    visited[i][j]=True
                    
        while queue:
            size=len(queue)
            for _ in range(size):
                currR,currC=queue.popleft()
                matrix[currR][currC]=step
                for d in directions:
                    nextR,nextC=currR+d[0],currC+d[1]
                    if 0<=nextR<m and 0<=nextC<n and not visited[nextR][nextC] and matrix[nextR][nextC]!=0:       
                        queue.append((nextR,nextC))
                        visited[nextR][nextC]=True
            step+=1
            
        return matrix
```


```python

```



### C++

```cpp

```

---



# 整理与总结

1. 

