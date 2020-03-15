---
title: easy-557
tags:
  - LeetCode
description: '反转字符串中的单词 III'
urlname: easy-557
date: 2020-03-15 18:01:42
---

# 题目

https://leetcode-cn.com/problems/reverse-words-in-a-string-iii/

给定一个字符串，你需要反转字符串中每个单词的字符顺序，同时仍保留空格和单词的初始顺序。

**示例 1:**

```
输入: "Let's take LeetCode contest"
输出: "s'teL ekat edoCteeL tsetnoc" 
```


注意：在字符串中，每个单词由单个空格分隔，并且字符串中不会有任何额外的空格。



# 解题思路 √

### Python

1. 很自然能想到使用Python自带的库

```python
class Solution:
    def reverseWords(self, s: str) -> str:
        return ' '.join([i[::-1] for i in s.split(' ')])
```

2. 堆


```python
class Solution:
    def reverseWords(self, s: str) -> str:
        from collections import deque
        deq=deque()
        result=''

        for i in s:
            if i != ' ':
                deq.append(i)
            else:
                while deq:
                    result+=deq.pop()
                result+=' '
        
        while deq:
            result+=deq.pop()
        return result
```



### C++

```cpp

```

---



# 整理与总结

1. 

