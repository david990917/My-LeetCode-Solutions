---
title: easy-414
tags:
  - LeetCode
description: ''
urlname: easy-414
date: 2020-03-24 12:09:40
---

# 题目

[第三大的数](https://leetcode-cn.com/problems/third-maximum-number/)

给定一个非空数组，返回此数组中第三大的数。如果不存在，则返回数组中最大的数。要求算法时间复杂度必须是O(n)。

示例 1:

```
输入: [3, 2, 1]

输出: 1

解释: 第三大的数是 1.
```

示例 2:

```
输入: [1, 2]

输出: 2

解释: 第三大的数不存在, 所以返回最大的数 2 .
```

示例 3:

```
输入: [2, 2, 3, 1]

输出: 1

解释: 注意，要求返回第三大的数，是指第三大且唯一出现的数。
存在两个值为2的数，它们都排第二。
```





# 解题思路 √

### Python

1. 正常处理 - 延伸到大于等于

```python
class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        allMax,secMax,thirdMax=-sys.maxsize,-sys.maxsize,-sys.maxsize
        for number in nums:
            if number>=allMax:
                if number == allMax:continue
                allMax,secMax,thirdMax=number,allMax,secMax
            elif number>=secMax:
                if number==secMax:continue
                secMax,thirdMax=number,secMax
            elif number>thirdMax:
                thirdMax=number
        
        return thirdMax if thirdMax!=-sys.maxsize else allMax
```


```python

```



### C++

```cpp

```

---



# 整理与总结

1. 

