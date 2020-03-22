---
title: easy-20
tags:
  - LeetCode
description: ''
urlname: easy-20
date: 2020-03-22 20:27:50
---

# 题目

[有效的括号](https://leetcode-cn.com/problems/valid-parentheses/)

给定一个只包括 '('，')'，'{'，'}'，'['，']' 的字符串，判断字符串是否有效。

有效字符串需满足：

左括号必须用相同类型的右括号闭合。
左括号必须以正确的顺序闭合。
注意空字符串可被认为是有效字符串。

示例 1:

```
输入: "()"
输出: true
```


示例 2:

```
输入: "()[]{}"
输出: true
```


示例 3:

```
输入: "(]"
输出: false
```


示例 4:

```
输入: "([)]"
输出: false
```


示例 5:

```
输入: "{[]}"
输出: true
```



# 解题思路 √

### Python

1. 

```python
class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        pairs={'(':')','[':']','{':'}'}
        for char in s:
            if char in pairs:
                stack.append(char)
            else:
                if len(stack)==0:return False
                if pairs[stack[-1]]!=char:return False
                else:stack.pop()
        return len(stack)==0
```


```python

```



### C++

```cpp

```

---



# 整理与总结

1. 

