| English | [简体中文](README.md) |

# [98. Validate Binary Search Tree](https://leetcode-cn.com/problems/validate-binary-search-tree)
 ### Description
<p>Given a binary tree, determine if it is a valid binary search tree (BST).</p>

<p>Assume a BST is defined as follows:</p>

<ul>
	<li>The left subtree of a node contains only nodes with keys <strong>less than</strong> the node&#39;s key.</li>
	<li>The right subtree of a node contains only nodes with keys <strong>greater than</strong> the node&#39;s key.</li>
	<li>Both the left and right subtrees must also be binary search trees.</li>
</ul>

<p>&nbsp;</p>

<p><strong>Example 1:</strong></p>

<pre>
    2
   / \
  1   3

<strong>Input:</strong>&nbsp;[2,1,3]
<strong>Output:</strong> true
</pre>

<p><strong>Example 2:</strong></p>

<pre>
    5
   / \
  1   4
&nbsp;    / \
&nbsp;   3   6

<strong>Input:</strong> [5,1,4,null,null,3,6]
<strong>Output:</strong> false
<strong>Explanation:</strong> The root node&#39;s value is 5 but its right child&#39;s value is 4.
</pre>

**Related Topics**  [Tree](https://leetcode-cn.com/tag/tree) [Depth-first Search](https://leetcode-cn.com/tag/depth-first-search) 

### Similar Questions
 - Medium:	[Binary Tree Inorder Traversal](https://leetcode-cn.com/problems/binary-tree-inorder-traversal) 
 - Easy:	[Find Mode in Binary Search Tree](https://leetcode-cn.com/problems/find-mode-in-binary-search-tree) 
