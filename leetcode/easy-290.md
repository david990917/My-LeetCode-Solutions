---
title: easy-290
tags:
  - LeetCode
description: ''
urlname: easy-290
date: 2020-03-24 12:40:32
---

# 题目

[单词规律](https://leetcode-cn.com/problems/word-pattern/)

给定一种规律 pattern 和一个字符串 str ，判断 str 是否遵循相同的规律。

这里的 遵循 指完全匹配，例如， pattern 里的每个字母和字符串 str 中的每个非空单词之间存在着双向连接的对应规律。

示例1:

```
输入: pattern = "abba", str = "dog cat cat dog"
输出: true
```


示例 2:

```
输入:pattern = "abba", str = "dog cat cat fish"
输出: false
```


示例 3:

```
输入: pattern = "aaaa", str = "dog cat cat dog"
输出: false
```


示例 4:

```
输入: pattern = "abba", str = "dog dog dog dog"
输出: false
说明:
你可以假设 pattern 只包含小写字母， str 包含了由单个空格分隔的小写字母。    
```



# 解题思路 √

### Python

1. 双向的对应关系

```python
class Solution:
    def wordPattern(self, pattern: str, str: str) -> bool:
        def compare(a,b):
            if len(a)!=len(b):return False
            hashmap={}
            for i in range(len(a)):
                if a[i] not in hashmap:
                    hashmap[a[i]]=b[i]
                else:
                    if hashmap[a[i]]!=b[i]:
                        return False
            return True
        str=str.split()
        return compare(pattern,str) and compare(str,pattern)
```


```python

```



### C++

```cpp

```

---



# 整理与总结

1. 

