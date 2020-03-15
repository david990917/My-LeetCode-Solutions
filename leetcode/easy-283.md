---
title: easy-283
tags:
  - LeetCode
description: 'Move Zeroes'
urlname: easy-283
date: 2019-09-01 17:16:49
---

# 题目

https://leetcode.com/problems/move-zeroes/description/

Given an array `nums`, write a function to move all `0`'s to the end of it while maintaining the relative order of the non-zero elements.

**Example:**

```
Input: [0,1,0,3,12]
Output: [1,3,12,0,0]
```

**Note**:

1. You must do this **in-place** without making a copy of the array.
2. Minimize the total number of operations.



# 解题思路 √

如果题目没有要求modify in-place 的话，我们可以先遍历一遍将包含0的和不包含0的存到两个数字， 然后拼接两个数组即可。 但是题目要求modify in-place， 也就是不需要借助额外的存储空间，刚才的方法 空间复杂度是O(n).

那么如果modify in-place呢？ 空间复杂度降低为1。

我们可以借助一个游标记录位置，然后遍历一次，将非0的原地修改，最后补0即可。			

# Python

```python
class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        slow = fast = 0
        while fast < len(nums):
            if nums[fast] != 0:
                nums[slow], nums[fast] = nums[fast], nums[slow]
                slow += 1
            fast += 1
```

同样的意思：

```python
slow=0
for fast in range(len(nums)):
	if nums[fast]!=0:
		nums[slow]=nums[fast]
		slow+=1
for fast in range(slow,len(nums)):
	nums[fast]=0
```



# 整理与总结

1. ```python
   nums[slow],nums[fast]=nums[fast],0 ❌
   ```

   我的第一次代码：错误了

   思考为什么呢？

   ```
   Input		[1]
   
   Output		[0]
   Expected	[1]
   ```

   我强行把他换成0了，实际上

