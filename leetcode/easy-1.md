---
title: easy-1
tags:
  - LeetCode
description: '两数之和'
urlname: easy-1
date: 2020-03-05 22:01:58
---

# 题目

[两数之和](https://leetcode-cn.com/problems/two-sum/)

给定一个整数数组 nums 和一个目标值 target，请你在该数组中找出和为目标值的那 两个 整数，并返回他们的数组下标。

你可以假设每种输入只会对应一个答案。但是，你不能重复利用这个数组中同样的元素。

**示例:**

```
给定 nums = [2, 7, 11, 15], target = 9

因为 nums[0] + nums[1] = 2 + 7 = 9
所以返回 [0, 1]
```

# 解题思路 √

## 简单直白的暴力双遍历

双循环找就完事儿了，注意`j`可以直接从`i`的基础上开始找。

***复杂度分析***

- 时间复杂度：$O(n^2)$
- 空间复杂度：$O(1)$

## Python字典模拟哈希表

保持元素与其索引相互对应的最好办法就是哈希表。

哈希表插入的同时进行搜索。

***复杂度分析***

- 时间复杂度：$O(n)$ 我们只遍历一次。
- 空间复杂度：$O(n)$ 额外需要存储。



# Python

```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        length=len(nums)
        for i in range(length):
            left=target-nums[i]
            for j in range(i+1,length):
                if nums[j]==left:
                    return [i,j]
```

```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        #遍历列表的同时查字典
        for idx, n in enumerate(nums):
            if target - n in hashmap:
                return [hashmap[target-n],idx]
            hashmap[n]=idx
```



# C++

```cpp

```

---

# 官方解答建议



# 整理与总结

1. Python的排序使用`nums=sorted(nums)`

2. 保持元素与其索引相互对应的最好办法就是哈希表。

   通过以空间换取速度的方式，我们可以将查找时间从 `O(n)` 降低到 `O(1)`

3. Bruce:

   > 实测三种判断方式各运行100万次用时（win10 python3.7.3）：
   >
   > 1. `key in dict` 用时 1.088 秒
   > 2. `dict.get(key)` 用时 1.294 秒
   > 3. `dict[key]` 用时 1.01 秒





