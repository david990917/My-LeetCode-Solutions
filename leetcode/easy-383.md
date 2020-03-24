---
title: easy-383
tags:
  - LeetCode
description: ''
urlname: easy-383
date: 2020-03-24 11:52:50
---

# 题目

[赎金信](https://leetcode-cn.com/problems/ransom-note/)

给定一个赎金信 (ransom) 字符串和一个杂志(magazine)字符串，判断第一个字符串ransom能不能由第二个字符串magazines里面的字符构成。如果可以构成，返回 true ；否则返回 false。

(题目说明：为了不暴露赎金信字迹，要从杂志上搜索各个需要的字母，组成单词来表达意思。)

注意：

你可以假设两个字符串均只含有小写字母。

- canConstruct("a", "b") -> false
- canConstruct("aa", "ab") -> false
- canConstruct("aa", "aab") -> true

# 解题思路 √

### Python

1. 下次可以锻炼检查一下-然后再提交

```python
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        hashmap={}
        for char in magazine:
            if char in hashmap:hashmap[char]+=1
            else:hashmap[char]=1
        for char in ransomNote:
            if char in hashmap:
                hashmap[char]-=1
                if hashmap[char]==0:
                    del hashmap[char]
            else:
                return False
        return True
```


```python

```



### C++

```cpp

```

---



# 整理与总结

1. 

