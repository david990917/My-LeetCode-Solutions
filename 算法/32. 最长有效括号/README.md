| [English](README_EN.md) | 简体中文 |

# [32. 最长有效括号](https://leetcode-cn.com/problems/longest-valid-parentheses)
<p>给定一个只包含 <code>&#39;(&#39;</code>&nbsp;和 <code>&#39;)&#39;</code>&nbsp;的字符串，找出最长的包含有效括号的子串的长度。</p>

<p><strong>示例&nbsp;1:</strong></p>

<pre><strong>输入:</strong> &quot;(()&quot;
<strong>输出:</strong> 2
<strong>解释:</strong> 最长有效括号子串为 <code>&quot;()&quot;</code>
</pre>

<p><strong>示例 2:</strong></p>

<pre><strong>输入:</strong> &quot;<code>)()())</code>&quot;
<strong>输出:</strong> 4
<strong>解释:</strong> 最长有效括号子串为 <code>&quot;()()&quot;</code>
</pre>

**标签:**  [字符串](https://leetcode-cn.com/tag/string) [动态规划](https://leetcode-cn.com/tag/dynamic-programming) 
 ### 相似题目
- 简单:	[有效的括号](https://leetcode-cn.com/problems/valid-parentheses) 

# 解题思路 √

### Python

1. 使用栈的做法
   - 关键点是初始化栈的时候是 [-1]

```python
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        maxCount=0
        stack=[-1]

        length=len(s)
        for i in range(length):
            if s[i]=='(':stack.append(i)
            else:
                stack.pop()
                if not stack:stack.append(i)
                if stack:maxCount=max(maxCount,i-stack[-1])

        return maxCount
```


```python

```

### C++

```cpp

```

---



# 整理与总结

1. 