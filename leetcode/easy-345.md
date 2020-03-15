---
title: easy-345
tags:
  - LeetCode
description: '反转字符串中的元音字母'
urlname: easy-345
date: 2020-03-11 19:21:58
---

# 题目

https://leetcode-cn.com/problems/reverse-vowels-of-a-string/submissions/

> 编写一个函数，以字符串作为输入，反转该字符串中的元音字母。
>
> 示例 1:
>
> 输入: "hello"
> 输出: "holle"
> 示例 2:
>
> 输入: "leetcode"
> 输出: "leotcede"
> 说明:
> 元音字母不包含字母"y"。

# 解题思路 √

### Python

1. 双指针

```python
class Solution:
    def reverseVowels(self, s: str) -> str:
        if len(s)==0 or len(s)==1:return s

        target,s='aeiouAEIOU',list(s)
        left,right=0,len(s)-1
        while left<right:
            if s[left] in target and s[right] in target:
                s[left],s[right]=s[right],s[left]
                right-=1
                left+=1
            else:
                if s[left] in target:right-=1
                elif s[right] in target: left+=1
                else:
                    right-=1
                    left+=1
            
        return ''.join(s)
```


```python

```



### C++

```cpp

```

---



# 整理与总结

1. 

