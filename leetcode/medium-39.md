---
title: medium-39
tags:
  - LeetCode
description: ''
urlname: medium-39
date: 2020-03-23 08:37:07
---

# 题目

[组合总和](https://leetcode-cn.com/problems/combination-sum/)

给定一个无重复元素的数组 candidates 和一个目标数 target ，找出 candidates 中所有可以使数字和为 target 的组合。

candidates 中的数字可以无限制重复被选取。

说明：

所有数字（包括 target）都是正整数。
解集不能包含重复的组合。 
示例 1:

```
输入: candidates = [2,3,6,7], target = 7,
所求解集为:
[
  [7],
  [2,2,3]
]
```


示例 2:

```
输入: candidates = [2,3,5], target = 8,
所求解集为:
[
  [2,2,2,2],
  [2,3,3],
  [3,5]
]
```





# 解题思路 √

### Python

1. 

```python
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        results=[]
        length=len(candidates)
        
        def backTracking(temp,start,target):
            if target==0:
                results.append(temp)
                return
            for i in range(start,length):
                if candidates[i]<=target:
                    backTracking(temp+[candidates[i]],i,target-candidates[i])
        
        backTracking([],0,target)
        return results
```


```python

```



### C++

```cpp

```

---



# 整理与总结

1. 三道题目 - 关于排列组合
   - medium-39 无重复元素 可重复使用
   - medium-40 有重复元素 不可重复使用 解集不重复
   - medium-78 无重复元素 不可重复使用 解集不重复

不可重复使用就是start=i+1，可重复使用start=i

解集不重复

- 对于重复元素，我们需要设置visited来检查（一个一个使用：如果前一个没有使用就不继续用）
- 对于元素不重复，避免回环【start就可以了】就可以了