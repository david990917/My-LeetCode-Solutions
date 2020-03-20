---
title: easy-485
tags:
  - LeetCode
description: '最大连续1的个数'
urlname: easy-485
date: 2020-03-20 21:33:42
---

# 题目

https://leetcode-cn.com/problems/max-consecutive-ones/


给定一个二进制数组， 计算其中最大连续1的个数。

**示例 1:**

```
输入: [1,1,0,1,1,1]
输出: 3
解释: 开头的两位和最后的三位都是连续1，所以最大连续1的个数是 3.
```

**注意：**

- 输入的数组只包含 `0` 和`1`。
- 输入数组的长度是正整数，且不超过 10,000。

# 解题思路 √

### Python

1. 时刻注意退出的情况

```python
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        if not nums:return 0
        currLen,maxLen=0,0,
        for i in range(len(nums)):
            if nums[i]==0:
                maxLen=max(maxLen,currLen)
                currLen=0
            else:
                currLen+=1
        maxLen=max(maxLen,currLen)
        return maxLen
```


```python

```



### C++

```cpp

```

---



# 整理与总结

1. 

