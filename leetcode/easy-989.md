---
title: easy-989
tags:
  - LeetCode
description: '989. 数组形式的整数加法'
urlname: easy-989
date: 2020-03-09 08:52:21
---

# 题目

> 对于非负整数 X 而言，X 的数组形式是每位数字按从左到右的顺序形成的数组。例如，如果 X = 1231，那么其数组形式为 [1,2,3,1]。
>
> 给定非负整数 X 的数组形式 A，返回整数 X+K 的数组形式。
>
>  
>
> 示例 1：
>
> 输入：A = [1,2,0,0], K = 34
> 输出：[1,2,3,4]
> 解释：1200 + 34 = 1234
> 示例 2：
>
> 输入：A = [2,7,4], K = 181
> 输出：[4,5,5]
> 解释：274 + 181 = 455
> 示例 3：
>
> 输入：A = [2,1,5], K = 806
> 输出：[1,0,2,1]
> 解释：215 + 806 = 1021
> 示例 4：
>
> 输入：A = [9,9,9,9,9,9,9,9,9,9], K = 1
> 输出：[1,0,0,0,0,0,0,0,0,0,0]
> 解释：9999999999 + 1 = 10000000000
>
>
> 提示：
>
> 1 <= A.length <= 10000
> 0 <= A[i] <= 9
> 0 <= K <= 10000
> 如果 A.length > 1，那么 A[0] != 0
>
> > 来源：力扣（LeetCode）
> > 链接：https://leetcode-cn.com/problems/add-to-array-form-of-integer
> > 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。



# 解题思路 √

### Python

1. 转换-然后进行操作

```python
class Solution:
    def addToArrayForm(self, A: List[int], K: int) -> List[int]:
        result=0
        for i in A:
            result=result*10+i
        result+=K

        result_list=[]
        if result==0:return [0]
        while result>0:
            result_list.append(result%10)
            result//=10
        return result_list[::-1]
```

2. 使用LIst进行操作


```python
class Solution:
    def addToArrayForm(self, A: List[int], K: int) -> List[int]:
        B=[]
        if K==0: B=[0]
        while K>0:
            B.append(K%10)
            K//=10
        
        A=A[::-1]
        carry,result=0,[]
        while A or B:
            a=A[0] if A else 0
            b=B[0] if B else 0
            value=a+b+carry
            result.append(value%10)
            carry=value//10
            if A:A=A[1:]
            if B:B=B[1:]
        if carry:
            result.append(1)

        return result[::-1]
```



### C++

```cpp

```

---



# 整理与总结

1. 数字的问题一定要注意0开头的问题，单独的0。

