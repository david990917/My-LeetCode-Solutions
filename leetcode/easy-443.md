---
title: easy-443
tags:
  - LeetCode
description: '压缩字符串'
urlname: easy-443
date: 2020-03-15 20:34:35
---

# 题目

https://leetcode-cn.com/problems/string-compression/

给定一组字符，使用原地算法将其压缩。

压缩后的长度必须始终小于或等于原数组长度。

数组的每个元素应该是长度为1 的字符（不是 int 整数类型）。

在完成原地修改输入数组后，返回数组的新长度。

**进阶：**
你能否仅使用O(1) 空间解决问题？

**示例 1：**

```
输入：
["a","a","b","b","c","c","c"]

输出：
返回6，输入数组的前6个字符应该是：["a","2","b","2","c","3"]

说明：
"aa"被"a2"替代。"bb"被"b2"替代。"ccc"被"c3"替代。
```

**示例 2：**

```
输入：
["a"]

输出：
返回1，输入数组的前1个字符应该是：["a"]

说明：
没有任何字符串被替代。
```

**示例 3：**

```
输入：
["a","b","b","b","b","b","b","b","b","b","b","b","b"]

输出：
返回4，输入数组的前4个字符应该是：["a","b","1","2"]。

说明：
由于字符"a"不重复，所以不会被压缩。"bbbbbbbbbbbb"被“b12”替代。
注意每个数字在数组中都有它自己的位置。
```

**注意：**

- 所有字符都有一个ASCII值在[35, 126]区间内。
- 1 <= len(chars) <= 1000。

# 解题思路 √

### Python

1. 双指针

   1. 先为了把全部元素都进行原地修改，添加一个辅助元素

   2. 设置一个指针pos用于指向原地修改的位置，设置一个指针i指向当前的元素；计数器count计算每次元素重复次数；

   3. 依次把当前的元素和后面的元素比较:

      **在不相同情况下**

      - 不相同就把当前的元素加入到这个表里面，pos + 1；
      - 然后判断这时候的count是否大于1，如果大于1把count转化成字符串加入进去，同时修改pos指针，使其大小等于修改后的表长；
      - 注意：这时候不需要对count等于1进行处理（如题目示例2）

      **在相同情况下**

      - 直接移动指针i即可,count进行累加

      **注意最后一个元素**

   4. 最终返回表长，即pos指向的位置，完成算法。

```python
class Solution:
    def compress(self, chars: List[str]) -> int:
        length=len(chars)
        if length==1:return 1

        count,pos=1,0
        for i in range(length-1):        
            if chars[i]!=chars[i+1]:
                chars[pos]=chars[i]
                pos+=1
                if count>1:
                    for j in str(count):
                        chars[pos]=j
                        pos+=1
                count=1
            else:count+=1
            
            if i==length-2:
                chars[pos]=chars[length-1]
                pos+=1
                if count>1:
                    for j in str(count):
                        chars[pos]=j
                        pos+=1
                
        return pos
```


```python

```



### C++

```cpp

```

---



# 整理与总结

1. 

