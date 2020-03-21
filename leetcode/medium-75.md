---
title: medium-75
tags:
  - LeetCode
description: ''
urlname: medium-75
date: 2020-03-21 18:46:41
---

# 题目

[颜色分类](https://leetcode-cn.com/problems/sort-colors/)

给定一个包含红色、白色和蓝色，一共 n 个元素的数组，原地对它们进行排序，使得相同颜色的元素相邻，并按照红色、白色、蓝色顺序排列。

此题中，我们使用整数 0、 1 和 2 分别表示红色、白色和蓝色。

注意:
不能使用代码库中的排序函数来解决这道题。

示例:

```
输入: [2,0,2,1,1,0]
输出: [0,0,1,1,2,2]
```


进阶：

一个直观的解决方案是使用计数排序的两趟扫描算法。
首先，迭代计算出0、1 和 2 元素的个数，然后按照0、1、2的排序，重写当前数组。
你能想出一个仅使用常数空间的一趟扫描算法吗？

# 解题思路 √

### Python

![image.png](medium-75/3ab6cc20bb91835c2722c688c2f894e407289333bae839a930957461e810a957-image.png)

我们用三个指针（p0, p2 和curr）来分别追踪0的最右边界，2的最左边界和当前考虑的元素。

![image.png](medium-75/5b3d372e0bfb293ca3aac12e90421d7612c9e75b78b579f954c42ebfe74705d4-image.png)

本解法的思路是沿着数组移动 curr 指针，若nums[curr] = 0，则将其与 nums[p0]互换；若 nums[curr] = 2 ，则与 nums[p2]互换。

**算法**

- 初始化0的最右边界：p0 = 0。在整个算法执行过程中 nums[idx < p0] = 0.


- 初始化2的最左边界 ：p2 = n - 1。在整个算法执行过程中 nums[idx > p2] = 2.


- 初始化当前考虑的元素序号 ：curr = 0.


- While curr <= p2 :
  - 若 nums[curr] = 0 ：交换第 curr个 和 第p0个 元素，并将指针都向右移。
  - 若 nums[curr] = 2 ：交换第 curr个和第 p2个元素，并将 p2指针左移 。
  - 若 nums[curr] = 1 ：将指针curr右移。





1. 荷兰国旗问题

```python
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero,one,two=0,0,len(nums)-1
        while one<=two:
            if nums[one]==0:
                nums[zero],nums[one]=nums[one],nums[zero]
                zero,one=zero+1,one+1
            elif nums[one]==2:
                nums[one],nums[two]=nums[two],nums[one]
                two-=1
            else:one+=1
```


```python

```



### C++

```cpp

```

---



# 整理与总结

1. 

