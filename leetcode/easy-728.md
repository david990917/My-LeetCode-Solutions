---
title: easy-728
tags:
  - LeetCode
description: ''
urlname: easy-728
date: 2020-04-05 23:03:40
---

# 题目

[自除数](https://leetcode-cn.com/problems/self-dividing-numbers/)



# 解题思路 √

### Python

1. 

```python
class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        def divideJudge(number):
            factors=[int(i) for i in str(number)]
            if 0 in factors:return False
            for factor in factors:
                if number%factor==0:continue
                else:return False
            return True

        result=[]
        for number in range(left,right+1):
           if divideJudge(number):
               result.append(number)
        return result
```


```python

```



### C++

```cpp

```

---



# 整理与总结

1. 

