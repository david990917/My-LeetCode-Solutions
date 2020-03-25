---
title: offer-5
tags:
  - LeetCode
description: '替换空格'
urlname: offer-5
date: 2020-03-15 09:27:06
---

# 题目

[替换空格](https://leetcode-cn.com/problems/ti-huan-kong-ge-lcof) 

请实现一个函数，把字符串 s 中的每个空格替换成"%20"。

**示例 1：**

```
输入：s = "We are happy."
输出："We%20are%20happy."
```

**限制：**

0 <= s 的长度 <= 10000

# 解题思路 √

### Python

1. 从后往前

```python
class Solution:
    def replaceSpace(self, s: str) -> str:
        length=len(s)
        result=''
        for i in range(length-1,-1,-1):
            if s[i]!=' ':
                result+=s[i]
            else:
                result+='02%'
        return result[::-1]
```


```python

```



### C++

```cpp

```

---



# 整理与总结

1. 

