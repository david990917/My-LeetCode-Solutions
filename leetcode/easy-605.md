---
title: easy-605
tags:
  - LeetCode
description: ''
urlname: easy-605
date: 2020-03-22 19:41:55
---

# 题目

[种花问题](https://leetcode-cn.com/problems/can-place-flowers/)

假设你有一个很长的花坛，一部分地块种植了花，另一部分却没有。可是，花卉不能种植在相邻的地块上，它们会争夺水源，两者都会死去。

给定一个花坛（表示为一个数组包含0和1，其中0表示没种植花，1表示种植了花），和一个数 n 。能否在不打破种植规则的情况下种入 n 朵花？能则返回True，不能则返回False。

示例 1:

```
输入: flowerbed = [1,0,0,0,1], n = 1
输出: True
```


示例 2:

```
输入: flowerbed = [1,0,0,0,1], n = 2
输出: False
```


注意:

数组内已种好的花不会违反种植规则。
输入的数组长度范围为 [1, 20000]。
n 是非负整数，且不会超过输入数组的大小。





# 解题思路 √

### Python

1. 检查前后

```python
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        length,count=len(flowerbed),0
        for idx in range(length):
            if flowerbed[idx]==1:continue
            pre=0 if idx==0 else flowerbed[idx-1]
            next=0 if idx==length-1 else flowerbed[idx+1]
            if pre==0 and next==0:
                flowerbed[idx]=1
                count+=1
                if count>=n:return True
        return count>=n
```


```python

```



### C++

```cpp

```

---



# 整理与总结

1. 

