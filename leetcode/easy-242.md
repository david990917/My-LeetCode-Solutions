---
title: easy-242
tags:
  - LeetCode
description: '有效的字母异位词'
urlname: easy-242
date: 2020-03-16 12:33:23
---

# 题目

https://leetcode-cn.com/problems/valid-anagram/

给定两个字符串 s 和 t ，编写一个函数来判断 t 是否是 s 的字母异位词。

**示例 1:**

```
输入: s = "anagram", t = "nagaram"
输出: true
```


**示例 2:**

```
输入: s = "rat", t = "car"
输出: false
```


说明:
你可以假设字符串只包含小写字母。

**进阶:**
如果输入字符串包含 unicode 字符怎么办？你能否调整你的解法来应对这种情况？

# 解题思路 √

### Python

1. 题意：判断另一个字符串是不是这个字符串打乱一下顺序。

```python
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s)==sorted(t)
```

2. 正常使用hashmap作为计数器


```python
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):return False

        hashmap={}
        for i in s:
            if i in hashmap:
                hashmap[i]+=1
            else:
                hashmap[i]=1

        for j in t:
            if j in hashmap:
                hashmap[j]-=1
                if hashmap[j]<0:
                    return False
            else:
                return False
        
        for key in hashmap:
            if hashmap[key]!=0:
                return False
        return True
```



### C++

```cpp

```

---



# 整理与总结

1. 

