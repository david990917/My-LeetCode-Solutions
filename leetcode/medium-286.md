---
title: medium-286
tags:
  - LeetCode
description: ''
urlname: medium-286
date: 2020-04-02 21:27:42
---

# 题目

[墙与门](https://leetcode-cn.com/problems/walls-and-gates/)

你被给定一个 m × n 的二维网格，网格中有以下三种可能的初始化值：

-1 表示墙或是障碍物
0 表示一扇门
INF 无限表示一个空的房间。然后，我们用 231 - 1 = 2147483647 代表 INF。你可以认为通往门的距离总是小于 2147483647 的。
你要给每个空房间位上填上该房间到 最近 门的距离，如果无法到达门，则填 INF 即可。

示例：

```
给定二维网格：

INF  -1  0  INF
INF INF INF  -1
INF  -1 INF  -1
  0  -1 INF INF
```

运行完你的函数后，该网格应该变成：

```
  3  -1   0   1
  2   2   1  -1
  1  -1   2  -1
  0  -1   3   4
```



# 解题思路 √

### Python

1. 纯正多源点发起的BFS超时了

```python
class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        if not rooms or not rooms[0]:return rooms
        m,n=len(rooms),len(rooms[0])
        
        def bfs(r,c):
            queue=collections.deque()
            visited=[[False for i in range(n)]for j in range(m)]
            directions=[(1,0),(-1,0),(0,1),(0,-1)]
            
            step=0
            queue.append((r,c))
            
            while queue:
                size=len(queue)
                for _ in range(size):
                    currR,currC=queue.popleft()
                    if currR<0 or currR>=m or currC<0 or currC>=n:continue
                    if visited[currR][currC]:continue                    
                    if rooms[currR][currC]==-1:continue
                    if rooms[currR][currC]>step:rooms[currR][currC]=step
                    visited[currR][currC]=True
                    
                    for d in directions:
                        queue.append((currR+d[0],currC+d[1]))
                step+=1
                    
        for i in range(m):
            for j in range(n):
                if rooms[i][j]==0:
                    bfs(i,j)
        return rooms
                    
```

2. 多源BFS可以同时添加进去，这样搜索会很方便


```python
class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        if not rooms or not rooms[0]:return rooms
        m,n=len(rooms),len(rooms[0])
        queue=collections.deque()
        visited=[[False for i in range(n)]for j in range(m)]
        directions=[(1,0),(-1,0),(0,1),(0,-1)]
        step=0
            
        for i in range(m):
            for j in range(n):
                if rooms[i][j]==0:
                    queue.append((i,j))
                    
        while queue:
            size=len(queue)
            for _ in range(size):
                currR,currC=queue.popleft()
                if currR<0 or currR>=m or currC<0 or currC>=n:continue
                if visited[currR][currC]:continue                    
                if rooms[currR][currC]==-1:continue
                if rooms[currR][currC]>step:rooms[currR][currC]=step
                visited[currR][currC]=True

                for d in directions:
                    queue.append((currR+d[0],currC+d[1]))
            step+=1  
                
        return rooms
                    
```



### C++

```cpp

```

---



# 整理与总结

1. 

