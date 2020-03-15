---
title: easy-88
tags:
  - LeetCode
description: '合并两个有序数组'
urlname: easy-88
date: 2019-08-30 18:58:07
---

# 题目

https://leetcode.com/problems/merge-sorted-array/description/

Given two sorted integer arrays *nums1* and *nums2*, merge *nums2* into *nums1* as one sorted array.

**Note:**

- The number of elements initialized in *nums1* and *nums2* are *m* and *n* respectively.
- You may assume that *nums1* has enough space (size that is greater or equal to *m* + *n*) to hold additional elements from *nums2*.

**Example:**

```
Input:
nums1 = [1,2,3,0,0,0], m = 3
nums2 = [2,5,6],       n = 3

Output: [1,2,2,3,5,6]
```

# 思路 √

我们需要三个指针：

1. current 用于记录当前填补到那个位置了
2. m 用于记录 nums1 数组处理到哪个元素了
3. n 用于记录 nums2 数组处理到哪个元素了

如图所示：

- 灰色代表 num2 数组已经处理过的元素
- 红色代表当前正在进行比较的元素
- 绿色代表已经就位的元素

[![88.merge-sorted-array-1](easy-88/88.merge-sorted-array-1.png)](https://github.com/azl397985856/leetcode/blob/master/assets/problems/88.merge-sorted-array-1.png) [![88.merge-sorted-array-2](easy-88/88.merge-sorted-array-2.png)](https://github.com/azl397985856/leetcode/blob/master/assets/problems/88.merge-sorted-array-2.png) [![88.merge-sorted-array-3](easy-88/88.merge-sorted-array-3.png)](https://github.com/azl397985856/leetcode/blob/master/assets/problems/88.merge-sorted-array-3.png)

## 关键点解析

- 从后往前比较，并从后往前插入
- 可以不使用 current 指针

# Python

1. 双指针，易于理解

```python
class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        index1,index2,index=m-1,n-1,m+n-1
        while index1>=0 and index2>=0:
            if nums2[index2]>nums1[index1]:
                nums1[index]=nums2[index2]
                index2-=1
            elif nums1[index1]>=nums2[index2]:
                nums1[index]=nums1[index1]
                index1-=1
            index-=1
        while index2>=0:
            nums1[:index2+1]=nums2[:index2+1]
            index2-=1
```



# 整理与总结

1. 无脑方法：直接把 nums2 插入到 nums1 中，然后排序。拒绝

2. mergeSort() 这个是插入到新数组中，我们需要练习的是就地。拒绝

3. 不用返回元素，判断的时候省事儿了

   - m 有 n 没有，无所谓

4. 从 m+n-1 的位置开始往回，甚至都不需要判断位置

   总元素个数是 m+n，所以肯定不会冲突

   需要注意元素个数 和 元素的位置之间的关系

5. 判断的方式，我是大于，标准中还带了等于

   这个的话：没什么影响，只是显示展示了处理的方式

6. 复制的方法，使用 [:n]