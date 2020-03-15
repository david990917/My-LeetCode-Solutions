---
title: easy-628
tags:
  - LeetCode
description: ''
urlname: easy-628
date: 2020-03-06 16:26:46
---

# 题目

https://leetcode-cn.com/problems/maximum-product-of-three-numbers/

> 给定一个整型数组，在数组中找出由三个数组成的最大乘积，并输出这个乘积。



# 解题思路 √

第一反应就是里面需要正负数乘法的判断。

### Python

1. 排序找到最大三个正数乘积，和带有两个负数的乘积进行比较。

   若负数不及两个也没有关系。

```python

    def maximumProduct(self, nums: List[int]) -> int:
        nums=sorted(nums)
        return max(nums[-1]*nums[-2]*nums[-3], nums[0]*nums[1]*nums[-1])
```

2. 找最大最小其实可以不用排序，需要预设值来进行比较。

   自己排序的时候需要注意重复元素的问题。


```python
class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        max1,max2,max3=-1001,-1001,-1001
        min1,min2=1001,1001
        for target in nums:
            # 重复的情况需要考虑
            if target>max1:
                max3,max2,max1=max2,max1,target
            elif target>max2:
                max3,max2=max2,target
            elif target > max3:
                max3=target
            
            #大小比较是两套系统
            if target<min1:
                min1,min2=target,min1
            elif target <min2:
                min2=target
        return max(max1*max2*max3,min1*min2*max1)
```



### C++

```cpp

```

---



# 整理与总结

1. `sorted(nums,key=abs)` 
2. `nums.sort()`看起来也可以使用。

