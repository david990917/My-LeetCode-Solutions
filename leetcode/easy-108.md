---
title: easy-108
tags:
  - LeetCode
description: ''
urlname: easy-108
date: 2020-03-10 13:40:41
---

# 题目

> 将一个按照升序排列的有序数组，转换为一棵高度平衡二叉搜索树。
>
> 本题中，一个高度平衡二叉树是指一个二叉树每个节点 的左右两个子树的高度差的绝对值不超过 1。
>
> 示例:
>
> 给定有序数组: [-10,-3,0,5,9],
>
> 一个可能的答案是：[0,-3,9,-10,null,5]，它可以表示下面这个高度平衡二叉搜索树：
>
>       0
>      / \
>    -3   9
>    /   /
>  -10  5
>
> 来源：力扣（LeetCode）
> 链接：https://leetcode-cn.com/problems/convert-sorted-array-to-binary-search-tree
> 著作权归领扣网络所有。商业转载请联系官方授权，非商业转载请注明出处。



# 解题思路 √

### Python

1. 直接做就行了

```python
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if len(nums)==0:return None
        mid=len(nums)//2
        root=TreeNode(nums[mid])
        root.left=self.sortedArrayToBST(nums[:mid])
        root.right=self.sortedArrayToBST(nums[mid+1:])
        return root
```


```python

```



### C++

```cpp

```

---



# 整理与总结

1. 

