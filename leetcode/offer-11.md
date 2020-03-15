---
title: offer-11
tags:
  - LeetCode
description: '旋转数组的最小数字'
urlname: offer-11
date: 2020-03-15 12:25:24
---

# 题目

https://leetcode-cn.com/problems/xuan-zhuan-shu-zu-de-zui-xiao-shu-zi-lcof/

把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。输入一个递增排序的数组的一个旋转，输出旋转数组的最小元素。例如，数组 [3,4,5,1,2] 为 [1,2,3,4,5] 的一个旋转，该数组的最小值为1。  

**示例 1：**

```
输入：[3,4,5,1,2]
输出：1
```


**示例 2：**

```
输入：[2,2,2,0,1]
输出：0
```



# 解题思路 √

### Python

![Picture1.png](offer-11/5884538fb9541a31a807d59c81226ded3dcd61df66efcdeb000165036ea68bb9-Picture1.png)

1. 前一个指针指向前面递增的数组；后一个指针指向后面递增的数组。

   终止条件就是`right-left==1`，返回的是（等于index2的中间节点）

   注意旋转后是原来数组的情况，返回首结点（初始化设置中间节点的index是index1）

```python
class Solution:
    def minArray(self, numbers: [int]) -> int:
        i, j = 0, len(numbers) - 1
        while i < j:
            m = (i + j) // 2
            if numbers[m] > numbers[j]: i = m + 1 #[m+1,j]
            elif numbers[m] < numbers[j]: j = m #[i,m]
            else: j -= 1
        return numbers[i]
```


```python

```



### C++

```cpp

```

---



# 整理与总结

1. Python注意除法的整除

