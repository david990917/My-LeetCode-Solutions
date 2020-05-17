| English | [简体中文](README.md) |

# [210. Course Schedule II](https://leetcode-cn.com/problems/course-schedule-ii)
 ### Description
<p>There are a total of <em>n</em> courses you have to take, labeled from <code>0</code> to <code>n-1</code>.</p>

<p>Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: <code>[0,1]</code></p>

<p>Given the total number of courses and a list of prerequisite <strong>pairs</strong>, return the ordering of courses you should take to finish all courses.</p>

<p>There may be multiple correct orders, you just need to return one of them. If it is impossible to finish all courses, return an empty array.</p>

<p><strong>Example 1:</strong></p>

<pre>
<strong>Input:</strong> 2, [[1,0]] 
<strong>Output: </strong><code>[0,1]</code>
<strong>Explanation:</strong>&nbsp;There are a total of 2 courses to take. To take course 1 you should have finished   
&nbsp;            course 0. So the correct course order is <code>[0,1] .</code></pre>

<p><strong>Example 2:</strong></p>

<pre>
<strong>Input:</strong> 4, [[1,0],[2,0],[3,1],[3,2]]
<strong>Output: </strong><code>[0,1,2,3] or [0,2,1,3]</code>
<strong>Explanation:</strong>&nbsp;There are a total of 4 courses to take. To take course 3 you should have finished both     
             courses 1 and 2. Both courses 1 and 2 should be taken after you finished course 0. 
&nbsp;            So one correct course order is <code>[0,1,2,3]</code>. Another correct ordering is <code>[0,2,1,3] .</code></pre>

<p><strong>Note:</strong></p>

<ol>
	<li>The input prerequisites is a graph represented by <strong>a list of edges</strong>, not adjacency matrices. Read more about <a href="https://www.khanacademy.org/computing/computer-science/algorithms/graph-representation/a/representing-graphs" target="_blank">how a graph is represented</a>.</li>
	<li>You may assume that there are no duplicate edges in the input prerequisites.</li>
</ol>

**Related Topics**  [Depth-first Search](https://leetcode-cn.com/tag/depth-first-search) [Breadth-first Search](https://leetcode-cn.com/tag/breadth-first-search) [Graph](https://leetcode-cn.com/tag/graph) [Topological Sort](https://leetcode-cn.com/tag/topological-sort) 

### Similar Questions
 - Medium:	[Course Schedule](https://leetcode-cn.com/problems/course-schedule) 
 - Hard:	[Alien Dictionary](https://leetcode-cn.com/problems/alien-dictionary) 
 - Medium:	[Minimum Height Trees](https://leetcode-cn.com/problems/minimum-height-trees) 
 - Medium:	[Sequence Reconstruction](https://leetcode-cn.com/problems/sequence-reconstruction) 
 - Hard:	[Course Schedule III](https://leetcode-cn.com/problems/course-schedule-iii) 
