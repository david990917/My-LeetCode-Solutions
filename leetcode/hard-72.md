---
title: hard-72
tags:
  - LeetCode
description: ''
urlname: hard-72
date: 2020-04-06 22:50:39
---

# 题目

[编辑距离](https://leetcode-cn.com/problems/edit-distance/)





# 解题思路 √

### Python

1. 

```python
class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        if not word1:return len(word2)
        if not word2:return len(word1)
        m,n=len(word1),len(word2)
        result=[[0 for i in range(n+1)]for j in range(m+1)]

        for i in range(n+1):result[0][i]=i
        for i in range(m+1):result[i][0]=i

        for i in range(1,m+1):
            for j in range(1,n+1):
                if word1[i-1]==word2[j-1]:
                    result[i][j]=result[i-1][j-1]
                else:
                    result[i][j]=min(result[i][j-1],result[i-1][j],result[i-1][j-1])+1
        return result[-1][-1]
```


```python

```



### C++

```cpp

```

---



# 整理与总结

1. 

