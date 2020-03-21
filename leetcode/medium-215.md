---
title: medium-215
tags:
  - LeetCode
description: ''
urlname: medium-215
date: 2020-03-21 17:56:57
---

# 题目

[数组中的第K个最大元素](https://leetcode-cn.com/problems/kth-largest-element-in-an-array/)

在未排序的数组中找到第 k 个最大的元素。请注意，你需要找的是数组排序后的第 k 个最大的元素，而不是第 k 个不同的元素。

示例 1:

```
输入: [3,2,1,5,6,4] 和 k = 2
输出: 5
```


示例 2:

```
输入: [3,2,3,1,2,4,5,5,6] 和 k = 4
输出: 4
```


说明:

你可以假设 k 总是有效的，且 1 ≤ k ≤ 数组的长度。

# 解题思路 √

### Python

1. 使用堆

```python
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        hp=nums[:k]
        heapq.heapify(hp)
        for idx in range(k,len(nums)):
            if nums[idx]>=hp[0]:
                heapq.heappop(hp)
                heapq.heappush(hp,nums[idx])
        return hp[0]
```


```python

```



### C++

```cpp

```

---



# 整理与总结

1. 

