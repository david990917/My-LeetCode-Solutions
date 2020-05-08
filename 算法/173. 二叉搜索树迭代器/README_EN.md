| English | [简体中文](README.md) |

# [173. Binary Search Tree Iterator](https://leetcode-cn.com/problems/binary-search-tree-iterator)
 ### Description
<p>Implement an iterator over a binary search tree (BST). Your iterator will be initialized with the root node of a BST.</p>

<p>Calling <code>next()</code> will return the next smallest number in the BST.</p>

<p>&nbsp;</p>

<ul>
</ul>

<p><strong>Example:</strong></p>

<p><strong><img alt="" src="https://assets.leetcode.com/uploads/2018/12/25/bst-tree.png" style="width: 189px; height: 178px;" /></strong></p>

<pre>
BSTIterator iterator = new BSTIterator(root);
iterator.next();    // return 3
iterator.next();    // return 7
iterator.hasNext(); // return true
iterator.next();    // return 9
iterator.hasNext(); // return true
iterator.next();    // return 15
iterator.hasNext(); // return true
iterator.next();    // return 20
iterator.hasNext(); // return false
</pre>

<p>&nbsp;</p>

<p><b>Note:</b></p>

<ul>
	<li><code>next()</code> and <code>hasNext()</code> should run in average O(1) time and uses O(<i>h</i>) memory, where <i>h</i> is the height of the tree.</li>
	<li>You may assume that&nbsp;<code>next()</code>&nbsp;call&nbsp;will always be valid, that is, there will be at least a next smallest number in the BST when <code>next()</code> is called.</li>
</ul>

**Related Topics**  [Stack](https://leetcode-cn.com/tag/stack) [Tree](https://leetcode-cn.com/tag/tree) [Design](https://leetcode-cn.com/tag/design) 

### Similar Questions
 - Medium:	[Binary Tree Inorder Traversal](https://leetcode-cn.com/problems/binary-tree-inorder-traversal) 
 - Medium:	[Flatten 2D Vector](https://leetcode-cn.com/problems/flatten-2d-vector) 
 - Medium:	[Zigzag Iterator](https://leetcode-cn.com/problems/zigzag-iterator) 
 - Medium:	[Peeking Iterator](https://leetcode-cn.com/problems/peeking-iterator) 
 - Medium:	[Inorder Successor in BST](https://leetcode-cn.com/problems/inorder-successor-in-bst) 
