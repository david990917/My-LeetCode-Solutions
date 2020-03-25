---
title: offer-19
tags:
  - LeetCode
description: ''
urlname: offer-19
date: 2020-03-25 22:05:37
---

# 题目

[正则表达式匹配](https://leetcode-cn.com/problems/zheng-ze-biao-da-shi-pi-pei-lcof/)

请实现一个函数用来匹配包含'. '和'*'的正则表达式。模式中的字符'.'表示任意一个字符，而'*'表示它前面的字符可以出现任意次（含0次）。在本题中，匹配是指字符串的所有字符匹配整个模式。例如，字符串"aaa"与模式"a.a"和"ab*ac*a"匹配，但与"aa.a"和"ab*a"均不匹配。

示例 1:

```
输入:
s = "aa"
p = "a"
输出: false
解释: "a" 无法匹配 "aa" 整个字符串。
```


示例 2:

```
输入:
s = "aa"
p = "a*"
输出: true
解释: 因为 '*' 代表可以匹配零个或多个前面的那一个元素, 在这里前面的元素就是 'a'。因此，字符串 "aa" 可被视为 'a' 重复了一次。
```


示例 3:

```
输入:
s = "ab"
p = ".*"
输出: true
解释: ".*" 表示可匹配零个或多个（'*'）任意字符（'.'）。
```


示例 4:

```
输入:
s = "mississippi"
p = "mis*is*p*."
输出: false
s 可能为空，且只包含从 a-z 的小写字母。
p 可能为空，且只包含从 a-z 的小写字母，以及字符 . 和 *。
```



# 解题思路 √

### Python

1. Python自己的正则匹配

```python
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        return True if re.match("^"+p+"$",s) else False
```

2. 二维数组的动态规划

定义一个二维数组`dp`，`dp[i][j]`表示`s`的前`i`个字符和`p`的前`j`个字符是匹配的

`dp[i][j]`的计算方式如下:

- 首先设置`dp[0][0]`为true，因为两个空字符是匹配的
- 如果`i = 0`, 那么表示以空字符串去匹配p的前`j`个字符，我们期望`p[j] == `, 这样之前的字符不用出现，`dp[i][j] = p[j] == * `and `dp[i][j-2]`
- 如果`s[i] == p[j]`那么，直接看`i-1`, 和`j-1`是不是匹配的，`dp[i][j]` = `dp[i-1][j-1]`
- 最后就是需要处理的情况，有两种选择，重复前字符一次，或者不要这个字符，只要其中一个能匹配就行。
  - 不要前一个字符， `dp[i][j-2]`
  - 重复一次，需要满足条件`p[j-1] == s[i]` 或者`p[j-1] == '.'`,`dp[i-1][j]`

最后返回`dp[m][n]`就是能不能匹配的结果


```python
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        s, p = '#'+s, '#'+p
        m, n = len(s), len(p)
        dp = [[False for _ in range(n)] for __ in range(m)]
        dp[0][0] = True
        
        for i in range(m):
            for j in range(1, n):
                if i == 0:
                    dp[i][j] = j > 1 and p[j] == '*' and dp[i][j-2]
                elif p[j] in [s[i], '.']:
                    dp[i][j] = dp[i-1][j-1]
                elif p[j] == '*':
                    dp[i][j] = j > 1 and dp[i][j-2] or p[j-1] in [s[i], '.'] and dp[i-1][j]
                else:
                    dp[i][j] = False
        return dp[-1][-1]
```



### C++

```cpp

```

---



# 整理与总结

1. 

