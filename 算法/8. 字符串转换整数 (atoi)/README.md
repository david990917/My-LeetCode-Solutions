| [English](README_EN.md) | 简体中文 |

# [8. 字符串转换整数 (atoi)](https://leetcode-cn.com/problems/string-to-integer-atoi)
<p>请你来实现一个&nbsp;<code>atoi</code>&nbsp;函数，使其能将字符串转换成整数。</p>

<p>首先，该函数会根据需要丢弃无用的开头空格字符，直到寻找到第一个非空格的字符为止。接下来的转化规则如下：</p>

<ul>
	<li>如果第一个非空字符为正或者负号时，则将该符号与之后面尽可能多的连续数字字符组合起来，形成一个有符号整数。</li>
	<li>假如第一个非空字符是数字，则直接将其与之后连续的数字字符组合起来，形成一个整数。</li>
	<li>该字符串在有效的整数部分之后也可能会存在多余的字符，那么这些字符可以被忽略，它们对函数不应该造成影响。</li>
</ul>

<p>注意：假如该字符串中的第一个非空格字符不是一个有效整数字符、字符串为空或字符串仅包含空白字符时，则你的函数不需要进行转换，即无法进行有效转换。</p>

<p>在任何情况下，若函数不能进行有效的转换时，请返回 0 。</p>

<p><strong>提示：</strong></p>

<ul>
	<li>本题中的空白字符只包括空格字符 <code>&#39; &#39;</code> 。</li>
	<li>假设我们的环境只能存储 32 位大小的有符号整数，那么其数值范围为&nbsp;[&minus;2<sup>31</sup>,&nbsp; 2<sup>31&nbsp;</sup>&minus; 1]。如果数值超过这个范围，请返回 &nbsp;INT_MAX (2<sup>31&nbsp;</sup>&minus; 1) 或&nbsp;INT_MIN (&minus;2<sup>31</sup>) 。</li>
</ul>

<p>&nbsp;</p>

<p><strong>示例&nbsp;1:</strong></p>

<pre><strong>输入:</strong> &quot;42&quot;
<strong>输出:</strong> 42
</pre>

<p><strong>示例&nbsp;2:</strong></p>

<pre><strong>输入:</strong> &quot;   -42&quot;
<strong>输出:</strong> -42
<strong>解释: </strong>第一个非空白字符为 &#39;-&#39;, 它是一个负号。
&nbsp;    我们尽可能将负号与后面所有连续出现的数字组合起来，最后得到 -42 。
</pre>

<p><strong>示例&nbsp;3:</strong></p>

<pre><strong>输入:</strong> &quot;4193 with words&quot;
<strong>输出:</strong> 4193
<strong>解释:</strong> 转换截止于数字 &#39;3&#39; ，因为它的下一个字符不为数字。
</pre>

<p><strong>示例&nbsp;4:</strong></p>

<pre><strong>输入:</strong> &quot;words and 987&quot;
<strong>输出:</strong> 0
<strong>解释:</strong> 第一个非空字符是 &#39;w&#39;, 但它不是数字或正、负号。
     因此无法执行有效的转换。</pre>

<p><strong>示例&nbsp;5:</strong></p>

<pre><strong>输入:</strong> &quot;-91283472332&quot;
<strong>输出:</strong> -2147483648
<strong>解释:</strong> 数字 &quot;-91283472332&quot; 超过 32 位有符号整数范围。 
&nbsp;    因此返回 INT_MIN (&minus;2<sup>31</sup>) 。
</pre>

**标签:**  [数学](https://leetcode-cn.com/tag/math) [字符串](https://leetcode-cn.com/tag/string) 
 ### 相似题目
- 简单:	[整数反转](https://leetcode-cn.com/problems/reverse-integer) 
- 困难:	[有效数字](https://leetcode-cn.com/problems/valid-number) 

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