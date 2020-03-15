---
title: easy-13
tags:
  - LeetCode
description: '罗马数字转整数'
urlname: easy-13
date: 2020-03-15 17:03:40
---

# 题目

罗马数字包含以下七种字符: I， V， X， L，C，D 和 M。

```
字符          数值
I             1
V             5
X             10
L             50
C             100
D             500
M             1000
```


例如， 罗马数字 2 写做 II ，即为两个并列的 1。12 写做 XII ，即为 X + II 。 27 写做  XXVII, 即为 XX + V + II 。

通常情况下，罗马数字中小的数字在大的数字的右边。但也存在特例，例如 4 不写做 IIII，而是 IV。数字 1 在数字 5 的左边，所表示的数等于大数 5 减小数 1 得到的数值 4 。同样地，数字 9 表示为 IX。这个特殊的规则只适用于以下六种情况：

- I 可以放在 V (5) 和 X (10) 的左边，来表示 4 和 9。
- X 可以放在 L (50) 和 C (100) 的左边，来表示 40 和 90。 
- C 可以放在 D (500) 和 M (1000) 的左边，来表示 400 和 900。

给定一个罗马数字，将其转换成整数。输入确保在 1 到 3999 的范围内。

**示例 1:**

```
输入: "III"
输出: 3
```


**示例 2:**

```
输入: "IV"
输出: 4
```


**示例 3:**

```
输入: "IX"
输出: 9
```


**示例 4:**

```
输入: "LVIII"
输出: 58
解释: L = 50, V= 5, III = 3.
```


**示例 5:**

```
输入: "MCMXCIV"
输出: 1994
解释: M = 1000, CM = 900, XC = 90, IV = 4.
```



# 解题思路 √

### Python

1. 通过观察我们发现，只有在遇到特殊情况时，两个字符中左边的字符小于右边的字符，且等于右边的字符代表的数减左边字符代表的数。 比如 CM 等于 `1000 - 100`，XC 等于 `100 - 10`...

   因此，我们将 字符：数值 存在 `Roman2Int` 的哈希表中。然后从左到右遍历每个字符，如果 `s[i] < s[i+1]`，就将结果减去 s[i] 代表的数字；否则，将结果加上 s[i] 代表的数字。


```python
class Solution:
    def romanToInt(self, s: str) -> int:
        hashdict={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
        length,value=len(s),0
        for i in range(length-1):
            if hashdict[s[i+1]]>hashdict[s[i]]:
                value-=hashdict[s[i]]
            else:value+=hashdict[s[i]]
        return value+hashdict[s[-1]]
```

2. Trick的方法：

   遍历经过 IVIV 的时候先记录 I 的对应值 1 再往前移动一步记录 IV 的值 3，加起来正好是 IV 的真实值 4。max 函数在这里是为了防止遍历第一个字符的时候出现 [-1:0][−1:0] 的情况



```python
class Solution:
    def romanToInt(self, s: str) -> int:
        d = {'I':1, 'IV':3, 'V':5, 'IX':8, 'X':10, 'XL':30, 'L':50, 'XC':80, 'C':100, 'CD':300, 'D':500, 'CM':800, 'M':1000}
        return sum(d.get(s[max(i-1, 0):i+1], d[n]) for i, n in enumerate(s))
```



### C++

```cpp

```

---



# 整理与总结

1. 

