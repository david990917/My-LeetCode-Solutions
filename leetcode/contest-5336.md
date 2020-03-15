---
title: contest-5336
tags:
  - LeetCode
description: '上升下降字符串'
urlname: contest-5336
date: 2020-03-07 22:50:12
---

# 题目

https://leetcode-cn.com/contest/biweekly-contest-21/problems/increasing-decreasing-string/

给你一个字符串 `s` ，请你根据下面的算法重新构造字符串：

1. 从 `s` 中选出 **最小** 的字符，将它 **接在** 结果字符串的后面。
2. 从 `s` 剩余字符中选出 **最小** 的字符，且该字符比上一个添加的字符大，将它 **接在** 结果字符串后面。
3. 重复步骤 2 ，直到你没法从 `s` 中选择字符。
4. 从 `s` 中选出 **最大** 的字符，将它 **接在** 结果字符串的后面。
5. 从 `s` 剩余字符中选出 **最大** 的字符，且该字符比上一个添加的字符小，将它 **接在** 结果字符串后面。
6. 重复步骤 5 ，直到你没法从 `s` 中选择字符。
7. 重复步骤 1 到 6 ，直到 `s` 中所有字符都已经被选过。

在任何一步中，如果最小或者最大字符不止一个 ，你可以选择其中任意一个，并将其添加到结果字符串。

请你返回将 `s` 中字符重新排序后的 **结果字符串** 。

# 解题思路 √

### Python

1. 

```python
class Solution:
    def sortString(self, s: str) -> str:
        length=len(s)
        hashmap={}
        for i in s:
            if i not in hashmap:
                hashmap[i]=1
            else:hashmap[i]+=1
        
        reduced_s=sorted(set([i for i in s]))
        
        result=''
        while reduced_s:
            for i in reduced_s:
                if hashmap[i]>0:
                    result+=i
                    hashmap[i]-=1
            reduced_s=[i for i in reduced_s if hashmap[i]>0]

            for i in reduced_s[::-1]:
                if hashmap[i]>0:
                    result+=i
                    hashmap[i]-=1
            reduced_s=[i for i in reduced_s if hashmap[i]>0]

            
        return result
```


```python

```



### C++

```cpp

```

---



# 整理与总结

1. 原因是用`for`发起任何形式的遍历时，它的遍历顺序都是从最初就确定的

