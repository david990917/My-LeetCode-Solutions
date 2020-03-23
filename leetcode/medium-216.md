---
title: medium-216
tags:
  - LeetCode
description: ''
urlname: medium-216
date: 2020-03-23 09:05:35
---

# 题目

[组合总和 III](https://leetcode-cn.com/problems/combination-sum-iii/)

找出所有相加之和为 n 的 k 个数的组合。组合中只允许含有 1 - 9 的正整数，并且每种组合中不存在重复的数字。

说明：

所有数字都是正整数。
解集不能包含重复的组合。 
示例 1:

```
输入: k = 3, n = 7
输出: [[1,2,4]]
```


示例 2:

```
输入: k = 3, n = 9
输出: [[1,2,6], [1,3,5], [2,3,4]]
```



# 解题思路 √

### Python

1. 还是回溯法

```python
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        results=[]
        visited=[False for i in range(10)]
        
        def backtracking(temp,start,k,n):
            if n==0 and k==0:
                results.append(temp)
                return
            if k==0:return
            for i in range(start,10):
                if not visited[i] and i<=n:
                    visited[i]=True
                    backtracking(temp+[i],i+1,k-1,n-i)
                    visited[i]=False
        backtracking([],1,k,n)
        return results
```

不用visited也可以


```python
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        results=[]
        
        def backtracking(temp,start,k,n):
            if n==0 and k==0:
                results.append(temp)
                return
            if k==0:return
            for i in range(start,10):
                if i<=n: 
                    backtracking(temp+[i],i+1,k-1,n-i)
        backtracking([],1,k,n)
        return results
```



### C++

```cpp

```

---



# 整理与总结

1. 递增序列-需要一个start - 避免访问的重复

