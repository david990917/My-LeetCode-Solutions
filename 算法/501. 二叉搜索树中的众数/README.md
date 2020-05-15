| [English](README_EN.md) | 简体中文 |

# [501. 二叉搜索树中的众数](https://leetcode-cn.com/problems/find-mode-in-binary-search-tree)
<p>给定一个有相同值的二叉搜索树（BST），找出 BST 中的所有众数（出现频率最高的元素）。</p>

<p>假定 BST 有如下定义：</p>

<ul>
	<li>结点左子树中所含结点的值小于等于当前结点的值</li>
	<li>结点右子树中所含结点的值大于等于当前结点的值</li>
	<li>左子树和右子树都是二叉搜索树</li>
</ul>

<p>例如：<br>
给定 BST <code>[1,null,2,2]</code>,</p>

<pre>   1
    \
     2
    /
   2
</pre>

<p><code>返回[2]</code>.</p>

<p><strong>提示</strong>：如果众数超过1个，不需考虑输出顺序</p>

<p><strong>进阶：</strong>你可以不使用额外的空间吗？（假设由递归产生的隐式调用栈的开销不被计算在内）</p>

**标签:**  [树](https://leetcode-cn.com/tag/tree) 
 ### 相似题目
- 中等:	[验证二叉搜索树](https://leetcode-cn.com/problems/validate-binary-search-tree) 

# 解题思路 √

### Python

1. 容易的-只用操作最中心的元素就可以啦

```python
class Solution:
    def findMode(self, root: TreeNode) -> List[int]:
        self.preVal,self.count,self.maxCount,self.result=None,0,0,[]
        def inorder(root):
            if not root:return
            inorder(root.left)
            if isinstance(self.preVal,int):
                if root.val==self.preVal:self.count+=1
                else:self.count=1
                if self.count==self.maxCount:
                    self.result.append(root.val)
                elif self.count>self.maxCount:
                    self.maxCount=self.count
                    self.result=[root.val]
                
            else:
                self.count=1
                self.maxCount=1
                self.result=[root.val]
            self.preVal=root.val
            inorder(root.right)

        inorder(root)
        return self.result
```


```python

```

### C++

```cpp

```

---



# 整理与总结

1. 