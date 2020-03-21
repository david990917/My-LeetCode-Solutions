---
title: medium-565
tags:
  - LeetCode
description: '数组嵌套'
urlname: medium-565
date: 2020-03-21 10:14:02
---

# 题目

https://leetcode-cn.com/problems/array-nesting/

索引从`0`开始长度为`N`的数组`A`，包含`0`到`N - 1`的所有整数。找到并返回最大的集合`S`，`S[i] = {A[i], A[A[i]], A[A[A[i]]], ... }`且遵守以下的规则。

假设选择索引为`i`的元素`A[i]`为`S`的第一个元素，`S`的下一个元素应该是`A[A[i]]`，之后是`A[A[A[i]]]...` 以此类推，不断添加直到`S`出现重复的元素。

**示例 1:**

```
输入: A = [5,4,0,3,1,6,2]
输出: 4
解释: 
A[0] = 5, A[1] = 4, A[2] = 0, A[3] = 3, A[4] = 1, A[5] = 6, A[6] = 2.

其中一种最长的 S[K]:
S[0] = {A[0], A[5], A[6], A[2]} = {5, 6, 2, 0}
```

**注意:**

1. `N`是`[1, 20,000]`之间的整数。
2. `A`中不含有重复的元素。
3. `A`中的元素大小在`[0, N-1]`之间。



# 解题思路 √

### Python

1. 引入了hashmap

```python
class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        hashset=set()
        maxLen=0
        for i in range(len(nums)):
            count=0
            j=i
            while j not in hashset:
                hashset.add(j)
                j=nums[j]
                count+=1
            maxLen=max(maxLen,count)
        return maxLen
```

2. 原地修改的话使用-1来进行


```python
class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        maxLen=0
        for i in range(len(nums)):
            count,j=0,i
            while nums[j]!=-1:
                temp=nums[j]
                nums[j]=-1
                j=temp
                count+=1
            maxLen=max(maxLen,count)
        return maxLen
```



### C++

```cpp

```

---



# 整理与总结

1. 数组嵌套

