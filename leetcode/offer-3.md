---
title: offer-3
tags:
  - LeetCode
description: '数组中重复的数字'
urlname: offer-3
date: 2020-03-07 20:33:47
---

# 题目

[数组中重复的数字](https://leetcode-cn.com/problems/shu-zu-zhong-zhong-fu-de-shu-zi-lcof/)

找出数组中重复的数字。


在一个长度为 n 的数组 nums 里的所有数字都在 0～n-1 的范围内。数组中某些数字是重复的，但不知道有几个数字重复了，也不知道每个数字重复了几次。请找出数组中任意一个重复的数字。

示例 1：

```
输入：
[2, 3, 1, 0, 2, 5, 3]
输出：2 或 3 
```


限制：

2 <= n <= 100000

# 解题思路 √

### Python

1. 直接做就行了。

   hashmap对于找这种很方便。

```python
class Solution:
    def findRepeatNumber(self, nums: List[int]) -> int:
        hashmap={}
        for idx,number in enumerate(nums):
            if number not in hashmap:
                hashmap[number]=idx
            else:return number
```

2. 线性扫描-比较：目的是把元素都放到对应的位置上去，方便判断重复元素。


```python
class Solution:
    def findRepeatNumber(self, nums: List[int]) -> int:
        length=len(nums)
        for i in range(length):
            while nums[i]!=i:
                if nums[i]==nums[nums[i]]:
                    return nums[i]
                #swap
                temp=nums[nums[i]]
                nums[nums[i]]=nums[i]
                nums[i]=temp
```

3. 加强题目：不能修改元素

```python
使用二分查找 书P42-P43
```



### C++

```cpp

```

---



# 整理与总结

1. 

