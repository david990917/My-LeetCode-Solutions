---
title: medium-17
tags:
  - LeetCode
description: '电话号码的字母组合'
urlname: medium-17
date: 2020-03-20 14:43:09
---

# 题目

https://leetcode-cn.com/problems/letter-combinations-of-a-phone-number/

给定一个仅包含数字 `2-9` 的字符串，返回所有它能表示的字母组合。

给出数字到字母的映射如下（与电话按键相同）。注意 1 不对应任何字母。

![img](medium-17/17_telephone_keypad.png)

**示例:**

```
输入："23"
输出：["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
```

**说明:**
尽管上面的答案是按字典序排列的，但是你可以任意选择答案输出的顺序。



# 解题思路 √

### Python

![img](https://pic.leetcode-cn.com/bc9a609acaeb67274452c2d2c6857df57af22950b1a4bd1fa0ccbd4a7fc38d5c-%E5%B9%BB%E7%81%AF%E7%89%871.JPG)

1. 回溯的想法

```python
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:return []
        keys=["abc","def","ghi","jkl","mno","pqrs","tuv","wxyz"]
        combinations=[]

        def doCombinations(prefix,digits):
            if len(prefix)==len(digits):
                combinations.append(prefix)
                return
            currDigit=int(digits[len(prefix)])
            letters=keys[currDigit-2]
            for letter in letters:
                prefix+=letter
                doCombinations(prefix,digits)
                prefix=prefix[:-1]
        
        doCombinations('',digits)
        return combinations
```


```python

```



### C++

```cpp

```

---



# 整理与总结

1. [电话号码的字母组合](https://leetcode-cn.com/problems/letter-combinations-of-a-phone-number/)

   回溯法也是DFS，但是他重要区别就是他常用于解决排列组合的问题，同时递归返回的时候注意`取消`标记。

   如果满足条件就处理并且退出，没有满足条件就继续进行递归运算。

   

