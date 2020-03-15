---
title: hard-4-还没做出来-答案也没看全呢
tags:
  - LeetCode
description: '还没做出来'
urlname: hard-4
date: 2020-03-05 20:23:59
---

# 题目

https://leetcode-cn.com/problems/median-of-two-sorted-arrays/

> 给定两个大小为 m 和 n 的有序数组 nums1 和 nums2。
>
> 请你找出这两个有序数组的中位数，并且要求算法的时间复杂度为 O(log(m + n))。
>
> 你可以假设 nums1 和 nums2 不会同时为空。
>
> 示例 1:
>
> > nums1 = [1, 3]
> > nums2 = [2]
>
> 则中位数是 2.0
> 示例 2:
>
> > nums1 = [1, 2]
> > nums2 = [3, 4]
> >
> > 则中位数是 (2 + 3)/2 = 2.5
> >



# 解题思路 √

## 

***复杂度分析***

- 时间复杂度：$O()$
- 空间复杂度：$O()$



# Python

```python

```

# C++

```cpp

```

---

# 官方解答建议

https://leetcode-cn.com/problems/median-of-two-sorted-arrays/solution/xun-zhao-liang-ge-you-xu-shu-zu-de-zhong-wei-shu-b/



# 整理与总结

1. 看到算法复杂度要求是`log`的时候，就可以直接往二分法上面想。
2. 中位数：奇数个的时候就是$m/2$，如果偶数个就是中间两个数$$和$$的平均数。
3. 额外中位数的技巧：如果我们是$O(m+n)$的时间要求，我们就可以使用双指针，移动第$(m+n+1)/2$的时候就是中位数了。
4. 

