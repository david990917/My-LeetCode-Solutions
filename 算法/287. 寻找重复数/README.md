| [English](README_EN.md) | 简体中文 |

# [287. 寻找重复数](https://leetcode-cn.com/problems/find-the-duplicate-number)
<p>给定一个包含&nbsp;<em>n</em> + 1 个整数的数组&nbsp;<em>nums</em>，其数字都在 1 到 <em>n&nbsp;</em>之间（包括 1 和 <em>n</em>），可知至少存在一个重复的整数。假设只有一个重复的整数，找出这个重复的数。</p>

<p><strong>示例 1:</strong></p>

<pre><strong>输入:</strong> <code>[1,3,4,2,2]</code>
<strong>输出:</strong> 2
</pre>

<p><strong>示例 2:</strong></p>

<pre><strong>输入:</strong> [3,1,3,4,2]
<strong>输出:</strong> 3
</pre>

<p><strong>说明：</strong></p>

<ol>
	<li><strong>不能</strong>更改原数组（假设数组是只读的）。</li>
	<li>只能使用额外的 <em>O</em>(1) 的空间。</li>
	<li>时间复杂度小于 <em>O</em>(<em>n</em><sup>2</sup>) 。</li>
	<li>数组中只有一个重复的数字，但它可能不止重复出现一次。</li>
</ol>

**标签:**  [数组](https://leetcode-cn.com/tag/array) [双指针](https://leetcode-cn.com/tag/two-pointers) [二分查找](https://leetcode-cn.com/tag/binary-search) 
 ### 相似题目
- 困难:	[缺失的第一个正数](https://leetcode-cn.com/problems/first-missing-positive) 
- 简单:	[只出现一次的数字](https://leetcode-cn.com/problems/single-number) 
- 中等:	[环形链表 II](https://leetcode-cn.com/problems/linked-list-cycle-ii) 
- 简单:	[缺失数字](https://leetcode-cn.com/problems/missing-number) 
- 简单:	[错误的集合](https://leetcode-cn.com/problems/set-mismatch) 

# 解题思路 √

### Python

1. 把nums想象成一根绳子，重复的值会在连接到前面的点（形成一些环）。

   假设有一个环。环的入口为m（所求），周长为c,  快指针在绳上走2n步，慢指针走n步相遇了。

   快指针多走的n步是在环里转圈，且刚好转够整数圈，所以n%c=0, 这时候慢指针在环里走了 n-m 步，新建find指针从0开始走，走到环口为m步，而慢针刚好走了n-m+m=n步，环周长的整数倍

   **慢针进环是在结合点，转够整数圈一定还在结合点，也就是重复值）**

```python
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        slow, fast = 0, 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]

            if slow == fast:
                break
            
        find = 0
        while True:
            find = nums[find]
            slow = nums[slow]
            if find == slow:
                return find
```


```python

```

### C++

1. 和上面的 1 相同的计算方法

```cpp
class Solution {
public:
	int findDuplicate(vector<int>& nums) {
		int slow = 0, fast = 0;
		while (true) {
			slow = nums[slow];
			fast = nums[nums[fast]];
			if (slow == fast) { break; }
		}

		int find = 0;
		while (find != slow) {
			find = nums[find];
			slow = nums[slow];
		}
		return find;
	}
};
```

---



# 整理与总结

1. 