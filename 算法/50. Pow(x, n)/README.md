| [English](README_EN.md) | 简体中文 |

# [50. Pow(x, n)](https://leetcode-cn.com/problems/powx-n)
<p>实现&nbsp;<a href="https://www.cplusplus.com/reference/valarray/pow/" target="_blank">pow(<em>x</em>, <em>n</em>)</a>&nbsp;，即计算 x 的 n 次幂函数。</p>

<p><strong>示例 1:</strong></p>

<pre><strong>输入:</strong> 2.00000, 10
<strong>输出:</strong> 1024.00000
</pre>

<p><strong>示例&nbsp;2:</strong></p>

<pre><strong>输入:</strong> 2.10000, 3
<strong>输出:</strong> 9.26100
</pre>

<p><strong>示例&nbsp;3:</strong></p>

<pre><strong>输入:</strong> 2.00000, -2
<strong>输出:</strong> 0.25000
<strong>解释:</strong> 2<sup>-2</sup> = 1/2<sup>2</sup> = 1/4 = 0.25</pre>

<p><strong>说明:</strong></p>

<ul>
	<li>-100.0 &lt;&nbsp;<em>x</em>&nbsp;&lt; 100.0</li>
	<li><em>n</em>&nbsp;是 32 位有符号整数，其数值范围是&nbsp;[&minus;2<sup>31</sup>,&nbsp;2<sup>31&nbsp;</sup>&minus; 1] 。</li>
</ul>

**标签:**  [数学](https://leetcode-cn.com/tag/math) [二分查找](https://leetcode-cn.com/tag/binary-search) 
 ### 相似题目
- 简单:	[x 的平方根](https://leetcode-cn.com/problems/sqrtx) 
- 中等:	[超级次方](https://leetcode-cn.com/problems/super-pow) 

# 解题思路 √

### Python

1. 自身就实现了

```python
class Solution:
    def myPow(self, x: float, n: int) -> float:
        return x**n
```


```python

```

### C++

我使用了快速幂的方式进行计算。下面是一组特殊的数据

```
1.00000
-2147483648
```

```cpp
class Solution {
public:
    double quickMul(double x,long long N){
        if(N==0){return 1.0;}
        double tmp=quickMul(x,N/2);
        return N%2 ? tmp*tmp*x : tmp*tmp;
    }
    double myPow(double x, int n) {
        long long N=n;
        return N>=0 ? quickMul(x,N) : 1.0/quickMul(x,-N);
    }
};
```

---

注意不能直接取负数，需要 `long long` 的原因是，`-2147483648` 无法直接变成正数的 `int`

# 整理与总结

1. C++ 注意不能直接取负数，需要 `long long` 的原因是，`-2147483648` 无法直接变成正数的 `int`
2. C++ 需要注意 `1.0`