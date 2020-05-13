| [English](README_EN.md) | 简体中文 |

# [102. 二叉树的层序遍历](https://leetcode-cn.com/problems/binary-tree-level-order-traversal)
<p>给你一个二叉树，请你返回其按 <strong>层序遍历</strong> 得到的节点值。 （即逐层地，从左到右访问所有节点）。</p>

<p>&nbsp;</p>

<p><strong>示例：</strong><br>
二叉树：<code>[3,9,20,null,null,15,7]</code>,</p>

<pre>    3
   / \
  9  20
    /  \
   15   7
</pre>

<p>返回其层次遍历结果：</p>

<pre>[
  [3],
  [9,20],
  [15,7]
]
</pre>

**标签:**  [树](https://leetcode-cn.com/tag/tree) [广度优先搜索](https://leetcode-cn.com/tag/breadth-first-search) 
 ### 相似题目
- 中等:	[二叉树的锯齿形层次遍历](https://leetcode-cn.com/problems/binary-tree-zigzag-level-order-traversal) 
- 简单:	[二叉树的层次遍历 II](https://leetcode-cn.com/problems/binary-tree-level-order-traversal-ii) 
- 简单:	[二叉树的最小深度](https://leetcode-cn.com/problems/minimum-depth-of-binary-tree) 
- 中等:	[二叉树的垂直遍历](https://leetcode-cn.com/problems/binary-tree-vertical-order-traversal) 
- 简单:	[二叉树的层平均值](https://leetcode-cn.com/problems/average-of-levels-in-binary-tree) 
- 中等:	[N叉树的层序遍历](https://leetcode-cn.com/problems/n-ary-tree-level-order-traversal) 
- 简单:	[二叉树的堂兄弟节点](https://leetcode-cn.com/problems/cousins-in-binary-tree) 

# 解题思路 √

### Python

1. 简单使用队列

```python
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root:return []

        result=[]
        from collections import deque
        deq=deque()
        deq.append(root)

        while deq:
            length=len(deq)
            tmp=[]
            for _ in range(length):
                curr=deq.popleft()
                tmp.append(curr.val)
                if curr.left:deq.append(curr.left)
                if curr.right:deq.append(curr.right)
            result.append(tmp)
        return result
```


```python

```

### C++

使用 `que` 和 `vector`

```cpp
class Solution {
public:
	vector<vector<int>> levelOrder(TreeNode* root) {
		vector<vector<int>> result;
		if (!root) { return result; }

		queue<TreeNode*> que;
		que.push(root);
		while (!que.empty()) {
			int currentLevelSize = que.size();
			result.push_back(vector<int>());
			for (int i = 1; i <= currentLevelSize; i++) {
				auto node = que.front(); que.pop();
				result.back().push_back(node->val);
				if (node->left) { que.push(node->left); }
				if (node->right) { que.push(node->right); }
			}
		}
		return result;
	}
};
```

---



# 整理与总结

1. 