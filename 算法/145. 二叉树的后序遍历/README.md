| [English](README_EN.md) | 简体中文 |

# [145. 二叉树的后序遍历](https://leetcode-cn.com/problems/binary-tree-postorder-traversal)
<p>给定一个二叉树，返回它的 <em>后序&nbsp;</em>遍历。</p>

<p><strong>示例:</strong></p>

<pre><strong>输入:</strong> [1,null,2,3]  
   1
    \
     2
    /
   3 

<strong>输出:</strong> [3,2,1]</pre>

<p><strong>进阶:</strong>&nbsp;递归算法很简单，你可以通过迭代算法完成吗？</p>

**标签:**  [栈](https://leetcode-cn.com/tag/stack) [树](https://leetcode-cn.com/tag/tree) 
 ### 相似题目
- 中等:	[二叉树的中序遍历](https://leetcode-cn.com/problems/binary-tree-inorder-traversal) 
- 简单:	[N叉树的后序遍历](https://leetcode-cn.com/problems/n-ary-tree-postorder-traversal) 

# 解题思路 √

### Python

1. 递归 - 后序遍历

```python
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        result=[]
        def postOrder(root):
            if not root:return 
            if root.left:postOrder(root.left)
            if root.right:postOrder(root.right)
            result.append(root.val)
        postOrder(root)
        return result
```

2. 后序遍历【左右中】 - 类比前序遍历【中左右】-> 【中右左】 --反向--> 【左中右】


```python
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:return []

        self.result=[]
        stack=[root]
        while stack:
            node=stack.pop()
            self.result.append(node.val)
            if node.left:stack.append(node.left)
            if node.right:stack.append(node.right)
        return self.result[::-1]
```

3. 颜色标记法

```python
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if not root:return []

        self.result=[]
        stack=[(root,0)]
        while stack:
            node,times=stack.pop()
            if not node:continue
            if times==0:
                stack.append((node,1))
                stack.append((node.left,0))
            elif times==1:
                stack.append((node,2))
                stack.append((node.right,0))
            else:
                self.result.append(node.val)
        return self.result
```



### C++

```cpp

```

---



# 整理与总结

1. 