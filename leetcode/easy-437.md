---
title: easy-437
tags:
  - LeetCode
description: 'Path Sum III'
urlname: easy-437
date: 2019-09-01 17:46:00
---

# 题目

https://leetcode-cn.com/problems/path-sum-iii/

给定一个二叉树，它的每个结点都存放着一个整数值。

找出路径和等于给定数值的路径总数。

路径不需要从根节点开始，也不需要在叶子节点结束，但是路径方向必须是向下的（只能从父节点到子节点）。

二叉树不超过1000个节点，且节点数值范围是 [-1000000,1000000] 的整数。

**示例：**

```
root = [10,5,-3,3,2,null,11,3,-2,null,1], sum = 8

      10
     /  \
    5   -3
   / \    \
  3   2   11
 / \   \
3  -2   1

返回 3。和等于 8 的路径有:

1.  5 -> 3
2.  5 -> 2 -> 1
3.  -3 -> 11
```

# 解题思路 √

这道题目是要我们求解出任何一个节点出发到子孙节点的路径中和为指定值。 注意这里，不一定是从根节点出发，也不一定在叶子节点结束。

一种简单的思路就是直接递归解决，空间复杂度O(n) 时间复杂度介于O(nlogn) 和 O(n^2)

但是还有一种空间复杂度更加优秀的算法，利用hashmap来避免重复计算，时间复杂度和空间复杂度都是O(n)。 这种思路是`subarray-sum-equals-k`的升级版本，如果那道题目你可以O(n)解决，这道题目难度就不会很大， 只是将数组换成了二叉树。关于具体的思路可以看[这道题目](https://github.com/azl397985856/leetcode/blob/master/problems/560.subarray-sum-equals-k.md)

这里有一个不一样的地方，这里我说明一下，就是为什么要有`hashmap[acc] = hashmap[acc] - 1;`， 原因很简单，就是我们DFS的时候，从底部往上回溯的时候，map的值应该也回溯。如果你对回溯法比较熟悉的话， 应该很容易理解，如果不熟悉可以参考[这道题目](https://github.com/azl397985856/leetcode/blob/master/problems/46.permutations.md)， 这道题目就是通过`tempList.pop()`来完成的。

另外我画了一个图，相信看完你就明白了。

当我们执行到底部的时候：

[![437.path-sum-iii](easy-437/437.path-sum-iii-1.jpg)](https://github.com/azl397985856/leetcode/blob/master/assets/problems/437.path-sum-iii-1.jpg)

接着往上回溯：

[![437.path-sum-iii-2](easy-437/437.path-sum-iii-2.jpg)](https://github.com/azl397985856/leetcode/blob/master/assets/problems/437.path-sum-iii-2.jpg)

很容易看出，我们的hashmap不应该有第一张图的那个记录了，因此需要减去。

具体实现见下方代码区。

## 关键点解析

- 通过hashmap，以时间换空间
- 对于这种连续的元素求和问题，有一个共同的思路，可以参考[这道题目](https://github.com/azl397985856/leetcode/blob/master/problems/560.subarray-sum-equals-k.md)

# 解题思路 √

### Python

1. 第一想法是递归

```python
class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        def pathSumCounter(root,sum):
            if not root:return 0
            count=0
            if root.val==sum:count+=1
            count+=pathSumCounter(root.left,sum-root.val)
            count+=pathSumCounter(root.right,sum-root.val)
            return count
        
        if not root:return 0
        return pathSumCounter(root,sum)+self.pathSum(root.left,sum)+self.pathSum(root.right,sum)
```

2. hashmap + 前缀和


```python
class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        self.count=0
        hashtable={0:1}
        prefixSum=0

        def dfs(root,sum,prefixSum,hashtable):
            if not root:return 0
            prefixSum+=root.val
            if prefixSum-sum in hashtable:
                self.count+=hashtable[prefixSum-sum]
            if prefixSum not in hashtable:hashtable[prefixSum]=1
            else:hashtable[prefixSum]+=1
            dfs(root.left,sum,prefixSum,hashtable)
            dfs(root.right,sum,prefixSum,hashtable)
            hashtable[prefixSum]-=1
    
        dfs(root,sum,prefixSum,hashtable)
        return self.count
```

3. 遍历

```python
class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        if not root:return 0
        count=0
        stack=[(root,[root.val])]
        while stack:
            node,valList=stack.pop()
            count+=valList.count(sum)
            valList+=[0]
            if node.right:
                newValList=[i+node.right.val for i in valList]
                stack.append((node.right,newValList))
            if node.left:
                newValList=[i+node.left.val for i in valList]
                stack.append((node.left,newValList))
        return count
```



### C++

```cpp

```

---



# 整理与总结

1. 



