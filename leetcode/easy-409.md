---
title: easy-409
tags:
  - LeetCode
description: ''
urlname: easy-409
date: 2020-03-16 20:59:09
---

# 题目

https://leetcode-cn.com/problems/implement-strstr

给定一个包含大写字母和小写字母的字符串，找到通过这些字母构造成的最长的回文串。

在构造过程中，请注意区分大小写。比如 "Aa" 不能当做一个回文字符串。

**注意:**
假设字符串的长度不会超过 1010。

**示例 1:**

```
输入:
"abccccdd"

输出:
7

解释:
我们可以构造的最长的回文串是"dccaccd", 它的长度是 7。
```



# 解题思路 √

### Python

1. 偶数直接加，奇数的把偶数的那部分加起来。最后处理中间的对称元素（如果存在奇数的话）。

```python
class Solution:
    def longestPalindrome(self, s: str) -> int:
        hashmap={}
        for i in s:
            if i not in hashmap:hashmap[i]=1
            else:hashmap[i]+=1
        
        count,oddFlag=0,False
        for key in hashmap:
            if hashmap[key]%2:
                count+=hashmap[key]-1
                oddFlag=True
            else:
                count+=hashmap[key]
        return count+oddFlag
```


```python

```



### C++

```cpp

```

---



# 整理与总结

1. 

