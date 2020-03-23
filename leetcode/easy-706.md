---
title: easy-706
tags:
  - LeetCode
description: ''
urlname: easy-706
date: 2020-03-23 18:26:26
---

# 题目

[设计哈希映射](https://leetcode-cn.com/problems/design-hashmap/)

不使用任何内建的哈希表库设计一个哈希映射

具体地说，你的设计应该包含以下的功能

put(key, value)：向哈希映射中插入(键,值)的数值对。如果键对应的值已经存在，更新这个值。
get(key)：返回给定的键所对应的值，如果映射中不包含这个键，返回-1。
remove(key)：如果映射中存在这个键，删除这个数值对。

示例：

```
MyHashMap hashMap = new MyHashMap();
hashMap.put(1, 1);          
hashMap.put(2, 2);         
hashMap.get(1);            // 返回 1
hashMap.get(3);            // 返回 -1 (未找到)
hashMap.put(2, 1);         // 更新已有的值
hashMap.get(2);            // 返回 1 
hashMap.remove(2);         // 删除键为2的数据
hashMap.get(2);            // 返回 -1 (未找到) 
```

注意：

- 所有的值都在 [0, 1000000]的范围内。
- 操作的总数目在[1, 10000]范围内。
- 不要使用内建的哈希库。

# 解题思路 √

哈希表是一个在不同语言中都有的通用数据结构。例如，Python 中的 dict 和 Java 中的 Hashmap。哈希表的特性是可以根据给出的 key 快速访问 value。

> 设计哈希表有两个问题需要去解决： 1). 如何设计哈希方法？ 和 2).如何避免哈希碰撞？ 。
>

1. 如何设计哈希方法？：哈希方法会将键值映射到某块存储空间，一个好的哈希方法应该将不同的键值 均匀 地分布在存储空间中。

2. 如何避免哈希碰撞？：哈希方法要将大量的键值映射到一个有限的空间里,这样就有可能会将不同的键值映射到同一个存储空间，这种情况称为 '哈希碰撞' 。哈希碰撞是不可避免的，但可以用策略来解决哈希碰撞。

### Python

1. Python中的hashmap就是{}

```python
class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.hashmap={}
        

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        self.hashmap[key]=value
        

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        return self.hashmap.get(key,-1)
        

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        if key in self.hashmap:
            del self.hashmap[key]
```

2. 取模 + 数组

最简单的思路就是用模运算作为哈希方法，为了降低哈希碰撞的概率，通常取素数的模，例如 模 `2069`。

定义 `array` 数组作为存储空间，通过哈希方法计算数组下标。为了解决 `哈希碰撞` （即键值不同，但映射下标相同），利用 `桶` 来存储所有对应的数值。

**算法**

定义哈希表方法，get()，put() 和 remove()，其中的寻址过程如下所示：

- 对于一个给定的 键值，利用哈希方法生成键值的哈希码，利用哈希码定位存储空间。对于每个哈希码，都能找到一个 桶 来存储该键值所对应的数值。


- 在找到一个桶之后，通过遍历来检查该 键值 对是否已经存在

![pic](easy-706/706_hashmap.png)


```python
class Bucket:
    def __init__(self):
        self.bucket=[]
    def get(self,key):
        for (k,v) in self.bucket:
            if k==key:
                return v
        return -1
    def update(self,key,value):
        found=False
        for i,kv in enumerate(self.bucket):
            if key==kv[0]:
                self.bucket[i]=(key,value)
                found=True
                break
        if not found:
            self.bucket.append((key,value))
    def remove(self,key):
        for i,kv in enumerate(self.bucket):
            if key==kv[0]:
                del self.bucket[i]
    
class MyHashMap:

    def __init__(self):
        self.key_space=2069
        self.hash_table=[Bucket() for i in range(self.key_space)]
        

    def put(self, key: int, value: int) -> None:
        hash_key=key%self.key_space
        self.hash_table[hash_key].update(key,value)
        

    def get(self, key: int) -> int:
        hash_key=key%self.key_space
        return self.hash_table[hash_key].get(key)
        

    def remove(self, key: int) -> None:
        hash_key = key % self.key_space
        self.hash_table[hash_key].remove(key)
```



### C++

```cpp

```

---



# 整理与总结

1. 

