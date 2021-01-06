| [English](README_EN.md) | 简体中文 |

# [239. 滑动窗口最大值](https://leetcode-cn.com/problems/sliding-window-maximum)
<p>给你一个整数数组 <code>nums</code>，有一个大小为 <code>k</code><em> </em>的滑动窗口从数组的最左侧移动到数组的最右侧。你只可以看到在滑动窗口内的 <code>k</code> 个数字。滑动窗口每次只向右移动一位。</p>

<p>返回滑动窗口中的最大值。</p>

<p> </p>

<p><strong>示例 1：</strong></p>

<pre>
<b>输入：</b>nums = [1,3,-1,-3,5,3,6,7], k = 3
<b>输出：</b>[3,3,5,5,6,7]
<b>解释：</b>
滑动窗口的位置                最大值
---------------               -----
[1  3  -1] -3  5  3  6  7       <strong>3</strong>
 1 [3  -1  -3] 5  3  6  7       <strong>3</strong>
 1  3 [-1  -3  5] 3  6  7      <strong> 5</strong>
 1  3  -1 [-3  5  3] 6  7       <strong>5</strong>
 1  3  -1  -3 [5  3  6] 7       <strong>6</strong>
 1  3  -1  -3  5 [3  6  7]      <strong>7</strong>
</pre>

<p><strong>示例 2：</strong></p>

<pre>
<b>输入：</b>nums = [1], k = 1
<b>输出：</b>[1]
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<b>输入：</b>nums = [1,-1], k = 1
<b>输出：</b>[1,-1]
</pre>

<p><strong>示例 4：</strong></p>

<pre>
<b>输入：</b>nums = [9,11], k = 2
<b>输出：</b>[11]
</pre>

<p><strong>示例 5：</strong></p>

<pre>
<b>输入：</b>nums = [4,-2], k = 2
<b>输出：</b>[4]</pre>

<p> </p>

<p><b>提示：</b></p>

<ul>
	<li><code>1 <= nums.length <= 10<sup>5</sup></code></li>
	<li><code>-10<sup>4</sup> <= nums[i] <= 10<sup>4</sup></code></li>
	<li><code>1 <= k <= nums.length</code></li>
</ul>

**标签:**  [堆](https://leetcode-cn.com/tag/heap) [None](https://leetcode-cn.com/tag/sliding-window) 
 ### 相似题目
- 困难:	[最小覆盖子串](https://leetcode-cn.com/problems/minimum-window-substring) 
- 简单:	[最小栈](https://leetcode-cn.com/problems/min-stack) 
- 中等:	[至多包含两个不同字符的最长子串](https://leetcode-cn.com/problems/longest-substring-with-at-most-two-distinct-characters) 
- 困难:	[粉刷房子 II](https://leetcode-cn.com/problems/paint-house-ii) 

# 解题思路 √

### Python

1. 使用优先级队列，比较直接的思路

```python
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        n = len(nums)
        # 注意 Python 默认的优先队列是小根堆
        q = [(-nums[i], i) for i in range(k)]
        heapq.heapify(q)

        ans = [-q[0][0]]
        for i in range(k, n):
            heapq.heappush(q, (-nums[i], i))
            while q[0][1] <= i - k: # 栈顶元素的位置
                heapq.heappop(q)
            ans.append(-q[0][0])
        
        return ans
```


```python

```

### C++

```cpp

```

---



# 整理与总结

1. 