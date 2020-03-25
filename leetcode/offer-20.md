---
title: offer-20
tags:
  - LeetCode
description: ''
urlname: offer-20
date: 2020-03-25 22:39:11
---

# 题目

[表示数值的字符串](https://leetcode-cn.com/problems/biao-shi-shu-zhi-de-zi-fu-chuan-lcof/)

请实现一个函数用来判断字符串是否表示数值（包括整数和小数）。例如，字符串"+100"、"5e2"、"-123"、"3.1416"、"0123"及"-1E-16"都表示数值，但"12e"、"1a3.14"、"1.2.3"、"+-5"及"12e+5.4"都不是。

# 解题思路 √

### Python

1. Python的方法

```python
class Solution:
    def isNumber(self, s: str) -> bool:
        try:
            s=float(s)
            return True
        except:
            return False
```

2. `A[.[B]][e|EC]`


```python
class Solution:
    def isNumber(self, s: str) -> bool:
        s=s.strip()
        if not s:return False
        dot_pos=s.find('.')
        e,E=s.find('e'),s.find('E')
        e_pos=e if e!=-1 else E
        if e_pos!=-1 and e_pos<dot_pos:return False # e/E后面不能有小数点
        C=self.isInteger(s,e_pos+1,len(s)-1) if e_pos!=-1 else True
        if dot_pos!=-1:
            B=self.isUnsigned(s,dot_pos+1,e_pos-1 if e_pos!=-1 else len(s)-1)
            if dot_pos==0 or (dot_pos==1 and s[0] in ('+','-')): # 如果A不存在，B必须存在
                if dot_pos==len(s)-1 or dot_pos+1==e_pos:return False # B不存在
                return B and C
            A=self.isInteger(s,0,dot_pos-1)
            if not(dot_pos==len(s)-1 or dot_pos+1==e_pos): # 如果B存在
                return A and B and C
            return A and C
        A=self.isInteger(s,0,e_pos-1 if e_pos!=-1 else len(s)-1)
        return A and C
    
    def isInteger(self,s,i,j):
        if 0<=i<len(s) and 0<=j<len(s):
            if s[i] in ('+','-'):
                i+=1
            return self.isUnsigned(s,i,j)
        return False
    
    def isUnsigned(self,s,i,j):
        if i>j:return False
        if 0<=i<len(s) and 0<=j<len(s):
            for index in range(i,j+1):
                if not s[index].isdigit():
                    return False
            return True
        return False
```



### C++

```cpp

```

---



# 整理与总结

1. 

