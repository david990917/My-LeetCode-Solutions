---
title: medium-524
tags:
  - LeetCode
description: '通过删除字母匹配到字典里最长单词'
urlname: medium-524
date: 2020-03-11 20:21:10
---

# 题目

https://leetcode-cn.com/problems/longest-word-in-dictionary-through-deleting/
给定一个字符串和一个字符串字典，找到字典里面最长的字符串，该字符串可以通过删除给定字符串的某些字符来得到。如果答案不止一个，返回长度最长且字典顺序最小的字符串。如果答案不存在，则返回空字符串。

**示例 1:**

```
输入:
s = "abpcplea", d = ["ale","apple","monkey","plea"]

输出: 
"apple"
```

**示例 2:**

```
输入:
s = "abpcplea", d = ["a","b","c"]

输出: 
"a"
```

**说明:**

1. 所有输入的字符串只包含小写字母。
2. 字典的大小不会超过 1000。
3. 所有输入的字符串长度不会超过 1000。



# 解题思路 √

### Python

1. 双指针移动判断是不是子串。

```python
class Solution:
    def findLongestWord(self, s: str, d: List[str]) -> str:
        def isSubString(s,target):
            index1,index2=0,0
            while index1<len(s) and index2<len(target):
                if s[index1]==target[index2]:
                    index2+=1
                index1+=1
            return index2==len(target)
        
        result=''
        for target in d:
            if len(result)>len(target) or (len(result)==len(target) and result<target):continue
            if isSubString(s, target):
                result=target
        return result
```


```python

```



### C++

```cpp

```

---



# 整理与总结

1. 

