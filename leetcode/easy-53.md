---
title: easy-53
tags:
  - LeetCode
description: 'Maximum Subarray'
urlname: easy-53
date: 2019-08-30 18:04:57
---

# 题目

https://leetcode.com/problems/maximum-subarray/

Given an integer array `nums`, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

**Example:**

```
Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
```

**Follow up:**

If you have figured out the O(*n*) solution, try coding another solution using the divide and conquer approach, which is more subtle.

# 思路

这道题求解连续最大子序列和，以下从时间复杂度角度分析不同的解题思路。

#### 解法一 - 暴力解 （暴力出奇迹， 噢耶！）√

一般情况下，先从暴力解分析，然后再进行一步步的优化。

**原始暴力解：**（超时）

求子序列和，那么我们要知道子序列的首尾位置，然后计算首尾之间的序列和。用2个for循环可以枚举所有子序列的首尾位置。 然后用一个for循环求解序列和。这里时间复杂度太高，`O(n^3)`.

#### 复杂度分析

- *时间复杂度：* `O(n^3) - n 是数组长度`
- *空间复杂度：* `O(1)`

#### 解法二 - 前缀和 + 暴力解

**优化暴力解：** (震惊，居然AC了）

在暴力解的基础上，用前缀和我们可以优化到暴力解`O(n^2)`, 这里以空间换时间。 这里可以使用原数组表示`prefixSum`, 省空间。

求序列和可以用前缀和（`prefixSum`) 来优化，给定子序列的首尾位置`（l, r),` 那么序列和 `subarraySum=prefixSum[r] - prefixSum[l - 1];` 用一个全局变量`maxSum`, 比较每次求解的子序列和，`maxSum = max(maxSum, subarraySum)`.

#### 复杂度分析

- *时间复杂度：* `O(n^2) - n 是数组长度`
- *空间复杂度：* `O(n) - prefixSum 数组空间为n`

> 如果用更改原数组表示前缀和数组，空间复杂度降为`O(1)`

但是时间复杂度还是太高，还能不能更优化。答案是可以，前缀和还可以优化到`O(n)`.

#### 解法三 - 优化前缀和 

我们定义函数` S(i)` ，它的功能是计算以 `0（包括 0）`开始加到 `i（包括 i）`的值。

那么 `S(j) - S(i - 1)` 就等于 从 `i` 开始（包括 i）加到 `j`（包括 j）的值。

我们进一步分析，实际上我们只需要遍历一次计算出所有的 `S(i)`, 其中 `i = 0,1,2....,n-1。` 然后我们再减去之前的`S(k)`,其中 `k = 0，1，i - 1`，中的最小值即可。 因此我们需要 用一个变量来维护这个最小值，还需要一个变量维护最大值。

#### 复杂度分析

- *时间复杂度：* `O(n) - n 是数组长度`
- *空间复杂度：* `O(1)`

#### 解法四 - [分治法](https://www.wikiwand.com/zh-hans/分治法)

我们把数组`nums`以中间位置（`m`)分为左（`left`)右(`right`)两部分. 那么有， `left = nums[0]...nums[m - 1]` 和 `right = nums[m + 1]...nums[n-1]`

最大子序列和的位置有以下三种情况：

1. 考虑中间元素`nums[m]`, 跨越左右两部分，这里从中间元素开始，往左求出后缀最大，往右求出前缀最大, 保持连续性。
2. 不考虑中间元素，最大子序列和出现在左半部分，递归求解左边部分最大子序列和
3. 不考虑中间元素，最大子序列和出现在右半部分，递归求解右边部分最大子序列和

分别求出三种情况下最大子序列和，三者中最大值即为最大子序列和。

举例说明，如下图： 

[![maximum subarray sum divide conquer](easy-53/53.maximum-sum-subarray-divideconquer.png)](https://github.com/azl397985856/leetcode/blob/master/assets/problems/53.maximum-sum-subarray-divideconquer.png)

#### 复杂度分析

- *时间复杂度：* `O(nlogn) - n 是数组长度`
- *空间复杂度：* `O(1)`

#### 解法五 - [动态规划](https://www.wikiwand.com/zh-hans/动态规划) √

动态规划的难点在于找到状态转移方程，

```
dp[i] - 表示到当前位置 i 的最大子序列和
```

状态转移方程为： `dp[i] = max(dp[i - 1] + nums[i], nums[i])`

初始化：`dp[0] = nums[0]`

从状态转移方程中，我们只关注前一个状态的值，所以不需要开一个数组记录位置所有子序列和，只需要两个变量，

```
currMaxSum - 累计最大和到当前位置i
```

`maxSum - 全局最大子序列和`:

- `currMaxSum = max(currMaxSum + nums[i], nums[i])`
- `maxSum = max(currMaxSum, maxSum)`

如图： 

[![maximum subarray sum dp](easy-53/53.maximum-sum-subarray-dp.png)](https://github.com/azl397985856/leetcode/blob/master/assets/problems/53.maximum-sum-subarray-dp.png)

#### 复杂度分析

- *时间复杂度:* `O(n) - n 是数组长度`
- *空间复杂度:* `O(1)`

## 关键点分析

1. 暴力解，列举所有组合子序列首尾位置的组合，求解最大的子序列和, 优化可以预先处理，得到前缀和
2. 分治法，每次从中间位置把数组分为左右中三部分， 分别求出左右中（这里中是包括中间元素的子序列）最大和。对左右分别深度递归，三者中最大值即为当前最大子序列和。
3. 动态规划，找到状态转移方程，求到当前位置最大和。

# Python

### 暴力法-超时了。。。

```python
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        
        lenth=len(nums)
        comp=0
        for i in range(0,lenth):
            comp+=nums[i]
        for i in range(0,lenth):
            for j in range(i,lenth):
                sum=0
                result=[]
                for k in range(i,j+1):
                    sum+=nums[k]
                if sum > comp:
                    comp=sum
                    for k in range(i,j+1):
                        result.append(nums[k])
                    print(result)
                    
        return comp
```

### 动态规划

```python
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        currMaxSum=maxSum=nums[0]
        for i in range(1,len(nums)):
            currMaxSum=max(nums[i]+currMaxSum,nums[i])
            maxSum=max(currMaxSum,maxSum)
        return maxSum
```



# 整理与总结

1. 第一次提交错误

   总忘记操作的是数组的元素 nums[i]

2. 第二次提交错误

   是因为没有考虑负值输入的问题  [-1]

   **考虑：**我把初始值设定为所有的加和

   ```python
   class Solution:
       def maxSubArray(self, nums: List[int]) -> int:
           
           lenth=len(nums)
           comp=0
           for i in range(0,lenth):
               for j in range(i,lenth):
                   sum=0
                   result=[]
                   for k in range(i,j+1):
                       sum+=nums[k]
                   if sum > comp:
                       comp=sum
                       for k in range(i,j+1):
                           result.append(nums[k])
                       print(result)
                       
           return comp
   ```

3. 理解动态规划-状态转移方程

   要是你之前还没有我从0开始好，那我们就没必要继续了。

   使用这个方法比使用 条件语句 判断要好，因为判断完还需要赋值
   - 不用 ide，手动在 LeetCode 上面编程吧。

   - ```python
     curr_max=all_max=0
     ```

     上面是我写的错误的，下面是标准的。

     我的代码初始化条件认识不足。

     ```python
     max_sum_ending_curr_index = max_sum = nums[0]
     ```

   - ```python
     for i in range(n):
     ```

     上面是我写的错误的，下面是正确的

     原因是初始化的时候使用了第0个元素，应该直接从后面处理

     ```python
     for i in range(1, n):
     ```

     

