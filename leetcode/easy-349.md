---
title: easy-349
tags:
  - LeetCode
description: ''
urlname: easy-349
date: 2019-09-01 17:41:48
---

# 题目

https://leetcode.com/problems/intersection-of-two-arrays/description/

Given two arrays, write a function to compute their intersection.

**Example 1:**

```
Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2]
```

**Example 2:**

```
Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [9,4]
```

**Note:**

- Each element in the result must be unique.
- The result can be in any order.

# 解题思路 √

先遍历第一个数组，将其存到hashtable中， 然后遍历第二个数组，如果在hashtable中存在就push到return，然后清空hashtable即可。

# Python

```python
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        visited,result={},[]
        for num in nums1:
            visited[num]=num
        for num in nums2:
            if num in visited:
                result.append(num)
                visited.pop(num)
        return result
```

```python
class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:        
        return set(nums1)&set(nums2)
```



# 整理与总结

1. python 里面的 hashtable 就是 dict 啊哈哈哈
2. python 里面的 stack 就是 list

