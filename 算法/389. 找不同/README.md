| [English](README_EN.md) | 简体中文 |

# [389. 找不同](https://leetcode-cn.com/problems/find-the-difference)
<p>给定两个字符串 <em><strong>s</strong></em> 和 <em><strong>t</strong></em>，它们只包含小写字母。</p>

<p>字符串&nbsp;<strong><em>t</em></strong>&nbsp;由字符串&nbsp;<strong><em>s</em></strong>&nbsp;随机重排，然后在随机位置添加一个字母。</p>

<p>请找出在 <em><strong>t</strong></em> 中被添加的字母。</p>

<p>&nbsp;</p>

<p><strong>示例:</strong></p>

<pre>输入：
s = &quot;abcd&quot;
t = &quot;abcde&quot;

输出：
e

解释：
&#39;e&#39; 是那个被添加的字母。
</pre>

**标签:**  [位运算](https://leetcode-cn.com/tag/bit-manipulation) [哈希表](https://leetcode-cn.com/tag/hash-table) 
 ### 相似题目
- 简单:	[只出现一次的数字](https://leetcode-cn.com/problems/single-number) 

# 解题思路 √

### Python

1. 简单易懂 hashmap

```python
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        hashmap={}
        for i in s:
            if i not in hashmap:hashmap[i]=1
            else:hashmap[i]+=1     

        for i in t:
            if i in hashmap:
                if hashmap[i]==1:
                    hashmap.pop(i)
                else:
                    hashmap[i]-=1
            else:return i
```

2. 异或


```python
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        number=0
        for char in s:number^=ord(char)
        for char in t:number^=ord(char)
        return chr(number)
```

### C++

```cpp

```

---



# 整理与总结

1. 