---
title: easy-205
tags:
  - LeetCode
description: '同构字符串'
urlname: easy-205
date: 2020-03-16 21:06:55
---

# 题目

https://leetcode-cn.com/problems/isomorphic-strings

给定两个字符串 s 和 t，判断它们是否是同构的。

如果 s 中的字符可以被替换得到 t ，那么这两个字符串是同构的。

所有出现的字符都必须用另一个字符替换，同时保留字符的顺序。两个字符不能映射到同一个字符上，但字符可以映射自己本身。

**示例 1:**

```
输入: s = "egg", t = "add"
输出: true
```


**示例 2:**

```
输入: s = "foo", t = "bar"
输出: false
```


**示例 3:**

```
输入: s = "paper", t = "title"
输出: true
```


说明:
你可以假设 s 和 t 具有相同的长度。

# 解题思路 √

### Python

1. 正反验证

```python
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        def helper(s,t):
            hashmap={}
            length=len(s)
            for i in range(length):
                target=s[i]
                if target not in hashmap:
                    hashmap[target]=t[i]
                if target in hashmap:
                    if hashmap[target]!=t[i]:
                        return False
            return True
        return helper(s,t) and helper(t,s)
```

2. 更新位置


```python
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        hashmap_s,hashmap_t={},{}
        for i in range(len(s)):
            if s[i] in hashmap_s and t[i] not in hashmap_t:return False
            if s[i] not in hashmap_s and t[i] in hashmap_t:return False

            if s[i] in hashmap_s and t[i] in hashmap_t:
                if hashmap_s[s[i]]!=hashmap_t[t[i]]:
                    return False
            
            hashmap_s[s[i]],hashmap_t[t[i]]=i,i
        return True
```



### C++

```cpp

```

---



# 整理与总结

1. 

