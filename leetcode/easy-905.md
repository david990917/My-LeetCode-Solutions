---
title: easy-905
tags:
  - LeetCode
description: 'Sort Array By Parity'
urlname: easy-905
date: 2019-09-19 21:20:03
---

# 题目

Given an array `A` of non-negative integers, return an array consisting of all the even elements of `A`, followed by all the odd elements of `A`.

You may return any answer array that satisfies this condition.

 

**Example 1:**

```
Input: [3,1,2,4]
Output: [2,4,3,1]
The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be accepted.
```

 

**Note:**

1. `1 <= A.length <= 5000`
2. `0 <= A[i] <= 5000`



# 解题思路 √

Python 就是可以直接拆分然后接在后面。没有考虑具体的实现和解决的思路。

双指针的方法就是我觉得可以的方法：

1. 头尾双指针
2. 出现交换情况就处理交换。
3. 指针的移动和处理交换相互独立编程。
   - i 奇数的时候等一下，偶数的时候直接冲
   - j 偶数的时候等一下，奇数的时候直接冲
   - 先把基础的 i+1，j-1 写好，然后再分别对于奇偶性加以变换。

C++ 的解法也很精巧（很简单的题目啦）直接把偶数交换到前面去就🆗

不会存在把前面的偶数交换到后面去的情况，代码其实就是说明了，index位置指的就是已识别偶数的下一位，然后交换就完事儿了



# Python

```python
class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        if not A:
            return None
        return [i for i in A if i%2==0]+[i for i in A if i%2==1]
```

双指针

```python
class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        if not A:
            return None
        i, j = 0 , len(A)-1
        while i < j:
            if A[i]%2==1 and A[j]%2==0:
                A[i],A[j]=A[j],A[i]
            i = i + 1 - A[i]%2
            j = j - 1 -(A[j]%2-1)
        return A
```

# C++

```c++
class Solution {
public:
    vector<int> sortArrayByParity(vector<int>& A) {
        int index = 0;
        for(int i = 0; i < A.size(); i++)
	        if(A[i] % 2 == 0)   swap(A[index++], A[i]);
        return A;
    }
};
```



# 整理与总结

1. 指针的移动和交换奇偶相互独立，是很新奇的操作。
2. 对我而言，记住了双指针的设置。一般可以是头尾指针。

