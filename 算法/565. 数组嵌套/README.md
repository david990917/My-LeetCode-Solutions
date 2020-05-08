| [English](README_EN.md) | 简体中文 |

# [565. 数组嵌套](https://leetcode-cn.com/problems/array-nesting)
<p>索引从<code>0</code>开始长度为<code>N</code>的数组<code>A</code>，包含<code>0</code>到<code>N - 1</code>的所有整数。找到并返回最大的集合<code>S</code>，<code>S[i] = {A[i], A[A[i]], A[A[A[i]]], ... }</code>且遵守以下的规则。</p>

<p>假设选择索引为<code>i</code>的元素<code>A[i]</code>为<code>S</code>的第一个元素，<code>S</code>的下一个元素应该是<code>A[A[i]]</code>，之后是<code>A[A[A[i]]]...</code> 以此类推，不断添加直到<code>S</code>出现重复的元素。</p>

<p><strong>示例&nbsp;1:</strong></p>

<pre>
<strong>输入:</strong> A = [5,4,0,3,1,6,2]
<strong>输出:</strong> 4
<strong>解释:</strong> 
A[0] = 5, A[1] = 4, A[2] = 0, A[3] = 3, A[4] = 1, A[5] = 6, A[6] = 2.

其中一种最长的 S[K]:
S[0] = {A[0], A[5], A[6], A[2]} = {5, 6, 2, 0}
</pre>

<p><strong>注意:</strong></p>

<ol>
	<li><code>N</code>是<code>[1, 20,000]</code>之间的整数。</li>
	<li><code>A</code>中不含有重复的元素。</li>
	<li><code>A</code>中的元素大小在<code>[0, N-1]</code>之间。</li>
</ol>

**标签:**  [数组](https://leetcode-cn.com/tag/array) 
 ### 相似题目
- 简单:	[嵌套列表权重和](https://leetcode-cn.com/problems/nested-list-weight-sum) 
- 中等:	[扁平化嵌套列表迭代器](https://leetcode-cn.com/problems/flatten-nested-list-iterator) 
- 中等:	[加权嵌套序列和 II](https://leetcode-cn.com/problems/nested-list-weight-sum-ii) 

# 解题思路 √

### Python

1. 

```python

```


```python

```

### C++

```cpp

```

---



# 整理与总结

1. 