| [English](README_EN.md) | 简体中文 |

# [1009. 十进制整数的反码](https://leetcode-cn.com/problems/complement-of-base-10-integer)
<p>每个非负整数&nbsp;<code>N</code>&nbsp;都有其二进制表示。例如，&nbsp;<code>5</code>&nbsp;可以被表示为二进制&nbsp;<code>&quot;101&quot;</code>，<code>11</code> 可以用二进制&nbsp;<code>&quot;1011&quot;</code>&nbsp;表示，依此类推。注意，除&nbsp;<code>N = 0</code>&nbsp;外，任何二进制表示中都不含前导零。</p>

<p>二进制的反码表示是将每个&nbsp;<code>1</code>&nbsp;改为&nbsp;<code>0</code>&nbsp;且每个&nbsp;<code>0</code>&nbsp;变为&nbsp;<code>1</code>。例如，二进制数&nbsp;<code>&quot;101&quot;</code>&nbsp;的二进制反码为&nbsp;<code>&quot;010&quot;</code>。</p>

<p>给你一个十进制数&nbsp;<code>N</code>，请你返回其二进制表示的反码所对应的十进制整数。</p>

<p>&nbsp;</p>

<ol>
</ol>

<p><strong>示例 1：</strong></p>

<pre><strong>输入：</strong>5
<strong>输出：</strong>2
<strong>解释：</strong>5 的二进制表示为 &quot;101&quot;，其二进制反码为 &quot;010&quot;，也就是十进制中的 2 。
</pre>

<p><strong>示例 2：</strong></p>

<pre><strong>输入：</strong>7
<strong>输出：</strong>0
<strong>解释：</strong>7 的二进制表示为 &quot;111&quot;，其二进制反码为 &quot;000&quot;，也就是十进制中的 0 。
</pre>

<p><strong>示例 3：</strong></p>

<pre><strong>输入：</strong>10
<strong>输出：</strong>5
<strong>解释：</strong>10 的二进制表示为 &quot;1010&quot;，其二进制反码为 &quot;0101&quot;，也就是十进制中的 5 。
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ol>
	<li><code>0 &lt;= N &lt; 10^9</code></li>
	<li>本题与 476：<a href="https://leetcode-cn.com/problems/number-complement/">https://leetcode-cn.com/problems/number-complement/</a> 相同</li>
</ol>

**标签:**  [数学](https://leetcode-cn.com/tag/math) 
# 解题思路 √

### Python

1. Python 自带的库

```python
class Solution:
    def bitwiseComplement(self, N: int) -> int:
        binNumberStr=bin(N)[2:]
        result=''
        for i in binNumberStr:
            result+=str(int(i)^1)
        return int(result,2)
```

2. 利用 `原码 + 反码` 相加的和是 `2**n-1`


```python
class Solution:
    def bitwiseComplement(self, N: int) -> int:
        binNumberStr=bin(N)[2:]
        return 2**len(binNumberStr)-1 -N
```

### C++

1. 直接异或就完事儿了

```cpp
class Solution {
public:
    int bitwiseComplement(int N) {
        if(N==0){return 1;}

        int tmp1=1;
        int tmp2=N;
        while(tmp2>0){
            N^=tmp1;
            tmp1=tmp1<<1;
            tmp2=tmp2>>1;
        }
        return N;
    }
};
```

2. 利用 原码 + 补码 的性质

```c++
class Solution {
public:
    int bitwiseComplement(int N) {
        int tmp=2;
        while(tmp<=N){tmp<<=1;}
        return tmp-1 -N;
    }
};
```



---



# 整理与总结

1. 很巧妙，总结在**语雀**上面了。