| [English](README_EN.md) | 简体中文 |

# [面试题 17.10. 主要元素](https://leetcode-cn.com/problems/find-majority-element-lcci)
<p>如果数组中多一半的数都是同一个，则称之为主要元素。给定一个<strong>整数</strong>数组，找到它的主要元素。若没有，返回-1。</p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>[1,2,5,9,5,9,5,5,5]
<strong>输出：</strong>5</pre>

<p>&nbsp;</p>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong>[3,2]
<strong>输出：</strong>-1</pre>

<p>&nbsp;</p>

<p><strong>示例 3：</strong></p>

<pre><strong>输入：</strong>[2,2,1,1,1,2,2]
<strong>输出：</strong>2</pre>

<p>&nbsp;</p>

<p><strong>说明：</strong><br>
你有办法在时间复杂度为 O(N)，空间复杂度为 O(1) 内完成吗？</p>

**标签:**  [位运算](https://leetcode-cn.com/tag/bit-manipulation) [数组](https://leetcode-cn.com/tag/array) [分治算法](https://leetcode-cn.com/tag/divide-and-conquer) 
# 解题思路 √

### Python

1. 排序的方法 找到最中间的元素

```python
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        if not nums:return -1
        
        nums.sort()
        length=len(nums)
        mid=(length-1)//2
        return nums[mid]
```

2. 位运算的方法，但是对于 `[-2147483648]` 这个输入无能为力


```python
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        result=0
        length=len(nums)

        for i in range(32):
            count=0
            currBit=1<<i
            for j in range(length):
                if nums[j] & currBit:count+=1
            if count>(length//2):result^=currBit
        return result
```

### C++

```cpp

```

---



# 整理与总结

1. 