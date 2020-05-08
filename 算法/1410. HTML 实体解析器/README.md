| [English](README_EN.md) | 简体中文 |

# [1410. HTML 实体解析器](https://leetcode-cn.com/problems/html-entity-parser)
<p>「HTML&nbsp;实体解析器」 是一种特殊的解析器，它将 HTML 代码作为输入，并用字符本身替换掉所有这些特殊的字符实体。</p>

<p>HTML 里这些特殊字符和它们对应的字符实体包括：</p>

<ul>
	<li><strong>双引号：</strong>字符实体为&nbsp;<code>&amp;quot;</code>&nbsp;，对应的字符是&nbsp;<code>&quot;</code>&nbsp;。</li>
	<li><strong>单引号：</strong>字符实体为&nbsp;<code>&amp;apos;</code>&nbsp;，对应的字符是&nbsp;<code>&#39;</code>&nbsp;。</li>
	<li><strong>与符号：</strong>字符实体为&nbsp;<code>&amp;amp;</code>&nbsp;，对应对的字符是&nbsp;<code>&amp;</code>&nbsp;。</li>
	<li><strong>大于号：</strong>字符实体为&nbsp;<code>&amp;gt;</code>&nbsp;，对应的字符是&nbsp;<code>&gt;</code>&nbsp;。</li>
	<li><strong>小于号：</strong>字符实体为&nbsp;<code>&amp;lt;</code>&nbsp;，对应的字符是&nbsp;<code>&lt;</code>&nbsp;。</li>
	<li><strong>斜线号：</strong>字符实体为&nbsp;<code>&amp;frasl;</code>&nbsp;，对应的字符是&nbsp;<code>/</code>&nbsp;。</li>
</ul>

<p>给你输入字符串&nbsp;<code>text</code>&nbsp;，请你实现一个 HTML&nbsp;实体解析器，返回解析器解析后的结果。</p>

<p>&nbsp;</p>

<p><strong>示例 1：</strong></p>

<pre>
<strong>输入：</strong>text = &quot;&amp;amp; is an HTML entity but &amp;ambassador; is not.&quot;
<strong>输出：</strong>&quot;&amp; is an HTML entity but &amp;ambassador; is not.&quot;
<strong>解释：</strong>解析器把字符实体 &amp;amp; 用 &amp; 替换
</pre>

<p><strong>示例&nbsp;2：</strong></p>

<pre>
<strong>输入：</strong>text = &quot;and I quote: &amp;quot;...&amp;quot;&quot;
<strong>输出：</strong>&quot;and I quote: \&quot;...\&quot;&quot;
</pre>

<p><strong>示例 3：</strong></p>

<pre>
<strong>输入：</strong>text = &quot;Stay home! Practice on Leetcode :)&quot;
<strong>输出：</strong>&quot;Stay home! Practice on Leetcode :)&quot;
</pre>

<p><strong>示例 4：</strong></p>

<pre>
<strong>输入：</strong>text = &quot;x &amp;gt; y &amp;amp;&amp;amp; x &amp;lt; y is always false&quot;
<strong>输出：</strong>&quot;x &gt; y &amp;&amp; x &lt; y is always false&quot;
</pre>

<p><strong>示例 5：</strong></p>

<pre>
<strong>输入：</strong>text = &quot;leetcode.com&amp;frasl;problemset&amp;frasl;all&quot;
<strong>输出：</strong>&quot;leetcode.com/problemset/all&quot;
</pre>

<p>&nbsp;</p>

<p><strong>提示：</strong></p>

<ul>
	<li><code>1 &lt;= text.length &lt;= 10^5</code></li>
	<li>字符串可能包含 256 个ASCII 字符中的任意字符。</li>
</ul>

**标签:**  [栈](https://leetcode-cn.com/tag/stack) [字符串](https://leetcode-cn.com/tag/string) 
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