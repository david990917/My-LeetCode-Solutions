---
title: easy-387
tags:
  - LeetCode
description: ''
urlname: easy-387
date: 2020-03-23 16:59:53
---

# 题目

[字符串中的第一个唯一字符](https://leetcode-cn.com/problems/first-unique-character-in-a-string/)

难度简单193

给定一个字符串，找到它的第一个不重复的字符，并返回它的索引。如果不存在，则返回 -1。

案例:

```
s = "leetcode"
返回 0.

s = "loveleetcode",
返回 2.


注意事项：您可以假定该字符串只包含小写字母。
```




# 解题思路 √

### Python

1. 直接操作就可以解了

```python
class Solution:
    def firstUniqChar(self, s: str) -> int:
        hashmap={}
        for idx,number in enumerate(s):
            if number in hashmap:hashmap[number]+=1
            else:hashmap[number]=1
        for idx,number in enumerate(s):
            if hashmap[number]==1:
                return idx
        return -1
```


```python

```



### C++

```cpp

```

---



# 整理与总结

1. 

