---
title: easy-7
tags:
  - LeetCode
description: '整数反转'
urlname: easy-7
date: 2020-03-16 12:21:53
---

# 题目

https://leetcode-cn.com/problems/reverse-integer/

给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转。

**示例 1:**

```
输入: 123
输出: 321
```


 **示例 2:**

```
输入: -123
输出: -321
```


**示例 3:**

```
输入: 120
输出: 21
```


**注意:**

假设我们的环境只能存储得下 32 位的有符号整数，则其数值范围为 [−231,  231 − 1]。请根据这个假设，如果反转后整数溢出那么就返回 0。

来源：力扣（LeetCode）
链接：https://leetcode-cn.com/problems/reverse-integer
著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。

# 解题思路 √

### Python

1. 字符串解法

```python
class Solution:
    def reverse(self, x: int) -> int:
        str_num=str(x)[::-1]
        if str_num.endswith('-'):
            str_num='-'+str_num[:-1]
            return int(str_num) if int(str_num)>=-2**31 else 0
        return int(str_num) if int(str_num)<=2**31-1 else 0
```

2. 正常解法


```python
class Solution:
    def reverse(self, x: int) -> int:
        y,result=abs(x),0
        of=2**31-1 if x>0 else 2**31
        while y>0:
            result=result*10+y%10
            if result>of:return 0
            y//=10
        return result if x>0 else -result
```



### C++

```cpp

```

---



# 整理与总结

1. 

