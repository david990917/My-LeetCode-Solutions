---
title: easy-171
tags:
  - LeetCode
description: 'Excel表列序号'
urlname: easy-171
date: 2020-03-15 18:08:57
---

# 题目

给定一个Excel表格中的列名称，返回其相应的列序号。

例如，

    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28 
    ...
**示例 1:**

```
输入: "A"
输出: 1
```


**示例 2:**

```
输入: "AB"
输出: 28
```


**示例 3:**

```
输入: "ZY"
输出: 701
```



# 解题思路 √

### Python

1. 26进制-递归

```python
class Solution:
    def titleToNumber(self, s: str) -> int:
        if not s:return 0
        return (ord(s[-1])-ord('A')+1)+26*self.titleToNumber(s[:-1])
```

2. 正常累加


```python
class Solution:
    def titleToNumber(self, s: str) -> int:
        result=0
        while s:
            temp=ord(s[0])-ord('A')+1
            result=result*26+temp
            s=s[1:]
        return result
```



### C++

```cpp

```

---



# 整理与总结

1. 

