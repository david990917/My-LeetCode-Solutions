---
title: medium-547
tags:
  - LeetCode
description: '朋友圈'
urlname: medium-547
date: 2020-03-20 11:26:10
---

# 题目

https://leetcode-cn.com/problems/friend-circles/

班上有 **N** 名学生。其中有些人是朋友，有些则不是。他们的友谊具有是传递性。如果已知 A 是 B 的朋友，B 是 C 的朋友，那么我们可以认为 A 也是 C 的朋友。所谓的朋友圈，是指所有朋友的集合。

给定一个 **N \* N** 的矩阵 **M**，表示班级中学生之间的朋友关系。如果M[i][j] = 1，表示已知第 i 个和 j 个学生**互为**朋友关系，否则为不知道。你必须输出所有学生中的已知的朋友圈总数。

**示例 1:**

```
输入: 
[[1,1,0],
 [1,1,0],
 [0,0,1]]
输出: 2 
说明：已知学生0和学生1互为朋友，他们在一个朋友圈。
第2个学生自己在一个朋友圈。所以返回2。
```

**示例 2:**

```
输入: 
[[1,1,0],
 [1,1,1],
 [0,1,1]]
输出: 1
说明：已知学生0和学生1互为朋友，学生1和学生2互为朋友，所以学生0和学生2也是朋友，所以他们三个在一个朋友圈，返回1。
```

**注意：**

1. N 在[1,200]的范围内。
2. 对于所有学生，有M[i][i] = 1。
3. 如果有M[i][j] = 1，则有M[j][i] = 1。

# 解题思路 √

### Python

1. DFS去除连通性

```python
class Solution:
    def findCircleNum(self, M: List[List[int]]) -> int:
        if not M:return 0
        if not M[0]:return 0
        n=len(M)
        count=0

        def dfs(i):
            for j in range(n):
                if j==i:M[i][i]=0
                if M[i][j]:
                    M[i][j]=0
                    dfs(j)

        for i in range(n):
            if sum(M[i]):count+=1
            dfs(i)
        return count
```


```python

```



### C++

```cpp

```

---



# 整理与总结

1. 朋友圈 - 无向图中的DFS搜索连通

   同样是计数问题，我们计数的时候要设计一个判断的条件。

   我们在连通分支中处理的时候要注意对于自己的处理，并且处理要处理地完全【注意对称】。

   

