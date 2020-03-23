---
title: easy-258
tags:
  - LeetCode
description: ''
urlname: easy-258
date: 2020-03-23 22:36:23
---

# 题目

[各位相加](https://leetcode-cn.com/problems/add-digits/)

给定一个非负整数 num，反复将各个位上的数字相加，直到结果为一位数。

示例:

```
输入: 38
输出: 2 
解释: 各位相加的过程为：3 + 8 = 11, 1 + 1 = 2。 由于 2 是一位数，所以返回 2。
进阶:
你可以不使用循环或者递归，且在 O(1) 时间复杂度内解决这个问题吗？
```

# 解题思路 √

### Python

1. 使用巧妙办法：

   ```
   100x+10y+z=99x+9y+(x+y+z)
   
   如果(x+y+z)是一位数就解决了
   如果是两位数: (x+y+z) = 10m+n = 9m + (m+n)
   ```

   但是如果原来是9的倍数不行了

```python
class Solution:
    def addDigits(self, num: int) -> int:
        if num%9==0 and num!=0:
            return 9
        return num%9
```


```python

```



### C++

```cpp

```

---



# 整理与总结

1. Python取模 得到的结果和除数相同

