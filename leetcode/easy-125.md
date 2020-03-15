---
title: easy-125
tags:
  - LeetCode
description: ''
urlname: easy-125
date: 2019-08-31 16:25:17
---

# 题目

https://leetcode.com/problems/valid-palindrome/description/

Given a string, determine if it is a palindrome, considering only alphanumeric characters and ignoring cases.

**Note:** For the purpose of this problem, we define empty string as valid palindrome.

**Example 1:**

```
Input: "A man, a plan, a canal: Panama"
Output: true
```

**Example 2:**

```
Input: "race a car"
Output: false
```

# 解题思路 √

这是一道考察回文的题目，而且是最简单的形式，即判断一个字符串是否是回文。

针对这个问题，我们可以使用头尾双指针，

- 如果两个指针的元素不相同，则直接返回false,
- 如果两个指针的元素相同，我们同时更新头尾指针，循环。 直到头尾指针相遇。

时间复杂度为O(n).

拿“noon”这样一个回文串来说，我们的判断过程是这样的：

[![125.valid-palindrome-1](easy-125/125.valid-palindrome-1.png)](https://github.com/azl397985856/leetcode/blob/master/assets/problems/125.valid-palindrome-1.png)

拿“abaa”这样一个不是回文的字符串来说，我们的判断过程是这样的：

[![125.valid-palindrome-2](easy-125/125.valid-palindrome-2.png)](https://github.com/azl397985856/leetcode/blob/master/assets/problems/125.valid-palindrome-2.png)

## 关键点解析

- 双指针

# Python

利用语言特性，直接颠倒顺序

```python
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=''.join(i for i in s if i.isalnum()).lower()
        return s==s[::-1]
```

我的代码

```python
class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s)-1
        while(right>left):
            if not s[left].isalnum():
                left+=1
                continue
            if not s[right].isalnum():
                right-=1
                continue
            if s[left].lower()==s[right].lower():
                left+=1
                right-=1
            else:
                return 0
        return 1
```

标准里面最后的判断是 `return left>=right` ，我觉的没有必要

# 整理与总结

1. **".," **  

   ```python
   ❌错误答案❌
   class Solution:
       def isPalindrome(self, s: str) -> bool:
           left = 0
           right = len(s)-1
           while(right>left):
               while not s[left].isalnum():
                   left+=1
               while not s[right].isalnum():
                   right-=1
               if s[left].lower()==s[right].lower():
                   left+=1
                   right-=1
               else:
                   return 0
           return 1
   ```

   我提交的代码是这样的，这个是错误的。

   遇到都是字符的情况就超出界限了

   - 本来以为这样判断能够更加快速跳过无效的字符，但是有可能超出了外层大循环的判断

   - 如果需要外层大循环的判断那么需要添加 continue

2. 大小写注意到了，有效字符的判断注意到了

3. 自己写的要比直接使用逆置要快

   

