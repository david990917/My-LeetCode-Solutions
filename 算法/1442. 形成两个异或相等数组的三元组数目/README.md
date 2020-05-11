| [English](README_EN.md) | 简体中文 |

# [1442. 形成两个异或相等数组的三元组数目](https://leetcode-cn.com/problems/count-triplets-that-can-form-two-arrays-of-equal-xor)
<p>给你一个整数数组 <code>arr</code> 。</p>

<p>现需要从数组中取三个下标 <code>i</code>、<code>j</code> 和 <code>k</code> ，其中 <code>(0 &lt;= i &lt; j &lt;= k &lt; arr.length)</code> 。</p>

<p><code>a</code> 和 <code>b</code> 定义如下：</p>

<ul>
	<li><code>a = arr[i] ^ arr[i + 1] ^ ... ^ arr[j - 1]</code></li>
	<li><code>b = arr[j] ^ arr[j + 1] ^ ... ^ arr[k]</code></li>
</ul>

<p>注意：<strong>^</strong> 表示 <strong>按位异或</strong> 操作。</p>

<p>请返回能够令 <code>a == b</code> 成立的三元组 (<code>i</code>, <code>j</code> , <code>k</code>) 的数目。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>arr = [2,3,1,6,7]
<strong>输出：</strong>4
<strong>解释：</strong>满足题意的三元组分别是 (0,1,2), (0,2,2), (2,3,4) 以及 (2,4,4)
</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong>arr = [1,1,1,1,1]
<strong>输出：</strong>10
</pre>

<p><strong>示例 3：</strong></p>

<pre><strong>输入：</strong>arr = [2,3]
<strong>输出：</strong>0
</pre>

<p><strong>示例 4：</strong></p>

<pre><strong>输入：</strong>arr = [1,3,5,7,9]
<strong>输出：</strong>3
</pre>

<p><strong>示例 5：</strong></p>

<pre><strong>输入：</strong>arr = [7,11,12,9,5,2,7,17,22]
<strong>输出：</strong>8
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= arr.length &lt;= 300</code></li>
	<li><code>1 &lt;= arr[i] &lt;= 10^8</code></li>
</ul>

**标签:**  [位运算](https://leetcode-cn.com/tag/bit-manipulation) [数组](https://leetcode-cn.com/tag/array) [数学](https://leetcode-cn.com/tag/math) 
# 解题思路 √

### Python

1. 我自己想出来的 DP，我觉得还不错 - **重点是对于异或数组的建立，坐标需要思考**

```python
class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        length=len(arr)
        tmp=[[0 for i in range(length)]for j in range(length)]
        for i in range(length):tmp[i][i]=arr[i]
        for i in range(length):
            for j in range(i+1,length):
                tmp[i][j]=tmp[i][j-1]^arr[j]
                
        count=0
        def helper(i,j):
            count=0
            for k in range(i+1,j+1):
                left = tmp[i][k-1]
                right= tmp[k][j]
                if left==right:
                    count+=1
            return count
                    
        for i in range(length):
            for j in range(i,length):
                if tmp[i][j]==0:
                    count+=helper(i,j)
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