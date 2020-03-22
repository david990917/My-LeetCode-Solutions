---
title: medium-208
tags:
  - LeetCode
description: ''
urlname: medium-208
date: 2020-03-21 23:42:03
---

# 题目

[实现 Trie (前缀树)](https://leetcode-cn.com/problems/implement-trie-prefix-tree/)

实现一个 Trie (前缀树)，包含 insert, search, 和 startsWith 这三个操作。

示例:

```
Trie trie = new Trie();

trie.insert("apple");
trie.search("apple");   // 返回 true
trie.search("app");     // 返回 false
trie.startsWith("app"); // 返回 true
trie.insert("app");   
trie.search("app");     // 返回 true
```

说明:

你可以假设所有的输入都是由小写字母 a-z 构成的。
保证所有输入均为非空字符串。

# 解题思路 √

Trie (发音为 "try") 或前缀树是一种树数据结构，用于检索字符串数据集中的键。这一高效的数据结构有多种应用：

1. 自动补全

   ![无效的图片地址](medium-208/963cd3fc83e9618aba9cb78365c8a5bf6b7cef8967da0d204dede7844f6738f2-file_1562596867150.png)


   图 1. 谷歌的搜索建议

2. 拼写检查

   ![image.png](medium-208/4d18efbdd4d51ae3935b42cd59b11d66fb62f1586b9638f9499d2a18fa8919d0-image.png)


   图2. 文字处理软件中的拼写检查

3. IP 路由 (最长前缀匹配)

   ![无效的图片地址](medium-208/e3f22b3ab2df82e6c0a7880996749b5e62707e9ef925876e583d666343644526-file_1562596867150.gif)


   图 3. 使用Trie树的最长前缀匹配算法，Internet 协议（IP）路由中利用转发表选择路径。

4. T9 (九宫格) 打字预测

   ![无效的图片地址](medium-208/00900cce532f199559249a47375a76b409f18876bc329087ac057fbe47085f5e-file_1562596867185.jfif)


   图 4. T9（九宫格输入），在 20 世纪 90 年代常用于手机输入

5. 单词游戏

   ![image.png](medium-208/e49e9f0b26566673c32bfbb7de404b5d563a0fe74070bb231de811a70e71f147-image.png)


   图 5. Trie 树可通过剪枝搜索空间来高效解决 Boggle 单词游戏

还有其他的数据结构，如平衡树和哈希表，使我们能够在字符串数据集中搜索单词。为什么我们还需要 Trie 树呢？尽管哈希表可以在 O(1) 时间内寻找键值，却无法高效的完成以下操作：

- 找到具有同一前缀的全部键值。
- 按词典序枚举字符串的数据集。

Trie 树优于哈希表的另一个理由是，随着哈希表大小增加，会出现大量的冲突，时间复杂度可能增加到 O(n)，其中 nn是插入的键的数量。与哈希表相比，Trie 树在存储多个具有相同前缀的键时可以使用较少的空间。此时 Trie 树只需要 O(m)的时间复杂度，其中 m 为键长。而在平衡树中查找键值需要 O(mlogn) 时间复杂度。

### Trie 树的结点结构

Trie 树是一个有根的树，其结点具有以下字段：

- 最多 R 个指向子结点的链接，其中每个链接对应字母表数据集中的一个字母。本文中假定 R 为 26，小写拉丁字母的数量。
- 布尔字段，以指定节点是对应键的结尾还是只是键前缀。

![无效的图片地址](medium-208/3463d9e7cb323911aa67cbd94910a34d88c9402a1ab41bbea10852cd0a74f2af-file_1562596867185.png)

图 6. 单词 "leet" 在 Trie 树中的表示

#### 向 Trie 树中插入键

我们通过搜索 Trie 树来插入一个键。我们从根开始搜索它对应于第一个键字符的链接。有两种情况：

- 链接存在。沿着链接移动到树的下一个子层。算法继续搜索下一个键字符。
- 链接不存在。创建一个新的节点，并将它与父节点的链接相连，该链接与当前的键字符相匹配。

重复以上步骤，直到到达键的最后一个字符，然后将当前节点标记为结束节点，算法完成。

**复杂度分析**

- 时间复杂度：O(m)，其中 m 为键长。在算法的每次迭代中，我们要么检查要么创建一个节点，直到到达键尾。只需要 m 次操作。


- 空间复杂度：O(m)。最坏的情况下，新插入的键和 Trie 树中已有的键没有公共前缀。此时需要添加 m 个结点，使用 O(m) 空间。


![无效的图片地址](medium-208/0cddad836ee9a200b150a3d89f96035f44f3643c4fba0cb1f329e2307c714895-file_1562596867185.png)

#### 在 Trie 树中查找键

每个键在 trie 中表示为从根到内部节点或叶的路径。我们用第一个键字符从根开始，。检查当前节点中与键字符对应的链接。有两种情况：

- 存在链接。我们移动到该链接后面路径中的下一个节点，并继续搜索下一个键字符。
- 不存在链接。若已无键字符，且当前结点标记为 isEnd，则返回 true。否则有两种可能，均返回 false :
  - 还有键字符剩余，但无法跟随 Trie 树的键路径，找不到键。
  - 没有键字符剩余，但当前结点没有标记为 isEnd。也就是说，待查找键只是Trie树中另一个键的前缀。

![image.png](medium-208/ba775065813363474d982b509ae99aa5423418a3ee7e5aa71f9aa4d062b6e19e-image.png)

**复杂度分析**

- 时间复杂度 : O(m)。算法的每一步均搜索下一个键字符。最坏的情况下需要 m 次操作。
- 空间复杂度 : O(1)。

#### 查找 Trie 树中的键前缀

该方法与在 Trie 树中搜索键时使用的方法非常相似。我们从根遍历 Trie 树，直到键前缀中没有字符，或者无法用当前的键字符继续 Trie 中的路径。与上面提到的“搜索键”算法唯一的区别是，到达键前缀的末尾时，总是返回 true。我们不需要考虑当前 Trie 节点是否用 “isend” 标记，因为我们搜索的是键的前缀，而不是整个键。

![image.png](medium-208/7cc64e93088feeedece697a7cae0c7240245e4c5e05de22634b610d7dddb31c8-image.png)

**复杂度分析**

- 时间复杂度 : O(m)。
- 空间复杂度 : O(1)。



### Python

1. 我自己写的太开心了！

```python
class TrieNode(dict):
    def __init__(self):
        self.end = False
        
class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root=TrieNode()


    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        curr=self.root
        for char in word:
            node=curr.get(char)
            if node is None:
                node=TrieNode()
                curr[char]=node
            curr=node
        curr.end=True


    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        curr=self.root
        for char in word:
            curr=curr.get(char)
            if curr is None:
                return False
        return curr.end


    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        curr=self.root
        for char in prefix:
            curr=curr.get(char)
            if curr is None:
                return False
        return True
            



# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
```


```python

```



### C++

```cpp

```

---



# 整理与总结

1. 

