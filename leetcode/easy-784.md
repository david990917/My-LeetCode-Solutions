---
title: easy-784
tags:
  - LeetCode
description: ''
urlname: easy-784
date: 2020-03-24 12:24:53
---

# 题目

[字母大小写全排列](https://leetcode-cn.com/problems/letter-case-permutation/)

给定一个字符串S，通过将字符串S中的每个字母转变大小写，我们可以获得一个新的字符串。返回所有可能得到的字符串集合。

示例:

```
输入: S = "a1b2"
输出: ["a1b2", "a1B2", "A1b2", "A1B2"]
```



```
输入: S = "3z4"
输出: ["3z4", "3Z4"]
```



```
输入: S = "12345"
输出: ["12345"]
```


注意：

- S 的长度不超过12。
- S 仅由数字和字母组成。



# 解题思路 √

### Python

1. 

```python
class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        length=len(S)
        self.results=[""]
        
        def searching(S,right):
            char=S[right]
            temp_list=[]
            if char.isalpha():
                for temp in self.results:
                    temp_list.append(char.lower()+temp)
                    temp_list.append(char.upper()+temp)
            else:
                for temp in self.results:
                    temp_list.append(char+temp)
            self.results=temp_list
            
        for right in range(length-1,-1,-1):
            searching(S,right)
       return self.results
```


```python

```



### C++

```cpp

```

---



# 整理与总结

1. 

