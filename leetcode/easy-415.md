---
title: easy-415
tags:
  - LeetCode
description: ''
urlname: easy-415
date: 2020-03-23 17:40:03
---

# 题目

[字符串相加](https://leetcode-cn.com/problems/add-strings/)

给定两个字符串形式的非负整数 num1 和num2 ，计算它们的和。

注意：

```
num1 和num2 的长度都小于 5100.
num1 和num2 都只包含数字 0-9.
num1 和num2 都不包含任何前导零。
你不能使用任何內建 BigInteger 库， 也不能直接将输入的字符串转换为整数形式。
```



# 解题思路 √

### Python

1. 从后往前相加 对其位数；注意最后的carry

```python
class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        m,n,carry=len(num1)-1,len(num2)-1,0
        result=""
        while m>=0 or n>=0:
            i=ord(num1[m])-ord('0') if m>=0 else 0
            j=ord(num2[n])-ord('0') if n>=0 else 0
            value=(i+j+carry)%10
            carry=(i+j+carry)//10
            result=str(value)+result
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

