| English | [简体中文](README.md) |

# [72. Edit Distance](https://leetcode-cn.com/problems/edit-distance)
 ### Description
<p>Given two words <em>word1</em> and <em>word2</em>, find the minimum number of operations required to convert <em>word1</em> to <em>word2</em>.</p>

<p>You have the following 3 operations permitted on a word:</p>

<ol>
	<li>Insert a character</li>
	<li>Delete a character</li>
	<li>Replace a character</li>
</ol>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input:</strong> word1 = &quot;horse&quot;, word2 = &quot;ros&quot;
<strong>Output:</strong> 3
<strong>Explanation:</strong> 
horse -&gt; rorse (replace &#39;h&#39; with &#39;r&#39;)
rorse -&gt; rose (remove &#39;r&#39;)
rose -&gt; ros (remove &#39;e&#39;)
</pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input:</strong> word1 = &quot;intention&quot;, word2 = &quot;execution&quot;
<strong>Output:</strong> 5
<strong>Explanation:</strong> 
intention -&gt; inention (remove &#39;t&#39;)
inention -&gt; enention (replace &#39;i&#39; with &#39;e&#39;)
enention -&gt; exention (replace &#39;n&#39; with &#39;x&#39;)
exention -&gt; exection (replace &#39;n&#39; with &#39;c&#39;)
exection -&gt; execution (insert &#39;u&#39;)
</pre>

**Related Topics**  [String](https://leetcode-cn.com/tag/string) [Dynamic Programming](https://leetcode-cn.com/tag/dynamic-programming) 

### Similar Questions
 - Medium:	[One Edit Distance](https://leetcode-cn.com/problems/one-edit-distance) 
 - Medium:	[Delete Operation for Two Strings](https://leetcode-cn.com/problems/delete-operation-for-two-strings) 
 - Medium:	[Minimum ASCII Delete Sum for Two Strings](https://leetcode-cn.com/problems/minimum-ascii-delete-sum-for-two-strings) 
 - Medium:	[Uncrossed Lines](https://leetcode-cn.com/problems/uncrossed-lines) 
