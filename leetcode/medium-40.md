---
title: medium-40
tags:
  - LeetCode
description: ''
urlname: medium-40
date: 2020-03-23 08:45:51
---

# 题目

[组合总和 II](https://leetcode-cn.com/problems/combination-sum-ii/)

给定一个数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。

candidates 中的每个数字在每个组合中只能使用一次。

说明：

所有数字（包括目标数）都是正整数。
解集不能包含重复的组合。 
示例 1:

```
输入: candidates = [10,1,2,7,6,1,5], target = 8,
所求解集为:
[
  [1, 7],
  [1, 2, 5],
  [2, 6],
  [1, 1, 6]
]
```


示例 2:

```
输入: candidates = [2,5,2,1,2], target = 5,
所求解集为:
[
  [1,2,2],
  [5]
]
```





# 解题思路 √

### Python

1. 

```python
class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        results=[]
        visited={}
        candidates=sorted(candidates)
        length=len(candidates)
        
        def backtracking(temp,start,target):
            if target==0:
                results.append(temp)
                return
            for i in range(start,length):
                if i!=0 and candidates[i]==candidates[i-1] and not visited.get(i-1,False):
                    continue
                if candidates[i]<=target:
                    visited[i]=True
                    backtracking(temp+[candidates[i]],i+1,target-candidates[i])
                    visited[i]=False
                    
        backtracking([],0,target)
        return results
```


```python

```



### C++

```cpp

```

---



# 整理与总结

1. 巧妙在存储访问过的是下标
2. dict.get(key,default_value)

