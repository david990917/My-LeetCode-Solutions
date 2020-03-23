---
title: easy-67
tags:
  - LeetCode
description: ''
urlname: easy-67
date: 2020-03-23 21:04:12
---

# 题目

[二进制求和](https://leetcode-cn.com/problems/add-binary/)

给定两个二进制字符串，返回他们的和（用二进制表示）。

输入为非空字符串且只包含数字 1 和 0。

示例 1:

```
输入: a = "11", b = "1"
输出: "100"
```


示例 2:

```
输入: a = "1010", b = "1011"
输出: "10101"
```



# 解题思路 √

### Python

1. 二进制就是2

```python
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        m,n,carry=len(a)-1,len(b)-1,0
        result=""
        while m>=0 or n>=0:
            i=int(a[m]) if m>=0 else 0
            j=int(b[n]) if n>=0 else 0
            value=i+j+carry
            result=str(value%2)+result
            carry=value//2
            m,n=m-1,n-1
        return result if carry==0 else '1'+result
```


```python

```



### C++

```cpp

```

---



# 整理与总结

1. 

