---
title: easy-27
tags:
  - LeetCode
description: ''
urlname: easy-27
date: 2020-03-06 17:35:03
---

# 题目

https://leetcode-cn.com/problems/remove-element/

给你一个数组 nums 和一个值 val，你需要 原地 移除所有数值等于 val 的元素，并返回移除后数组的新长度。

不要使用额外的数组空间，你必须仅使用 O(1) 额外空间并 原地 修改输入数组。

元素的顺序可以改变。你不需要考虑数组中超出新长度后面的元素。

**示例 1:**

```
给定 nums = [3,2,2,3], val = 3,

函数应该返回新的长度 2, 并且 nums 中的前两个元素均为 2。

你不需要考虑数组中超出新长度后面的元素。
```

**示例 2:**

```
给定 nums = [0,1,2,2,3,0,4,2], val = 2,

函数应该返回新的长度 5, 并且 nums 中的前五个元素为 0, 1, 3, 0, 4。

注意这五个元素可为任意顺序。

你不需要考虑数组中超出新长度后面的元素。
```

**说明:**

为什么返回数值是整数，但输出的答案是数组呢?

请注意，输入数组是以「引用」方式传递的，这意味着在函数里修改输入数组对于调用者是可见的。

你可以想象内部操作如下:

```
// nums 是以“引用”方式传递的。也就是说，不对实参作任何拷贝
int len = removeElement(nums, val);

// 在函数里修改输入数组对于调用者是可见的。
// 根据你的函数返回的长度, 它会打印出数组中 该长度范围内 的所有元素。
for (int i = 0; i < len; i++) {
    print(nums[i]);
}
```



# 解题思路 √

### Python

1. 快慢指针：基础不重复指针 + 前进到何处指针

```python
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        slow=0
        for fast in range(len(nums)):
            if nums[fast]!=val:
                nums[slow]=nums[fast]
                slow+=1
        return slow
```

2. 双指针：前进到何处指针，最终长度指针

   面对情况：删除的元素很少 + 我们对于顺序并不要求

   当前元素（val）和最后一个元素交换（对于本题，把最后一个拿回来就行了）

   - 最后一个元素不用`显式`的删掉，会在总长度减少的时候，自动不考虑

   - 如果最后一个元素也是`val`呢？再检查一次来规避风险

```python
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        length=len(nums)
        idx=0
        
        while idx < length:
            if nums[idx]==val:
                nums[idx]=nums[length-1]
                length-=1
            else: idx+=1
        return length
```



### C++

```cpp

```

---



# 整理与总结

1. 

