---
title: easy-942
tags:
  - LeetCode
description: ''
urlname: easy-942
date: 2020-04-05 23:15:19
---

# 题目

[增减字符串匹配](https://leetcode-cn.com/problems/di-string-match/)



# 解题思路 √

### Python

1. 

```python
class Solution:
    def diStringMatch(self, S: str) -> List[int]:
        length=len(S)
        result=[]
        left,right=0,length
        for char in S:
            if char=='I':
                result.append(left)
                left+=1
            else:
                result.append(right)
                right-=1
        return result+[left]
```


```python

```



### C++

```cpp

```

---



# 整理与总结

1. 

