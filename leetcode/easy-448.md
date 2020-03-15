---
title: easy-448
tags:
  - LeetCode
description: ''
urlname: easy-448
date: 2020-03-06 15:22:48
---

# 题目

https://leetcode-cn.com/problems/find-all-numbers-disappeared-in-an-array/

> 给定一个范围在  1 ≤ a[i] ≤ n ( n = 数组大小 ) 的 整型数组，数组中的元素一些出现了两次，另一些只出现一次。
>
> 找到所有在 [1, n] 范围之间没有出现在数组中的数字。
>
> 您能在不使用额外空间且时间复杂度为O(n)的情况下完成这个任务吗? 你可以假定返回的数组不算在额外空间内。
>



# 解题思路 √

# Python

1. 直白翻译题目意思。

```python
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        length=len(nums)
        nums=set(nums) #减少搜索时间，避免超时
        ans=[]
        for i in range(1,length+1):
            if i not in nums:
                ans.append(i)
        return ans
```

2. 原来的位置进行操作，通过标记的方法。

   原地标记可以通过增加负号的方式来进行标记。

   两次的话就是会引起一些障碍，因为`负负得正`。

   ![在这里插入图片描述](easy-448/aHR0cHM6Ly9waWMubGVldGNvZGUtY24uY29tL0ZpZ3VyZXMvNDQ4L2FuaW0zNy5wbmc.jfif)

```python
class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        length=len(nums)
        for i in range(length):
            #现在出现的这个数字(绝对值)，对应数组的坐标位置(3 -> 2)
            pos=abs(nums[i])-1 
            #这个位置上现在有的数字 -> 需要判断正负号
            value=nums[pos] 
            #原来正的变负数，如果是负的就不变
            nums[pos] = -value if value>0 else value 
        
        ans=[]
        for i in range(length):
            if nums[i]>0:
                ans.append(i+1)
        return ans
```



# C++

```cpp

```

---



# 整理与总结

1. 涉及到`nums[0]`, `nums[-1]`的时候一定要注意边界条件。
2. `for i in range(1,len(nums))` 对于1也要注意边界条件。
