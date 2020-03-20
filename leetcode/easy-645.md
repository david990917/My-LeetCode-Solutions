---
title: easy-645
tags:
  - LeetCode
description: '错误的集合'
urlname: easy-645
date: 2020-03-20 22:04:57
---

# 题目

https://leetcode-cn.com/problems/set-mismatch/

集合 `S` 包含从1到 `n` 的整数。不幸的是，因为数据错误，导致集合里面某一个元素复制了成了集合里面的另外一个元素的值，导致集合丢失了一个整数并且有一个元素重复。

给定一个数组 `nums` 代表了集合 `S` 发生错误后的结果。你的任务是首先寻找到重复出现的整数，再找到丢失的整数，将它们以数组的形式返回。

**示例 1:**

```
输入: nums = [1,2,2,4]
输出: [2,3]
```

**注意:**

1. 给定数组的长度范围是 [2, 10000]。
2. 给定的数组是无序的。

# 解题思路 √

### Python

1. 交换数组元素，使之出现在正确的位置上

```python
class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        n=len(nums)
        for i in range(n):
            while nums[i]!=i+1 and nums[nums[i]-1]!=nums[i]:
                nums[nums[i]-1],nums[i]=nums[i],nums[nums[i]-1]
        for i in range(n):
            if nums[i]!=i+1:return [nums[i],i+1]
```


```python

```



### C++

```cpp

```

---



# 整理与总结

1. [错误的集合](https://leetcode-cn.com/problems/set-mismatch/)
2. 涉及了内部元素的交换，就要小心！
3. 和其他题目不太一样，继续思考一下！

