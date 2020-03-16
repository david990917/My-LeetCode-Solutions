---
title: easy-204
tags:
  - LeetCode
description: '计数质数'
urlname: easy-204
date: 2020-03-10 17:11:07
---

# 题目

https://leetcode-cn.com/problems/count-primes/

统计所有小于非负整数 *n* 的质数的数量。

**示例:**

```
输入: 10
输出: 4
解释: 小于 10 的质数一共有 4 个, 它们是 2, 3, 5, 7 。
```

# 解题思路 √

### Python

1. 暴力

```python
class Solution:
    def countPrimes(self, n: int) -> int:
        def isPrime(n):
            for i in range(2,n):
                if n%i==0:
                    return False
            return True

        count=0
        for i in range(2,n):
            count+=isPrime(i)
        return count
```

2. 排除法


```python
class Solution:
    def countPrimes(self, n: int) -> int:
        if n==0 or n==1:return 0
        
        results=[True]*n
        i=2
        while i*i<n:
            if results[i]:
                j=i*i
                while j<n:
                    results[j]=False
                    j+=i
            i+=1
        return sum(results)-2
```



### C++

```cpp

```

---



# 整理与总结

1. 

