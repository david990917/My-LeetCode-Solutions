| [English](README_EN.md) | 简体中文 |

# [面试题38. 字符串的排列](https://leetcode-cn.com/problems/zi-fu-chuan-de-pai-lie-lcof)
<p>输入一个字符串，打印出该字符串中字符的所有排列。</p>

<p>&nbsp;</p>

<p>你可以以任意顺序返回这个字符串数组，但里面不能有重复元素。</p>

<p>&nbsp;</p>

<p><strong>示例:</strong></p>

<pre><strong>输入：</strong>s = &quot;abc&quot;
<strong>输出：[</strong>&quot;abc&quot;,&quot;acb&quot;,&quot;bac&quot;,&quot;bca&quot;,&quot;cab&quot;,&quot;cba&quot;<strong>]</strong>
</pre>

<p>&nbsp;</p>

<p><strong>限制：</strong></p>

<p><code>1 &lt;= s 的长度 &lt;= 8</code></p>

**标签:**  [回溯算法](https://leetcode-cn.com/tag/backtracking) 
# 解题思路 √

### Python

1. 回溯法直接就可以做

```python
class Solution:
    def permutation(self, s: str) -> List[str]:
        target=len(s)
        t=list(s)
        result=set()

        def backtracking(curr,t):
            if len(curr)==target:
                result.add(curr)
                return 
            for i in range(len(t)):
                tmp=t[:i]+t[i+1:]
                backtracking(curr+t[i],tmp)
        
        backtracking("",t)
        return list(result)
```


```python

```

### C++

```cpp

```

---



# 整理与总结

1. 