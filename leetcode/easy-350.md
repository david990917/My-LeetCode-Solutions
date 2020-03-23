---
title: easy-350
tags:
  - LeetCode
description: ''
urlname: easy-350
date: 2020-03-23 22:48:36
---

# 题目

[两个数组的交集 II](https://leetcode-cn.com/problems/intersection-of-two-arrays-ii/)

给定两个数组，编写一个函数来计算它们的交集。

示例 1:

```
输入: nums1 = [1,2,2,1], nums2 = [2,2]
输出: [2,2]
```


示例 2:

```
输入: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
输出: [4,9]
说明：

输出结果中每个元素出现的次数，应与元素在两个数组中出现的次数一致。
我们可以不考虑输出结果的顺序。
```

进阶:

- 如果给定的数组已经排好序呢？你将如何优化你的算法？
- 如果 nums1 的大小比 nums2 小很多，哪种方法更优？
- 如果 nums2 的元素存储在磁盘上，磁盘内存是有限的，并且你不能一次加载所有的元素到内存中，你该怎么办？



# 解题思路 √

### Python

1. 哈希直接冲 - 调整顺序，为了空间复杂度小

```python
class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if len(nums1)>len(nums2):
            return self.intersect(nums2,nums1)
        hashmap={}
        for i in range(len(nums1)):
            if nums1[i] in hashmap:
                hashmap[nums1[i]]+=1
            else:hashmap[nums1[i]]=1
                
        result=[]
        for i in range(len(nums2)):
            if nums2[i] in hashmap:
                result.append(nums2[i])
                hashmap[nums2[i]]-=1
                if hashmap[nums2[i]]==0:
                    del hashmap[nums2[i]]
        return result
```

2. 排序

当输入数据是有序的，推荐使用此方法。在这里，我们对两个数组进行排序，并且使用两个指针在一次扫面找出公共的数字。

![在这里插入图片描述](easy-350/aHR0cHM6Ly9waWMubGVldGNvZGUtY24uY29tL0ZpZ3VyZXMvMzUwLzM1MF9hcHByb2FjaDItdjIucG5n.jfif)


```python

```



### C++

```cpp

```

---



# 整理与总结

1. 

