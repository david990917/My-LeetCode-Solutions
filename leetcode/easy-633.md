---
title: easy-633
tags:
  - LeetCode
description: '平方数之和'
urlname: easy-633
date: 2020-03-11 18:41:55
---

# 题目

https://leetcode-cn.com/problems/sum-of-square-numbers/

> 给定一个非负整数 `c` ，你要判断是否存在两个整数 `a` 和 `b`，使得 $a^2$ + $b^2$ = c。
>
> **示例1:**
>
> ```
> 输入: 5
> 输出: True
> 解释: 1 * 1 + 2 * 2 = 5
> ```
>
> **示例2:**
>
> ```
> 输入: 3
> 输出: False
> ```



# 解题思路 √

### Python

1. 头尾双指针

```python
import math
class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        length=int(math.sqrt(c))
        left,right=0,length
        while left<=right:
            temp=left*left+right*right
            if temp==c:return True
            elif temp>c:right-=1
            else:left+=1
        return False
```


```python

```



### C++

```cpp

```

---



# 整理与总结

1. 

