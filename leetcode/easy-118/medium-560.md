---
title: medium-560
tags:
  - LeetCode
description: '和为K的连续子数组'
urlname: medium-560
date: 2020-03-19 08:43:09
---

# 题目

https://leetcode-cn.com/problems/subarray-sum-equals-k/

给定一个整数数组和一个整数 **k，**你需要找到该数组中和为 **k** 的连续的子数组的个数。

**示例 1 :**

```
输入:nums = [1,1,1], k = 2
输出: 2 , [1,1] 与 [1,1] 为两种不同的情况。
```

**说明 :**

1. 数组的长度为 [1, 20,000]。
2. 数组中元素的范围是 [-1000, 1000] ，且整数 **k** 的范围是 [-1e7, 1e7]。

# 解题思路 √

### Python

1. 利用前缀和 + hashtable

   转换 `prefixSum[j]-prefixSum[i]=k` -> `prefixSum[i]=prefixSum[j]-k`

```python
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        hashmap={0:1}
        currPrefixSum,count=0,0
        for i in nums:
            currPrefixSum+=i
            if currPrefixSum-k in hashmap:count+=hashmap[currPrefixSum-k]
            if currPrefixSum in hashmap:
                hashmap[currPrefixSum]+=1
            else:hashmap[currPrefixSum]=1
        return count
```


```python

```



### C++

```cpp

```

---



# 整理与总结

1. 

