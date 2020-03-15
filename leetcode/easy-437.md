---
title: easy-437
tags:
  - LeetCode
description: 'Path Sum III'
urlname: easy-437
date: 2019-09-01 17:46:00
---

# 题目

https://leetcode.com/problems/path-sum-iii/description/

You are given a binary tree in which each node contains an integer value.

Find the number of paths that sum to a given value.

The path does not need to start or end at the root or a leaf, but it must go downwards (traveling only from parent nodes to child nodes).

The tree has no more than 1,000 nodes and the values are in the range -1,000,000 to 1,000,000.

**Example:**

```
root = [10,5,-3,3,2,null,11,3,-2,null,1], sum = 8

      10
     /  \
    5   -3
   / \    \
  3   2   11
 / \   \
3  -2   1

Return 3. The paths that sum to 8 are:

1.  5 -> 3
2.  5 -> 2 -> 1
3. -3 -> 11
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

# Python

```python

```



# 整理与总结

1. 

