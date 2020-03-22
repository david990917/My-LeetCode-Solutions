---
title: medium-776
tags:
  - LeetCode
description: ''
urlname: medium-776
date: 2020-03-22 09:07:32
---

# 题目

[拆分二叉搜索树](https://leetcode-cn.com/problems/split-bst/)

给你一棵二叉搜索树（BST）、它的根结点 root 以及目标值 V。

请将该树按要求拆分为两个子树：其中一个子树结点的值都必须小于等于给定的目标值 V；另一个子树结点的值都必须大于目标值 V；树中并非一定要存在值为 V 的结点。

除此之外，树中大部分结构都需要保留，也就是说原始树中父节点 P 的任意子节点 C，假如拆分后它们仍在同一个子树中，那么结点 P 应仍为 C 的子结点。

你需要返回拆分后两个子树的根结点 TreeNode，顺序随意。

示例 1：

```
输入：root = [4,2,6,1,3,5,7], V = 2
输出：[[2,1],[4,3,6,null,null,5,7]]
解释：
注意根结点 output[0] 和 output[1] 都是 TreeNode 对象，不是数组。
```

给定的树 [4,2,6,1,3,5,7] 可化为如下示意图：

          4
        /   \
      2      6
     / \    / \
    1   3  5   7

输出的示意图如下：

          4
        /   \
      3      6       和    2
            / \           /
           5   7         1
注意：

- 二叉搜索树节点个数不得超过 50 个
- 二叉搜索树始终是有效的，并且每个节点的值都不相等



# 解题思路 √

根节点要么在第一棵子树中，要么在第二棵子树中。假设根节点在第一棵子树中，那么这棵树的左子树一定在第一棵子树中，右子树中部分节点在第一棵子树，部分在第二棵子树中。

![img](medium-776/split_line.png)



如上图所示，粗线代表原始节点之间主要父子关系，有色细线代表了分割之后子树的父子关系。

`bns = split(root.right) `为分割树的结果。`bns[0]` 和 `bns[1]` 在分割之后依然还是二叉搜索树，其中 `bns[0]` 在第一棵子树中，`bns[1]` 为第二棵子树。

![img](medium-776/sub_tree.png)

作者：LeetCode
链接：https://leetcode-cn.com/problems/split-bst/solution/chai-fen-er-cha-sou-suo-shu-by-leetcode/
来源：力扣（LeetCode）
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。

### Python

1. 递归 - 想明白就好了

```python
class Solution:
    def splitBST(self, root: TreeNode, V: int) -> List[TreeNode]:
        if not root:return [None,None]
        if root.val<=V:
            res=self.splitBST(root.right,V)
            root.right=res[0]
            return root,res[1]
        if root.val>V:
            res=self.splitBST(root.left,V)
            root.left=res[1]
            return res[0],root
```


```python

```



### C++

```cpp

```

---



# 整理与总结

1. 

