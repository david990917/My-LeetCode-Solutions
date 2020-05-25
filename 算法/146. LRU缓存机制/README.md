| [English](README_EN.md) | 简体中文 |

# [146. LRU缓存机制](https://leetcode-cn.com/problems/lru-cache)
<p>运用你所掌握的数据结构，设计和实现一个&nbsp; <a href="https://baike.baidu.com/item/LRU" target="_blank">LRU (最近最少使用) 缓存机制</a>。它应该支持以下操作： 获取数据 <code>get</code> 和 写入数据 <code>put</code> 。</p>

<p>获取数据 <code>get(key)</code> - 如果密钥 (key) 存在于缓存中，则获取密钥的值（总是正数），否则返回 -1。<br>
写入数据 <code>put(key, value)</code> - 如果密钥已经存在，则变更其数据值；如果密钥不存在，则插入该组「密钥/数据值」。当缓存容量达到上限时，它应该在写入新数据之前删除最久未使用的数据值，从而为新的数据值留出空间。</p>

<p>&nbsp;</p>

<p><strong>进阶:</strong></p>

<p>你是否可以在&nbsp;<strong>O(1)</strong> 时间复杂度内完成这两种操作？</p>

<p>&nbsp;</p>

<p><strong>示例:</strong></p>

<pre>LRUCache cache = new LRUCache( 2 /* 缓存容量 */ );

cache.put(1, 1);
cache.put(2, 2);
cache.get(1);       // 返回  1
cache.put(3, 3);    // 该操作会使得密钥 2 作废
cache.get(2);       // 返回 -1 (未找到)
cache.put(4, 4);    // 该操作会使得密钥 1 作废
cache.get(1);       // 返回 -1 (未找到)
cache.get(3);       // 返回  3
cache.get(4);       // 返回  4
</pre>

**标签:**  [设计](https://leetcode-cn.com/tag/design) 
 ### 相似题目
- 困难:	[LFU缓存](https://leetcode-cn.com/problems/lfu-cache) 
- 困难:	[设计内存文件系统](https://leetcode-cn.com/problems/design-in-memory-file-system) 
- 简单:	[迭代压缩字符串](https://leetcode-cn.com/problems/design-compressed-string-iterator) 

# 解题思路 √

### Python

1. 

```python

```


```python

```

### C++

使用 **双向链表** 和 **哈希表** 来进行操作：

```cpp
struct doubleLinkedNode {
	int key, value;
	doubleLinkedNode* prev;
	doubleLinkedNode* next;
	doubleLinkedNode() :key(0), value(0), prev(nullptr), next(nullptr) {};
	doubleLinkedNode(int _key, int _value) :key(_key), value(_value), prev(nullptr), next(nullptr) {};
};

class LRUCache {
private:
	unordered_map<int, doubleLinkedNode*> cache;
	doubleLinkedNode* head;
	doubleLinkedNode* tail;
	int size;
	int capacity;
public:
	LRUCache(int _capacity) :capacity(_capacity), size(0) {
		head = new doubleLinkedNode();
		tail = new doubleLinkedNode();
		head->next = tail;
		tail->prev = head;
	}

	int get(int key) {
		if (!cache.count(key)) { return -1; }
		doubleLinkedNode* node = cache[key];
		moveToHead(node);
		return node->value;
	}

	void put(int key, int value) {
		if (!cache.count(key)) {
			doubleLinkedNode* node = new doubleLinkedNode(key, value);
			cache[key] = node;
			addToHead(node);
			++size;
			if (size > capacity) {
				doubleLinkedNode* removed = removeTail();
				cache.erase(removed->key);
				--size;
			}
		}
		else {
			doubleLinkedNode* node = cache[key];
			node->value = value;
			moveToHead(node);
		}
	}
	void addToHead(doubleLinkedNode* node) {
		node->prev = head;
		node->next = head->next;
		head->next->prev = node;
		head->next = node;
	}
	void removeNode(doubleLinkedNode* node) {
		node->prev->next = node->next;
		node->next->prev = node->prev;
	}
	void moveToHead(doubleLinkedNode* node) {
		removeNode(node);
		addToHead(node);
	}
	doubleLinkedNode* removeTail() {
		doubleLinkedNode* node = tail->prev;
		removeNode(node);
		return node;
	}
};

/**
 * Your LRUCache object will be instantiated and called as such:
 * LRUCache* obj = new LRUCache(capacity);
 * int param_1 = obj->get(key);
 * obj->put(key,value);
 */
```

---



# 整理与总结

1. 