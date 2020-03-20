---
title: medium-130
tags:
  - LeetCode
description: '被围绕的区域'
urlname: medium-130
date: 2020-03-20 11:38:18
---

# 题目

https://leetcode-cn.com/problems/surrounded-regions/

给定一个二维的矩阵，包含 `'X'` 和 `'O'`（**字母 O**）。

找到所有被 `'X'` 围绕的区域，并将这些区域里所有的 `'O'` 用 `'X'` 填充。

**示例:**

```
X X X X
X O O X
X X O X
X O X X
```

运行你的函数后，矩阵变为：

```
X X X X
X X X X
X X X X
X O X X
```

**解释:**

被围绕的区间不会存在于边界上，换句话说，任何边界上的 `'O'` 都不会被填充为 `'X'`。 任何不在边界上，或不与边界上的 `'O'` 相连的 `'O'` 最终都会被填充为 `'X'`。如果两个元素在水平或垂直方向相邻，则称它们是“相连”的。

# 解题思路 √

### Python

1. BFS

```python
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if not board:return 
        if not board[0]:return
        m,n=len(board),len(board[0])
        directions=[(1,0),(-1,0),(0,1),(0,-1)]

        def dfs(c,r):
            if (c<0 or c>=m or r<0 or r>=n or board[c][r]!='O'):return 
            board[c][r]='T'
            for direction in directions:
                dfs(c+direction[0],r+direction[1])
        
        for i in range(m):
            dfs(i,0)
            dfs(i,n-1)
        
        for i in range(n):
            dfs(0,i)
            dfs(m-1,i)
        
        for i in range(m):
            for j in range(n):
                if board[i][j]=='T':board[i][j]='O'
                elif board[i][j]=='O':board[i][j]='X'
```


```python

```



### C++

```cpp

```

---



# 整理与总结

1. 被围绕的区域

   这个题目提供了一个不同的思考角度：

   前面的题目都是全局遍历然后DFS，这个题目呢从边界着手：边界上发起，连通的枝我们把它拿出来。之后的反转标识，也是很巧妙的想法了。

   标记一下边界着手的方法：

   - 遍历行：列头/列尾
   - 遍历列：行头/行尾

   全局转换输出

