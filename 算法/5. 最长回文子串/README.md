| [English](README_EN.md) | 简体中文 |

# [5. 最长回文子串](https://leetcode-cn.com/problems/longest-palindromic-substring)
<p>给定一个字符串 <code>s</code>，找到 <code>s</code> 中最长的回文子串。你可以假设&nbsp;<code>s</code> 的最大长度为 1000。</p>

<p><strong>示例 1：</strong></p>

<pre><strong>输入:</strong> &quot;babad&quot;
<strong>输出:</strong> &quot;bab&quot;
<strong>注意:</strong> &quot;aba&quot; 也是一个有效答案。
</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入:</strong> &quot;cbbd&quot;
<strong>输出:</strong> &quot;bb&quot;
</pre>

**标签:**  [字符串](https://leetcode-cn.com/tag/string) [动态规划](https://leetcode-cn.com/tag/dynamic-programming) 
 ### 相似题目
- 困难:	[最短回文串](https://leetcode-cn.com/problems/shortest-palindrome) 
- 简单:	[回文排列](https://leetcode-cn.com/problems/palindrome-permutation) 
- 困难:	[回文对](https://leetcode-cn.com/problems/palindrome-pairs) 
- 中等:	[最长回文子序列](https://leetcode-cn.com/problems/longest-palindromic-subsequence) 
- 中等:	[回文子串](https://leetcode-cn.com/problems/palindromic-substrings) 

# 解题思路 √

### Python

1. 动态规划的方法


```python
class Solution:
    def longestPalindrome(self, s: str) -> str:
        length=len(s)
        maxPalLength,leftIDX,rightIDX=0,0,0
        store_table=[[True]*i for i in range(1,length+1)]
        for j in range(length):
            for i in range(j+1):
                if j==i:target=True
                elif j==i+1:target=(s[i]==s[j])
                else:target=store_table[j-1][i+1] and (s[i]==s[j])
                store_table[j][i]=target
                if target: 
                    if j-i+1>maxPalLength:
                        maxPalLength=j-i+1
                        leftIDX,rightIDX=i,j
        return s[leftIDX:rightIDX+1]
```

### C++

```cpp

```

---



# 整理与总结

1. 