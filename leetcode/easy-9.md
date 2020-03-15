---
title: easy-9
tags:
  - LeetCode
description: '回文数'
urlname: easy-9
date: 2020-03-10 18:38:45
---

# 题目

https://leetcode-cn.com/problems/palindrome-number

判断一个整数是否是回文数。回文数是指正序（从左向右）和倒序（从右向左）读都是一样的整数。

**示例 1:**

```
输入: 121
输出: true
```

**示例 2:**

```
输入: -121
输出: false
解释: 从左向右读, 为 -121 。 从右向左读, 为 121- 。因此它不是一个回文数。
```

**示例 3:**

```
输入: 10
输出: false
解释: 从右向左读, 为 01 。因此它不是一个回文数。
```

**进阶:**

你能不将整数转为字符串来解决这个问题吗？

# 解题思路 √

### Python

1. 字符串

```python
class Solution:
    def isPalindrome(self, x: int) -> bool:
        x=str(x)
        def helper(x):
            if len(x)==0 or len(x)==1:return True
            return x[0]==x[-1] and helper(x[1:-1])
        return helper(x)
```


```python
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x<0 or (x%10==0 and x!=0):return False
        revertedNumber=0
        while x>revertedNumber:
            revertedNumber=revertedNumber*10+x%10
            x//=10
        return x==revertedNumber or x==revertedNumber//10
```



### C++

```cpp

```

---



# 整理与总结

1. 

