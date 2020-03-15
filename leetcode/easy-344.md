---
title: easy-344
tags:
  - LeetCode
description: '反转字符串'
urlname: easy-344
date: 2020-03-15 17:19:40
---

# 题目

https://leetcode-cn.com/problems/reverse-string

编写一个函数，其作用是将输入的字符串反转过来。输入字符串以字符数组 char[] 的形式给出。

不要给另外的数组分配额外的空间，你必须原地修改输入数组、使用 O(1) 的额外空间解决这一问题。

你可以假设数组中的所有字符都是 ASCII 码表中的可打印字符。 

**示例 1：**

```
输入：["h","e","l","l","o"]
输出：["o","l","l","e","h"]
```

**示例 2：**

```
输入：["H","a","n","n","a","h"]
输出：["h","a","n","n","a","H"]
```



# 解题思路 √

### Python

1. 自身的库

```python
class Solution:
    def reverseString(self, s: List[str]) -> None:
        s.reverse()
```

2. #### 递归

   原地反转字符串不代表了空间复杂度为常数：原地反转字符串是一种不使用辅助数据结构的算法。

   虽然是原地反转，但是空间复杂度却不是常数级空间，因为递归过程中使用了堆栈空间。

   ![在这里插入图片描述](easy-344/aHR0cHM6Ly9waWMubGVldGNvZGUtY24uY29tL0ZpZ3VyZXMvMzQ0L3N0YWNrMi5wbmc.jfif)


```python
class Solution:
    def reverseString(self, s: List[str]) -> None:
        def helper(left,right):
            if left<right:
                s[left],s[right]=s[right],s[left]
                helper(left+1,right-1)
        helper(0,len(s)-1)
```

3. #### 双指针法

```python
class Solution:
    def reverseString(self, s: List[str]) -> None:
        left,right=0,len(s)-1
        while left<right:
            s[left],s[right]=s[right],s[left]
            left+=1
            right-=1
```



### C++

```cpp

```

---



# 整理与总结

1. 

