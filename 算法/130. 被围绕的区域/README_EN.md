| English | [简体中文](README.md) |

# [130. Surrounded Regions](https://leetcode-cn.com/problems/surrounded-regions)
 ### Description
<p>Given a 2D board containing <code>&#39;X&#39;</code> and <code>&#39;O&#39;</code> (<strong>the letter O</strong>), capture all regions surrounded by <code>&#39;X&#39;</code>.</p>

<p>A region is captured by flipping all <code>&#39;O&#39;</code>s into <code>&#39;X&#39;</code>s in that surrounded region.</p>

<p><strong>Example:</strong></p>

<pre>
X X X X
X O O X
X X O X
X O X X
</pre>

<p>After running your function, the board should be:</p>

<pre>
X X X X
X X X X
X X X X
X O X X
</pre>

<p><strong>Explanation:</strong></p>

<p>Surrounded regions shouldn&rsquo;t be on the border, which means that any <code>&#39;O&#39;</code>&nbsp;on the border of the board are not flipped to <code>&#39;X&#39;</code>. Any <code>&#39;O&#39;</code>&nbsp;that is not on the border and it is not connected to an <code>&#39;O&#39;</code>&nbsp;on the border will be flipped to <code>&#39;X&#39;</code>. Two cells are connected if they are adjacent cells connected horizontally or vertically.</p>

**Related Topics**  [Depth-first Search](https://leetcode-cn.com/tag/depth-first-search) [Breadth-first Search](https://leetcode-cn.com/tag/breadth-first-search) [Union Find](https://leetcode-cn.com/tag/union-find) 

### Similar Questions
 - Medium:	[Number of Islands](https://leetcode-cn.com/problems/number-of-islands) 
 - Medium:	[Walls and Gates](https://leetcode-cn.com/problems/walls-and-gates) 
