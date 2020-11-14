| [English](README_EN.md) | 简体中文 |

# [1122. 数组的相对排序](https://leetcode-cn.com/problems/relative-sort-array)
<p>给你两个数组，<code>arr1</code> 和&nbsp;<code>arr2</code>，</p>

<ul>
	<li><code>arr2</code>&nbsp;中的元素各不相同</li>
	<li><code>arr2</code> 中的每个元素都出现在&nbsp;<code>arr1</code>&nbsp;中</li>
</ul>

<p>对 <code>arr1</code>&nbsp;中的元素进行排序，使 <code>arr1</code> 中项的相对顺序和&nbsp;<code>arr2</code>&nbsp;中的相对顺序相同。未在&nbsp;<code>arr2</code>&nbsp;中出现过的元素需要按照升序放在&nbsp;<code>arr1</code>&nbsp;的末尾。</p>

<p>&nbsp;</p>

<p><strong>示例：</strong></p>

<pre><strong>输入：</strong>arr1 = [2,3,1,3,2,4,6,7,9,2,19], arr2 = [2,1,4,3,9,6]
<strong>输出：</strong>[2,2,2,1,4,3,3,9,6,7,19]
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>arr1.length, arr2.length &lt;= 1000</code></li>
	<li><code>0 &lt;= arr1[i], arr2[i] &lt;= 1000</code></li>
	<li><code>arr2</code>&nbsp;中的元素&nbsp;<code>arr2[i]</code>&nbsp;各不相同</li>
	<li><code>arr2</code> 中的每个元素&nbsp;<code>arr2[i]</code>&nbsp;都出现在&nbsp;<code>arr1</code>&nbsp;中</li>
</ul>

**标签:**  [排序](https://leetcode-cn.com/tag/sort) [数组](https://leetcode-cn.com/tag/array) 
# 解题思路 √

### Python

1. 简单直白的方法 - 直接翻译题目的要求

```python
class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        helpD=[]
        result=[]
        hashmap={}
        for element in arr2:
            hashmap[element]=0
        for i in arr1:
            if i in hashmap:
                hashmap[i]+=1
            else:
                helpD.append(i)
        helpD.sort()

        for i in arr2:
            for j in range(hashmap[i]):
                result.append(i)
        result+=helpD
        return result
```


```python

```

### C++

```cpp

```

---



# 整理与总结

1. 