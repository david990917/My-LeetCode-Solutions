---
title: easy-412
tags:
  - LeetCode
description: ''
urlname: easy-412
date: 2020-03-23 20:31:06
---

# 题目



写一个程序，输出从 1 到 n 数字的字符串表示。

1. 如果 n 是3的倍数，输出“Fizz”；

2. 如果 n 是5的倍数，输出“Buzz”；

3. 如果 n 同时是3和5的倍数，输出 “FizzBuzz”。

示例：

```
n = 15,

返回:
[
    "1",
    "2",
    "Fizz",
    "4",
    "Buzz",
    "Fizz",
    "7",
    "8",
    "Fizz",
    "Buzz",
    "11",
    "Fizz",
    "13",
    "14",
    "FizzBuzz"
]
```



# 解题思路 √

### Python

1. 直接做

```python
class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        results=[]
        for i in range(1,n+1):
            if i%3==0 and i%5==0:
                results.append("FizzBuzz")
            elif i%3==0:
                results.append("Fizz")
            elif i%5==0:
                results.append("Buzz")
            else:
                results.append(str(i))
        return results
```


```python

```



### C++

```cpp

```

---



# 整理与总结

1. 

