---
title: easy-680
tags:
  - LeetCode
description: '验证回文字符串 Ⅱ'
urlname: easy-680
date: 2020-03-11 19:35:58
---

# 题目

https://leetcode-cn.com/problems/valid-palindrome-ii/

> 给定一个非空字符串 s，最多删除一个字符。判断是否能成为回文字符串。
>
> 示例 1:
>
> 输入: "aba"
> 输出: True
> 示例 2:
>
> 输入: "abca"
> 输出: True
> 解释: 你可以删除c字符。
> 注意:
>
> 字符串只包含从 a-z 的小写字母。字符串的最大长度是50000。
>



# 解题思路 √

### Python

1. #### 头尾指针 - 超时了但是没错

```python
class Solution:
    def validPalindrome(self, s: str) -> bool:
        def isPalindrome(s):
            length=len(s)
            if length==0 or length==1:return True
            return isPalindrome(s[1:-1]) and s[0]==s[-1]
        
        length=len(s)        
        left,right=0,length-1
        while left<right:
            if s[left]!=s[right]:
                return isPalindrome(s[left:right]) or isPalindrome(s[left+1:right+1])
            left+=1
            right-=1
        return True
```




### C++

```cpp

```

---



# 整理与总结

1. 

