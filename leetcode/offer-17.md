---
title: offer-17
tags:
  - LeetCode
description: ''
urlname: offer-17
date: 2020-03-25 17:37:49
---

# 题目

[打印从1到最大的n位数](https://leetcode-cn.com/problems/da-yin-cong-1dao-zui-da-de-nwei-shu-lcof/)

输入数字 n，按顺序打印出从 1 到最大的 n 位十进制数。比如输入 3，则打印出 1、2、3 一直到最大的 3 位数 999。

示例 1:

```
输入: n = 1
输出: [1,2,3,4,5,6,7,8,9]
```


说明：

```
用返回一个整数列表来代替打印
n 为正整数
```



# 解题思路 √

### Python

1. 直接返回

```python
class Solution:
    def printNumbers(self, n: int) -> List[int]:
        return [i for i in range(1,10**n)]
```

2. 但是不是本题目核心考察的点


```python
class Solution:
    def printNumbers(self, n: int) -> List[int]:
        self.result=[]
        def bfs(temp,length):
            if len(temp)==length:
                if int(temp)==0:return 
                self.result.append(int(temp))
                return
            for i in range(10):
                bfs(temp+str(i),length)
        bfs('',n)
        return self.result
```



### C++

```cpp

```

---



# 整理与总结

1. 

