---
title: medium-79
tags:
  - LeetCode
description: '单词搜索'
urlname: medium-79
date: 2020-03-20 15:38:10
---

# 题目

https://leetcode-cn.com/problems/word-search/

给定一个二维网格和一个单词，找出该单词是否存在于网格中。

单词必须按照字母顺序，通过相邻的单元格内的字母构成，其中“相邻”单元格是那些水平相邻或垂直相邻的单元格。同一个单元格内的字母不允许被重复使用。

 

**示例:**

```
board =
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

给定 word = "ABCCED", 返回 true
给定 word = "SEE", 返回 true
给定 word = "ABCB", 返回 false
```

 

**提示：**

- `board` 和 `word` 中只包含大写和小写英文字母。
- `1 <= board.length <= 200`
- `1 <= board[i].length <= 200`
- `1 <= word.length <= 10^3`

# 解题思路 √

### Python

1. 回溯 - 把True层层传回来

```python
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        if not board:return False
        if not board[0]:return False
        m,n=len(board),len(board[0])
        visited=[[False for i in range(n)] for j in range(m)]
        directions=[(1,0),(-1,0),(0,1),(0,-1)]

        def backTrack(currLen,r,c):
            if currLen==len(word):return True
            if r<0 or r>=m or c<0 or c>=n or visited[r][c] or board[r][c]!=word[currLen]:return False
            visited[r][c]=True
            for d in directions:
                if backTrack(currLen+1,r+d[0],c+d[1]):return True
            visited[r][c]=False
        
        for i in range(m):
            for j in range(n):
                if backTrack(0,i,j):return True
        return False
```


```python

```



### C++

```cpp

```

---



# 整理与总结

1. 单词搜索

