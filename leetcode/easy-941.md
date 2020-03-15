---
title: easy-941
tags:
  - LeetCode
description: ''
urlname: easy-941
date: 2020-03-06 11:16:26
---

# 题目

https://leetcode-cn.com/problems/valid-mountain-array/

> 给定一个整数数组 A，如果它是有效的山脉数组就返回 true，否则返回 false。
>
> 让我们回顾一下，如果 A 满足下述条件，那么它是一个山脉数组：
>
> A.length >= 3
>
> 在 0 < i < A.length - 1 条件下，存在 i 使得：
> A[0] < A[1] < ... A[i-1] < A[i]
> A[i] > A[i+1] > ... > A[A.length - 1]

# 解题思路 √

## 直接思路-翻译公式

这种方法以后被称作线性扫描。

## 





# Python

直接翻译公式

```python
class Solution:
    def validMountainArray(self, A: List[int]) -> bool:
        length=len(A)
        if length<3:
            return False
        
        idx=0
        for i in range(1,length):
            if A[i]>A[i-1]:
                idx=i
            else:break
        if idx==0 or idx==length-1:return False

        for i in range(idx,length-1):
            if A[i+1]>=A[i]:
                return False
        
        return True
```

改良版本-`if` - > `while`

```python
class Solution:
    def validMountainArray(self, A: List[int]) -> bool:
        length=len(A)
        if length<3:
            return False
        
        idx=0
        # UP
        while idx+1<length and A[idx]<A[idx+1]:
            idx+=1
        if idx==0 or idx==length-1:return False

        # Down
        while idx+1<length and A[idx]>A[idx+1]:
            idx+=1
        
        return idx==length-1
```



# C++

```cpp

```

---



# 整理与总结

1. 

