---
title: easy-704
tags:
  - LeetCode
description: '二分查找'
urlname: easy-704
date: 2020-03-20 19:49:25
---

# 题目

https://leetcode-cn.com/problems/binary-search/

给定一个 `n` 个元素有序的（升序）整型数组 `nums` 和一个目标值 `target` ，写一个函数搜索 `nums` 中的 `target`，如果目标值存在返回下标，否则返回 `-1`。


**示例 1:**

```
输入: nums = [-1,0,3,5,9,12], target = 9
输出: 4
解释: 9 出现在 nums 中并且下标为 4
```

**示例 2:**

```
输入: nums = [-1,0,3,5,9,12], target = 2
输出: -1
解释: 2 不存在 nums 中因此返回 -1
```

 

**提示：**

1. 你可以假设 `nums` 中的所有元素是不重复的。
2. `n` 将在 `[1, 10000]`之间。
3. `nums` 的每个元素都将在 `[-9999, 9999]`之间。



# 解题思路 √

![img](easy-704/a613c4cd4a24456a6f0ce9c36b003392e00e28e0228707c08b3e555b1c68cfc3-0035-3.png)

### Python

1. 使用区间排除法来进行判断

```python
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if not nums:return -1
        l,h=0,len(nums)-1
        while l<h:
            mid=l+(h-l)//2
            if nums[mid]<target:
                l=mid+1
            else:
                h=mid
        return l if nums[l]==target else -1
```


```python

```



### C++

```cpp

```

---



# 整理与总结

1. [二分查找](https://leetcode-cn.com/problems/binary-search/)

   if里面排除掉不可能的区间，else里面是可能的区间；使用闭括号

