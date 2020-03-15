---
title: easy-167
tags:
  - LeetCode
description: 'Two Sum II - Input array is sorted'
urlname: easy-167
date: 2019-08-31 17:12:46
---

# 题目

https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/

Given an array of integers that is already **sorted in ascending order**, find two numbers such that they add up to a specific target number.

The function twoSum should return indices of the two numbers such that they add up to the target, where index1 must be less than index2.

**Note:**

- Your returned answers (both index1 and index2) are not zero-based.
- You may assume that each input would have *exactly* one solution and you may not use the *same* element twice.

**Example:**

```
Input: numbers = [2,7,11,15], target = 9
Output: [1,2]
Explanation: The sum of 2 and 7 is 9. Therefore index1 = 1, index2 = 2.
```

Accepted

# 解题思路 √

由于题目没有对空间复杂度有求，用一个hashmap 存储已经访问过的数字即可。

假如题目空间复杂度有要求，由于数组是有序的，只需要双指针即可。一个left指针，一个right指针， 如果left + right 值 大于target 则 right左移动， 否则left右移。

> 如果数组无序，需要先排序（从这里也可以看出排序是多么重要的操作）
>
> 我们面对的这个数组已经排好序了，所以利用双指针的话节约空间复杂度。
>
> hashmap - > $O(n)$    Ours -> $O(1)$

# Python

hashmap

```python
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        visited = {}
        for index, number in enumerate(numbers):
            if target - number in visited:
                return [visited[target-number], index+1]
            else:
                visited[number] = index + 1
```

双指针

```python
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left,right=0,len(numbers)-1
        while left<right:
            if numbers[left] + numbers[right] < target:
                left+=1
            elif numbers[left] + numbers[right] > target:
                right-=1
            else:return [left+1,right+1]
```



# 整理与总结

1. 双指针最后不用再判断啦，我自己的代码最后还判断了一个返回0
2. 注意输出的时候 实际位置 和 位置代码的区别
3. 和前面一道题目的区别`easy-1`：1的那个题目是没有排序的 + 返回的下标定义不同。

