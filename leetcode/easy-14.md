---
title: easy-14
tags:
  - LeetCode
description: '最长公共前缀'
urlname: easy-14
date: 2020-03-10 18:05:23
---

# 题目

https://leetcode-cn.com/problems/longest-common-prefix

编写一个函数来查找字符串数组中的最长公共前缀。

如果不存在公共前缀，返回空字符串 ""。

**示例 1:**

```
输入: ["flower","flow","flight"]
输出: "fl"
```


**示例 2:**

```
输入: ["dog","racecar","car"]
输出: ""
解释: 输入不存在公共前缀。
```


**说明:**

所有输入只包含小写字母 a-z 。

# 解题思路 √

### Python

1. 暴力

```python
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs: return ""
        length=min([len(i) for i in strs])
        result=""
        for i in range(length):
            target=strs[0][i]
            flag=True
            for j in range(len(strs)):
                if strs[j][i] != target:                    
                    flag=False
                    return result

            if flag:
                result+=target
        return result
```

2. 差不多的匹配方法


```python
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:return ""

        target=strs[0]
        while target:
            for i in range(len(strs)):
                if strs[i].find(target)!=0:
                    target=target[:-1]
        return target
```



### C++

```cpp

```

---



# 整理与总结

1. 

