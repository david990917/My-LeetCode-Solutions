| [English](README_EN.md) | 简体中文 |

# [628. 三个数的最大乘积](https://leetcode-cn.com/problems/maximum-product-of-three-numbers)
<p>给定一个整型数组，在数组中找出由三个数组成的最大乘积，并输出这个乘积。</p>

<p><strong>示例 1:</strong></p>

<pre>
<strong>输入:</strong> [1,2,3]
<strong>输出:</strong> 6
</pre>

<p><strong>示例 2:</strong></p>

<pre>
<strong>输入:</strong> [1,2,3,4]
<strong>输出:</strong> 24
</pre>

<p><strong>注意:</strong></p>

<ol>
	<li>给定的整型数组长度范围是[3,10<sup>4</sup>]，数组中所有的元素范围是[-1000, 1000]。</li>
	<li>输入的数组中任意三个数的乘积不会超出32位有符号整数的范围。</li>
</ol>

**标签:**  [数组](https://leetcode-cn.com/tag/array) [数学](https://leetcode-cn.com/tag/math) 
 ### 相似题目
- 中等:	[乘积最大子数组](https://leetcode-cn.com/problems/maximum-product-subarray) 

# 解题思路 √

### Python

1. 以前的做法

```python
class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        max1,max2,max3=-1001,-1001,-1001
        min1,min2=1001,1001
        for target in nums:
            # 重复的情况需要考虑
            if target>max1:
                max3,max2,max1=max2,max1,target
            elif target>max2:
                max3,max2=max2,target
            elif target > max3:
                max3=target
            
            #大小比较是两套系统
            if target<min1:
                min1,min2=target,min1
            elif target <min2:
                min2=target
        return max(max1*max2*max3,min1*min2*max1)
```

2. 现在的做法：直接比较里面大小情况


```python
class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        nums=sorted(nums)
        max0=nums[-1]*nums[-2]*nums[-3]
        max1=nums[0]*nums[1]*nums[2]
        max2=nums[0]*nums[1]*nums[-1]
        return max(max0,max1,max2)
```

### C++

```cpp

```

---



# 整理与总结

1. 