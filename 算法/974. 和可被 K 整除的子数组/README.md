| [English](README_EN.md) | 简体中文 |

# [974. 和可被 K 整除的子数组](https://leetcode-cn.com/problems/subarray-sums-divisible-by-k)
<p>给定一个整数数组 <code>A</code>，返回其中元素之和可被 <code>K</code>&nbsp;整除的（连续、非空）子数组的数目。</p>

<p>&nbsp;</p>

<p><strong>示例：</strong></p>

<pre><strong>输入：</strong>A = [4,5,0,-2,-3,1], K = 5
<strong>输出：</strong>7
<strong>解释：
</strong>有 7 个子数组满足其元素之和可被 K = 5 整除：
[4, 5, 0, -2, -3, 1], [5], [5, 0], [5, 0, -2, -3], [0], [0, -2, -3], [-2, -3]
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ol>
	<li><code>1 &lt;= A.length &lt;= 30000</code></li>
	<li><code>-10000 &lt;= A[i] &lt;= 10000</code></li>
	<li><code>2 &lt;= K &lt;= 10000</code></li>
</ol>

**标签:**  [数组](https://leetcode-cn.com/tag/array) [哈希表](https://leetcode-cn.com/tag/hash-table) 
 ### 相似题目
- 中等:	[和为K的子数组](https://leetcode-cn.com/problems/subarray-sum-equals-k) 

# 解题思路 √

### Python

1. 使用 hashmap 来存储前缀和

```python
class Solution:
    def subarraysDivByK(self, A: List[int], K: int) -> int:
        hashmap={0:1}
        length=len(A)
        preSum=0
        count=0
        for i in range(length):
            preSum=(preSum+A[i])%K
            count+=hashmap.setdefault(preSum,0)
            if preSum in hashmap:hashmap[preSum]+=1
            else:hashmap[preSum]=1
           
        return count
```


```python

```

### C++

```cpp

```

---



# 整理与总结

1. 