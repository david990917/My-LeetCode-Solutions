---
title: easy-202
tags:
  - LeetCode
description: ''
urlname: easy-202
date: 2020-03-10 16:57:32
---

# 题目

> 编写一个算法来判断一个数是不是“快乐数”。
>
> 一个“快乐数”定义为：对于一个正整数，每一次将该数替换为它每个位置上的数字的平方和，然后重复这个过程直到这个数变为 1，也可能是无限循环但始终变不到 1。如果可以变为 1，那么这个数就是快乐数。
>
> 示例: 
>
> 输入: 19
> 输出: true
> 解释: 
> 12 + 92 = 82
> 82 + 22 = 68
> 62 + 82 = 100
> 12 + 02 + 02 = 1
>
> 来源：力扣（LeetCode）
> 链接：https://leetcode-cn.com/problems/happy-number
> 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。



# 解题思路 √

解决无限循环的问题就是使用快慢指针。

### Python

1. 快慢指针

```python
class Solution:
    def isHappy(self, n: int) -> bool:
        left=sum([int(i)*int(i) for i in str(n)])
        right=sum([int(i)*int(i) for i in str(left)])
        if left==1 or right==1:return True

        while left!=right:
            left=sum([int(i)*int(i) for i in str(left)])
            right=sum([int(i)*int(i) for i in str(right)])
            right=sum([int(i)*int(i) for i in str(right)])
            if right==1 or left==1:
                return True
        return False
```


```python

```



### C++

```cpp

```

---



# 整理与总结

1. 

