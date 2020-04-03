---
title: medium-494
tags:
  - LeetCode
description: ''
urlname: medium-494
date: 2020-04-03 16:55:45
---

# 题目

[目标和](https://leetcode-cn.com/problems/target-sum/)

给定一个非负整数数组，a1, a2, ..., an, 和一个目标数，S。现在你有两个符号 + 和 -。对于数组中的任意一个整数，你都可以从 + 或 -中选择一个符号添加在前面。

返回可以使最终数组和为目标数 S 的所有添加符号的方法数。

示例 1:

```
输入: nums: [1, 1, 1, 1, 1], S: 3
输出: 5
解释: 

-1+1+1+1+1 = 3
+1-1+1+1+1 = 3
+1+1-1+1+1 = 3
+1+1+1-1+1 = 3
+1+1+1+1-1 = 3

一共有5种方法让最终目标和为3。
```


注意:

1. 数组非空，且长度不会超过20。
2. 初始的数组的和不会超过1000。
3. 保证返回的最终结果能被32位整数存下。

# 解题思路 √

### Python

1. Python自己纯正的DFS超时了（的确大量的重复计算了）

```python
class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        if not nums:return 0
        self.count,self.length=0,len(nums)
        
        def dfs(curr,bit):
            if curr==0 and bit==self.length:
                self.count+=1
                return
            if bit==self.length:return
            dfs(curr+nums[bit],bit+1)
            dfs(curr-nums[bit],bit+1)
        
        dfs(-S,0)
        return self.count
```

2. 另一个思路的DFS


```python
class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        if not nums:return 0
        self.visited,self.length={},len(nums)
        def dfs(curr,i):
            if i<self.length and (curr,i) not in self.visited:
                self.visited[(curr,i)]=dfs(curr+nums[i],i+1)+dfs(curr-nums[i],i+1)
            return self.visited.get((curr,i),int(curr==S))
        return dfs(0,0)
```



### C++

```cpp

```

---



# 整理与总结

1. 

