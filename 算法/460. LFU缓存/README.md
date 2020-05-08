| [English](README_EN.md) | 简体中文 |

# [460. LFU缓存](https://leetcode-cn.com/problems/lfu-cache)
<p>请你为 <a href="https://baike.baidu.com/item/%E7%BC%93%E5%AD%98%E7%AE%97%E6%B3%95">最不经常使用（LFU）</a>缓存算法设计并实现数据结构。它应该支持以下操作：<code>get</code>&nbsp;和&nbsp;<code>put</code>。</p>

<ul>
	<li><code>get(key)</code>&nbsp;- 如果键存在于缓存中，则获取键的值（总是正数），否则返回 -1。</li>
	<li><code>put(key, value)</code>&nbsp;- 如果键已存在，则变更其值；如果键不存在，请插入键值对。当缓存达到其容量时，则应该在插入新项之前，使最不经常使用的项无效。在此问题中，当存在平局（即两个或更多个键具有相同使用频率）时，应该去除最久未使用的键。</li>
</ul>

<p>「项的使用次数」就是自插入该项以来对其调用 <code>get</code> 和 <code>put</code> 函数的次数之和。使用次数会在对应项被移除后置为 0 。</p>

<p>&nbsp;</p>

<p><strong>进阶：</strong><br>
你是否可以在&nbsp;<strong>O(1)&nbsp;</strong>时间复杂度内执行两项操作？</p>

<p>&nbsp;</p>

<p><strong>示例：</strong></p>

<pre>LFUCache cache = new LFUCache( 2 /* capacity (缓存容量) */ );

cache.put(1, 1);
cache.put(2, 2);
cache.get(1);       // 返回 1
cache.put(3, 3);    // 去除 key 2
cache.get(2);       // 返回 -1 (未找到key 2)
cache.get(3);       // 返回 3
cache.put(4, 4);    // 去除 key 1
cache.get(1);       // 返回 -1 (未找到 key 1)
cache.get(3);       // 返回 3
cache.get(4);       // 返回 4</pre>

**标签:**  [设计](https://leetcode-cn.com/tag/design) 
 ### 相似题目
- 中等:	[LRU缓存机制](https://leetcode-cn.com/problems/lru-cache) 
- 困难:	[设计内存文件系统](https://leetcode-cn.com/problems/design-in-memory-file-system) 

# 解题思路 √

### Python

1. 

```python

```


```python

```

### C++

```cpp

```

---



# 整理与总结

1. 