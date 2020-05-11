| [English](README_EN.md) | 简体中文 |

# [面试题 17.04. 消失的数字](https://leetcode-cn.com/problems/missing-number-lcci)
<p>数组<code>nums</code>包含从<code>0</code>到<code>n</code>的所有整数，但其中缺了一个。请编写代码找出那个缺失的整数。你有办法在O(n)时间内完成吗？</p>

<p><strong>注意：</strong>本题相对书上原题稍作改动</p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>[3,0,1]
<strong>输出：</strong>2</pre>

<p>&nbsp;</p>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong>[9,6,4,2,3,5,7,0,1]
<strong>输出：</strong>8
</pre>

**标签:**  [位运算](https://leetcode-cn.com/tag/bit-manipulation) [数组](https://leetcode-cn.com/tag/array) [数学](https://leetcode-cn.com/tag/math) 
# 解题思路 √

### Python

1. 

```python

```


```python

```

### C++

1. 直觉操作使用 `hashset`，学习了 `unordered_set` 更新在语雀上了

```cpp
class Solution {
public:
    int missingNumber(vector<int>& nums) {
        int length = nums.size();
        unordered_set<int> hashset;
        for (int i = 0; i <= length; i++) { hashset.insert(i); }
        for (int i = 0; i < length; i++) {
            auto iter = hashset.find(nums[i]);
            hashset.erase(iter);
        }
        return *hashset.begin();
    }
};
```

2. 做差

```cpp
class Solution {
public:
	int missingNumber(vector<int>& nums) {
		int length = nums.size();
		int sum = 0;
		int totalSum = length * (length + 1) >> 1;
		for (int i = 0; i < length; i++) { sum += nums[i]; }
		return totalSum - sum;
	}
};
```

3. 异或

```cpp
class Solution {
public:
    int missingNumber(vector<int>& nums) {
        int number=0,length=nums.size();
        for(int i=1;i<=length;i++){number^=i;}
        for(int i=0;i<length;i++){number^=nums[i];}
        return number;
    }
};
```

---



# 整理与总结

1. 