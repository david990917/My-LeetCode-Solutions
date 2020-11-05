| [English](README_EN.md) | 简体中文 |

# [127. 单词接龙](https://leetcode-cn.com/problems/word-ladder)
<p>给定两个单词（<em>beginWord&nbsp;</em>和 <em>endWord</em>）和一个字典，找到从&nbsp;<em>beginWord</em> 到&nbsp;<em>endWord</em> 的最短转换序列的长度。转换需遵循如下规则：</p>

<ol>
	<li>每次转换只能改变一个字母。</li>
	<li>转换过程中的中间单词必须是字典中的单词。</li>
</ol>

<p><strong>说明:</strong></p>

<ul>
	<li>如果不存在这样的转换序列，返回 0。</li>
	<li>所有单词具有相同的长度。</li>
	<li>所有单词只由小写字母组成。</li>
	<li>字典中不存在重复的单词。</li>
	<li>你可以假设 <em>beginWord</em> 和 <em>endWord </em>是非空的，且二者不相同。</li>
</ul>

<p><strong>示例&nbsp;1:</strong></p>

<pre><strong>输入:</strong>
beginWord = &quot;hit&quot;,
endWord = &quot;cog&quot;,
wordList = [&quot;hot&quot;,&quot;dot&quot;,&quot;dog&quot;,&quot;lot&quot;,&quot;log&quot;,&quot;cog&quot;]

<strong>输出: </strong>5

<strong>解释: </strong>一个最短转换序列是 &quot;hit&quot; -&gt; &quot;hot&quot; -&gt; &quot;dot&quot; -&gt; &quot;dog&quot; -&gt; &quot;cog&quot;,
     返回它的长度 5。
</pre>

<p><strong>示例 2:</strong></p>

<pre><strong>输入:</strong>
beginWord = &quot;hit&quot;
endWord = &quot;cog&quot;
wordList = [&quot;hot&quot;,&quot;dot&quot;,&quot;dog&quot;,&quot;lot&quot;,&quot;log&quot;]

<strong>输出:</strong>&nbsp;0

<strong>解释:</strong>&nbsp;<em>endWord</em> &quot;cog&quot; 不在字典中，所以无法进行转换。</pre>

**标签:**  [广度优先搜索](https://leetcode-cn.com/tag/breadth-first-search) 
 ### 相似题目
- 困难:	[单词接龙 II](https://leetcode-cn.com/problems/word-ladder-ii) 
- 中等:	[最小基因变化](https://leetcode-cn.com/problems/minimum-genetic-mutation) 

# 解题思路 √

### Python

1. BFS计算

```python
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        def addWord(word: str):
            if word not in wordId:
                nonlocal nodeNum
                wordId[word] = nodeNum
                nodeNum += 1
        
        def addEdge(word: str):
            addWord(word)
            id1 = wordId[word]
            chars = list(word)
            for i in range(len(chars)):
                tmp = chars[i]
                chars[i] = "*"
                newWord = "".join(chars)
                addWord(newWord)
                id2 = wordId[newWord]
                edge[id1].append(id2)
                edge[id2].append(id1)
                chars[i] = tmp

        wordId = dict()
        edge = collections.defaultdict(list)
        nodeNum = 0

        for word in wordList:
            addEdge(word)
        
        addEdge(beginWord)
        if endWord not in wordId:
            return 0
        
        dis = [float("inf")] * nodeNum
        beginId, endId = wordId[beginWord], wordId[endWord]
        dis[beginId] = 0

        que = collections.deque([beginId])
        while que:
            x = que.popleft()
            if x == endId:
                return dis[endId] // 2 + 1
            for it in edge[x]:
                if dis[it] == float("inf"):
                    dis[it] = dis[x] + 1
                    que.append(it)
        
        return 0
```


```python

```

### C++

```cpp

```

---



# 整理与总结

1. 